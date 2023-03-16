var TrackingService = require('../services/tracking.service')    

exports.verifyUser = async function (req, res, next) {
    try {
        var response = await TrackingService.verifyUser(req.body.image);
        return res.status(response.status).json({ id: response.id });
    } catch (e) {
        return res.status(500).json({ status: 500, message: "Cannot verify user" });
    }
}

exports.identification = async function (req, res, next) {
    try {
        var response = await TrackingService.identification(req.body);
        // #TODO
        return res.status(response.status).json({ data: response });
    } catch (e) {
        return res.status(500).json({ status: 500, message: "Cannot store identification" });
    }
}
