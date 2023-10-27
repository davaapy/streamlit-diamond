import pickle
import streamlit as st

model = pickle.load(open('chart.sav', 'rb'))

st.title('Estimasi Chart Diamonds')

carat = st.number_input('Masukan Nomer Karat')
color = st.number_input('Masukan Berat')
clarity = st.number_input('Masukan Kejelasan,Dengan Input Nomer')
depth = st.number_input('Masukan Harga')
table = st.number_input('Masukan No Antrian')
price = st.number_input('Masukan Jumlah Yang Akan Di Pesan')
x = st.number_input('Masukan Nomer Diamonds')
y = st.number_input('Masukan Nomer ID Pesanan')
z = st.number_input('Masukan Nomer ID Price')

predict = ''

if st.button('Estimasi Chart Diamonds'):
    predict = model.predict(
        [[carat, color, clarity, depth, table, price, x, y, z]]
    )
    st.write('Estimasi Chart Diamonds : ', predict)
    st.write('Estimasi Chart Diamonds   : ', predict)
