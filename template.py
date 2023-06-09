import os
from pathlib import  Path


project_name = 'Self-adaptiveDeepRL'

list_of_files = [
    f"src\{project_name}\__init__.py",
    f"src\{project_name}\dqn\__init__.py",
    "config\config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    
        with open(filepath, "w") as f:
            ...
            
    else:
        print(f"{filename} already exists")
        
        
        
    