# UHACK 2024

This project was our submission to the hackathon at the University of Quebec in Outaouais in 2024.

#### By Mohammed Elhasnaoui, Ayman Lahdili, Dhia Naas and Hechun Ouyang


## Project description

The project's goal was to help find a solution for the city of Gatineau to find and repair potholes as quickly as possible. The city has two ways to signal a pothole: either call the city or fill out a form online. We created an application that allows citizens to report a pothole directly in a user-friendly way, from their phones, and track the progress of the repair.

## Local installation

## Extensive documentation

### Algorithm

This project implements an algorithm to efficiently schedule pothole repairs for maintenance teams. It prioritizes dangerous potholes on main roads and optimizes routes to minimize travel time and workload distribution among teams.

#### Prioritization

Three inputs are used to determine which potholes should be repaired first:

1. Danger (How dangerous is the pothole?)
2. Street Priority (Is the pothole on an important street?)
3. Age of pothole (How long has the pothole been there?)

Potholes are classified and sorted into six categories:

1. Dangerous/Main
2. Dangerous/Collector
3. Dangerous/Local
4. Non-dangerous/Main
5. Non-dangerous/Collector
6. Non-dangerous/Local

The age of the pothole is only used as a deciding factor between two potholes in the same category, in which case the "older" one takes priority.

#### Route Optimization

For each category, the algorithm:

* Builds a graph using pothole locations.
* Finds an optimized path using a modified nearest-neighbor approach.
* Combines paths across all categories into a single repair sequence using minimal transition distances.

#### Workload distribution

Teams are assigned potholes sequentially while respecting:

* Travel Time: Calculated using geodesic distance and an average speed of 45 km/h.
* Repair Time: Fixed at 15 minutes per pothole.
* Workday Constraint: Maximum of 480 minutes per team.

#### Output

A dictionary mapping each team to its assigned potholes, including priority indices.

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




