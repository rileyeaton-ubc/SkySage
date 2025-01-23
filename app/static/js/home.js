import { api_routes } from "./api_routes.js";
// Function to fetch data from the backend for location coordinates
const fetchLocationCoordinates = async (search) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.LOCATION_COORDINATES_ENDPOINT, {
      params: { search },
    });
    console.log("Location Coordinates:", response.data);
    return response.data;
  } catch (error) {
    console.error("Failed to fetch location coordinates:", error);
  }
};

// Function to fetch data from the backend for autocomplete suggestions
const fetchAutoCompleteLocations = async (search) => {
  try {
    const response = await axios.get(api_routes.BASE_DOMAIN+api_routes.AUTOCOMPLETE_LOCATIONS_ENDPOINT, {
      params: { search },
    });
    console.log("Autocomplete Suggestions:", response.data);
    return response.data;
  } catch (error) {
    console.error("Failed to fetch autocomplete suggestions:", error);
  }
};

async function redirectToLocation() {
  // Get the value from the search bar
  const location = document.getElementById("search-bar").value.trim();
  
  // Ensure the input is not empty
  if (location) {
    try {
      // Fetch autocomplete suggestions and location coordinates
      console.log("Fetching data for:", location);
      
      const locationCoordinates = await fetchLocationCoordinates(location);
      console.log("Fetched Coordinates:", locationCoordinates);
      
      if (locationCoordinates) {
        // Construct the query string with location and coordinates
        const encodedLocation = encodeURIComponent(location);
        const encodedCoordinates = encodeURIComponent(JSON.stringify(locationCoordinates));
        window.location.href = `location_page.html?location=${encodedLocation}&locationCoordinates=${encodedCoordinates}`;
      } else {
        alert("Could not fetch location coordinates. Please try again.");
      }
    } catch (error) {
      console.error("Error while redirecting:", error);
      alert("An error occurred while fetching location data. Please try again.");
    }
  } else {
    // Alert the user if the search bar is empty
    alert("Please enter a location.");
  }
}

// Function to render autocomplete suggestions
const renderSuggestions = (suggestions) => {
  const suggestionsContainer = document.getElementById("suggestions");
  suggestionsContainer.innerHTML = ""; // Clear previous suggestions

  if (suggestions && suggestions.length > 0) {
    suggestionsContainer.style.visibility = "visible"; // Make container visible
    suggestions.forEach((suggestion) => {
      // Assuming `name` is the property to display; adjust as needed
      const suggestionText = suggestion.name || suggestion.label || suggestion.toString(); 
      
      const suggestionItem = document.createElement("div");
      suggestionItem.className = "suggestion-item";
      suggestionItem.textContent = suggestionText; // Use the extracted text
      
      suggestionItem.onclick = () => {
        document.getElementById("search-bar").value = suggestionText;
        suggestionsContainer.innerHTML = ""; // Clear suggestions on selection
        suggestionsContainer.style.visibility = "hidden"; // Hide container
      };

      suggestionsContainer.appendChild(suggestionItem);
    });
  } else {
    suggestionsContainer.style.visibility = "hidden"; // Hide container if no suggestions
  }
};

// Event listener for search bar input
document.getElementById("search-bar").addEventListener("input", async (event) => {
  const search = event.target.value.trim();
  if (search) {
    const suggestions = await fetchAutoCompleteLocations(search);
    renderSuggestions(suggestions);
  } else {
    const suggestionsContainer = document.getElementById("suggestions");
    suggestionsContainer.innerHTML = ""; // Clear suggestions if input is empty
    suggestionsContainer.style.visibility = "hidden"; // Hide container
  }
});

window.redirectToLocation = redirectToLocation;