import streamlit as st
import plotly.express as px

st.write("Halo, ini aplikasi penjualan buah!")


st.title("Analisis Penjualan Buah")
st.write("Pilih Buah Favoritmu!")

Buah = st.selectbox("pilih Buah:",["Mangga", "Kelengkeng", "Duku"])
st.write("Pilihanmu Adalah:", Buah)

Harga = st.slider("Pilih Harga (Rp):", 100.000, 200.000, 500.000)
st.write("Harga Yang Dipilih Adalah:", Harga, "Rp")

if st.button("Tampilkan Pesan"):
    st.write("TERIMA KASIH TELAH MEMILIH", Buah, "DENGAN HARGA", Harga, "Rp!")

   
data = {
    "Buah": [Buah],
    "Harga": [Harga],
    "Penjualan": [Harga * 10]  # Contoh: Penjualan = Harga x 10 . (hanya contoh)
}

fig = px.bar(data, x="Buah", y="Penjualan", title="Penjualan Berdasarkan Pilihan",
             color="Buah", color_discrete_sequence=["#FF9999", "#99FF99", "#66B2FF"])
st.plotly_chart(fig)