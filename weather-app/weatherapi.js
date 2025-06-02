const express = require('express');
const axios = require('axios');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Manually serve static assets
app.use('/weather.css', express.static(path.join(__dirname, 'weather.css')));
app.use('/weather.js', express.static(path.join(__dirname, 'weather.js')));

// Serve the HTML page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'weather.html'));
});

// Weather API route
app.get('/weather', async (req, res) => {
  const city = req.query.city;
  const apiKey = process.env.OPENWEATHER_API_KEY;

  if (!city) {
    return res.status(400).json({ error: 'City is required' });
  }

  try {
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`;
    const response = await axios.get(apiUrl);
    const weather = response.data;

    res.json({
      city: weather.name,
      temperature: weather.main.temp,
      condition: weather.weather[0].main,
      humidity: weather.main.humidity,
      windSpeed: weather.wind.speed,
    });
  } catch (error) {
    console.error(error.response?.data || error.message);
    if (error.response?.status === 404) {
      res.status(404).json({ error: 'City not found' });
    } else {
      res.status(500).json({ error: 'Failed to fetch weather data' });
    }
  }
});

app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
