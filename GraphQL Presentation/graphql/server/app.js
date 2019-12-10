const express = require('express');
const graphqlHTTP = require('express-graphql');
const schema = require('./schema/schema');
const mongoose = require('mongoose');

const app = express();

//mongoose.connect('mongodb+srv://garrett:<forthehorde4311>@garrett-wjlxt.mongodb.net/Garrett?retryWrites=true&w=majority');
mongoose.connect('mongodb://garrett:forthehorde4311@garrett-shard-00-00-wjlxt.mongodb.net:27017,garrett-shard-00-01-wjlxt.mongodb.net:27017,garrett-shard-00-02-wjlxt.mongodb.net:27017/Garrett?ssl=true&replicaSet=Garrett-shard-0&authSource=admin&retryWrites=true&w=majority');
mongoose.connection.once('open', () => {
  console.log('connected to database');
});

app.use('/graphql', graphqlHTTP({
  schema,
  graphiql: true
}));

app.listen(4000,()=>{
  console.log('now listening for requests on port 4000');
})
