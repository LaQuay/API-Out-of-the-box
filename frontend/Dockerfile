FROM node:8.15.1-alpine

#ADD yarn.lock /yarn.lock
ADD package.json /package.json

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin
RUN yarn

WORKDIR /app
ADD . /app

ENTRYPOINT ["/bin/sh", "/app/run.sh"]
