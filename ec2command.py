# Connect to EC2 Instance:
"# Use SSH command with .pem file and public DNS/IP address."
"# Example: ssh -i /path/to/your-file.pem ubuntu@ec2-xx-xx-xx-xx.compute-1.amazonaws.com"

# Ensure .pem File Permissions:
"# Set read-only permissions for owner: chmod 400 /path/to/your-file.pem"

# Check CPU Information:
"# Command: lscpu"

# Check RAM Information:
"# Command: free -h"

# Check OS Information:
"# Command: cat /etc/os-release"

# Check Disk Usage:
"# Command: df -h"

# Script in Terminal (Part 1):
"# Switch to root user: sudo -i"
"# Clear terminal screen: clear"
"# Update package lists: apt-get update"
"# Check Nginx configuration syntax: nginx -t"

# Install Nginx Web Server:
"# Command: apt-get install nginx"

# Verify Nginx Installation:
"# Command: nginx -t"

# Check Nginx Service Status:
"# Command: service nginx status"

# Test Nginx Web Server:
"# Command: curl localhost"

# Navigate to Web Root Directory:
"# Command: cd /var/www/html/"

# List Directory Contents:
"# Command: ls"

# Display Default Nginx HTML File:
"# Command: cat index.nginx-debian.html"

# Create a New HTML File:
"# Command: echo 'i m a prince katiyar' > index.html"

# Test New HTML File:
"# Command: curl localhost"

# Bootstrap Script:
"# Bash script to automate Nginx installation and create a welcome message in index.html."
