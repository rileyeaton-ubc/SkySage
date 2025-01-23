const { validateCreateAccountForm } = require("../../app/static/js/createAccount");
import { test_val } from "./setupTest";
describe("Create Account Form Validation Tests", () => {
    beforeEach(() => {
        setupAccountPageMockHTML(); // Set up the mock HTML before each test
    });

    test("should always return true", () => {
        expect(1 + 1).toBe(2);
    });

    test("should return true for valid inputs", () => {
        document.querySelector("#username").value = test_val.USERNAME;
        document.querySelector("#email").value = test_val.EMAIL;
        document.querySelector("#password").value = test_val.PASSWORD;
        document.querySelector("#confirmPassword").value = test_val.PASSWORD;
        document.querySelector("#errorMessage").value = test_val.ERROR_MESSAGE;

        const result = validateCreateAccountForm(
            document.querySelector("#username").value,
            document.querySelector("#email").value,
            document.querySelector("#password").value,
            document.querySelector("#confirmPassword").value,
            document.querySelector("#errorMessage").value
        );

        expect(result).toBe(true);
    });

    test("should return false if passwords do not match", () => {
        document.querySelector("#username").value = test_val.USERNAME;
        document.querySelector("#email").value = test_val.EMAIL;
        document.querySelector("#password").value = test_val.PASSWORD;
        document.querySelector("#confirmPassword").value = test_val.CONFIRM_PASSWORD;
        document.querySelector("#errorMessage").value = test_val.ERROR_MESSAGE;
        const result = validateCreateAccountForm(
            document.querySelector("#username").value,
            document.querySelector("#email").value,
            document.querySelector("#password").value,
            document.querySelector("#confirmPassword").value
        );

        expect(result).toBe(false);
    });

    test("should return false for invalid email", () => {

        document.querySelector("#username").value = test_val.USERNAME;
        document.querySelector("#email").value = test_val.EMPTY_STRING;
        document.querySelector("#password").value = test_val.PASSWORD;
        document.querySelector("#confirmPassword").value = test_val.CONFIRM_PASSWORD;
        document.querySelector("#errorMessage").value = test_val.ERROR_MESSAGE;


        const result = validateCreateAccountForm(
            document.querySelector("#username").value,
            document.querySelector("#email").value,
            document.querySelector("#password").value,
            document.querySelector("#confirmPassword").value
        );

        expect(result).toBe(false);
    });

    test("should return false for missing fields", () => {
        document.querySelector("#username").value = test_val.EMPTY_STRING;
        document.querySelector("#email").value = test_val.EMPTY_STRING;
        document.querySelector("#password").value = test_val.EMPTY_STRING;
        document.querySelector("#confirmPassword").value = test_val.EMPTY_STRING;

        const result = validateCreateAccountForm(
            document.querySelector("#username").value,
            document.querySelector("#email").value,
            document.querySelector("#password").value,
            document.querySelector("#confirmPassword").value
        );

        expect(result).toBe(false);
    });
});
