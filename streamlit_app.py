import glob
import os
import re

import pandas as pd
import streamlit as st
from PIL import Image

# ------------------ SESSION STATE ------------------

if "language" not in st.session_state:
    st.session_state.language = "pt"

# ------------------ I18N SIMPLES ------------------

TRANSLATIONS = {
    "pt": {
        "Day {day}": "Slide {day}",
        "# 30 Days of Streamlit": "# Objetivo: Desenvolver um guardrail que não use LLM para dar a avaliação.",
        #"Start the Challenge 👇": "Inicie o Desafio 👇",
        "About the #30DaysOfStreamlit": "Sobre Desenvolver um guardrail que não use LLM para dar a avaliação.",
        "About": "Sobre",
        "Resources": "Recursos",
        "Deploy": "Publicar",
        "Which {day_num}": "Qual {day_num}",
    }
}

def _(text: str):
    lang = st.session_state.get("language", "pt")
    return TRANSLATIONS.get(lang, {}).get(text, text)

# ------------------ CONFIGURAÇÃO STREAMLIT ------------------

st.set_page_config(layout="wide")

query_params = st.query_params
selected_language = st.session_state["language"]

# ------------------ FUNÇÕES AUXILIARES ------------------

def update_params():
    st.query_params["challenge"] = st.session_state.day

def format_day(label):
    return _("Day {day}").format(day=int(re.search(r"\d+", label).group()))

# ------------------ LISTAGEM DOS DIAS ------------------

md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1(f"content/{selected_language}", "*.md")]
)

days_list = [f"Day{x}" for x in md_files]

# ------------------ HEADER ------------------

placeholder = st.empty()
with placeholder:
    st.write(_("Day {day}").format(day=1))
placeholder.empty()

col1, col2, col3 = st.columns((1, 4, 1))
st.markdown(_("# Desafio proposto: Desenvolver um guardrail que não use ***Large Language Model*** (LLM) para dar a avaliação."))

# ------------------ SELETOR DE SLIDE ------------------

if query_params:
    try:
        selected_day = query_params["challenge"][0]
        if selected_day in days_list:
            st.session_state.day = selected_day
    except KeyError:
        st.session_state.day = days_list[0]

selected_day = st.selectbox(
    _("Escolha o slide para visualizar a proposta de solução"),
    days_list,
    key="day",
    on_change=update_params,
    format_func=format_day
)

# ------------------ ABOUT ------------------

with st.expander(_("About the #30DaysOfStreamlit")):
    st.markdown(
        """
        Baseado no requisito **desenvolver um guardrail que não use LLM para dar a avaliação**, 
        este desafio tem sua solução pormenorizadas nos 5 slides, conforme descrito abaixo:
        - Slide 1: Introdução e Contextualização.
        - Slide 2: Limitações técnicas dos LLMs para moderação étnica.
        - Slide 3: Arquitetura da solução "Sentinela étnico-cultural".
        - Slide 4: Explicação da Arquitetura proposta.
        - Slide 5: Conclusão e Trabalhos Futuros.
        """
    )

# ------------------ SIDEBAR ------------------

st.sidebar.header(_("Definição"))
st.sidebar.markdown(
    "Guardrails em IA são mecanismos de controle que limitam e monitoram o comportamento "
    "de modelos inteligentes para garantir segurança, ética, conformidade e previsibilidade."
)

st.sidebar.header(_("Tecnologias utilizadas"))
st.sidebar.markdown(
    """
    - Python  
    - Streamlit  
    - Git/GitHub  
    - Linux / WSL  
    """
)

st.sidebar.header(_("Sobre o Candidato"))
st.sidebar.markdown(
    """
    - Leonardo Brendo G. Nascimento  
    - Mestre em Ciência da Computação  
    - Desenvolvedor de Software Sênior  
    - Professor de Computação e Informática  
    """
)

# ------------------ CONTEÚDO PRINCIPAL ------------------

for day in days_list:
    if selected_day == day:

        st.markdown(
            "# 🗓️ Slide {day_num}".format(
                day_num=int(re.search(r"\d+", day).group())
            )
        )

        # ---------- LÊ MARKDOWN COMPLETO ----------
        md_path = f"content/pt/{day}.md"
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        # ---------- EXTRAI IMAGENS DO MARKDOWN ----------
        image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
        images = image_pattern.findall(md_content)

        # Remove imagens do markdown para evitar quebra
        md_without_images = image_pattern.sub("", md_content)

        # ---------- RENDERIZA MARKDOWN (EQUAÇÕES OK) ----------
        st.markdown(md_without_images, unsafe_allow_html=True)

        # ---------- RENDERIZA IMAGENS ----------
        for alt_text, img_path in images:
            if os.path.exists(img_path):
                st.image(
                    img_path,
                    caption=alt_text,
                    use_container_width=True
                )
            else:
                st.warning(f"Imagem não encontrada: {img_path}")

        # ---------- FIGURAS VIA CSV ----------
        figures_path = f"content/pt/figures/{day}.csv"
        if os.path.isfile(figures_path):
            st.markdown("---")

            df = pd.read_csv(figures_path, engine="python")

            for i in range(len(df)):
                img_file = f"content/pt/images/{df.img[i]}"
                if os.path.exists(img_file):
                    st.image(img_file, use_container_width=True)
                    st.info(f"{df.figure[i]}: {df.caption[i]}")
                else:
                    st.warning(f"Imagem não encontrada: {img_file}")
