import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Weinauswahl", page_icon="🍷", layout="wide")

# -------- Daten laden --------
@st.cache_data
def load_excel(path="weine.xlsx"):
    p = Path(path)
    return pd.read_excel(p)

df = load_excel()

groups = []
for (wg, reg, land), g in df.groupby(["Weingut","Region","Land"], sort=False):
    wines = g[["Art","Weinname","Jahr"]].to_dict(orient="records")
    groups.append({"weingut": wg, "region": reg, "land": land, "wines": wines})

# -------- CSS mit Google Fonts --------
CSS = """
<link href="https://fonts.googleapis.com/css2?
family=Lato:wght@300;400;700&
family=Playfair+Display:wght@600;700;800&
family=Herr+Von+Muellerhoff&display=swap" rel="stylesheet">

<style>
.block-container {
  background: linear-gradient(160deg, #2a0f16 0%, #1a0a0d 100%) !important;
  color: #f7f7f7 !important;
  border-radius: 0px;
  padding: 50px 70px;
  text-align: center;
}
h1 {
  font-family: 'Playfair Display', serif;
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 8px;
  color: #fdfdfd !important;
  text-align: center;
}
.sub {
  font-family: "Herr Von Muellerhoff", cursive;
  font-size: 2.8rem;
  color: #f5f5f5;
  margin-bottom: 24px;
  text-align: center;
}
.group-title-big {
  font-family: 'Playfair Display', serif;
  font-weight: 800;
  font-size: 5.0rem;
  margin: 26px 0 12px;
  color: #fff;
  text-align: center;

}
.group-title {
  font-family: 'Playfair Display', serif;
  font-weight: 800;
  font-size: 1.3rem;
  margin: 26px 0 12px;
  color: #fff;
}
hr.rule {
  border: none;
  border-top: 1px solid rgba(255,255,255,.15);
  margin: 28px auto;
  width: 60%;
}
.wine-row {
  font-family: 'Lato', sans-serif;
  font-size: 1.05rem;
  margin: 6px 0;
}
.year {
  color: #d1d1d6;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

sprueche = ["Wein ist Traubensaft mit mehr Lebenserfahrung",
            "Meine Laune ist im Keller - ich hoffe sie bringt Wein mit",
            "Zu Vino sag ich nie no",
            "Test Test Test",
            "Test Test Test"]

# -------- Header --------
st.markdown("<div class='group-title-big'>Enoteca</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>in · feriore · motzo  </div>", unsafe_allow_html=True)

# -------- Inhalt --------
for i, g in enumerate(groups):
    if i >= 0:
        st.markdown('<hr class="rule">', unsafe_allow_html=True)
    st.markdown(f"<div class='group-title'>{g['weingut']}, {g['region']} ({g['land']})</div>", unsafe_allow_html=True)
    for w in g["wines"]:
        jahr = int(w["Jahr"]) if pd.notna(w["Jahr"]) else ""
        art = w["Art"].upper()
        st.markdown(
  #          f"<div class='wine-row'>{w['Weinname']} | <span class='year'>{jahr}</span></div>",
            f"<div class='wine-row'>{art} | {w["Weinname"]} | {jahr}",
            unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>“" + sprueche[i] + "”</div>",
        unsafe_allow_html=True
    )
