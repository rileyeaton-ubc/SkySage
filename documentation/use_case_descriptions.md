## Use Case Descriptions

### Use Case 1. Create Account

**_Primary actor:_** User

**_Description:_** Allows a user to create an account within SkySage.

**_Pre-condition:_** User accesses the SkySage home page.

**_Post-condition:_** User will have an account and be logged in, which gives them access to view and edit account information.

**_Main scenario:_**

1. User clicks on the "Create Account" button on the home page.
2. User is prompted to enter a user name, password, and contact email.
3. User enters a valid user name, password, and contact email into the indicated fields.
4. User confirms their account creation by clicking the sign-up button. This sends a confirmation link to their provided contact email.
5. User clicks the confirmation link emailed to them, which will redirect them to the site and log them in with their new account.

**_Extensions:_**

3\.1 User Name and Password Length Requirements

- 3.1.1 A length requirement is specified for an account username. If this requirement is not met, the user will be prompted to change the current username.
- 3.1.2 Length, special character count, and number count are requirements that are specified for an account password. If this requirement is not met, the user will be prompted to change the current password.

3\.2 Username & Password Generation

- 3.2.1 User can create a user name and password on their own, or a username, password, or both can be auto generated for them.

---

<br>

### Use Case 2. Log In

**_Primary actor:_** User

**_Description:_** Allows a user to log in to a pre-existing account in order to access their dashboard, account information, and to share weather information with other users.

**_Pre-condition:_** User must have a pre-existing account, know the login credentials for that account, and access to the SkySage home page.

**_Post-condition:_** User will be logged in to their account and have access to all related account information.

**_Main scenario:_**

1. User clicks on the "Log In" button on the home page.
2. User is brought to the login page, where they are prompted to enter their username and password for the existing account they wish to log into.
3. User enters their account's username and password into the required field.
4. User clicks the "Login" button.
5. User is redirected back to the home page, this time logged into their account.

**_Extensions:_**

4\.1 Incorrect Username

- 4.1.1 If the user has entered an username that does not exist in the system, they will be altered that it is incorrect after clicking the login button.

4\.1 Incorrect Password

- 4.1.1 If the user has entered an incorrect password for the username, they will be alerted that it is incorrect after clicking the login button.
- 4.1.2 The user is given 5 attempts to enter the correct password for their username before they are prompted to reset their password.

---

<br>

### Use Case 3. Log Out

**_Primary actor:_** User

**_Description:_** Allows a user to log out of their account.

**_Pre-condition:_** User must be on the SkySage site, and logged into their account.

**_Post-condition:_** User will be logged out of their account, and redirected to the SkySage home page.

**_Main scenario:_**

1. When a user is logged in anywhere on the site, they will see an account icon in the top right of the navbar.
2. User clicks the account button, which redirects them to their account page.
3. User clicks the "Log Out" button
4. User is logged out, and redirected to the SkySage home page.

**_Extensions:_**

2\.1 Unsaved Work

- 2.1.1 If the user has unsaved work on their dashboard or otherwise and they attempt to leave to the account page, they will be notified through a popup if they are sure they want to discard their current changes or not.

---

<br>

### Use Case 4. Reset Password

**_Primary actor:_** User

**_Description:_** Allows a user to reset their account password.

**_Pre-condition:_** User must have a pre-existing account, know the contact email for that account, and access to the SkySage login page.

**_Post-condition:_** User's password will be reset to what they provided, and they can then login with their username and new password.

**_Main scenario:_**

1. User click the "Reset Password" hyperlink which redirects them to a page where they are prompted to enter their username.
2. User enters their username and confirms it.
3. User clicks the "Reset Password" button.
4. User receives an email with a link to reset their password.
5. User clicks the link provided via email, which redirects them to a page where they are prompted to enter a new password.
6. User must enter the new new password twice.
7. User clicks the button labeled "Confirm Reset".
8. Successful reset message is displayed to the user, and they are then redirected back to the login page.

**_Extensions:_**

2\.1 Username Does Not Exist in DB

- 2.1.1 If the username is not found in the internal DB, the user will be alerted of this, and will be asked to enter a valid username.

2\.2 User Does Not Have Access to Contact Email

- 2.2.1 The password reset link will be sent to the contact email associated with the username. If the user attempting to reset their password does not have access to this contact email, they will not be able to reset their password. If a recovery email has been provided as part of the user's account information, and a password reset confirmation link sent to this email can be accessed, the user can continue to successfully reset their password.

