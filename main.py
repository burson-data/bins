import streamlit as st
from sheets.gsheet import connect_gsheet

# Connect ke Google Sheet
SPREADSHEET_NAME = "data"  # ganti dengan nama file kamu
sheet = connect_gsheet(SPREADSHEET_NAME)

# Ambil worksheet
produk_ws = sheet.worksheet("Product")
media_ws = sheet.worksheet("Partner")
pinjam_ws = sheet.worksheet("Peminjaman")

# Ambil data
produk_data = produk_ws.get_all_records()
media_data = media_ws.get_all_records()
pinjam_data = pinjam_ws.get_all_records()

# Dashboard awal
st.title("📦 Dashboard Inventaris Samsung")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Produk", len(produk_data))
col2.metric("Sedang Dipinjam", sum([1 for p in produk_data if p["Status"] == "Dipinjam"]))
col3.metric("Media Partner", len(media_data))
col4.metric("Belum Kembali", sum([1 for p in pinjam_data if p["Status Surat"] != "Sudah diunggah"]))

st.info("Aplikasi ini masih dalam tahap pengembangan awal.")
