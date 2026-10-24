"""
VFX forward-test report: mean net % per trade, day-clustered t-stat, bootstrap CI, and REAL vs CONTROL.
Usage: python vfx_report.py [results/vfx_forward_log.csv]
Only judge the result at the pre-registered checkpoints (150 / 300 / 500 real trades) - see results/VFX_FORWARD_TEST.md.
"""
import sys

import numpy as np
import pandas as pd

LOG = sys.argv[1] if len(sys.argv) > 1 else "results/vfx_forward_log.csv"
CHECKS = {150: 2.8, 300: 2.5, 500: 2.2}


def clustered_t(x, days):
    """t-stat of the mean with day-clustered standard errors"""
    x, days = np.asarray(x, float), np.asarray(days)
    n = len(x)
    if n < 2:
        return np.nan
    m = x.mean()
    u = pd.Series(x - m).groupby(days).sum().to_numpy()
    g = len(u)
    if g < 2:
        return np.nan
    var = (u ** 2).sum() / n ** 2 * g / (g - 1)
    return m / np.sqrt(var) if var > 0 else np.nan


def boot_ci(x, days, b=5000, seed=1):
    """95% CI of the mean, resampling whole days"""
    x, days = np.asarray(x, float), np.asarray(days)
    if len(x) < 2:
        return np.nan, np.nan
    rng = np.random.default_rng(seed)
    ud = np.unique(days)
    groups = [x[days == d] for d in ud]
    sums = np.array([g.sum() for g in groups])
    cnts = np.array([len(g) for g in groups])
    idx = rng.integers(0, len(ud), (b, len(ud)))
    means = sums[idx].sum(1) / cnts[idx].sum(1)
    return tuple(np.percentile(means, [2.5, 97.5]))


def stats(df):
    x, d = df["net_pct"].to_numpy(float), df["date"].to_numpy()
    lo, hi = boot_ci(x, d)
    return dict(n=len(x), days=len(np.unique(d)), mean=x.mean() if len(x) else np.nan,
                median=np.median(x) if len(x) else np.nan, sd=x.std(ddof=1) if len(x) > 1 else np.nan,
                t=clustered_t(x, d), ci_lo=lo, ci_hi=hi)


def report(df):
    df = df.copy()
    df["net_pct"] = pd.to_numeric(df["net_pct"], errors="coerce")
    real = df[(df["arm"] == "REAL") & df["net_pct"].notna()]
    ctrl = df[(df["arm"] == "CONTROL") & df["net_pct"].notna()]
    out = [f"# VFX forward test report ({LOG})", ""]
    counts = df["arm"].value_counts().to_dict()
    out.append(f"Rows by arm: {counts}")
    S, C = stats(real), stats(ctrl)
    out += ["", "| Arm | n | days | mean net % | median | sd | day-clustered t | 95% bootstrap CI |", "|---|---|---|---|---|---|---|---|"]
    for nm, s in (("REAL", S), ("CONTROL", C)):
        out.append(f"| {nm} | {s['n']} | {s['days']} | {s['mean']:+.2f} | {s['median']:+.2f} | {s['sd']:.1f} | {s['t']:.2f} | "
                   f"{s['ci_lo']:+.2f} .. {s['ci_hi']:+.2f} |")
    # paired difference (each real trade vs its own control, matched by fire_id)
    pr = real.merge(ctrl[["fire_id", "net_pct"]], on="fire_id", suffixes=("", "_ctrl"))
    if len(pr):
        dd = pr["net_pct"] - pr["net_pct_ctrl"]
        P = stats(pr.assign(net_pct=dd))
        out += ["", f"**REAL - CONTROL (paired by fire_id, n {P['n']}):** {P['mean']:+.2f}% per trade, t {P['t']:.2f}, "
                    f"95% CI {P['ci_lo']:+.2f} .. {P['ci_hi']:+.2f}"]
    else:
        P = dict(mean=np.nan, t=np.nan)
        out += ["", "No paired control trades yet."]
    # costs check
    for k in ("slip_in_pct", "slip_out_pct"):
        v = pd.to_numeric(real.get(k), errors="coerce").dropna() if k in real else pd.Series(dtype=float)
        if len(v):
            out.append(f"Median {k}: {v.median():.2f}% of mid" + ("  **> 1% - STOP (costs kill the edge)**" if v.median() > 1 else ""))
    # decision
    n, m, t = S["n"], S["mean"], S["t"]
    verdict = "keep running (not at a checkpoint)"
    if n > 50 and np.isfinite(t) and t <= -2:
        verdict = "STOP - futility (t <= -2 after 50 trades)"
    for cp, need in CHECKS.items():
        if n >= cp and n < cp + 25:
            beats = np.isfinite(P["mean"]) and P["mean"] > 0
            if m > 0 and beats and t >= need:
                verdict = f"SUCCESS at {cp} (mean > 0, beats control, t {t:.2f} >= {need})"
            elif cp == 150 and m <= 0:
                verdict = "STOP - futility (mean <= 0 at 150)"
            elif cp == 300 and m < 1:
                verdict = "STOP - futility (mean < +1% at 300)"
            else:
                verdict = f"checkpoint {cp}: not yet significant (need t >= {need}) - continue"
    out += ["", f"**Verdict:** {verdict}"]
    return "\n".join(out)


if __name__ == "__main__":
    try:
        df = pd.read_csv(LOG)
    except FileNotFoundError:
        sys.exit(f"{LOG} not found - no trades logged yet.")
    print(report(df))
