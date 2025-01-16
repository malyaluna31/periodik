import streamlit as st

# Data unsur kimia dalam dictionary
unsur_data = {
    "hidrogen": {"simbol": "H", "nomor_atom": 1, "nomor_massa": 1.008},
    "helium": {"simbol": "He", "nomor_atom": 2, "nomor_massa": 4.0026},
    "litium": {"simbol": "Li", "nomor_atom": 3, "nomor_massa": 6.941},
    "berilium": {"simbol": "Be", "nomor_atom": 4, "nomor_massa": 9.0122},
    "boron": {"simbol": "B", "nomor_atom": 5, "nomor_massa": 10.811},
    "karbon": {"simbol": "C", "nomor_atom": 6, "nomor_massa": 12.0107},
    "nitrogen": {"simbol": "N", "nomor_atom": 7, "nomor_massa": 14.0067},
    "oksigen": {"simbol": "O", "nomor_atom": 8, "nomor_massa": 15.9994},
    "fluorin": {"simbol": "F", "nomor_atom": 9, "nomor_massa": 18.9984},
    "neon": {"simbol": "Ne", "nomor_atom": 10, "nomor_massa": 20.1797},
    "sodium": {"simbol": "Na", "nomor_atom": 11, "nomor_massa": 22.9897},
    "magnesium": {"simbol": "Mg", "nomor_atom": 12, "nomor_massa": 24.305},
    "alumunium": {"simbol": "Al", "nomor_atom": 13, "nomor_massa": 26.9815},
    "silikon": {"simbol": "Si", "nomor_atom": 14, "nomor_massa": 28.0855},
    "fosfor": {"simbol": "P", "nomor_atom": 15, "nomor_massa": 30.9737},
    "sulfur": {"simbol": "S", "nomor_atom": 16, "nomor_massa": 32.065},
    "klorin": {"simbol": "Si", "nomor_atom": 17, "nomor_massa": 35.453},
    "argon": {"simbol": "Ar", "nomor_atom": 18, "nomor_massa": 39.948},
    "kalium": {"simbol": "K", "nomor_atom": 19, "nomor_massa": 39.0983},
    "kalsium": {"simbol": "Ca", "nomor_atom": 20, "nomor_massa": 40.078},
    "skandium": {"simbol": "Sc", "nomor_atom": 21, "nomor_massa": 24.9559},
    "titanium": {"simbol": "Ti", "nomor_atom": 22, "nomor_massa": 47.867},
    "vanadium": {"simbol": "V", "nomor_atom": 23, "nomor_massa": 50.9415},
    "kromium": {"simbol": "Cr", "nomor_atom": 24, "nomor_massa": 51.9961},
    "mangan": {"simbol": "Mn", "nomor_atom": 25, "nomor_massa": 59.9380},
    "besi": {"simbol": "Fe", "nomor_atom": 26, "nomor_massa": 55.845},
    "kobalt": {"simbol": "Co", "nomor_atom": 27, "nomor_massa": 58.9331},
    "nikel": {"simbol": "Ni", "nomor_atom": 28, "nomor_massa": 58.6934},
    "tembaga": {"simbol": "Cu", "nomor_atom": 29, "nomor_massa": 63.546},
    "seng": {"simbol": "Zn", "nomor_atom": 30, "nomor_massa": 65.38},
    "galium": {"simbol": "Ga", "nomor_atom": 31, "nomor_massa": 69.723},
    "germanium": {"simbol": "Ge", "nomor_atom": 32, "nomor_massa": 72.63},
    "arsen": {"simbol": "As", "nomor_atom": 33, "nomor_massa": 74.9216},
    "selenium": {"simbol": "Se", "nomor_atom": 34, "nomor_massa": 78.96},
    "bromin": {"simbol": "Br", "nomor_atom": 35, "nomor_massa": 79.904},
    "kripton": {"simbol": "Kr", "nomor_atom": 36, "nomor_massa": 83.798},
    "rubidium": {"simbol": "Rb", "nomor_atom": 37, "nomor_massa": 85.4678},
    "stronsium": {"simbol": "Sr", "nomor_atom": 38, "nomor_massa": 87.62},
    "itrium": {"simbol": "Y", "nomor_atom": 39, "nomor_massa": 88.9058},
    "zirkonium": {"simbol": "Zr", "nomor_atom": 40, "nomor_massa": 91.224},
    "niobium": {"simbol": "Nb", "nomor_atom": 41, "nomor_massa": 92.9063},
    "molibdenum": {"simbol": "Mo", "nomor_atom": 42, "nomor_massa": 95.96},
    "teknesium": {"simbol": "Tc", "nomor_atom": 43, "nomor_massa": 98},
    "rutenium": {"simbol": "Ru", "nomor_atom": 44, "nomor_massa": 101.07},
    "rodium": {"simbol": "Rh", "nomor_atom": 45, "nomor_massa": 102.91},
    "paladium": {"simbol": "Pd", "nomor_atom": 46, "nomor_massa": 106.42},
    "perak": {"simbol": "Ag", "nomor_atom": 47, "nomor_massa": 107.87},
    "kadnium": {"simbol": "Cd", "nomor_atom": 48, "nomor_massa": 112.41},
    "indium": {"simbol": "In", "nomor_atom": 49, "nomor_massa": 114.82},
    "timah": {"simbol": "Sn", "nomor_atom": 50, "nomor_massa": 118.71},
    "antimon": {"simbol": "Sb", "nomor_atom": 51, "nomor_massa": 121.76},
    "telurium": {"simbol": "Te", "nomor_atom": 52, "nomor_massa": 127.60},
    "iodin": {"simbol": "I", "nomor_atom": 53, "nomor_massa": 126.90},
    "xenon": {"simbol": "Xe", "nomor_atom": 54, "nomor_massa": 131.29},
    "cesium": {"simbol": "Cs", "nomor_atom": 55, "nomor_massa": 132.91},
    "barium": {"simbol": "Ba", "nomor_atom": 56, "nomor_massa": 137.33},
    "lantanum": {"simbol": "La", "nomor_atom": 57, "nomor_massa": 138.91},
    "cerium": {"simbol": "Ce", "nomor_atom": 58, "nomor_massa": 140.12},
    "praseodimium": {"simbol": "Pr", "nomor_atom": 59, "nomor_massa": 140.91},
    "neodimium": {"simbol": "Nd", "nomor_atom": 60, "nomor_massa": 144.24},
    "prometium": {"simbol": "Pm", "nomor_atom": 61, "nomor_massa": 145},
    "samarium": {"simbol": "Sm", "nomor_atom": 62, "nomor_massa": 150.36},
    "europium": {"simbol": "Eu", "nomor_atom": 63, "nomor_massa": 151.98},
    "gadolinium": {"simbol": "Gd", "nomor_atom": 64, "nomor_massa": 157.25},
    "terbium": {"simbol": "Tb", "nomor_atom": 65, "nomor_massa": 158.93},
    "dysprosium": {"simbol": "Dy", "nomor_atom": 66, "nomor_massa": 162.50},
    "holmium": {"simbol": "Ho", "nomor_atom": 67, "nomor_massa": 164.93},
    "erbium": {"simbol": "Er", "nomor_atom": 68, "nomor_massa": 167.26},
    "thulium": {"simbol": "Tm", "nomor_atom": 69, "nomor_massa": 168.93},
    "ytterbium": {"simbol": "Yb", "nomor_atom": 70, "nomor_massa": 173.04},
    "lutetium": {"simbol": "Lu", "nomor_atom": 71, "nomor_massa": 175.00},
    "hafnium": {"simbol": "Hf", "nomor_atom": 72, "nomor_massa": 178.49},
    "tantalum": {"simbol": "Ta", "nomor_atom": 73, "nomor_massa": 180.95},
    "wolfram": {"simbol": "W", "nomor_atom": 74, "nomor_massa": 183.84},
    "renium": {"simbol": "Re", "nomor_atom": 75, "nomor_massa": 186.21},
    "osmium": {"simbol": "Os", "nomor_atom": 76, "nomor_massa": 190.23},
    "iridium": {"simbol": "Ir", "nomor_atom": 77, "nomor_massa": 192.22},
    "platinum": {"simbol": "Pt", "nomor_atom": 78, "nomor_massa": 195.08},
    "emas": {"simbol": "Au", "nomor_atom": 79, "nomor_massa": 196.97},
    "merkuri": {"simbol": "Hg", "nomor_atom": 80, "nomor_massa": 200.59},
    "timbal": {"simbol": "Pb", "nomor_atom": 82, "nomor_massa": 207.2},
    "bismut": {"simbol": "Bi", "nomor_atom": 83, "nomor_massa": 208.98},
}

