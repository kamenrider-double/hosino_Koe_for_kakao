const express = require('express');
const app = express();
const logger = require('morgan');

const apiRouter = express.Router();

app.use(logger('dev', {}));
app.use(express.json());
app.use('/api', apiRouter)

const result = require('child_process').spawn('python', [ 'sei.py', userRequest.user.id, userRequest.utterance , action.name]);

app.listen(3000, function() {
  console.log('Example skill server listening on port 3000!');
});