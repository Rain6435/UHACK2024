# UHACK 2024

This project was our submission to the hackathon at the University of Quebec in Outaouais in 2024.

#### By Mohammed Elhasnaoui, Ayman Lahdili, Dhia Naas and Hechun Ouyang


## Project description

The project's goal was to help find a solution for the city of Gatineau to find and repair potholes as quickly as possible. The city has two ways to signal a pothole: either call the city or fill out a form online. We created an application that allows citizens to report a pothole directly in a user-friendly way, from their phones, and track the progress of the repair.

## Local installation

To complete the "Local installation" section of the README:

---

## Local Installation

### Prerequisites

1. Install [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/).
2. Install [Python 3](https://www.python.org/) with `pip`.
3. Set up MySQL and create a database.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Rain6435/UHACK2024.git
   cd UHACK2024
   ```

2. **Backend Setup:**
   - Navigate to the backend folder:
     ```bash
     cd backend
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure `config.py` with your MySQL credentials.
   - Initialize the database:
     ```bash
     python init_db.py
     ```
   - Start the Flask server:
     ```bash
     flask run
     ```

3. **Frontend Setup:**
   - Navigate to the frontend folder:
     ```bash
     cd ../frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm run dev
     ```

4. **Access the Application:**
   - Open `http://localhost:3000` in your browser for the frontend.
   - Backend API will run on `http://localhost:5000`.

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

The frontend is built using React with TypeScript and leverages several modern web technologies for a responsive and user-friendly interface.

#### Tech Stack
- React + TypeScript
- React Router for navigation
- React Query for server state management
- Tailwind CSS + DaisyUI for styling
- Google Maps API for location services

#### Key Features

1. **User Authentication**
   - Citizen login using phone number and name
   - Employee login using team ID
   - Admin dashboard access for authorized teams
   - Session management using localStorage

2. **Pothole Reporting System**
   - User-friendly form for reporting potholes
   - Image upload capability
   - Google Places autocomplete for accurate addresses
   - Danger level indication
   - Optional contact information for updates

3. **Request Tracking**
   - Unique ID tracking system for citizens
   - Real-time status updates
   - Image preview of reported potholes
   - Detailed view of individual reports

4. **Team Management Interface**
   - Team-specific dashboard
   - Request status management (En attente, En réparation, Complété)
   - Task transfer between teams (admin only)
   - Sorted display of requests by priority

5. **Admin Dashboard**
   - Overview of all teams
   - Workload distribution visualization
   - Request transfer capabilities
   - Team performance monitoring

#### Component Structure

1. **Authentication Components**
   - `Citoyen.tsx`: Citizen login interface
   - `Employee.tsx`: Employee login interface
   - Session management through localStorage

2. **Core Components**
   - `Router.tsx`: Main routing configuration
   - `Navbar.tsx`: Navigation and user menu
   - `Home.tsx`: Landing page
   - `Report.tsx`: Pothole reporting form

3. **Team Management**
   - `Team.tsx`: Team dashboard
   - `Row.tsx`: Individual request management
   - `Admin.tsx`: Administrative controls

4. **Request Tracking**
   - `TrackReport.tsx`: Request lookup
   - `ViewReport.tsx`: Detailed request view
   - `CitoyenView.tsx`: Citizen dashboard

5. **Utility Components**
   - `BaseDialog.tsx`: Reusable dialog component
   - `Preview.tsx`: Image preview component
   - Various icon components

#### Key Features Implementation

1. **Authentication Flow**
```typescript
// Example from Employee.tsx
async function handleLogIn(event: React.FormEvent<HTMLFormElement>) {
  event.preventDefault();
  setButtonState("reqSent");
  await TeamLogInMutation.mutateAsync(teamId)
    .then((data) => {
      setButtonState("success");
      localStorage.setItem("logged", "employe," + teamId);
      navigate("/team", { state: { id: teamId } });
    })
    .catch((e) => {
      // Look into file for implementation code for error handling
    });
}
```

2. **Request Management**
```typescript
// Example from Row.tsx
async function handleSave() {
  await UpdateMutation.mutateAsync({ id: report.id, status: status })
    .then((resStatus) => {
      if (resStatus == 201) {
        window.location.reload();
      }
    })
    .catch((e) => {
      // Look into file for implementation code for error handling
    });
}
```

3. **Image Handling**
```typescript
// Example from Report.tsx
async function handleUpload(event: React.FormEvent<HTMLInputElement>) {
  const target = event.target as HTMLInputElement & { files: FileList };
  if (target.files && target.files.length > 0) {
    const newImage: File = target.files[0];
    fileToBase64(newImage)
      .then((base64String) => {
        setImage(base64String);
      })
      .catch((error) => {
        console.error("Error converting file to Base64:", error);
      });
  }
}
```

#### State Management

The application uses a combination of:
- Local state with `useState` for component-level state
- React Query for server state management
- URL state through React Router for navigation
- localStorage for persistent authentication

#### API Integration

API calls are centralized in `AuthUtils.ts` and utilize axios for HTTP requests:
- Error handling with custom `ServerError` class
- Consistent API endpoint construction
- Type-safe request/response handling

#### Styling

The application uses Tailwind CSS with DaisyUI components for:
- Responsive design
- Consistent theming
- Pre-built components (buttons, cards, modals)
- Custom styling through utility classes

#### Future Improvements

1. **Performance Optimization**
   - Implement request caching
   - Add pagination for large request lists
   - Optimize image loading and storage

2. **Feature Enhancements**
   - Real-time notifications
   - Advanced filtering options
   - Enhanced route optimization
   - Offline support

3. **Security**
   - Implement JWT authentication
   - Add request rate limiting
   - Enhanced error handling

4. **User Experience**
   - Add loading skeletons
   - Implement progressive image loading
   - Add more interactive feedback

### Database

This database is designed to manage service requests, the teams handling them, and the individuals submitting them. We used mySQL.

The key tables are:
* request: Stores service request details like location, status, priority, and assigned team.
* requestor: Contains information about the people submitting the requests (name, contact info, etc.).
* team: Represents the teams responsible for handling requests, including their work schedules and work regions.




