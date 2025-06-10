import streamlit as st
import pandas as pd

# Lista spółek z tickerami GPW (na razie statyczne)
spolki = {
    "Vercom": "VRM",
    "Rainbow": "RBW",
    "LPP": "LPP",
    "Toya": "TOY",
    "Decora": "DCR"
}

def get_demo_data(ticker):
    # Demo: dane fikcyjne
    data = {
        "Rok": [2019, 2020, 2021, 2022, 2023],
        "Przychody (mln zł)": [100, 110, 120, 130, 140],
        "Zysk netto (mln zł)": [10, 12, 11, 14, 15],
        "Dywidenda (zł/akcja)": [2.0, 2.5, 3.0, 3.5, 4.0]
    }
    return pd.DataFrame(data)

st.set_page_config(page_title="GPW Analyzer", layout="wide")
st.title("📈 Analiza spółek GPW - wersja demo")

wybrana_spolka = st.selectbox("Wybierz spółkę", list(spolki.keys()))
ticker = spolki[wybrana_spolka]

df = get_demo_data(ticker)

st.subheader(f"Dane finansowe dla {wybrana_spolka} ({ticker})")
st.line_chart(df.set_index("Rok")[["Przychody (mln zł)", "Zysk netto (mln zł)"]])

st.dataframe(df.set_index("Rok"))
