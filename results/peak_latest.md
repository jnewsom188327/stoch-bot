# PEAK REPLAY - entry vs peak on real 1-minute option bars - 2026-10-28 06:59 ET
720 trades from the paper bots (2026-10-20 to 2026-10-27). 0 legs had no option bars and are left out.

## 1) Entry vs peak - how high it really went while the bot held it
| Bot | Trades | Got +10% | Got +20% | Got +10% then closed RED | Avg true peak | Avg exit | Kept of the peak | Higher within 30 min AFTER the exit |
|---|---|---|---|---|---|---|---|---|
| Diamond YOURS P3 | 65 | 66% | 46% | 23 | +37% | -3% | 19% | 37% |
| Diamond YOURS P2 | 65 | 63% | 40% | 19 | +22% | -2% | 39% | 54% |
| Diamond YOURS Q-scale | 65 | 45% | 26% | 0 | +16% | -0% | 32% | 71% |
| Diamond YOURS P1 | 65 | 58% | 28% | 12 | +13% | -3% | 40% | 66% |
| Diamond YOURS P4 | 63 | 63% | 41% | 18 | +22% | +1% | 45% | 54% |
| Diamond YOURS P5 | 62 | 34% | 13% | 4 | +8% | -0% | 74% | 74% |
| Diamond YOURS P6 | 56 | 59% | 30% | 11 | +13% | -4% | 39% | 64% |
| Trend Flip | 44 | 70% | 55% | 11 | +32% | -2% | 22% | 50% |
| Diamond TUNED P4 | 22 | 64% | 32% | 8 | +18% | -3% | 23% | 45% |
| Diamond TUNED Q-scale | 22 | 41% | 23% | 0 | +18% | +0% | 29% | 64% |
| Diamond TUNED D-scale 1DTE | 22 | 36% | 18% | 0 | +12% | -1% | 33% | 32% |
| Diamond TUNED P1 | 22 | 59% | 18% | 6 | +13% | -6% | -3% | 55% |
| Diamond TUNED P3 | 22 | 73% | 45% | 10 | +39% | +1% | 17% | 23% |
| Diamond TUNED P2 | 22 | 68% | 32% | 8 | +18% | -1% | 23% | 45% |
| Diamond TUNED P5 | 19 | 37% | 11% | 1 | +9% | +2% | 73% | 53% |
| Clean Scan A | 16 | 44% | 19% | 3 | +23% | -9% | 3% | 44% |
| Diamond TUNED P6 | 16 | 69% | 25% | 6 | +14% | -9% | -22% | 44% |
| Clean Scan B | 15 | 33% | 0% | 4 | +6% | -7% | 8% | 40% |
| Original bot | 13 | 54% | 23% | 4 | +16% | -11% | 8% | 46% |
| Fear Snap (averaged, kept as is) | 11 | 73% | 36% | 5 | +16% | -9% | -57% | 45% |
| FG Flow | 7 | 86% | 86% | 2 | +118% | +24% | 25% | 14% |
| Fear Snap | 6 | 100% | 100% | 0 | +40% | +25% | 62% | 50% |

