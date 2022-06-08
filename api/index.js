const axios = require('axios');
const express = require('express')
const mongoose = require('mongoose');
const url = require('url')
const app = express()
app.use(express.json());


let UserSchema = new mongoose.Schema({
	name: String,
	user: String,
	pass: String
});

// ---

var User = mongoose.model('User', UserSchema);

// ---

[['Administrator', 'admin', 'admin'], ['John Smith', 'jsmith', 'password'], ['Mark Doe', 'mdoe', 'password']].forEach(function (cred) {
	var instance = new User();

	// ---

	instance.name = cred[0];
	instance.user = cred[1];
	instance.pass = cred[2];

	// ---

	instance.save();
});

app.get('/', function (req, res) {
  const token = req.header("token")
  axios.get('http://iserv:3000/verify?token=' + token)
    .then(d => {
      if (d.data["status"] === "denied") {
        return res.json({"status": "resource access denied."});
      }
      res.json({"welcome": "home"});
    });
});

app.post('/login', function (req, res) {
  const body = req.body
  User.findOne({user: body.user, pass: body.pass}, function (err, user) {
		if (err) {
			return res.status(401).json({"status": "Invalid credentials"})
		}

		// ---

		if (!user) {
			return res.status(401).json({"status": "Invalid credentials"})
		}

		// ---
    let responseData = {}
    if (body.user == "admin") {
      responseData['token'] = "adminusertoken"
    } else if (body.user == "jsmith") {
      responseData['token'] = "firstusertoken"
    } else if (body.user == "mdoe") {
      responseData['token'] = "secondusertoken"
    } else {
      responseData['token'] = "adminusertoken"
    }
		return res.json(responseData)
	});
  
});

app.get('/me', function (req, res) {
  const token = req.header("token");
  let fields = req.query.fields;
  if (!fields) {
    fields = 'name,surname';
  }

  axios.get('http://iserv:3000/verify?token=' + token)
    .then(d => {
      if (d.data["status"] === "denied") {
        return d
      } else {
        return axios.get('http://iserv:3000/identity?fields=' + fields + '&id=' + d.data["id"])
        //return axios.get('http://iserv:3000/identity', { params: {fields: fields, id: d.data["id"]}})
      }
    })
    .then(d => {
      console.log(d.data);
      res.json(d.data);
  });
});

app.get('/resource', function (req, res) {
  const token = req.header("token")
  let rid = req.query.rid;
  if ((rid !== '1') || (token === null)) {
    return res.status(401).json({"status": "resource access denied."});
  }

  axios.get('http://rserv:3000/resource?token=' + token + '&rid=' + rid)
  //axios.get('http://rserv:3000/resource', { params: {token: token, rid: rid}})
  .then(d => {
    console.log(d.data);
    res.json(d.data);
  });
});

app.get('/thirdparty', function (req, res) {
  const token = req.header("token")
  let rid = req.query.rid;
  if (Object.prototype.toString.call(rid) === '[object Array]') {
    rid = rid[0]
  }
  let all_params = url.parse(req.url).query;
  if ((rid !== '1') || (token === null)) {
    return res.status(401).json({"status": "resource access denied."});
  }

  axios.get('http://tserv:80/api/test?' + all_params)
  .then(d => {
    console.log(d.data);
    res.json(d.data);
  });
});

app.get('/funky', function (req, res) {
  const token = req.header("token")
  let rid = req.query.rid
  if (Object.prototype.toString.call(rid) === '[object Array]') {
    console.log(rid)
    rid = rid[0]
  }
  res.json(rid);
});

app.get('/corebank', function (req, res) {
  const token = req.header("token")
  let rid = req.query.rid;
  let crid = ""
  if (Object.prototype.toString.call(rid) === '[object Array]') {
    crid = rid[0]
  } else {
    crid = rid
  }

  if ((crid !== '1') || (token === null)) {
    return res.status(401).json({"status": "resource access denied."});
  }
  axios.get('http://cserv:80/WeatherForecast?rid=' + rid.toString())
  .then(d => {
    console.log(d.data);
    res.json(d.data);
  });
});

app.post('/linkaccount', function (req, res) {
  const token = req.header("token")
  const body = req.body
  let rid = body.customerId
  let linkedAcnt = body.linkedAcnt
  let newLkAcnt = []

  if ((rid !== '1') || (token === null)) {
    return res.status(401).json({"status": "resource access denied."});
  }

  axios.get('http://cserv:80/WeatherForecast?rid=' + rid + '&linkedAcnt=' + linkedAcnt)
  .then(d => {
    d.data.forEach(acnt => {
      newLkAcnt.push(acnt['customerId'])
    });
    res.json({
      "customerIdLinked": newLkAcnt,
      "accountToLink": linkedAcnt 
    });
  });
});

app.listen(3000, () => {
  mongoose.connect('mongodb://localhost/acme-no-login');
  console.log('Server started on 3000')
});