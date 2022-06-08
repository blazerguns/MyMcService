FROM node:9.11-alpine

EXPOSE 3000
RUN mkdir -p /app && chown -R node /app

COPY package.json yarn.lock /tmp/
RUN cd /tmp && yarn install && yarn cache clean && mv /tmp/node_modules /app/
RUN apk add --no-cache mongodb
WORKDIR /app
COPY . /app
RUN mkdir -p /data/mongodb && chmod +x /app/start.sh

CMD ["./start.sh"]

