const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const router = express.Router();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.resolve(__dirname, "../dist")));

router.get("*", async (_req, res) => {
  res.sendFile(path.resolve(__dirname, "../dist/index.html"));
});

app.use("/", router);

app.listen(process.env.PORT || 3000, () => {
  console.log(`listening on port ${process.env.PORT || 3000}`);
});
