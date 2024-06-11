name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-test:
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
          pylint .

      - name: Run tests
        run: |
          source .venv/bin/activate
          pytest --junitxml=report.xml

      - name: Build Docker image
        run: docker build -t user/myapp:latest .

      - name: Push Docker image to Docker Hub (deploy)
        run: |
          echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
          docker push user/myapp:latest

  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest

    steps:
      - name: Set up SSH
        uses: webfactory/ssh-agent@v2.3.3
        with:
          ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}

      - name: Deploy to Production
        run: |
          ssh -o StrictHostKeyChecking=no ec2-user@your-ec2-public-dns "docker pull user/myapp:latest && docker stop myapp && docker rm myapp && docker run -d --name myapp -p 80:80 user/myapp:latest"