## 2) What if - $ result of each rule added on top of the bot's own exits (best rule in bold)
| Bot | Actual | BE@10 | BE@15 | BE@20 | TP@20 | TP@30 | TP@40 | TP@50 | BE@10+TP@30 | BE@10+TP@40 | BE@15+TP@40 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Diamond YOURS P3 | -339 | **+245** | -106 | -9 | -556 | -689 | -493 | -340 | -417 | -377 | -696 |
| Diamond YOURS P2 | -199 | -329 | -660 | -561 | -559 | -619 | -544 | -361 | -463 | -536 | -867 |
| Diamond YOURS Q-scale | -36 | -59 | **-28** | -36 | -137 | -148 | -118 | -89 | -189 | -175 | -110 |
| Diamond YOURS P1 | -394 | -332 | -716 | -650 | -430 | -444 | -392 | -394 | **-243** | -330 | -714 |
| Diamond YOURS P4 | +93 | -136 | -336 | -274 | -263 | -338 | -195 | -44 | -291 | -311 | -511 |
| Diamond YOURS P5 | -72 | -59 | -78 | -78 | **-51** | -72 | -72 | -72 | -59 | -59 | -78 |
| Diamond YOURS P6 | -263 | -335 | -487 | -442 | -328 | -292 | **-262** | -263 | -291 | -334 | -486 |
| Trend Flip | +126 | **+530** | -123 | -133 | +204 | -145 | -131 | -169 | +294 | +290 | -363 |
| Diamond TUNED P4 | -65 | +18 | **+35** | -71 | -192 | -290 | -256 | -222 | -128 | -108 | -156 |
| Diamond TUNED Q-scale | -96 | -200 | **-91** | -96 | -107 | -148 | -134 | -120 | -200 | -200 | -129 |
| Diamond TUNED D-scale 1DTE | -253 | -252 | -253 | -253 | -324 | -230 | -203 | -253 | -230 | **-202** | -203 |
| Diamond TUNED P1 | -249 | **-107** | -147 | -232 | -160 | -284 | -249 | -249 | -142 | -107 | -147 |
| Diamond TUNED P3 | +89 | **+268** | +250 | +168 | -69 | -92 | -200 | -107 | +120 | +21 | -84 |
| Diamond TUNED P2 | -0 | **+127** | +89 | +1 | -101 | -206 | -172 | -138 | +2 | +22 | -83 |
| Diamond TUNED P5 | +42 | **+54** | +42 | +42 | +13 | +21 | +42 | +42 | +33 | +54 | +42 |
| Clean Scan A | -919 | **-639** | -901 | -901 | -912 | -924 | -893 | -862 | -676 | -645 | -907 |
| Diamond TUNED P6 | -243 | **-101** | -196 | -222 | -184 | -264 | -243 | -243 | -122 | -101 | -196 |
| Clean Scan B | -637 | **-521** | -618 | -637 | -637 | -637 | -637 | -637 | -521 | -521 | -618 |
| Original bot | -323 | **-188** | -303 | -281 | -338 | -281 | -396 | -378 | -209 | -261 | -376 |
| Fear Snap (averaged, kept as is) | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 | -2,770 |
| FG Flow | +168 | -16 | -16 | -16 | +133 | -231 | -158 | -81 | +4 | +57 | +57 |
| Fear Snap | +2,202 | +143 | +601 | +1,243 | +1,884 | **+2,447** | +2,188 | +2,222 | +164 | +143 | +601 |

## 3) Best rule per bot
| Bot | Actual | Best rule | With it | Trades it changed |
|---|---|---|---|---|
| Diamond YOURS P3 | -339 | BE@10 | +245 | 31 of 65 |
| Diamond YOURS P2 | -199 | none beats actual | -199 | 0 of 65 |
| Diamond YOURS Q-scale | -36 | BE@15 | -28 | 2 of 65 |
| Diamond YOURS P1 | -394 | BE@10+TP@30 | -243 | 23 of 65 |
| Diamond YOURS P4 | +93 | none beats actual | +93 | 0 of 63 |
| Diamond YOURS P5 | -72 | TP@20 | -51 | 5 of 62 |
| Diamond YOURS P6 | -263 | TP@40 | -262 | 1 of 56 |
| Trend Flip | +126 | BE@10 | +530 | 15 of 44 |
| Diamond TUNED P4 | -65 | BE@15 | +35 | 7 of 22 |
| Diamond TUNED Q-scale | -96 | BE@15 | -91 | 1 of 22 |
| Diamond TUNED D-scale 1DTE | -253 | BE@10+TP@40 | -202 | 4 of 22 |
| Diamond TUNED P1 | -249 | BE@10 | -107 | 9 of 22 |
| Diamond TUNED P3 | +89 | BE@10 | +268 | 12 of 22 |
| Diamond TUNED P2 | -0 | BE@10 | +127 | 11 of 22 |
| Diamond TUNED P5 | +42 | BE@10 | +54 | 2 of 19 |
| Clean Scan A | -919 | BE@10 | -639 | 6 of 16 |
| Diamond TUNED P6 | -243 | BE@10 | -101 | 9 of 16 |
| Clean Scan B | -637 | BE@10 | -521 | 4 of 15 |
| Original bot | -323 | BE@10 | -188 | 6 of 13 |
| Fear Snap (averaged, kept as is) | -2,770 | none beats actual | -2,770 | 0 of 11 |
| FG Flow | +168 | none beats actual | +168 | 0 of 7 |
| Fear Snap | +2,202 | TP@30 | +2,447 | 5 of 6 |

**All bots together:** actual -4,139 | BE@10 -4,660 | BE@15 -6,813 | BE@20 -6,209 | TP@20 -5,882 | TP@30 -6,637 | TP@40 -6,287 | TP@50 -5,529 | BE@10+TP@30 -6,332 | BE@10+TP@40 -6,451 | BE@15+TP@40 -8,794

**Read with care:** this is about 6 trading days of paper trades - a rule that wins here can still be luck. Breakeven stops are scored worst case inside each minute, but a quick dip under the entry that the bot rode out WILL stop the trade out here, so the cost of shake-outs is in these numbers. Legs: results/peak_legs.csv

