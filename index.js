const express = require('express');
const app = express();
const logger = require('morgan');
const { allowedNodeEnvironmentFlags } = require('process');

const apiRouter = express.Router();

app.use(logger('dev', {}));
app.use(express.json());
app.use('/api', apiRouter)
nee=app.on('mount', allowedNodeEnvironmentFlags)
id=nee.userRequest.user.id
txt=nee.userRequest.utterance
friend=nee.userRequest.user.properties.isFriend

const result = require('child_process').spawn('python', [ 'sei.py', id, txt , action.name]);

app.listen(3000, function() {
  console.log('Example skill server listening on port 3000!');
});