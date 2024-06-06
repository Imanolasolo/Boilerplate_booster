import os
import shutil
import streamlit as st
from modules.flask_module import create_flask_boilerplate
from modules.fastapi_module import create_fastapi_boilerplate
from modules.django_module import create_django_boilerplate
from modules.expressjs_module import create_expressjs_boilerplate
from modules.nestjs_module import create_nestjs_boilerplate
from modules.streamlit_module import create_streamlit_boilerplate
from modules.react_module import create_react_boilerplate
from modules.vue_module import create_vue_boilerplate

st.title("Boilerplate Creator")

# Input para el nombre del proyecto
project_name = st.text_input("Enter the project name")

# Selección del framework en la barra lateral
framework = st.sidebar.radio(
    "Select the framework",
    ("Flask", "FastAPI", "Django", "ExpressJS", "NestJS", "Streamlit", "React", "Vue")  # Añadir la opción Vue
)

include_auth = False
include_db = False

if framework == "Django":
    include_auth = st.sidebar.checkbox("Include authentication")
    include_db = st.sidebar.checkbox("Include database setup")

# Botón para crear el boilerplate
if st.button("Create Boilerplate"):
    if project_name:
        try:
            if framework == "Flask":
                project_path = create_flask_boilerplate(project_name)
            elif framework == "FastAPI":
                project_path = create_fastapi_boilerplate(project_name)
            elif framework == "Django":
                project_path = create_django_boilerplate(project_name, include_auth, include_db)
            elif framework == "ExpressJS":
                project_path = create_expressjs_boilerplate(project_name)
            elif framework == "NestJS":
                st.info("Please open and check your terminal to work with the NestJS CLI.")
                project_path = create_nestjs_boilerplate(project_name)
            elif framework == "Streamlit":
                project_path = create_streamlit_boilerplate(project_name)
            elif framework == "React":
                st.info("Please open and check your terminal to work with the React CLI.")
                project_path = create_react_boilerplate(project_name)
            elif framework == "Vue":
                st.info("Please open and check your terminal to work with the Vue CLI.")
                project_path = create_vue_boilerplate(project_name)
            
            st.success(f"Boilerplate created successfully at: {project_path}")
        except Exception as e:
            st.error(f"Error creating boilerplate: {e}")
    else:
        st.error("Please enter a project name.")



