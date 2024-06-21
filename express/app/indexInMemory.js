const express = require("express");
const fs = require("fs");

let largeFile;

fs.readFile('app/resources/large-file.json', 'utf8', (err, data) => {
  if(!err) {
    largeFile = data;
  } else {
    console.log(err)
    res.send({message: "Error reading file: " + err.message});
  }
});

const app = express();

app.get("/file/open", (req, res) => {
  res.send(largeFile);
});

app.get("/hello", (req, res) => {
  res.send("Hello World");
});

app.listen(8080);
console.log("Express started on port 8080");
