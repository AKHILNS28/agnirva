const axios = require('axios');

const apiKey = 'YOUR_REAL_API_KEY_HERE'; // Replace with your API key
const city = 'London';

const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`;

axios.get(apiUrl)
  .then(response => {
    console.log('Success:', response.data);
  })
  .catch(error => {
    console.error('Error:', error.response?.data || error.message);
  });
