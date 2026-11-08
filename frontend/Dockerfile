FROM node:18-alpine
WORKDIR /app
<<<<<<< HEAD
COPY package*.json ./
RUN npm install
COPY . .
=======

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy source files
COPY . .

>>>>>>> a7c09ad (Update frontend configuration for separate EC2 backend IP)
ENV PORT=3000
EXPOSE 3000
CMD ["npm", "start"]