
# Trading Strategy Evaluation Framework

This project is aimed at substantiating the hypothesis that random trading often outperforms heuristic strategies. This is done by creating a so-called trading monkey which randomly operates a portfolio under the same conditions as the user. It generates a series of trades and determines if its strategy was more effective than the user's.

## Usage

### Quick Start

For quick start, run `launch.py` and input "sample_trading_history.csv" when prompted to enter file name. Then, follow the directions — the process is fairly intuitive.

### Custom Trade History

For custom settings, stick to the following process:

1. Export `.csv` file from any exchange and format it accordingly
2. Import the file inside the root folder
3. Run `launch.py` and follow instructions

Done!

### Constraints & Formatting

Custom trading history **must** be of `.csv` format and contain the following columns:

- `Date`
- `Ticker`
- `Price`
- `Quantity`
- `Trans Code`

> All tickers must match the supported symbol list below.

<details>
<summary><strong>Supported Tickers (click to expand)</strong></summary>

NVDA, HTZ, F, INTC, PLTR, TSLA, ABEV, LCID, BTG, PFE,  
AAL, AAPL, SXTC, BAC, SOFI, RIG, AMZN, JBLU, AGNC, SMX,  
MSGM, APLD, AMD, NU, GOOGL, PBR, NVO, SNAP, WBD, HBAN,  
AMCR, VRN, BBAI, UNH, TSM, SMCI, VALE, ERIC, BBD, T,  
LYG, HOOD, NGD, NIO, KMI, KVUE, AVGO, HPE, AGL, UBER,  
CMCSA, CSX, MRK, WMT, CLSK, ITUB, MSFT, UUUU, ACHR, RIOT,  
WOLF, KO, INFY, MU, QXO, MP, CNH, GOLD, KGC, GOOG, MARA,  
FNA, SCHW, KEY, WFC, NKE, TGL, RF, PTEN, HIMS, STLA,  
SBSW, HAL, IAG, XOM, BABA, AG, GRAB  

</details>

Stock data last updated:
**2025-04-30**