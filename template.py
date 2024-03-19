import os

# On Unix-like systems (such as Linux or macOS), the path separator is /, while on Windows systems, it's \.
# However, when you're using Path() in your code, you can use / as the path separator regardless of the underlying operating system. Path() will automatically translate it to the appropriate separator when you interact with the filesystem.
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name = "mongodb_connect"

list_of_files=[
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/unit/__init__.py", # Unit testing is testing individual component of an application but integrated test is testing the different units once
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_setup.sh",# Seller script, I can use it to run linux command on the terminal
    "requirements.txt",# for production
    "requirements_dev.txt",# for local, we may need things like testing libraries which wlll not be used in the production environment
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",# for testing in local environment
    "experiments/experiments.ipynb",
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath) # Converting the file path we specifyed in windows, we used backword slash but using the Path() class it converts it to windows path
    filedir, filename = os.path.split(filepath) # Split the filepath variable to the directory and file name
    
    if filedir != "": # If the file path contains a folder that means it is not a single file do the below
        os.makedirs(filedir, exist_ok=True) # Create the directory and if it exists no problem
        logging.info(f"Creating directory: {filedir} for the file: {filename}") # Log your progress

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If the file exist or
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existing")