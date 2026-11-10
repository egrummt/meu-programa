
import streamlit as st

st.title("Meu primeiro programa")

nome = st.text_input("Insira seu nome:")
idade = st.number_input("Insira sua idade:", min_value=0, step=1)

if st.button("Ver resultado"):
    st.write("Olá, " + nome + "!")

    if idade >= 30:
        st.write("Você tem", idade, "anos")
       	st.write("Você está velho")
    else:
        st.write("Você está novo ainda")
