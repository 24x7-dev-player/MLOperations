# --------------Buiild Docker Image

# Use an official Node.js runtime as a parent image
FROM node:14
# Set the working directory
WORKDIR /usr/src/app
# Copy the package.json and package-lock.json files
COPY package*.json ./
# Install the dependencies
RUN npm install
# Copy the rest of the application code
COPY..
# Expose the port the app runs on
EXPOSE 8080
# Define the command to run the application
CMD ["node", "app.js"]



# Build the docker Image
docker build -t myapp:latest .

#Test the docker Image Locally
docker run -d -p 8080:8080 myapp:latest

#Push the docker to container registry
docker login

docker tag myapp:latest myregistry.com/myapp:latest
docker push myregistry.com/myapp:latest
docker run -d -p 80:8080 <Your-dockerhub username>/myapp:latest