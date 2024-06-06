import os
import shutil

def create_fastapi_boilerplate(project_name):
    project_path = f'generated_boilerplates/{project_name}_fastapi'
    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    os.makedirs(project_path, exist_ok=True)
    with open(os.path.join(project_path, 'main.py'), 'w') as f:
        f.write("""from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\nasync def read_root():\n    return {"message": "Hello World"}\n\n@app.get('/items/{item_id}')\nasync def read_item(item_id: int, q: str = None):\n    return {"item_id": item_id, "q": q}\n\nif __name__ == "__main__":\n    import uvicorn\n    uvicorn.run(app, host="localhost", port=8000)\n""")

    return project_path
