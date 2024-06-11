name: CI Workflow

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.8"

      - name: Install dependencies
        run: |
          python -m venv .venv
          source .venv/bin/activate
          pip install -r requirements.txt

      - name: Run static analysis
        run: |
          source .venv/bin/activate
          pylint mymodule/

      - name: Run tests
        run: |
          source .venv/bin/activate
          pytest --junitxml=report.xml

      - name: Generate coverage report
        run: |
          source .venv/bin/activate
          pytest --cov=mymodule

      - name: Build Docker image
        run: docker build -t myapp:latest .

      - name: Push Docker image
        run: |
          echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
          docker push myapp:latest

      - name: Notify
        if: always()
        uses: actions/slack@v2
        with:
          status: ${{ job.status }}
