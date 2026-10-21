name: Fear Snap backtest

on:
  workflow_dispatch:
    inputs:
      symbols:
        description: "Symbols (comma separated)"
        default: "SPY,QQQ"
      start:
        description: "Start date"
        default: "2026-01-01"

jobs:
  backtest:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install pandas numpy requests
      - run: python fearsnap_bt.py
        env:
          ALPACA_API_KEY: ${{ secrets.ALPACA_API_KEY }}
          ALPACA_SECRET_KEY: ${{ secrets.ALPACA_SECRET_KEY }}
          SYMBOLS: ${{ inputs.symbols }}
          START: ${{ inputs.start }}
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: fearsnap-fires
          path: fires_*.csv
