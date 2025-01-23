# Project Test Plan

## Table Legend

**Test Type**

- **I:** Integration Testing
- **S:** System Functionality Testing
- **O:** Operational Acceptance Testing
- **UN:** Unit Testing
- **US:** Usability Testing
- **A:** Acceptance Testing

**Pass/Fail**

- **P:** Test Case _Passed_
- **F:** Test Case _Failed_

**Contributor**

- **MO:** Max Oberhellman
- **MN:** Mridul Nohria
- **KG:** Kai Gehry
- **RE:** Riley Eaton

## Test Table

| Requirements                                                                                                       | Test Type | Pass/Fail | Contributor |
| :----------------------------------------------------------------------------------------------------------------- | :-------- | :-------- | :---------- |
| **1. User Requirements**                                                                                           |           |           |             |
| **1.1. Ability to search for a desired city/location using its name to get subsequent weather details**            |           |           |             |
| **1.2 Notify user if a searched city/location does not exist and allow search by specific address**                |           |           |             |
| **1.3 Display current weather for the selected city/location**                                                     |           |           |             |
| **1.4. Option to view 5-day weather forecast for a city/location**                                                 |           |           |             |
| **1.5. Accessible on Chrome, Safari, Firefox, and Edge browsers**                                                  |           |           |             |
| **1.6. Users can create accounts and log in for a personalized experience**                                        |           |           |             |
| **1.7. Option for users to reset forgotten passwords**                                                             |           |           |             |
| **1.8. Users can favorite locations they've searched to easily keep track**                                        |           |           |             |
| **1.9. Ability to unfavorite locations if no longer desired**                                                      |           |           |             |
| **1.10. Dashboard shows summary of weather for each favourited location (if at least one location is favourited)** |           |           |             |
| **1.11. Users can favorite up to 8 locations**                                                                     |           |           |             |
| **1.12. Users can share their dashboard with other users**                                                         |           |           |             |
| **1.13. Option to remove individual users' access to a shared dashboard**                                          |           |           |             |
| **2. Functional Requirements**                                                                                     |           |           |             |
| **2.1. Support search by city/location name based on external API availability**                                   |           |           |             |
| **2.2 Location searches are not case-sensitive**                                                                   |           |           |             |
| **2.3. Search also supports specific address instead of city name**                                                |           |           |             |
| **2.4. Application displays predicted weather for the next 5 days**                                                |           |           |             |
| **2.5. AI-generated summary describes weather trends over the next 5 days in brief**                               |           |           |             |
| **2.6 Display maximum and minimum weather parameters for requested period**                                        |           |           |             |
| **2.7. Weather parameters include temperature, wind speed, rainfall, and humidity**                                |           |           |             |
| **2.8. Save favorite locations on dashboard for quick weather summary**                                            |           |           |             |
| **2.9. Users can create accounts to manage favorites, dashboards, and sharing**                                    |           |           |             |
| **2.10. Account creation is optional for basic site access to search and view weather**                            |           |           |             |
| **3. Non-Functional Requirements**                                                                                 |           |           |             |
| **3.1. Use OpenWeather’s Weather API for weather data retrieval**                                                  |           |           |             |
| **3.2. Use Google Places API for location search, returning coordinates for weather API**                          |           |           |             |
| **3.3. Weather results should return from the API within 5 seconds**                                               |           |           |             |
| **3.4. Store user details in a secure relational database, such as MySQL**                                         |           |           |             |
| **3.5. Secure user data by hashing and salting PII and password data**                                             |           |           |             |
| **3.6. Database access restricted to admins with rotating passwords**                                              |           |           |             |
| **3.7. Use Adapter Pattern to interface with external weather API**                                                |           |           |             |
| **3.8. REST API layer serves information retrieved from external weather API**                                     |           |           |             |
| **3.9. Use Singleton Pattern to manage a single instance of the API client**                                       |           |           |             |
| **3.10. Use Facade Pattern to simplify fetching and displaying weather data**                                      |           |           |             |
| **3.11. Control system manages data flow and transformations between API fetching and client response**            |           |           |             |
| **3.12. Use an API for generating AI summaries of forecasted weather conditions**                                  |           |           |             |
| **3.13. Implement Continuous Integration (CI) and automated testing**                                              |           |           |             |
| **3.14. Application should be dockerized for deployment**                                                          |           |           |             |
| **3.15. Follow Test-Driven Development (TDD), with tests written before implementation**                           |           |           |             |
| **3.16. Unit tests and integration tests required for code quality and functionality assurance**                   |           |           |             |
