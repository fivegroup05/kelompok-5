import streamlit as st

def main():
    st.title("Aplikasi perhitungan COD")

    menu = ["Pengertian", "Rumus", "Contoh Soal", "Kalkulator"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Pengertian":
        st.subheader("pengertian COD")

    elif choice == "rumus":
        st.subheader("rumus")

    elif choice == "contoh soal":
        st.subheader("contoh soal")
        
    elif choice == "kalkulator":
        st.subheader("Kalkulator")
