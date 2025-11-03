import streamlit as st
import pandas as pd
import os

# === PAGE CONFIGURATION ===
st.set_page_config(page_title="Suivi Joueuse RMBB", layout="centered")

# === LOGO RMBB VIA LINK RAW GITHUB ===
logo_url = "https://raw.githubusercontent.com/Marchais795/mon_projet_streamlit/main/image/Rouen%20Bihorel%20basket.png"

st.markdown(f"""
<div class="header-banner">
    <div class="top-text">🏀 Saison 2025-2026 — Championnat LF2</div>
    <div class="header-content">
        <img src="{logo_url}" width="80">
        <h1>Suivi de la Charge - RMBB</h1>
        <img src="{logo_url}" width="80">
    </div>
</div>
""", unsafe_allow_html=True)

# === STYLE MODERNE ===
st.markdown("""
<style>
body, .stApp {
    background-color: #e0e0e0;
    color: black;
    font-family: 'Segoe UI', sans-serif;
}

.header-banner {
    width: 100%;
    margin: 0;
    background-color: #003366;
    color: white;
    padding: 15px 20px;
    border-bottom: 4px solid #0055a5;
    border-radius: 0 0 15px 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header-content h1 {
    color: white;
    text-align: center;
    font-weight: 700;
    font-size: 1.8em;
    flex-grow: 1;
}

.header-content img {
    width: 80px;
    margin: 0 15px;
}

.top-text {
    text-align: center;
    font-size: 1em;
    color: #cce0ff;
    margin-bottom: 5px;
    letter-spacing: 0.5px;
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.info-card {
    background-color: #f5f5f5;
    border-left: 6px solid #0055a5;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 25px;
}

h4 {
    color: #003366;
    margin-bottom: 10px;
    border-left: 5px solid #0055a5;
    padding-left: 8px;
}

.label-line {
    font-weight: bold;
    color: #003366;
    margin-bottom: 5px;
}

.inline-scale {
    font-weight: normal;
    font-size: 0.85em;
    color: #555;
    margin-left: 5px;
    font-style: italic;
}

.stButton>button {
    background-color: #003366;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 20px;
    width: 100%;
    transition: all 0.2s ease-in-out;
}

.stButton>button:hover {
    background-color: #0055a5;
    transform: scale(1.02);
}

.success-msg {
    text-align: center;
    font-weight: bold;
    color: #003366;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# === FICHE EXPLICATIVE ===
st.markdown("""
<div class="info-card">
<h4>ℹ️ Pourquoi remplir ce suivi ?</h4>
<p>
Ce questionnaire permet de suivre ton état de forme et ta récupération au fil des jours.<br>
L’objectif est d’adapter les entraînements pour éviter la fatigue excessive et améliorer tes performances.
</p>

<ul>
<li><b>État mental :</b> ton ressenti psychologique, motivation, concentration, stress.</li>
<li><b>État physique :</b> ton ressenti corporel, douleurs, énergie, fatigue générale.</li>
<li><b>Échelle de Borg :</b> à quel point l’entraînement t’a semblé difficile (effort perçu).</li>
</ul>

<p style='font-size:0.9em; color:#444;'>
👉 <b>0 = parfait</b> (très bien mentalement/physiquement, facile à l’entraînement)<br>
👉 <b>10 = difficile</b> (fatiguée, stressée ou effort très intense)
</p>
</div>
""", unsafe_allow_html=True)

# === NOM Joueuse ===
joueuse = st.text_input("👤 Nom et prénom de la joueuse")

# === ÉTAT DU JOUR ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h4>🧠 État du jour</h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="label-line">Mental<span class="inline-scale">(0 = excellent / 10 = très fatiguée)</span></div>', unsafe_allow_html=True)
    etat_mental = st.slider("", 0, 10, 0, key="mental")

with col2:
    st.markdown('<div class="label-line">Physique<span class="inline-scale">(0 = excellent / 10 = très fatiguée)</span></div>', unsafe_allow_html=True)
    etat_physique = st.slider("", 0, 10, 0, key="physique")

st.markdown('</div>', unsafe_allow_html=True)

# === ÉVALUATION ENTRAÎNEMENT ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h4>💪 Évaluation de l’entraînement</h4>", unsafe_allow_html=True)
st.markdown('<div class="label-line">Échelle de Borg<span class="inline-scale">(0 = très facile / 10 = effort maximal)</span></div>', unsafe_allow_html=True)
entrainement = st.slider("", 0, 10, 5, key="borg")
st.markdown('</div>', unsafe_allow_html=True)

# === COMMENTAIRE ===
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h4>📝 Commentaire libre</h4>", unsafe_allow_html=True)
commentaire = st.text_area("Comment t’es-tu sentie aujourd’hui ?", "")
st.markdown('</div>', unsafe_allow_html=True)

# === ENREGISTREMENT ===
if st.button("💾 Enregistrer mes données"):
    if not joueuse:
        st.error("⚠️ Merci d’entrer ton nom avant d’enregistrer.")
    else:
        file_path = "suivi_joueuse.csv"
        df_new = pd.DataFrame({
            "Joueuse": [joueuse],
            "Etat_Mental (0=Excellent,10=Fatiguée)": [etat_mental],
            "Etat_Physique (0=Excellent,10=Fatiguée)": [etat_physique],
            "Evaluation_Entrainement (Borg)": [entrainement],
            "Commentaire": [commentaire]
        })

        if os.path.exists(file_path):
            df_new.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df_new.to_csv(file_path, index=False)

        st.success("✅ Données enregistrées avec succès !")
        st.markdown("<div class='success-msg'>Merci pour ta participation 💙</div>", unsafe_allow_html=True)
