# SkySage Milestone Progress Tracker

Milestone progress, and more specifically milestone tasks are assigned and tracked on the project board [here](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/1)

## Milestone 1 - Complete

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/6)

## Milestone 2 - Complete

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/7)

## Milestone 3 - Complete

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/8)

Up to this point, the project work has just been planning & documentation.

## Milestone 4 - In Progress

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/9)

**Summary:**

The requirement for test is currently satisfied. As the rest of the components are added it will be further test. The CI tools is selected but still, needs to be integrated. Design patterns are done, but dockerization is left to do. The UML design is done. Code still needs to be connected between frontend and backend. The structure of the current work is good, but needs to be restructured as more work is added. The team progress is currently being managed properly using software engineering practices like kan-ban board, branches and PR requirements. The databases are tested. The progress should be about 30-40% based on project requirements.

**Reflection:**

As part of this milestone, the HTML and CSS files for the front end of our site were developed, an instance of the backend DB to store user information was created using SQLite, automated tests were written to ensure proper functionality of DB actions, and a CI tool was chosen.

In terms of the process taken to completing these tasks, the tasks were split based on what each member of the team felt they were best at. Riley and Kai were assigned the backend development tasks which included deciding on a CI tool, creating an instance of an SQLite DB and writing tests to test this instance creation. Mridul and Max were assigned the front end development which covered the design of HTML and CSS files as they felt their experiences were best fit for this.

In order to organize the development process, Riley decided to use the projects tab in github to keep track of progress. The process followed here is similar to Kanban development model which was suited well for this project. This provided for an easily maintainable workflow.

What was done well during this milestone was the communication through git hub and timely reply times to requested changes. We will need to become better at not leaving task late, and starting early to provide best results possible. Some challenges included becoming familiar with SQLite in python, however Riley and Kai were quick to adapt.

### Completed Branches/Issues:

**feature-47** Completed by Kai
Creating a DDL for the backend database which will house all the user data.

**feature-55** Completed by Kai
Created a file header template to be used for all source code files.

**feature-20** Completed by Kai and Riley
Decided on CI tool being GitHub Actions. This is to be implemented in full elsewhere

**feature-43** Completed by Kai and Riley
UML class diagram was ditched due to the lack of the object oriented nature in this project.

**feature-58** Completed by Kai and Riley
Completed the initialization of the SQlite instance

**feature-15** Completed by Riley
Tested the location search API with postman using new credentials.

**feature-16** Completed by Riley
Tested the AI generation API with postman using new credentials.

**feature-14** Completed by Riley
Tested the weather API with postman using new credentials.

**feature-24** Completed by Riley
Tested the email sending API with postman using new credentials.

**feature-37** Completed by Riley
Tracking milestone-4 progress using this very markdown, and the milestone-4 branch.

**feature-46** Completed by Riley
Created PR template and added to main to have consistency across all PRs

**feature-59** Completed by Riley
Refactor the file structure given our new chosen stack to follow industry standards.

**feature-44**, **feature-60**, **feature-61** Completed by Max and Mridul
Collected and edited all the sample code for the frontend which includes the html, css, and javascript. 5 pages in total were worked on.

**feature-13** Completed by whole team
Decided on our framework for the project. We decided as a team that we will be using html/css/js for the frontend, Rapid API for the backend with Axios, and SQLite for the database.

### In-Progress Branches/Issues:

(or those moving to milestone-5)

**feature-32**, **feature-33**, **feature-34**, **feature-35**, **feature-36**
Polishing up all the sample code for the frontend into a working, production-ready site.

**feature-18**
Boilerplate code for backend using Rapid API.

### Burn Up Chart

![Burn Up Chart](/documentation/diagrams/burn-up-chart.png)

### Status Chart

![Status Chart](/documentation/diagrams/status-chart.png)



## Milestone 5 - Completed

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/10)

**<ins>Summary:</ins>**

As part of milestone 5, the HTML and CSS files were completed, testing for these files was carried out, and the connection between the front and back ends was started. In addition to this, the AI Generation API, Location Search API, and Autocomplete search API's were implemented after writing tests for all allowing for further progression of development in the backend. This backend development additionally included implementing docker compose for the SQLite DB initialization and testing. Finally, as part of the backend development effort for this sprint, the DB querying was integrated into the backend model to allow for functionality of the front end features. Overall, the team has done well with keeping to schedule, and as it stands, no tasks have been pushed to the next sprint. The goals for this sprint have been met, and considering the development was ahead of schedule at the end of the last sprint, concluding this sprint, development should still be ahead of schedule.

**<ins>Reflection:</ins>**

Concluding milestone 5, the requirements were met, and the team is on track for on time or slightly early completion of the development efforts. Considering what has been completed during this milestone, each team member has done a good job of keeping on track with individual development tasks and helping each other out when it was needed. Given that all team members are new to using Docker besides Riley, troubleshooting was efficient when issues arose. As Riley is experienced with Docker, and testing configurations issues that arose did not last for long in these areas. 

As testing is an important part of the development process, testing of both the front and backends were considered closely. JEST was used to test the front end, and a python testing framework using pytest was implement for the backend features such as the SQLite DB functionality and Docker. The JEST testing was completed by Max, Mridul, and Kai whereas the backend testing of the DB and API features was completed by Riley and Kai.

Overall, the team did a good job of communicating effectively and working together well as a team, helping with each other's tasks where needed. Considering the progress of this milestone, the completion of the project should be on time and potentially early.

