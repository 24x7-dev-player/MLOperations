# Initialize DVC in a Project:
dvc init

# Add a Data File or Directory:
dvc add <path/to/data>

# Create a DVC Pipeline Stage:
dvc run -n <stage-name> -d <dependency> -o <output> <command>

# Push Data to Remote Storage:
dvc push

# Pull Data from Remote Storage:
dvc pull

# Example Workflow
# Initialize a Git Repository and DVC:
git init
dvc init

# Add Data and Create a Pipeline:
dvc add data/raw
git add data/raw.dvc .gitignore
git commit -m "Add raw data"
dvc run -n preprocess -d data/raw -o data/processed python preprocess.py
git add dvc.yaml dvc.lock
git commit -m "Add preprocessing stage"


# Run an Experiment and Track Metrics:
dvc run -n train -d data/processed -o model python train.py
git add dvc.yaml dvc.lock
git commit -m "Add training stage"

# Push Data and Models to Remote Storage:
dvc remote add -d myremote s3://mybucket/path
dvc push
git add .dvc/config
git commit -m "Configure remote storage"

# Manage and Compare Experiments:
dvc exp run
dvc exp show
dvc exp diff

# Visualizatio Pipeline
dvc dag