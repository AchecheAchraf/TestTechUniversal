# Use Node.js as base image for build stage
FROM node:20.11.0-alpine as build-stage
WORKDIR /app

# Copy package.json and package-lock.json to work directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files from current directory to work directory
COPY . .

# Build the Vue.js application
RUN npm run build

# Production environment
FROM nginx:stable-alpine as production-stage

# Copy build output from build stage to Nginx web directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
