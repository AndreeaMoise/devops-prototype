'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.identify = function identify (req, res, next, body) {
  Default.identify(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.verifyImage = function verifyImage (req, res, next) {
  // Default.verifyImage()
  //   .then(function (response) {
  //     utils.writeJson(res, response);
  //   })
  //   .catch(function (response) {
  //     utils.writeJson(res, response);
  //   });
  verifyImage()
    .then(() => {
      console.log('something');
    })
};
