import { useLocation, useNavigate } from "react-router-dom";
import { ReportObjectProps, TeamInfo } from "../../Types/Types";
import Row from "./Row";
import { useEffect, useState } from "react";
import { TeamLogIn } from "../../Tools/AuthUtils";
import { useMutation } from "react-query";

interface Props {}

function SortReports(reports: ReportObjectProps[]): ReportObjectProps[] {
  // Define the order of statuses
  const statusOrder: { [key: string]: number } = {
    "en réparation": 1,
    "en attente": 2,
    complété: 3,
  };

  // Sort the reports array based on the defined order
  return reports.sort((a, b) => {
    // Get the index of each status in the defined order
    const indexA =
      statusOrder[a.status.toLowerCase()] || Number.MAX_SAFE_INTEGER;
    const indexB =
      statusOrder[b.status.toLowerCase()] || Number.MAX_SAFE_INTEGER;

    // Compare the indices
    return indexA - indexB;
  });
}

const Team: React.FC<Props> = () => {
  let location = useLocation();
  const navigate = useNavigate();
  const state = location.state;
  const [reports, setReports] = useState<ReportObjectProps[]>([]);
  const teamId = state.id;
  const TeamLogInMutation = useMutation((credentials: string) =>
    TeamLogIn(credentials)
  );
  const [info, setInfo] = useState<TeamInfo>();
  useEffect(() => {
    TeamLogInMutation.mutateAsync(teamId)
      .then((data) => {
        if (data.info.is_admin == 1) {
          navigate("/admin", {
            state: { id: teamId },
          });
        } else {
          setInfo(data.info);
          setReports(SortReports(data.requests));
        }
      })
      .catch(() => {});
  }, []);
  return (
    <div className="flex m-4 flex-col">
      <div className="flex">
        <h1 className="my-4 text-3xl mx-4 font-bold">Team {info?.id}</h1>
        <h1 className="my-4 text-3xl mx-4 font-bold ml-auto">
          {info?.secteur}
        </h1>
      </div>
      <div>
        <h1 className="my-4 text-3xl mx-4 font-bold">
          Nids-de-poule à traiter
        </h1>
      </div>
      <div className="flex justify-center mb-2 border-b-4">
        <h1 className=" flex w-1/3">
          <p className="mr-auto">ID</p>
        </h1>
        <h1 className="w-1/3 flex">
          <p className="m-auto">Statut</p>
        </h1>
        <h1 className="w-1/3 flex">
          <p className="ml-auto mr-4">Actions</p>
        </h1>
      </div>

      {reports.length != 0 ? (
        <div className="flex flex-col">
          <ul className="flex flex-col gap-4 h-[400px] overflow-scroll">
            {reports.map((report: ReportObjectProps, index: number) => (
              <li key={index}>
                <Row report={report} teamId={teamId}></Row>
                <div className="h-[2px] bg-base-200 mt-2"></div>
              </li>
            ))}
          </ul>

          <a className="m-auto my-4">
            <button className="btn" onClick={Test}>
              Voir itinéraire
            </button>
          </a>
        </div>
      ) : (
        <div className="flex">
          <h1 className="m-auto">Aucun nid-de-poule à traiter</h1>
        </div>
      )}
    </div>
  );
};

export default Team;

function Test() {
  // Define the waypoints (multiple stops)
  const waypoints = [
    { location: "San Francisco, CA", stopover: true },
    { location: "Los Angeles, CA", stopover: true },
    // Add more waypoints as needed
  ];
  // Create a DirectionsService object
  const directionsService = new google.maps.DirectionsService();
  directionsService.route(
    {
      origin: "San Jose, CA", // Starting point
      destination: "San Diego, CA", // Destination
      waypoints: waypoints,
      optimizeWaypoints: true, // Optimize the order of waypoints
      travelMode: google.maps.TravelMode.DRIVING, // Specify the travel mode
    },
    (response, status) => {
      if (status === "OK") {
        // Extract polyline from the response
        if (response) {
          const route = response.routes[0].overview_polyline as any;

          // Encode the polyline
          const encodedRoute = google.maps.geometry.encoding.encodePath(route);

          // Create a link for the route
          const mapLink = `https://www.google.com/maps/dir/?api=1&origin=San+Jose,CA&destination=San+Diego,CA&waypoints=San+Francisco,CA|Los+Angeles,CA&travelmode=driving&dir_action=navigate&polyline=${encodedRoute}`;

          console.log("Link for the route:", mapLink);
        }
      } else {
        // Handle error
        window.alert("Directions request failed due to " + status);
      }
    }
  );
}
