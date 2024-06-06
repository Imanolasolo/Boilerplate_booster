import os
import shutil

def create_streamlit_boilerplate(project_name):
    # Definir la ruta del proyecto
    project_path = f'generated_boilerplates/{project_name}_streamlit'

    # Verificar si el directorio ya existe y eliminarlo si es necesario
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    # Crear el directorio del proyecto y los subdirectorios necesarios
    os.makedirs(project_path)
    os.makedirs(os.path.join(project_path, 'src'))

    # Crear el archivo app.py de Streamlit
    with open(os.path.join(project_path, 'src', 'app.py'), 'w') as f:
        f.write("""import streamlit as st\n\n""")
        f.write(f"def main():\n")
        f.write(f"    st.title('{project_name} App')\n\n")
        f.write(f"    st.write('Welcome to your Streamlit app!')\n\n")
        f.write(f"    if st.button('Say Hello'):\n")
        f.write(f"        st.write('Hello World!')\n\n")
        f.write(f"if __name__ == '__main__':\n")
        f.write(f"    main()\n")

    return project_path
