#docker run -p "127.0.0.1:8080:3000" -d app
# pull official base image
FROM node:21.5.0-alpine

# set working directory
WORKDIR /app

COPY public/ /app/public
COPY src/ /app/src
COPY package.json /app/
COPY package-lock.json /app/
# install app dependencies

RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# start app
CMD ["npm", "start"]