import streamlit as st

# Data barang
harga_barang = {
    "beras": 50000,
    "susu": 15000,
    "sabun": 10000
}

st.title("🧾 Aplikasi Kasir Mini")

st.subheader("Pilih Barang yang Ingin Dibeli:")

keranjang = {}
for barang, harga in harga_barang.items():
    jumlah = st.number_input(f"{barang.title()} (Rp{harga:,})", min_value=0, step=1)
    if jumlah > 0:
        keranjang[barang] = jumlah

def hitung_total(keranjang):
    total = 0
    for barang, jumlah in keranjang.items():
        total += harga_barang[barang] * jumlah
    return total

if st.button("Hitung Total"):
    if keranjang:
        st.subheader("Struk Belanja")
        for barang, jumlah in keranjang.items():
            subtotal = harga_barang[barang] * jumlah
            st.write(f"{barang.title()} x{jumlah} = Rp{subtotal:,}")
        st.success(f"Total: Rp{hitung_total(keranjang):,}")
    else:
        st.warning("Belum ada barang yang dipilih.")

