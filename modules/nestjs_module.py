import os
import shutil

def create_nestjs_boilerplate(project_name):
    project_path = f'generated_boilerplates/{project_name}_nestjs'
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    os.makedirs(project_path, exist_ok=True)

    # Construir el comando npx para crear el proyecto NestJS
    command = f'npx @nestjs/cli@latest new {project_name}'

    # Cambiar el directorio de trabajo a project_path y ejecutar el comando
    current_dir = os.getcwd()
    os.chdir(project_path)
    try:
        os.system(command)
    finally:
        os.chdir(current_dir)

    return project_path
