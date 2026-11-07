const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const FLASK_URL = process.env.FLASK_URL || 'http://localhost:5000';

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/', async (req, res) => {
    try {
        res.sendFile(path.join(__dirname, 'views', 'todo.html'));
    } catch (err) {
        res.status(500).send("Error loading page");
    }
});

app.post('/submittodoitem', async (req, res) => {
    try {
        const response = await axios.post(`${FLASK_URL}/submittodoitem`, new URLSearchParams(req.body), {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(500).send({ error: "Failed to communicate with Flask backend" });
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Express frontend running on port ${PORT}`);
});