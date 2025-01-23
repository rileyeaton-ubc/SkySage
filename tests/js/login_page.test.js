const { validateLoginForm } = require("../../app/static/js/login.page");
import { test_val } from "./setupTest";

describe("Create Login Form Validation Tests", () => {
    beforeEach(() => {
        setupLoginPageMockHTML(); // Set up the mock HTML before each test
    });

    test("should always return true", () => {
        expect(1 + 1).toBe(2);
    });

    test("Displays an error if the username is empty", () => {
        document.getElementById("username").value = test_val.EMPTY_STRING; // Empty username
        document.getElementById("password").value = test_val.LOGIN_PASSWORD;

        const isValid = validateLoginForm();

        expect(isValid).toBe(false);
        expect(document.getElementById("errorMessage").textContent).toBe(
            "Both username and password are required."
        );
    });

    test("Displays an error if the password is empty", () => {
        document.getElementById("username").value = test_val.LOGIN_USER;
        document.getElementById("password").value = test_val.EMPTY_STRING; // Empty password

        const isValid = validateLoginForm();

        expect(isValid).toBe(false);
        expect(document.getElementById("errorMessage").textContent).toBe(
            "Both username and password are required."
        );
    });

    test("Does not display an error when both fields are filled", () => {

        const isValid = validateLoginForm();

        expect(isValid).toBe(true);
        expect(document.getElementById("errorMessage").textContent).toBe(test_val.EMPTY_STRING);
    });
});
