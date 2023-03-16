var axios = require('axios');

exports.verifyUser = async function (image) {
    return axios.post('https://xpks7yhjdf.execute-api.us-east-1.amazonaws.com/Production/verifyimage', {
        image: image
    }).then(function (response) {
        if (response.data.statusCode === 200) {
            return {
                status: 200,
                id: response.data.body
            };
        } else if (response.data.statusCode === 404) {
            return {
                status: 401
            };
        }
    }).catch(function (error) {
        console.error(error);
        throw Error(error);
    });
}

exports.identification = async function (trace) {
    try {
        throw Error("Not implemented");
    } catch (error) {
        console.error(error);
        throw Error(error);
    }
}