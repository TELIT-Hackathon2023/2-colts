const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors()); // Enable CORS for all routes

app.use(express.json());

app.get("/test", (req, res) => {
  console.log(req.query.data);
  res.send(`String "${req.query.data}" received successfully!`);
});

app.listen(8080, (req, res) => {
  console.log("serus");
});