# Fungsi untuk menampilkan elemen berdasarkan input pengguna
def tampilkan_unsur(nama_unsur):
    nama_unsur = nama_unsur.lower()  # Konversi ke huruf kecil untuk konsistensi
    if nama_unsur in unsur_data:
        data = unsur_data[nama_unsur]
        st.write(f"**Nama Unsur:** {nama_unsur.capitalize()}")
        st.write(f"**Simbol:** {data['simbol']}")
        st.write(f"**Nomor Atom:** {data['nomor_atom']}")
        st.write(f"**Nomor Massa:** {data['nomor_massa']}")
    else:
        st.write(f"Unsur dengan nama '{nama_unsur}' tidak ditemukan.")

# Fungsi untuk menambahkan beberapa gaya kustom
def add_custom_styles():
    st.markdown("""
        <style>
        body {
            background-color: #808080;  /* Warna abu-abu */
            color: white;  /* Warna teks putih untuk kontras yang lebih baik */
        }
        </style>
    """, unsafe_allow_html=True)

# Menambahkan gaya kustom
add_custom_styles()

# Input nama unsur dari pengguna
nama_unsur = st.text_input("Masukkan nama unsur kimia:")

# Menampilkan informasi tentang unsur yang dimasukkan
if nama_unsur:
    tampilkan_unsur(nama_unsur)

