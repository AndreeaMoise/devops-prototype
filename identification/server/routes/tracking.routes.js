var express = require('express');
var router = express.Router();

var TrackingController = require('../controllers/tracking.controller');

router.post('/verifyUser', TrackingController.verifyUser)
router.post('/identification', TrackingController.identification)

module.exports = router;