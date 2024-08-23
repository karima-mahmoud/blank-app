import streamlit as st
import pickle

st.title("car co2 emssion")
f1= st.number_input('feture 1',min_value=1,max_value=10)
f2= st.number_input('feture 2',min_value=1,max_value=10)
f3= st.number_input('feture 3',min_value=1,max_value=100)

with open('model2.pkl','rb') as file:
 model= pickle.load(file)
output=model.predict([[f1,f2,f3]])

st.write(output[0][0])
