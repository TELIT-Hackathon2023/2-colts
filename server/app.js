const express = require("express");

const app = express();

app.get("/test", (req, res) => {
    console.log(req);
    console.log(res);
    res._write(req);
});

app.listen(8080, (req, res) => {
    console.log("serus")
});