import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Muat model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

pilihanmenu = st.sidebar.radio("Navigasi", ['Beranda', 'Tentang', 'Kontak'])

# Judul dan deskripsi aplikasi
if pilihanmenu == "Beranda":
    st.title('Aplikasi Prediksi Bullying di Sekolah')
    st.write("""
    Aplikasi ini digunakan untuk memprediksi risiko bullying di sekolah berdasarkan data yang dimasukkan. 
    Silakan isi formulir berikut untuk melakukan prediksi.
    """)

    # Form input pengguna
    st.subheader('Input Data')

    age = st.slider('Usia (Tahun)', min_value=5, max_value=18, value=10, step=1)
    gender = st.selectbox('Jenis Kelamin', ('Laki-laki', 'Perempuan'))
    physically_attacked = st.selectbox('Frekuensi Diserang Secara Fisik', 
                                       ('0 kali', '1 kali', '2 atau 3 kali', '4 atau 5 kali',
                                        '6 atau 7 kali', '8 atau 9 kali', '10 atau 11 kali', '12 kali atau lebih'))
    physical_fighting = st.selectbox('Frekuensi Berkelahi Secara Fisik',
                                     ('0 kali', '1 kali', '2 atau 3 kali', '4 atau 5 kali', 
                                      '6 atau 7 kali', '8 atau 9 kali', '10 atau 11 kali', '12 kali atau lebih'))
    felt_lonely = st.selectbox('Seberapa Sering Merasa Kesepian?',('Tidak Pernah', 'Jarang', 'Kadang-kadang', 'Sering', 'Selalu'))
    close_friends = st.number_input('Jumlah Teman Dekat', min_value=0, max_value=10, value=1, step=1)
    miss_school = st.selectbox('Tidak Masuk Sekolah Tanpa Izin', ('0 hari', '1 hingga 2 hari', '3 hingga 5 hari', '6 hingga 9 hari', '10 hari atau lebih'))
    kind_helpful_students = st.selectbox('Siswa Lain Baik dan Membantu?', ('Tidak Pernah', 'Jarang', 'Kadang-kadang', 'Sering', 'Selalu'))
    parents_understand = st.selectbox('Apakah Orang Tua Memahami Masalah Saya?', ('Tidak Pernah', 'Jarang', 'Kadang-kadang', 'Sering', 'Selalu'))

    # Proses encoding input
    gender_encoded = 0 if gender == 'Laki-laki' else 1
    physically_attacked_encoded = {'0 kali': 0, '1 kali': 1, '2 atau 3 kali': 2, '4 atau 5 kali': 3, 
                               '6 atau 7 kali': 4, '8 atau 9 kali': 5, '10 atau 11 kali': 6, '12 kali atau lebih': 7}[physically_attacked]
    physical_fighting_encoded = {'0 kali': 0, '1 kali': 1, '2 atau 3 kali': 2, '4 atau 5 kali': 3, 
                             '6 atau 7 kali': 4, '8 atau 9 kali': 5, '10 atau 11 kali': 6, '12 kali atau lebih': 7}[physical_fighting]
    felt_lonely_encoded = {'Tidak Pernah': 0, 'Jarang': 1, 'Kadang-kadang': 2, 'Sering': 3, 'Selalu': 4}[felt_lonely]
    miss_school_encoded = {'0 hari': 0, '1 hingga 2 hari': 1, '3 hingga 5 hari': 2, '6 hingga 9 hari': 3, '10 hari atau lebih': 4}[miss_school]
    kind_helpful_students_encoded = {'Tidak Pernah': 0, 'Jarang': 1, 'Kadang-kadang': 2, 'Sering': 3, 'Selalu': 4}[kind_helpful_students]
    parents_understand_encoded = {'Tidak Pernah': 0, 'Jarang': 1, 'Kadang-kadang': 2, 'Sering': 3, 'Selalu': 4}[parents_understand]

    # Buat data untuk prediksi
    input_data = pd.DataFrame({
        'Custom_Age': [age],
        'Sex': [gender_encoded],
        'Physically_attacked': [physically_attacked_encoded],
        'Physical_fighting': [physical_fighting_encoded],
        'Felt_lonely': [felt_lonely_encoded],
        'Close_friends': [close_friends],
        'Miss_school_no_permission': [miss_school_encoded],
        'Other_students_kind_and_helpful': [kind_helpful_students_encoded],
        'Parents_understand_problems': [parents_understand_encoded]
        })

    # Prediksi
    if st.button('Prediksi'):
        prediction = model.predict(input_data)
        result = 'Berisiko' if prediction[0] == 1 else 'Tidak Berisiko'
        st.subheader('Hasil Prediksi')
        st.write(f"Hasil: **{result}**")

if pilihanmenu == "Tentang":
    st.subheader('Tentang Aplikasi')
    st.image('stopbully.jpg', caption='Ilustrasi Bullying', use_container_width=True)
    st.write("""
    **Bullying** adalah tindakan agresif yang dilakukan secara sengaja dan berulang-ulang oleh seseorang atau kelompok untuk menyakiti, 
    mengancam, atau merendahkan individu lain. Bullying dapat terjadi dalam berbagai bentuk, seperti fisik, verbal, sosial, atau bahkan cyberbullying.

    Aplikasi ini bertujuan untuk membantu memprediksi risiko bullying di sekolah berdasarkan data yang diinputkan, sehingga 
    pihak sekolah atau orang tua dapat mengambil langkah preventif untuk mencegah terjadinya bullying.
    """)

if pilihanmenu == "Kontak":
    st.subheader('Hubungi Kami')
    st.write("""
    Jika Anda memiliki pertanyaan atau memerlukan bantuan, silakan hubungi kami melalui:
    - **Nomor Darurat Indonesia**: 112
    - **Nomor Telepon**: 0812-34xx-xx0
    - **Email**: support@bullyingprediction.com
    - **Nomor Darurat Indonesia**: 112
    """)
