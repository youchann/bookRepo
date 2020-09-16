const webpack = require("webpack");
const path = require("path");
const WebpackBar = require("webpackbar"); // プログレスバーを表示してくれるやつ
const HtmlWebpackPlugin = require("html-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const ForkTsCheckerWebpackPlugin = require("fork-ts-checker-webpack-plugin"); // 構文チェックをしてくれるやつ

const IS_PRODUCTION = process.env.NODE_ENV === "production";
const outputPath = path.resolve(__dirname, "dist"); // このファイルが存在するディレクトリの名前(__dirname)/distを絶対パスで出力

/**
 * @type import('webpack').Configuration
 */
module.exports = {
  target: "web", // default
  mode: IS_PRODUCTION ? "production" : "development",
  entry: path.resolve(__dirname, "src/index.tsx"),
  output: {
    path: outputPath, // 実際に配置するパス
    publicPath: "/", // 外すと/loginとかでアクセスされた際outputPath/login/bundle.jsを参照してしまう
    filename: "bundle.js", // default
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx", ".json"],
    modules: ["node_modules"],
  },
  devtool: "eval-source-map", // error時にバンドル前のソースコードを見せてくれる
  devServer: {
    contentBase: outputPath, // 絶対パス推奨
    port: 9000,
    historyApiFallback: true, // これがないとルーティングできないらしい
    hot: true, // バンドル後、変更のあったコンポーネントのみをリロードする
    inline: true, // バンドル後、変更があった場合ページ全体をリロード
    watchContentBase: true, // contentBase配下で変更があった場合リロード
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        exclude: [/node_modules/],
        use: [
          {
            loader: "babel-loader",
          },
          {
            loader: "ts-loader",
            options: {
              // MEMO: トランスパイル後にbabelを噛ませているので、設定は再考する余地がある
              configFile: "tsconfig.json",
              transpileOnly: true,
              happyPackMode: true,
            },
          },
        ],
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[path][name].[ext]",
            },
          },
        ],
      },
      {
        test: /\.svg$/,
        use: [
          {
            loader: "react-svg-loader",
          },
        ],
      },
    ],
  },
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin()],
  },
  plugins: [
    new WebpackBar(),
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: "./src/index.html",
      filename: "./index.html",
    }),
    new ForkTsCheckerWebpackPlugin({
      eslint: true,
    }),
    new webpack.DefinePlugin({
      "process.env.API_URL": JSON.stringify(
        IS_PRODUCTION ? process.env.API_URL : "http://localhost:5000",
      ),
    }),
  ],
};