6\.1 Password Constraints

- 6.1.1 The length of password is limited to 20 characters and must include at least one special character and at least one number
- 6.1.2 The new password cannot be the same as an old password.

---

<br>

### Use Case 5. Delete Account

**_Primary actor:_** User

**_Description:_** Allows a user to permanently delete their account.

**_Pre-condition:_** User must be on the SkySage site, and logged into their account.

**_Post-condition:_** User's account will be deleted from the database and they will receive a notification of this to their email. The user will also be logged out of their account, and redirected to the SkySage home page.

**_Main scenario:_**

1. When a user is logged in anywhere on the site, they will see an account icon in the top right of the navbar.
2. User clicks the account button, which redirects them to their account page.
3. User clicks the "Delete Account" button
4. User is prompted to enter their password to confirm the account deletion.
5. User enters their password.
6. User clicks the "Confirm Account Deletion" button.
7. User is logged out, and redirected to the SkySage home page.
8. User receives an email detailing the deletion of their account and removal of their data from SkySage data stores.

**_Extensions:_**

2\.1 Unsaved Work

- 2.1.1 If the user has unsaved work on their dashboard or otherwise and they attempt to leave to the account page, they will be notified through a popup if they are sure they want to discard their current changes or not.

6\.1 Incorrect Password

- 6.1.1 If the user has entered an incorrect password for their account, they will be alerted that it is incorrect after clicking the confirmation button, and they will continue to be prompted for the correct password.

---

<br>

### Use Case 6. Search for Location

**_Primary actor:_** User

**_Description:_** Allows a user to search for weather conditions in a particular location.

**_Pre-condition:_** User must navigate to the SkySage home page, where a search bar is provided to search for a location.

**_Post-condition:_** The user is redirected to the page for the location, and current weather conditions can be viewed.

**_Main scenario:_**

1. User clicks on the search bar.
2. User types their desired location into the search bar.
3. User clicks the auto-filled address or location name from the drop-down to select it.
4. User is redirected to the location page.

**_Extensions:_**

3\.1 No Location Results

- 3.1.1 If the user has misspelled the location, or weather information on the location searched is not available through the API, the user is notified of this.

---

<br>

### Use Case 7. View Current Weather for Location

**_Primary actor:_** User

**_Description:_** Allows a user to view the current weather conditions for a location.

**_Pre-condition:_** User must be on the SkySage page for the desired location.

**_Post-condition:_** User is provided with the current conditions for the selected location.

**_Main scenario:_**

1. Once user is on the location's page the current weather is displayed for the location.
2. User can pick between tabs that give options for viewing the current conditions, or a 5 day forecast.

**_Extensions:_**

1\.1 No Weather Results Available for Location

- 1.1.1 If there are no results are available for the location, the user is given a message that the given location may not have any current weather information.

---

<br>

### Use Case 8. View 5-Day Forecast for Location

**_Primary actor:_** User

**_Description:_** Allows the user to view a 5-day forecast for a location.

**_Pre-condition:_** User must be on the SkySage page for the desired location.

**_Post-condition:_** User is provided with the weather conditions for the next 5 days at the location.

**_Main scenario:_**

1. If a result is returned for the location, the current weather conditions are displayed automatically.
2. User selects a tab labeled "5-Day Forecast".
3. Both the 5-Day forecast, and the AI summary of the upcoming weather will be displayed to the user.

**_Extensions:_**

3\.1 No Weather Results Available for Location

- 3.1.1 If there are no results are available for the location, the user is given a message that the given location may not have any current weather information.

---

<br>

### Use Case 9. Favorite Location

**_Primary actor:_** User

**_Description:_** Allows a user to save a favourite location to their dashboard.

**_Pre-condition:_** User has logged in and and has searched for a location.

**_Post-condition:_** User has successfully saved the location to their dashboard and can access/view weather conditions for that location easily through their dashboard as needed.

**_Main scenario:_**

1. User has successfully searched for and has results returned for a desired location.
2. User navigates and clicks the "Save Location To Dashboard" button.
3. User can view their saved location by navigating to their account dashboard and clicking on the "Saved Locations" tab in the dashboard environment.

**_Extensions:_**

2\.1 Too Many Favourites

- 2.1.1 If a user already has 8 locations favourited, they will be alerted with a pop-up that they cannot favourite any more locations due to dashboard limitations.

3\.1 Past Location Viewing

