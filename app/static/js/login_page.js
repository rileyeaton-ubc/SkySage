import { sendBasicEmail } from "./api_functions.js";

function validateLoginForm() {
    console.log("Form validation is running.");
    return true; // Example logic
}

var email_to = "riley.j.eaton@gmail.com"
var email_subject = "Skysage Account Created"
var email_body = "Hello, your account has been created!"
var send_email_result = await sendBasicEmail(email_to, email_subject, email_body)
console.log(`email send to ${email_to} was${send_email_result.success ? "" : " not"} successful`)

window.validateLoginForm = validateLoginForm;