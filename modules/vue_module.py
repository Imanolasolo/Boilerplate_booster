import os
import shutil

def create_vue_boilerplate(project_name):
    # Definir la ruta del proyecto
    project_path = f'generated_boilerplates/{project_name}_vue'

    # Verificar si el directorio ya existe y eliminarlo si es necesario
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    # Crear el directorio del proyecto y cambiar al directorio
    os.makedirs(project_path)
    os.chdir(project_path)

    # Construir el comando para crear el proyecto Vue usando Vue CLI
    command = f'vue create {project_name}'

    # Ejecutar el comando en el terminal del usuario
    os.system(command)

    return project_path
