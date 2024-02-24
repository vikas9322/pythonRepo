const express = require("express");
const app = express();

app.get("/" ,(req,res) => {
    res.send("<h1>Visiting rootby docker </h1>")

});


app.listen(8000, () => {
    console.log("App is running at 8000");
})


