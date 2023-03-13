import streamlit as st
import pandas as pd

tabel = pd.DataFrame({"column1": [1, 2, 3, 4], "column2": [4, 5, 6, 7]})


# Poner titulo
st.title("Hello There title :) ")
# OCULTAR MENU DEFAULT Y FOOTER DEFAULT

hide_menu = """

<style>
#MainMenu{visibility:hidden;}
footer {visibility:hidden;}

</style>
 """
st.markdown(hide_menu, unsafe_allow_html=True)
##-------------------------------------

st.subheader("Un subtitulo")

st.header("I am header")

st.text("hi I am text for derscription about something")

st.markdown("*Se utiliza markdown* **WOW** look: ")

st.caption("eso es caption")
st.latex(r"@latex.lenguaje")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
# json
estejson = {"a": "1,2,3", "b": "4,5,6"}
st.json(estejson)
st.markdown("---")

codigo = """
    print("hello world")

"""
st.code(codigo, language="python")

# cambios
st.metric(label="win speed", value="120ms", delta="1.4ms")  # delta="-1.4ms"

st.table(tabel)  # table

st.dataframe(tabel)  # mejor tabla

st.image(
    "221013_Haewon_(NMIXX)_Airport_Departure.jpg",
    caption="esto es una imagen",
    width=250,
)
st.download_button(
    "desarga foto",
    data="jpg",
    file_name="221013_Haewon_(NMIXX)_Airport_Departure.jpg",
    mime="image/jpg",
)
st.audio("NEW_Jeans_OMG.mp3")

st.code(
    """ # codigo para video 
st.video("ruta_video")""",
    language="python",
)

st.checkbox("checkbox")
# radio boton
radio_btn = st.radio("which country do you live?", options=("US", "UK", "COL"))


def btn_click():
    print("dio click")


btn = st.button("click me", on_click=btn_click)

selectop = st.selectbox(
    "what is yor favorite fruit?", options=("Audi", "Bmm2", "pear", "apple")
)

multi_select = st.multiselect(
    "mira los multiples select", options=("option1", "option2", "option3")
)

st.markdown("---")
st.markdown("Uploading Files")
cosaDesubir = st.file_uploader("Porfa sube archivo imagen", type=["png", "jpg"])
if cosaDesubir is not None:
    st.image(cosaDesubir)

co_slider = st.slider("esto es un slider", min_value=50, max_value=150, value=70)

inpt_text = st.text_input("escribe aqui", max_chars=60)

inpt_text_area = st.text_area("escribwe.....")

inpt_date = st.date_input("pon fecha")

inpt_time = st.time_input("selecciona  hora")

import time

# barra de progreso
bar_progr = st.progress(0)
# poner 10 en 00
for barrita in range(00):
    bar_progr.progress((barrita + 1) * 10)
    time.sleep(1)
st.markdown("-----")
st.markdown("Formularios")
# formularios
formulario = st.form("form 1")
formulario.text_input("first name")
formulario.form_submit_button("Enviar")

with st.form("form 2"):
    col1, clo2 = st.columns(2)
    f_name = col1.text_input("firs name")
    s_name = clo2.text_input("second name")

    day, month, year = st.columns(3)
    day.text_input("day")
    month.text_input("Month")
    year.text_input("year")
    stado_f = st.form_submit_button("submit")
    if stado_f:
        if f_name == "" and s_name == "":
            st.warning("please llenalo  -__-")
        else:
            st.success("genial lo llenaaste :) ")

# side bar
# st.sidebar.write("esto es un sidebar")