- 3.1.1 Past viewed locations will not save to a user's dashboard unless they explicitly save them.
- 3.1.2 Locations that were previously viewed can be accessed in the "Location History" tab which provides a list of past locations which have been viewed. (Drop-out stack implementation?)

---

<br>

### Use Case 10. Unfavorite Location

**_Primary actor:_** User

**_Description:_** Allows for unfavouriting/removing a saved location from their dashboard.

**_Pre-condition:_** User has logged in granting access to their dashboard.

**_Post-condition:_** User has successfully removed a location from their dashboard. The location is no longer viewable or shareable directly from the user's dashboard.

**_Main scenario:_**

1. User navigates to the saved locations tab in their dashboard environment.
2. User finds the location they would like to remove, and clicks on a three dots icon (indicating a "More" button) and selects the "Remove Favourited Location" submenu option.
3. A message is displayed to the user allowing the user to confirm or cancel the removal.
4. User selects the "Confirm" option.

**_Extensions:_**

2\.1 No Saved Locations

- 2.1.1 If the user has no saved locations, there are no locations to remove, and the three dots ("More" button) will not be present in the dashboard environment.

---

<br>

### Use Case 11. View Dashboard

**_Primary actor:_** User

**_Description:_** Allows a user to view a dashboard, whether it's their own or one that was shared with them.

**_Pre-condition:_** User is logged in. If they want to view their own dashboard they need to have at least one location favourited. If the user wants to view a dashboard that has been shared with them, they need to have the link provided by the other user, and permission to view it.

**_Post-condition:_** User will be able to view the weather forecast for each location saved to the dashboard in one compact view.

**_Main scenario:_**

1. Once logged in, if the user wants to see the dashboard of another user, they must click the link that was emailed to them.
2. Otherwise, if they wish to see their own dashboard, they can click the dashboard link on the main website's menu bar.
3. Once on a dashboard, the user will be presented with all the favourited locations of their own, or the user who's dashboard it is.

**_Extensions:_**

1\.1 No access to dashboard

- 1.1.1 If the user has no access to the dashboard for which they have a link (their access may have been revoked) then they will be presented with a message on the webpage detailing so.

3\.1 No favourited locations

- 3.1.1 if the user has no locations currently favourited, then they will be presented with a message that they cannot have a dashboard unless they have at least 1 favourited location.
- 3.2.1 If the user is viewing another user's dashboard for which they have no favourited locations, they will be provided a similar message as above, but this time indicating that the sharing user must take action to remedy this.

---

<br>

### Use Case 12. Share Dashboard

**_Primary actor:_** User

**_Description:_** Allows a user to share their dashboard with other registered users.

**_Pre-condition:_** User must be logged in, have a dashboard of their own, and have the username for the account they want to share their dashboard with.

**_Post-condition:_** User who is having the dashboard shared with them will have received an email with a link to the dashboard they now have access to.

**_Main scenario:_**

1. Once logged in, the user will navigate to their dashboard.
2. User clicks on the sharing button in the dashboard menu.
3. Once prompted, the user will enter the username of the account which they want to share their dashboard with.
4. User confirms the sharing of their dashboard with the desired account.
5. User receives confirmation that an email will be sent out to the account they are sharing with, and they can unshare any time from the dashboard menu.

**_Extensions:_**

3\.1 Account not found

- 3.1.1 If the username entered cannot be found for any account, the user will receive a message detailing this and be required to input a valid username.

4\.1 Cancel confirmation

- 4.1.1 If the user does not want to confirm the sharing to the username/account provided, they can click the cancel button which will return them to the sharing modal.

---

<br>

### Use Case 13. Unshare Dashboard

**_Primary actor:_** User

**_Description:_** Allows a user to stop sharing their dashboard with other registered users.

**_Pre-condition:_** User must be logged in, have a dashboard of their own, currently be sharing it with another user.

**_Post-condition:_** User who is having the dashboard shared with them will have received an email notifying them that they no longer have access to the dashboard.

**_Main scenario:_**

1. Once logged in, the user will navigate to their dashboard
2. User clicks on the sharing button in the dashboard menu
3. User clicks the X beside one of the usernames which the dashboard is already being shared with.
4. User confirms the unsharing of their dashboard with the desired account
5. User receives confirmation that an email will be sent out to the account they are sharing with, and they will no longer have access to the dashboard.

**_Extensions:_**

4\.1 Cancel confirmation

- 4.1.1 If the user does not want to confirm the unsharing, they can click the cancel button which will return them to the sharing modal.

---

<br>
