const express = require('express')
const app = express()

const identities = require('./identities.json');

const validTokens = {
  'firstusertoken': 1,
}

function getUserForToken(token) {
  if (validTokens[token]) {
    return validTokens[token];
  }
  return null;
}

function filterFields(obj, fields) {
  if (fields === '*') {
    return obj
  }
  let result = {};
  fields.split(',').forEach(field => {
    result[field] = obj[field];
  });
  return result;
}

app.get('/identity', function (req, res) {
  const id = parseInt(req.query.id, 10);
  const fields = req.query.fields;
  const identity = identities.find(identityObject => identityObject.id === id);
  return res.json(filterFields(identity, fields));
});

app.get('/verify', function (req, res) {
  const token = req.query.token;
  const id = getUserForToken(token);
  if (!id) {
    return res.json({"status": "denied"});
  }
  res.json({"status": "granted", "id": id});
});

app.listen(3000, () => console.log('Server started on 3000'));