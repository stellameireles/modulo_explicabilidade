import streamlit as st
import streamlit.components.v1 as components
import json


def denuncias():

    st.title("Módulo de Explicabilidade FARO")
    st.header("Explicabilidade")

    file_path = 'resources/denuncias.json'

    def load_json(file_path):
        with open(file_path, "r") as file:
            data = json.loads(file.read())
        return [(item["Identificador"], item["Denuncia"]) for item in data]

    def display_ids_and_texts(ids_and_texts):
        clicked_id = None
        for id_, text in ids_and_texts:
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button(id_):
                    clicked_id = id_
            with col2:
                st.text_area(label=f"Denuncia {id_}", value=text, height=200, key=id_)
        return clicked_id


    list_id_text = load_json(file_path)


    result = display_ids_and_texts(list_id_text)

    if result:
        st.session_state['clicked_id'] = result
        st.session_state['page'] = 'Explicabilidade'
        st.experimental_rerun()
    #st.experimental_rerun()


def explicabilidade():

    st.title("Módulo de Explicabilidade FARO")
    st.header("Denúncias")
    clicked_id = st.session_state.get('clicked_id', 'id101')
    #st.write(f"You clicked: {clicked_id}")



    filepath_lime_exp = f'resources/lime_explanations/{clicked_id}.html'

    with open(filepath_lime_exp, 'r') as f:
        html = f.read()
    components.html(html, height=1600)
    st.experimental_rerun()





if 'page' not in st.session_state:
    st.session_state['page'] = 'Denuncias'


page = st.sidebar.radio("Menu", ['Denuncias', 'Explicabilidade',
                'Informacoes Adicionais'],
                index=['Denuncias', 'Explicabilidade', 'Informacoes Adicionais'].index(st.session_state['page']))



if page == 'Denuncias':
    denuncias()
elif page == 'Explicabilidade':
    explicabilidade()
elif page ==  'Informacoes Adicionais':
    denuncias()


