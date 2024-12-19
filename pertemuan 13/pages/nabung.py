import streamlit as st 

st.title("Ini Halaman nabung!")

with st.form("nabung"):
    nama = st.text_input("masukkan nama")
    nominal = st.number_input("masukkan nominal")
    submitButton = st.form_submit_button("Simpan")
    
    if submitButton:
       st.write(nama)
       st.session_state['Nabung'].append({
           "Nama" : nama,
           "Nominal" : nominal,
})
    st.success("Berhasil Menabung")