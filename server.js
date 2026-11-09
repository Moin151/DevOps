const express = require('express');
const axios = require('axios');
const app = express();

const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://backend-service:5000';

// Middleware to parse URL-encoded form data and JSON
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve the To-Do form
app.get('/', (req, res) => {
    res.send(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Express to Flask To-Do Form</title>
</head>
<body>
    <h2>Add To-Do Item (Via Express Frontend)</h2>
    <form method="POST" action="/submittodoitem">
        <label for="itemName">Item Name:</label><br>
        <input type="text" id="itemName" name="itemName" required><br><br>
        
        <label for="itemDescription">Item Description:</label><br>
        <textarea id="itemDescription" name="itemDescription" required></textarea><br><br>
        
        <button type="submit">Submit to Backend</button>
    </form>
</body>
</html>`);
});

// Handle form submission and forward to Flask backend
app.post('/submittodoitem', async (req, res) => {
    try {
        const { itemName, itemDescription } = req.body;
        await axios.post(`${BACKEND_URL}/submittodoitem`, {
            itemName: itemName,
            itemDescription: itemDescription
        });
        res.send(`<h3>Item added successfully!</h3><a href="/">Go Back</a>`);
    } catch (error) {
        console.error('Error communicating with backend:', error.message);
        res.status(500).json({ error: "Failed to communicate with Flask backend" });
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Frontend server running on port ${PORT}`);
});
