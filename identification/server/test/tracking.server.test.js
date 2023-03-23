var TrackingService = require('../services/tracking.service');
var axios = require("axios");
var MockAdapter = require("axios-mock-adapter");
var assert = require('assert');

var mock = new MockAdapter(axios);

beforeEach(() => {
  mock.reset();
})

const url = "https://xpks7yhjdf.execute-api.us-east-1.amazonaws.com/Production";

describe('TrackingService API', () => {
  it('/verifyimage should get succesful response', () => {
    const image = '1234';
    const response = {
      statusCode: 200,
      body: '456'
    };

    mock.onPost(url + '/verifyimage').reply(200, response);

    return TrackingService.verifyUser(image).then(result => {
      assert.equal(result.status, 200);
      assert.equal(result.id, response.body);
    });
  });

  it('/verifyimage should get unsuccesful response', () => {
    const image = '1234';
    const response = {
      statusCode: 404
    };

    mock.onPost(url + '/verifyimage').reply(200, response);

    return TrackingService.verifyUser(image).then(result => {
      assert.equal(result.status, 401);
    });
  });

  it('/trace should get succesful response', () => {
    const trace = {
      truckId: '213456789',
      load: [
        {
          "sku": "124AB",
          "quantity": 28
        }],
      location: {
        latitude: null,
        longitude: null
      },
      driverId: '1234'
    };

    const response = {
      statusCode: 200
    };

    mock.onPost(url + '/trace').reply(200, response);

    return TrackingService.identification(trace).then(result => {
      assert.equal(result.status, 200);
    });
  });

  it('/trace should get bad request', () => {
    const trace = {};
    const response = {
      statusCode: 200
    };

    mock.onPost(url + '/trace').reply(200, response);

    return TrackingService.identification(trace).then(result => {
      assert.equal(result.status, 400);
    });
  });

  it('/trace should get unsuccesful response', () => {
    const trace = {
      truckId: '213456789',
      load: [
        {
          "sku": "124AB",
          "quantity": 28
        }],
      location: {
        latitude: null,
        longitude: null
      }, driverId: '12345'
    };
    const response = {
      statusCode: 404
    };

    mock.onPost(url + '/trace').reply(200, response);

    return TrackingService.identification(trace).then(result => {
      assert.equal(result.status, 404);
    });
  });
});
