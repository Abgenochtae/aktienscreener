  import yfinance as yf
  import streamlit as st
  import pandas as pd

  st.title("Aktienscreener")

  tickers = st.text_input("Gib Ticker ein (kommagetrennt):", "AAPL,MSFT,GOOGL").split(',')

  result_list = []

  for ticker in tickers:
      ticker = ticker.strip().upper()
      try:
          data = yf.Ticker(ticker).info
          kgv = data.get("trailingPE")
          fcf = data.get("freeCashflow")
          debt = data.get("totalDebt")
          growth = data.get("revenueGrowth")

          if kgv and kgv <= 10 and fcf and debt and fcf > debt and growth and growth >= 0.10:
              result_list.append({
                  "Ticker": ticker,
                  "KGV": kgv,
                  "Verschuldung": debt,
                  "Free Cashflow": fcf,
                  "Umsatzwachstum": growth
              })
      except Exception as e:
          st.write(f"Fehler bei {ticker}: {e}")

  df = pd.DataFrame(result_list)
  st.dataframe(df)
