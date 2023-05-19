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

def input pengertian():
    st.subheader("Pengertian")
    st.write("Chemical Oxygen Demand (COD) adalah ukuran kuantitatif dari jumlah oksigen yang diperlukan untuk mengoksidasi bahan organik dalam suatu sampel air atau limbah. Pengukuran kadar COD umumnya dilakukan dalam bidang pengolahan air limbah dan pengujian kualitas air.")



if __name__ == "__main__":
    main()
