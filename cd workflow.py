name: CI/CD Pipeline

# CI Workflow Here

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
