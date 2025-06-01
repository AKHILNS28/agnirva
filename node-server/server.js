const express = require("express");
const app = express();

console.log("Starting server...");

app.get("/", (req, res) => {
    console.log("Received request to /");
    res.send("Hello, World");
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`The server is running on http://localhost:${PORT}`);
});

app.get("/greet/:name", (req, res) => {
    const name = req.params.name;
    res.send(`Hello, ${name}! Welcome to our server.`);
});