// User Favourites Locations will be stored here placeholder for now
const favoriteLocations = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
  ];
  
  // Initial verfication test will be changed when we have actual User Database
  const userToEmail = {
    john_doe: "john.doe@example.com",
    jane_smith: "jane.smith@example.com",
    mike89: "mike89@example.com",
    emma_w: "emma.w@example.com",
  };
  
  function displayFavorites() {
    // Function to Display the User's Favourite Locations
    const container = document.getElementById("favorites-container");
    container.innerHTML = ""; // Clear the container
  
    if (favoriteLocations.length === 0) {
      // Show a message if there are no favorites
      container.innerHTML =
        '<p class="no-favorites">No favorite locations yet. Add some from the location page!</p>';
      return;
    }
  
    // Create favorite location items
    favoriteLocations.forEach((location, index) => {
      const item = document.createElement("div");
      item.className = "favorite-item";
  
      const name = document.createElement("span");
      name.className = "favorite-name";
      name.textContent = location;
  
      const removeButton = document.createElement("button");
      removeButton.className = "remove-button";
      removeButton.textContent = "Remove";
      removeButton.onclick = () => removeFavorite(index);
  
      item.appendChild(name);
      item.appendChild(removeButton);
      container.appendChild(item);
    });
  }
  
  function removeFavorite(index) {
    // Function to Remove a Favourite Location
    favoriteLocations.splice(index, 1); // Remove the location
    displayFavorites(); // Refresh the list
    alert("Location removed from favorites.");
  }
  
  function shareDashboard() {
    // Function to Share the User's Dashboard
    const username = document.getElementById("username-input").value.trim();
  
    if (!username) {
      alert("Please enter a username.");
      return;
    }
  
    // Check if username exists in the mapping
    const email = userToEmail[username];
    if (!email) {
      alert("Username not found. Please check and try again.");
      return;
    }
  
    // Simulate sending an email
    alert(`Dashboard shared with ${username} (${email})!`);
    console.log(`Sending dashboard link to: ${email}`);
  
    // Backend or API integration would go here to actually send the email
  }
  
  // Display the initial list of favorite locations
  if (document.getElementById("dashboard")) {
    displayFavorites();
  }