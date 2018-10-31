const path = require('path');

var mode = 'production';
var publicPath = '/static/';
if (!process.env.BUILD) {
  mode = 'development';
  publicPath = 'http://localhost:8001' + publicPath
}


module.exports = {
  mode: mode,
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'build/'),
    publicPath: publicPath,
  },
  resolve: {
    extensions: ['.js'],
  },
  module: {
    rules: [
      {
        test: /\.styl$/,
        use: ['style-loader', 'css-loader', 'stylus-loader'],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.(jpe?g|png|gif)$/,
        loader: 'file-loader?name=images/[name].[hash].[ext]'
      },
      {
        test: /\.(eot|ttf|ijmap|woff|woff2|svg)$/,
        loader: 'file-loader?name=fonts/[name].[hash].[ext]'
      },
    ],
  },
  devtool: '#eval-source-map',
};
