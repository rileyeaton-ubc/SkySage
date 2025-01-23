import { fetchLocationCurrentWeather, fetchLocationForecastWeather, fetchForecastAIGeneration } from "./api_functions.js";

function displayCurrentWeather(weather_data) {
  // Populate current weather section
  const currentWeatherDiv = document.getElementById("current-weather");
  currentWeatherDiv.innerHTML = ""; // Clear existing content

  const currentWeatherInfo = `
      <div class="weather-info">
          <div class="weather-item">Current Temperature: ${weather_data.temperature.toFixed(1)}°C</div>
          <div class="weather-item">Max Temperature: ${weather_data.temp_max.toFixed(1)}°C, Min Temperature: ${weather_data.temp_min.toFixed(1)}°C</div>
          <div class="weather-item">Feels Like: ${weather_data.feels_like.toFixed(1)}°C</div>
          <div class="weather-item">Conditions: ${weather_data.conditions}</div>
          <div class="weather-item">Humidity: ${weather_data.humidity}%</div>
          <div class="weather-item">Wind: ${weather_data.wind_speed.toFixed(1)} km/h, Direction: ${weather_data.wind_direction}°</div>
          <div class="weather-item">Pressure: ${weather_data.pressure} hPa</div>
      </div>
  `;
  currentWeatherDiv.innerHTML = currentWeatherInfo;
}

function formatDate(date) {
  // Get current date in JS
  const today = new Date();
  
  // Create a date object from the date string passed
  const dateObj = new Date(date);

  // Check if the date is today
  if (dateObj.getDate() === today.getDate()) {
      return "Today";
  }

  // Check if the date is tomorrow
  today.setDate(today.getDate() + 1);
  if (dateObj.getDate() === today.getDate()) {
      return "Tomorrow";
  }

  // Return the passed in the format "Month Day" with the correct postfix (e.g. 1st, 2nd, 3rd)
  const day = dateObj.getDate();
  let postfix = "th";
  if (day === 1 || day === 21 || day === 31) {
      postfix = "st";
  } else if (day === 2 || day === 22) {
      postfix = "nd";
  } else if (day === 3 || day === 23) {
      postfix = "rd";
  }
  return `${dateObj.toLocaleString("default", { month: "short" })} ${day}${postfix}`;
}

function displayForecastWeather(weather_data) {
  // Populate forecast section
  const forecastWeatherDiv = document.getElementById("forecast");
  forecastWeatherDiv.innerHTML = ""; // Clear existing content

  const forecastArray = weather_data.forecast_list;
  const groupedForecasts = {};

  // Group forecasts by date and calculate averages
  forecastArray.forEach(forecastItem => {
      var date = formatDate(forecastItem.date_string);
      if (!groupedForecasts[date]) {
          groupedForecasts[date] = {
              temperature: 0,
              feels_like: 0,
              humidity: 0,
              cloud_cover_percent: 0,
              chance_of_precipitation: 0,
              wind_speed: 0,
              wind_direction: 0,
              conditions: {},
              count: 0,
          };
      }
      const group = groupedForecasts[date];
      group.temperature += forecastItem.temperature;
      group.feels_like += forecastItem.feels_like;
      group.humidity += forecastItem.humidity;
      group.cloud_cover_percent += forecastItem.cloud_cover_percent;
      group.chance_of_precipitation += forecastItem.chance_of_precipitation;
      group.wind_speed += forecastItem.wind_speed;
      group.wind_direction += forecastItem.wind_direction;

      const condition = forecastItem.conditions.toLowerCase();
      group.conditions[condition] = (group.conditions[condition] || 0) + 1;
      group.count++;
  });

  // Generate forecast HTML
  const dates = Object.keys(groupedForecasts);
  for (let i = 0; i < 5; i++) {
      const date = dates[i];
      const group = groupedForecasts[date];
      const majorityCondition = Object.keys(group.conditions).reduce((a, b) =>
          group.conditions[a] > group.conditions[b] ? a : b
      );

      const forecastInfo = `
          <div class="forecast-item">
              <strong>${date}</strong>
              <div>Temperature: ${(group.temperature / group.count).toFixed(1)}°C</div>
              <div>Feels Like: ${(group.feels_like / group.count).toFixed(1)}°C</div>
              <div>Conditions: ${majorityCondition}</div>
              <div>Humidity: ${(group.humidity / group.count).toFixed(1)}%</div>
              <div>Wind: ${(group.wind_speed / group.count).toFixed(1)} km/h</div>
          </div>
      `;
      forecastWeatherDiv.innerHTML += forecastInfo;
  }
  forecastWeatherDiv.innerHTML += `<div id="pre-generation" class="summary-header">Generating AI Summary...</div>`;
}

