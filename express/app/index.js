const express = require("express");
const fs = require("fs");

const app = express();

app.get("/file/open", (req, res) => {
  console.log("Starting reading file...");
  fs.readFile('app/resources/large-file.json', 'utf8', (err, data) => {
    console.log("Ended reading file...");
    if(!err) {
      res.send(data);
    } else {
      console.log(err)
      res.send({message: "Error reading file: " + err.message});
    }
  });
});

app.get("/hello", (req, res) => {
  res.send("Hello World");
});

app.listen(8080);
console.log("Express started on port 8080");
