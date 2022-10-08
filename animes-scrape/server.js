require('dotenv').config();
const express = require('express');
const app = express();
const runPuppeteer = require('./src');

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/scrap', async (req, res) => {
    let data = await runPuppeteer(req.body);
    return res.json(data);
});

app.listen(process.env.PORT, function () {
    console.log(`app listening on port ${process.env.PORT}`)
})