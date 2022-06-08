#!/bin/ash
mongod --fork --dbpath /data/mongodb --logpath /var/log/mongod.log
node index.js