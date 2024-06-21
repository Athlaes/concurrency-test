let axios = require("axios")

console.time("First call")
axios.get("http://localhost:8080/file/open").then(res => {
    console.timeEnd("First call")
}).catch(() => console.log("failure"));

console.time("Second call")
axios.get("http://localhost:8080/file/open").then(res => {
    console.timeEnd("Second call")
}).catch(() => console.log("failure"));

console.time("Hello")
axios.get("http://localhost:8080/hello").then(res => {
    console.timeEnd("Hello")
}).catch(() => console.log("failure"));
