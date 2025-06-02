console.log("✅ JS Loaded");

document.getElementById("getWeather").addEventListener("click", async () => {
  const city = document.getElementById("city").value.trim();
  const resultDiv = document.getElementById("result");

  if (!city) {
    resultDiv.textContent = "Please enter a city name.";
    return;
  }

  try {
    const res = await fetch(`/weather?city=${encodeURIComponent(city)}`);
    const data = await res.json();

    if (!res.ok) {
      resultDiv.textContent = data.error || "Error fetching weather";
      return;
    }

    resultDiv.innerHTML = `
      <h2>Weather in ${data.city}</h2>
      <p>Temperature: ${data.temperature} °C</p>
      <p>Condition: ${data.condition}</p>
    `;
  } catch (err) {
    console.error(err);
    resultDiv.textContent = "Something went wrong.";
  }
});