### <ins>Completed Branches/Issues:</ins>

**feature-80** completed by Riley
- Complete a GitHub action for testing Docker

**feature-86** completed by Kai
- Implement Docker compose 

**feature-89** completed by Kai
- Complete milestone progress documentation for milestone 5

**feature-70** completed by Riley and Kai
- Write all backend API tests before implementation

**feature-72** completed by Mridul
-  Completed all HTML and CSS files for account page

**feature-73** completed by Mridul
- Completed all HTML and CSS files for login page

**feature-74** completed by Max
- Completed all HTML and CSS files for dashboard page

**feature-75** completed by Max
- Completed all HTML and CSS files for location page

**feature-76** completed by Max
- Completed all HTML and CSS files for home page

**feature-71** completed by Max and Mridul
- Wrote all frontend JavaScript tests before implementation

**feature-18** completed by Riley
- Write boilerplate code for backend

**feature-84** completed by Riley
- Completed database initialization and testing

**feature-88** completed by Riley
- Fixed GitHub Actions to include environment variables


### <ins>In-Progress Branches/Issues:</ins>

**feature-49** completed by Riley
- Implemented the AI Generation API

**feature-50** completed by Riley
- Implemented the Location Search API

**feature-51** completed by Riley
- Implemented Autocomplete Search API

**feature-45** completed by Kai
- Integrated DB querying into backend model

__<ins>Moving to Milsetone 6:</ins>__ 

feature-49, feature-50, feature-51


### Burn Up Chart

![Burn Up Chart](/documentation/diagrams/burn-up-chart-milestone-5.png)

### Status Chart

![Status Chart](/documentation/diagrams/status-chart-milestone-5.png)



## Milestone 6 - In Progress

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/11)


**<ins>Summary:</ins>**

As part of milestone 6, the backend was further developed and a large portion of the frontend testing was completed. This sprint included the implementation of the AI generation, E-Mail, location search and autocomplete search APIs. Refactors for decoupling the docker compose file and db initialization were also completed as part of the backend development efforts. As a continuation of the development in the previous milestone, the models written for the backend DB were refactored to include certain functions for easy querying in the front end. Furthermore, the routers and controllers for the db models were created and tested both using pytest and postman. All tests were successfully passing and only small modifications need to be made at this point. Considering the frontend development during this milestone, Javascript for the account and login pages as well as the tests for both were completed, and a config file for all frontend files was made. In addition to this, the Javascript tests for the home, dashboard, and location pages are in progress.


**<ins>Reflection:</ins>**

Concluding milestone 6, most requirements were completed, and the team worked well together. Riley completed task of getting the frontend axios running, implemented the location search and autocomplete search, AI generation, and Email APIs, and also worked on preventing corruption of the SQLite db file from corrupting docker compose. Riley also worked with Max and Mridul to write the javascript for all the frontend files. Max worked on completing the frontend JavaScript tests for the home, dashboard, and location pages. Mridul created a config file for the frontend files and additionally wrote javascript files for the account and login pages as well as wrote tests for those pages. Kai completed the models for the backend db, as well as made the controllers and routers for the models to query the backend. In addition to this, Kai wrote all tests for the controllers and modified them accordingly to function with the router parameters. Postman was additionally used for testing the outputs of get and post requests. Overall, the team got their assignments done, and collaboration was good among teammates. In the final development efforts, the team could improve on getting parts done earlier.


### <ins>Completed Branches/Issues:</ins>

**feature-127** - Riley
- Decouple Docker compose and db initialization

**feature-118** - Riley
- Get frontend Axios running to query backend 

**feature-50** - Riley
- Implement Location Search API

**feature-51** - Riley
- Implement Autocomplete Search API

**feature-139** - Riley
- Fix local SQLite db file from corrupting docker compose

**feature-102** - Max and Riley
- Complete JavaScript for The Dashboard Page

**feature-143** - Max and Riley
- Complete JavaScript for the Add Favourites Function for the Location Page

**feature-120** - Mridul
- Complete JavaScript for the Account Page

**feature-121** - Mridul
- Complete JavaScript for Login Page

**feature-123** - Mridul
- Write all JavaScript tests for Account page

**feature-124** - Mridul
- Write all JavaScript tests for Login page

**feature-125** - Mridul
- Create a config file for all frontend files

**feature-122** - Kai
- Document progress for milestone 6

**feature-119** - Kai
- Refactoring and Test Additions for Models


### <ins>In-Progress Branches/Issues:</ins>

**feature-130** - Kai
- Enable Database API access using router/controller

**feature-112** - Max
- Complete Frontend JavaScript test for Home page

**feature-113** - Max
- Complete Frontend JavaScript test for Dashboard page

**feature-114** - Max
- Complete Frontend JavaScript test for Location page

**feature-111** - Max and Riley 
- Complete JavaScript for the Current Weather and Forecast Weather Display for the Location Page

**feature-138** - Max and Riley
- Complete JavaScript for the Location Search for the Home Page


**feature-49** - Riley
- Implement AI Generation API

**feature-126** - Riley
- Implement E-Mail API


### Burn Up Chart

![Burn Up Chart](/documentation/diagrams/burn-up-chart-milestone-6.png)

### Status Chart

![Status Chart](/documentation/diagrams/status-chart-milestone-6.png)

## Final Milestone - Upcoming

[Tracking Board](https://github.com/orgs/UBCO-COSC-310-Winter-2024-T1/projects/34/views/12)