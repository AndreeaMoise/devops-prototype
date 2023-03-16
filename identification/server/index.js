var express = require('express');
var cors = require('cors');
var bodyParser = require('body-parser');
var routes = require('./routes/tracking.routes');

var app = express();
var port = 3000;

app.use(cors());
app.use(bodyParser.json({limit: '50mb', type: 'application/json'}));
app.use('/', routes);

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});