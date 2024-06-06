import os
import shutil
import subprocess

def create_django_boilerplate(project_name, include_auth, include_db):
    project_path = f'generated_boilerplates/{project_name}_django'
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    command = ['django-admin', 'startproject', project_name]
    subprocess.run(command, cwd='generated_boilerplates', check=True)

    django_project_dir = os.path.join(project_path, project_name)
    shutil.move(os.path.join('generated_boilerplates', project_name), django_project_dir)

    django_app_dir = os.path.join(django_project_dir, 'django_app')
    os.makedirs(django_app_dir, exist_ok=True)

    if include_auth:
        with open(os.path.join(django_app_dir, 'auth.py'), 'w') as f:
            f.write("# Código de autenticación\n")
    if include_db:
        with open(os.path.join(django_app_dir, 'db.py'), 'w') as f:
            f.write("# Configuración de base de datos\n")

    return project_path