function displayAIGeneratedSummary(ai_data) {
  // Populate AI summary section
  const generatingAIMessage = document.getElementById("pre-generation");
  const aiSummaryDiv = document.getElementById("forecast"); // Keep it in the Forecast tab
  aiSummaryDiv.removeChild(generatingAIMessage);
  const aiGeneratedSummary = `
      <div class="summary-header">Weather Forecast AI Summary</div>
      <div class="summary-data">${ai_data.ai_generation}</div>
  `;
  aiSummaryDiv.innerHTML += aiGeneratedSummary;
}

function switchTab(tabId) {
  const tabs = document.querySelectorAll(".tab");
  const contents = document.querySelectorAll(".tab-content");

  // Hide all tab contents and deactivate tabs
  tabs.forEach(tab => tab.classList.remove("active"));
  contents.forEach(content => content.classList.remove("active"));

  // Show the selected tab's content and activate the tab
  document.querySelector(`button[onclick="switchTab('${tabId}')"]`).classList.add("active");
  document.getElementById(tabId).classList.add("active");
}
  
function toggleFavorite() {
    /* Function to Toggle your Favourite Location */
    const heartIcon = document.getElementById("favorite-icon");
    heartIcon.classList.toggle("favorited");

    if (heartIcon.classList.contains("favorited")) {
    heartIcon.innerHTML = "&#9829;"; // Filled heart
    alert("Location added to favorites!");
    } else {
    heartIcon.innerHTML = "&#9825;"; // Outlined heart
    alert("Location removed from favorites.");
    }
}


document.addEventListener('DOMContentLoaded', async function() {

  const weatherInfo = `<div class="weather-info"><div class="weather-item">Loading...</div></div>`;

  const forecastWeatherDiv = document.getElementById("forecast");
  forecastWeatherDiv.innerHTML = ""; // Clear existing content
  forecastWeatherDiv.innerHTML = weatherInfo;

  const currentWeatherDiv = document.getElementById("current-weather");
  currentWeatherDiv.innerHTML = ""; // Clear existing content
  currentWeatherDiv.innerHTML = weatherInfo;

  // Function to get the query parameter
  function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
  }

  // Get the 'location' and 'locationCoordinates' query parameters
  const location = getQueryParam("location");
  const locationCoordinates = getQueryParam("locationCoordinates");



  if (location && locationCoordinates) {
    const decodedLocation = decodeURIComponent(location);
    const coordinates = JSON.parse(decodeURIComponent(locationCoordinates));
    const { latitude, longitude } = coordinates;

    // Update the title and header with the location
    document.title = `${decodedLocation} - Weather Info`;
    document.getElementById("location-name").textContent = decodedLocation;

    // Fetch weather data using the coordinates
    const current_data = await fetchLocationCurrentWeather(latitude, longitude);
    console.log("Fetched Current Weather Data:", current_data);
    displayCurrentWeather(current_data);
    const forecast_data = await fetchLocationForecastWeather(latitude, longitude);
    console.log("Fetched Forecast Weather Data:", forecast_data);
    displayForecastWeather(forecast_data);
    const ai_generation_data = await fetchForecastAIGeneration(forecast_data);
    console.log("Fetched Forecast Weather Data:", ai_generation_data);
    displayAIGeneratedSummary(ai_generation_data);
 } else {
     //Handle case where no location is provided
   alert("No location or coordinates provided!");
  }
});
  

window.switchTab = switchTab;
window.toggleFavorite = toggleFavorite;