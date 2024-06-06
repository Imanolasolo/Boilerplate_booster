import os
import shutil

def create_flask_boilerplate(project_name):
    project_path = f'generated_boilerplates/{project_name}_flask'
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    os.makedirs(project_path, exist_ok=True)
    os.makedirs(os.path.join(project_path, 'templates'))
    os.makedirs(os.path.join(project_path, 'static', 'css'))
    os.makedirs(os.path.join(project_path, 'static', 'js'))

    with open(os.path.join(project_path, 'app.py'), 'w') as f:
        f.write("""from flask import Flask, render_template\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return render_template('index.html')\n\nif __name__ == '__main__':\n    app.run(debug=True)\n""")

    with open(os.path.join(project_path, 'templates', 'index.html'), 'w') as f:
        f.write("""<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>Flask App</title>\n    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">\n</head>\n<body>\n    <h1>Hello, Flask!</h1>\n    <p>Welcome to my Flask application.</p>\n    <script src="{{ url_for('static', filename='js/script.js') }}"></script>\n</body>\n</html>\n""")

    return project_path
