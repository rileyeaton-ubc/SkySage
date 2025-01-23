// tests/js/setupTests.js
import '@testing-library/jest-dom';

// Global setup for tests
beforeEach(() => {
    // Reset the DOM before each test
    document.body.innerHTML = "";
});

// Example: A helper function to set up the mock HTML for the account page
global.setupAccountPageMockHTML = () => {
    document.body.innerHTML = `
        <form id="createAccountForm">
            <input id="username" type="text" />
            <input id="email" type="email" />
            <input id="password" type="password" />
            <input id="confirmPassword" type="password" />
            <button id="submit">Submit</button>
            <div id="errorMessage" style="color: red;"></div>
        </form>
    `;

};

// Example: A helper function to set up the mock HTML for the login page
global.setupLoginPageMockHTML = () => {
    document.body.innerHTML = `
    <form id="loginForm">
         <input type="text" id="username" name="username" placeholder="Username">
         <input type="password" id="password" name="password" placeholder="Password">
         <button type="submit" id="loginButton">Login</button>
         <div id="errorMessage" style="color: red;"></div>
    </form>
    `;
};

export var test_val = {
    USERNAME: "user123",
    EMAIL: "user@example.com",
    PASSWORD: "password123",
    CONFIRM_PASSWORD: "password456",
    LOGIN_USER: "testuser",
    LOGIN_PASSWORD: "testpassword",
    EMPTY_STRING: "",
    ERROR_MESSAGE: "This is error message",
}

