'use strict';
const https = require('https');

/**
 * Verify whether the driver, truck, load and location sent at a checkpoint match
 *
 * body Identification  (optional)
 * no response value expected for this operation
 **/
exports.identify = function (body) {
  return new Promise(function (resolve, reject) {
    resolve();
  });
}


/**
 *
 * returns String
 **/
exports.verifyImage = function () {
  const options = {
    host: 'https://xpks7yhjdf.execute-api.us-east-1.amazonaws.com/Production/', //URL
    path: '/verifyimage', // Path
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json; charset=UTF-8'
    }
  };

  return new Promise(function (resolve, reject) {
    const postData = JSON.stringify({
      'msg' : 'Hello World!'
  });
    const request = https.request(options, (res) => {
      if (res.statusCode === 200) {
        resolve();
      } else if (res.statusCode === 404) {
        resolve();
      }
    });
  });
}

