import streamlit as st

def hitung_cod(a, b, N, F, V):
    return (a - b) * N * F / V

st.title("Aplikasi Perhitungan COD")

a = st.number_input("Masukkan nilai a:")
b = st.number_input("Masukkan nilai b:")
N = st.number_input("Masukkan nilai N:")
F = st.number_input("Masukkan nilai F:")
V = st.number_input("Masukkan nilai V:")

if st.button("Hitung COD"):
    cod = hitung_cod(a, b, N, F, V)
    st.write("Nilai COD adalah:", cod)
