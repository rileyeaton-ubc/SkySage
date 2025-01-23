--*************************************************************************************
-- COSC 310 Project - SkySage
--
-- DDL for DB to hold user and dashboard information (contents and sharing)
--
-- Author: Kai Gehry
-- Date: 2024-11-15
--
--*************************************************************************************
CREATE DATABASE SkySageData;

-- Contains data for a particular user. Includes user name, password, associated email, and a unique userId which identifies a user.
CREATE TABLE
	userData (
		userId INT NOT NULL, -- A user is identified by a unique userId
		userName VARCHAR(30) NOT NULL, -- User has a unique user name
		userPassword VARCHAR(30), -- Password for a user's account
		userEmail VARCHAR(50), -- User must provide an email which is associated with their account
		CONSTRAINT PK_User PRIMARY KEY (userId, userName) -- Need both the userId and userName for a given user to be unique
	);

-- Contains the data for a particular user's dashboard. Includes a unique dashboardId, associated userId, and all saved locations
CREATE TABLE
	dashboard (
		dashboardId INT, -- A dashboard for a user should have a particular Id by which it can be uniquely ideniified
		userId INT, -- Stores the userId of the user who's dashboard it is
		savedLocations VARCHAR(100), -- Need to figure out how this will be stored. Realistically need to hold multiple locations
		PRIMARY KEY (dashboardId),
		FOREIGN KEY (customerId) REFERENCES userData (customerId) ON UPDATE CASCADE ON DELETE CASCADE -- Connects a particular customer with a dashboard
	);

-- Holds data on who a dashboard has been shared with
CREATE TABLE
	sharedDashboard (
		shareId INT, -- Unique identifier for a particular share instance
		sharedUserId INT, -- Holds the userId of the user the dashboard has been shared with
		dashboardId INT,
		sharedUserEmail VARCHAR(30), --may need to have a foreign key here as a user can only share a dashboard to other account holders
		PRIMARY KEY (shareId),
		FOREIGN KEY (dashboardId) REFERENCES dashboard (dashboardId) ON UPDATE CASCADE ON DELETE CASCADE, --Connects a particular share instance to a particular dashboard
		FOREIGN KEY (sharedUserId) REFERENCES userData (userId) ON UPDATE CASCADE ON DELETE CASCADE --Connects a particular share instance with the user it has been shared with 
	);