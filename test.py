import streamlit as st

def hitung_cod(volume_blanko, volume_reaksi, normalitas, volume_sampel):
    hasil = (volume_blanko - volume_reaksi) * normalitas * 8000 / volume_sampel
    return hasil

def pengertian_cod():
    st.subheader("Pengertian Chemical Oxygen Demand (COD)")
    st.write("Chemical Oxygen Demand (COD) adalah ukuran kuantitatif dari jumlah oksigen yang diperlukan untuk mengoksidasi bahan organik dalam suatu sampel air atau limbah. Pengukuran kadar COD umumnya dilakukan dalam bidang pengolahan air limbah dan pengujian kualitas air.")

def main():
    st.title("Aplikasi Kalkulator COD")

    menu = ["Kalkulator COD", "Pengertian COD"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Kalkulator COD":
        st.header("Kalkulator Kadar COD")

        # Tampilkan input form
        volume_blanko = st.number_input("Masukkan volume blanko (mL):")
        volume_reaksi = st.number_input("Masukkan volume reaksi (mL):")
        normalitas = st.number_input("Masukkan normalitas:")
        volume_sampel = st.number_input("Masukkan volume sampel (mL):")

        # Tampilkan tombol untuk menghitung kadar COD
        if st.button("Hitung Kadar COD"):
            hasil_cod = hitung_cod(volume_blanko, volume_reaksi, normalitas, volume_sampel)
            st.success(f"Kadar COD: {hasil_cod}")

    elif choice == "Pengertian COD":
        pengertian_cod()
        st.write("Rumus kadar COD adalah kadar COD=((a-b)×N ×8000)/(v )")
        st.write("A= volume blanko")
        st.write("B = volume reaksi")
        st.write("N = normalitas")
        st.write("v= volume sampel")

if __name__ == "__main__":
    main()
