FROM node:13.12.0-alpine

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY ./frontend .

EXPOSE 3001


CMD ["npm", "start"]
