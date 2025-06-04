const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const path = require("path");
const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use(express.static(__dirname));
let posts = [];
app.get("/posts", (req, res) => {
  res.json(posts);
});
app.post("/posts", (req, res) => {
  const { title, content } = req.body;
  const id = Date.now(); // Unique ID
  posts.push({ id, title, content });
  res.status(201).json({ message: "Post created successfully" });
});
app.delete("/posts/:id", (req, res) => {
  const id = parseInt(req.params.id);
  posts = posts.filter((post) => post.id !== id);
  res.json({ message: "Post deleted successfully" });
});
const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));