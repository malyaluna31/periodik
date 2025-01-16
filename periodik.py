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
    # Tambahkan unsur lainnya sesuai kebutuhan
}

# Fungsi untuk menambahkan gaya kustom
def add_custom_styles():
    st.markdown("""
        <style>
        body { background-color: #e0f7e8; }
        .stTextInput, .stButton { background-color: #e0f7e8 !important; border: 1px solid #76c893 !important; border-radius: 5px; }
        .stButton button { color: white; background-color: #ffa500 !important; font-weight: bold; }
        .stButton button:hover { background-color: #e4882c !important; }
        h1 { color: #4d88ff; text-align: center; }
        .card { border-radius: 5px; padding: 20px; margin: 20px 0; }
        .card-green { background-color: #e0f7e8; border: 1px solid #76c893; color: #006644; }
        .card-orange { background-color: #ffe5cc; border: 1px solid #ff9f43; color: #cc5200; }
        .card-blue { background-color: #d8e9ff; border: 1px solid #4d88ff; color: #0040cc; }
        </style>
    """, unsafe_allow_html=True)

# Panggil fungsi untuk menambahkan gaya kustom
add_custom_styles()

# Inisialisasi halaman jika belum ada
if "page" not in st.session_state:
    st.session_state["page"] = "welcome"

# Halaman Selamat Datang
if st.session_state["page"] == "welcome":
    st.title("Selamat Datang di Aplikasi Tabel Periodik Sederhana")
    st.markdown("""
        <div class="card card-blue">
        <h3>Tujuan Pembuatan:</h3>
        <ul>
            <li>Memberikan informasi dasar tentang unsur-unsur kimia.</li>
            <li>Mempermudah pengguna mencari data unsur secara cepat.</li>
            <li>Melatih pengguna memahami tabel periodik dengan cara yang sederhana.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Next"):
        st.session_state["page"] = "table"

# Halaman Tabel Periodik
elif st.session_state["page"] == "table":
    st.title("Tabel Periodik Sederhana")
    unsur = st.text_input("Masukkan Nama Unsur (misal: Hidrogen):")
    
    if unsur:
        unsur = unsur.lower()  # Pastikan input pengguna dalam huruf kecil
        if unsur in unsur_data:
            data = unsur_data[unsur]
            st.markdown(f'<div class="card card-green"><strong>Simbol Unsur:</strong> {data["simbol"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card card-orange"><strong>Nomor Atom:</strong> {data["nomor_atom"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card card-blue"><strong>Nomor Massa:</strong> {data["nomor_massa"]}</div>', unsafe_allow_html=True)
        else:
            st.error("Unsur tidak ditemukan. Harap masukkan nama unsur yang benar.")

    if st.button("Back"):
        st.session_state["page"] = "welcome"
