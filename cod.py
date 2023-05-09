import streamlit as st

def hitung_cod(Blanko, Pereaksi, Normalitas, Faktor Pengali, Volume Sampel):
    return (Blanko - Pereaksi) * Normalitas * Faktor Pengali / Volume Sampel

st.title("Aplikasi Perhitungan COD")

Blanko = st.number_input("Masukkan nilai Blanko:")
Pereaksi = st.number_input("Masukkan nilai Pereaksi:")
Normalitas = st.number_input("Masukkan nilai Normalitas:")
Faktor Pengali = st.number_input("Masukkan nilai Faktor Pengali:")
Volume Sampel = st.number_input("Masukkan nilai Volume Sampel:")

if st.button("Hitung COD"):
    cod = hitung_cod(Blanko, Pereaksi, Normalitas, Faktor Pengali, Volume Sampel)
    st.write("Nilai COD adalah:", cod)
