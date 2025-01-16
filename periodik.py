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
    "klorin": {"simbol": "Cl", "nomor_atom": 17, "nomor_massa": 35.453},
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
    "europium": {"simbol": "Eu", "nomor_atom": 63, "nomor_massa": 151.96},
    "gadolinium": {"simbol": "Gd", "nomor_atom": 64, "nomor_massa": 157.25},
    "terbium": {"simbol": "Tb", "nomor_atom": 65, "nomor_massa": 158.93},
    "disprosium": {"simbol": "Dy", "nomor_atom": 66, "nomor_massa": 162.50},
    "holmium": {"simbol": "Ho", "nomor_atom": 67, "nomor_massa": 164.93},
    "erbium": {"simbol": "Er", "nomor_atom": 68, "nomor_massa": 167.26},
    "tulium": {"simbol": "Tm", "nomor_atom": 69, "nomor_massa": 168.93},
    "iterbium": {"simbol": "Yb", "nomor_atom": 70, "nomor_massa": 173.05},
    "lutesium": {"simbol": "Lu", "nomor_atom": 71, "nomor_massa": 174.97},
    "hafnium": {"simbol": "Hf", "nomor_atom": 72, "nomor_massa": 178.49},
    "tantalum": {"simbol": "Ta", "nomor_atom": 73, "nomor_massa": 180.95},
    "wolfram": {"simbol": "W", "nomor_atom": 74, "nomor_massa": 183.84},
    "renium": {"simbol": "Re", "nomor_atom": 75, "nomor_massa": 186.21},
    "osmiun": {"simbol": "Os", "nomor_atom": 76, "nomor_massa": 190.23},
    "iridium": {"simbol": "Ir", "nomor_atom": 77, "nomor_massa": 192.22},
    "platina": {"simbol": "Pt", "nomor_atom": 78, "nomor_massa": 195.08},
    "emas": {"simbol": "Au", "nomor_atom": 79, "nomor_massa": 196.97},
    "raksa": {"simbol": "Hg", "nomor_atom": 80, "nomor_massa": 200.59},
    "talium": {"simbol": "Tl", "nomor_atom": 81, "nomor_massa": 204.38},
    "timbal": {"simbol": "Pb", "nomor_atom": 82, "nomor_massa": 207.2},
    "bismut": {"simbol": "Bi", "nomor_atom": 83, "nomor_massa": 208.98},
    "polonium": {"simbol": "Po", "nomor_atom": 84, "nomor_massa": 209},
    "astatin": {"simbol": "At", "nomor_atom": 85, "nomor_massa": 210},
    "radon": {"simbol": "Rn", "nomor_atom": 86, "nomor_massa": 222},
    "fransium": {"simbol": "Fr", "nomor_atom": 87, "nomor_massa": 223},
    "radium": {"simbol": "Ra", "nomor_atom": 88, "nomor_massa": 226},
    "aktinium": {"simbol": "Ac", "nomor_atom": 89, "nomor_massa": 227},
    "torium": {"simbol": "Th", "nomor_atom": 90, "nomor_massa": 232.04},
    "protaktinium": {"simbol": "Pa", "nomor_atom": 91, "nomor_massa": 231.04},
    "uranium": {"simbol": "U", "nomor_atom": 92, "nomor_massa": 238.03},
    "neptunium": {"simbol": "Np", "nomor_atom": 93, "nomor_massa": 237},
    "plutonium": {"simbol": "Pu", "nomor_atom": 94, "nomor_massa": 244},
    "amerisium": {"simbol": "Am", "nomor_atom": 95, "nomor_massa": 243},
    "kurium": {"simbol": "Cm", "nomor_atom": 96, "nomor_massa": 247},
    "berkelium": {"simbol": "Bk", "nomor_atom": 97, "nomor_massa": 247},
    "kalifornium": {"simbol": "Cf", "nomor_atom": 98, "nomor_massa": 251},
    "einstenium": {"simbol": "Es", "nomor_atom": 99, "nomor_massa": 252},
    "fermium": {"simbol": "Fm", "nomor_atom": 100, "nomor_massa": 257},
    "mendelevium": {"simbol": "Md", "nomor_atom": 101, "nomor_massa": 258},
    "nobelium": {"simbol": "No", "nomor_atom": 102, "nomor_massa": 259},
    "laurensium": {"simbol": "Lr", "nomor_atom": 103, "nomor_massa": 266},
    "ruterfordium": {"simbol": "Rf", "nomor_atom": 104, "nomor_massa": 267},
    "dubnium": {"simbol": "Db", "nomor_atom": 105, "nomor_massa": 268},
    "seaborgium": {"simbol": "Sg", "nomor_atom": 106, "nomor_massa":269 },
    "bohrium": {"simbol": "Bh", "nomor_atom": 107, "nomor_massa": 270},
    "hasium": {"simbol": "Hs", "nomor_atom": 108, "nomor_massa": 277},
    "meitmerium": {"simbol": "Mt", "nomor_atom": 109, "nomor_massa": 278},
    "darmstadtium": {"simbol": "Ds", "nomor_atom": 110, "nomor_massa": 281},
    "roentgenium": {"simbol": "Rg", "nomor_atom": 111, "nomor_massa": 282},
    "kopernesium": {"simbol": "Cn", "nomor_atom": 112, "nomor_massa": 285},
    "nihonium": {"simbol": "Nh", "nomor_atom": 113, "nomor_massa": 286},
    "flerovium": {"simbol": "Fi", "nomor_atom": 114, "nomor_massa": 289},
    "moskovium": {"simbol": "Mc", "nomor_atom": 115, "nomor_massa": 290},
    "livermonium": {"simbol": "Lv", "nomor_atom": 116, "nomor_massa": 293},
    "tenesium": {"simbol": "Ts", "nomor_atom": 117, "nomor_massa": 294},
    "oganeson": {"simbol": "Og", "nomor_atom": 118, "nomor_massa": 294},
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
        st.experimental_rerun()
