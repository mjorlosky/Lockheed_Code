const express = require("express");
const app = express();

app.use((req,res) => {
    res.send('<h1>This is my webpage!</h1>')
})
app.listen(3000, () => {
    console.log("LISTENING ON 3000")
})