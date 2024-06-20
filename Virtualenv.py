# Create a Virtual Environment:
python -m venv <env_name>

# Activate the Virtual Environment:
.\<env_name>\Scripts\activate
source <env_name>/bin/activate

# Deactivate the Virtual Environment:
deactivate

# Deleting a Virtual Environment:
rm -rf <env_name>

# Managing Packages
pip install <package_name>
pip list
pip freeze > requirements.txt
pip install -r requirements.txt

# Example Workflow
mkdir my_project
cd my_project
python -m venv venv
.\venv\Scripts\activate
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
deactivate
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
