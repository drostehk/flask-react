var path = require('path');



module.exports = {
  cache: true,
  entry: [
    './reactjs/index.js'
  ],
  output: {
    path: path.join(__dirname, 'static', 'js'),
    filename: 'index_bundle.js'
  },
  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader' }
    ]
  },
  plugins: []
};
