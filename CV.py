import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Léontine Tendeng", layout="centered")

# Titre
st.header("Léontine Théodoria Élisabeth TENDENG")

# Information personnelle
st.sidebar.title ("Léontine Théodoria Elisabeth TENDENG")
st.sidebar.write(" Information personnelle")
st.sidebar.write(" Adresse : Dakar, Sénégal")
st.sidebar.write(" Email : leontinetendeng46@email.com")
st.sidebar.write(" Nationalité : Sénégalaise")
# Profil
st.subheader(" Profil")
st.write("""Professionnelle en Geomatique je suis capable d'intervenir sur le terrain
et faire des traitements d'information géographique.
""")

# Formation
st.subheader(" Formation")
st.write("Brevet de Technique Supérieur - GEOMATIQUE")

# Expériences académiques
st.subheader(" Expériences académiques")
st.write ("Stagiaire Geomaticienne - Direction de la Gestion et de la Planification des Ressource en Eau")
st.write ("Realisation des cartes")

# Compétences
st.subheader(" Compétences")

st.markdown("""
- SIG : ArcGIS, QGIS  
- Cartographie numérique  
- Géoréférencement 
- Numérisation
- Bases de données spatiales 
- Télédetection
- Webmapping
- MNT
- Analyse territoriale  
- Microsoft Office (Word, Excel, PowerPoint)  
- Autocad
- Google Earth
""")

