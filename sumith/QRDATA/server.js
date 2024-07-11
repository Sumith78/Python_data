// server.js
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

mongoose.connect('mongodb://localhost:27017/qrData', { useNewUrlParser: true, useUnifiedTopology: true });

const userSchema = new mongoose.Schema({
    name: String,
    contact: String,
    details: String
});

const User = mongoose.model('User', userSchema);

app.post('/submit', (req, res) => {
    const newUser = new User({
        name: req.body.name,
        contact: req.body.contact,
        details: req.body.details
    });

    newUser.save((err) => {
        if (err) {
            res.status(500).send('Error saving user data.');
        } else {
            res.status(200).send('User data saved successfully.');
        }
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
