import streamlit as st

def main():
    st.title("Aplikasi Streamlit dengan Sidebar")

    menu = ["Menu 1", "Menu 2", "Menu 3"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Menu 1":
        st.subheader("Menu 1 Dipilih")
        # Tambahkan kode untuk menu 1 di sini

    elif choice == "Menu 2":
        st.subheader("Menu 2 Dipilih")
        # Tambahkan kode untuk menu 2 di sini

    elif choice == "Menu 3":
        st.subheader("Menu 3 Dipilih")
        # Tambahkan kode untuk menu 3 di sini

if __name__ == "__main__":
    main()
