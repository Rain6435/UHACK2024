# UHACK 2024

This project was our submission to the hackathon at the University of Quebec in Outaouais in 2024.

#### By Mohammed Elhasnaoui, Ayman Lahdili, Dhia Naas and Hechun Ouyang


## Project description

The project's goal was to help find a solution for the city of Gatineau to find and repair potholes as quickly as possible. The city has two ways to signal a pothole: either call the city or fill out a form online. We created an application that allows citizens to report a pothole directly in a user-friendly way, from their phones, and track the progress of the repair.

## Local installation

## Extensive documentation

### Algorithm

### Backend

The backend supports the management of road maintenance requests, teams, and users. It features endpoints for creating, retrieving, updating, and deleting data, as well as task distribution logic for pothole fixes. It uses Flask for API management and MySQL for database operations.

#### Key Features

* Request Management: Submit, update, retrieve, or delete pothole repair requests.
* User Management: Manage requestor and team details.
* Task Distribution: An algorithm to allocate pothole repair tasks to teams.
* Health Monitoring: An endpoint to check service availability.

#### Routes and Endpoints

1. Health Check
  - Endpoint: /v1/health
  - Method: GET
  - Description: Verifies the application's operational status.
  - Response: "operational"

2. Pothole Repair Request Management


| Method | Route    | Functionality    |
| :---   | :--- | :--- |
| GET | /v1/requests   | Retrives all or specific requests   |
| POST | /v1/requests   | Creates a new request   |
| PUT | /v1/requests   | Updates an existing request   |
| DELETE | /v1/requests   | Deletes a request  |
| PUT | /v1/requests/distribute   | Distributes requests among teams   |

The algorithm's endpoint /v1/requests/distribute is responsible for allocating repair tasks to different teams. It allocates repair tasks based on:

* Priority
* Location
* Team Availability

Input: Repair Request Data, Team IDs

Output: A mapping of team IDs to assigned tasks

3. User Management


| Method | Route    | Functionality    |
| :---   | :--- | :--- |
| GET | /v1/users   | Retrives all or specific users  |
| POST | /v1/users  | Creates a new user   |
| PUT | /v1/users  | Updates an existing user   |
| DELETE | /v1/users   | Deletes a user  |
| POST | /v1/users/login   | Logs in a user   |

4. Team Management


| Method | Route    | Functionality    |
| :---   | :--- | :--- |
| GET | /v1/teams   | Retrives all or specific teams  |
| POST | /v1/teams  | Creates a new team   |
| PUT | /v1/teams  | Updates an existing team   |
| DELETE | /v1/teams   | Deletes a team  |
| POST | /v1/teams/login   | Logs in a team   |

### Frontend

### Database

This database is designed to manage service requests, the teams handling them, and the individuals submitting them. We used mySQL.

The key tables are:
* request: Stores service request details like location, status, priority, and assigned team.
* requestor: Contains information about the people submitting the requests (name, contact info, etc.).
* team: Represents the teams responsible for handling requests, including their work schedules and work regions.




