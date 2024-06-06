import os

def create_expressjs_boilerplate(project_name):
    project_path = f'generated_boilerplates/{project_name}_expressjs'
    os.makedirs(project_path, exist_ok=True)
    os.makedirs(os.path.join(project_path, 'src'))
    open(os.path.join(project_path, '.env'), 'a').close()

    with open(os.path.join(project_path, 'src', 'index.js'), 'w') as f:
        f.write("""const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());

app.get('/', (req, res) => {
  res.send('¡Hola, mundo!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor Express escuchando en el puerto ${PORT}`);
});
""")

    return project_path

