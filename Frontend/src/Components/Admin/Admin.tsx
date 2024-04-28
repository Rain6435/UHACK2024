import { useMutation } from "react-query";
import { Link, useLocation } from "react-router-dom";
import { GetTeams } from "../../Tools/AuthUtils";
import { useEffect, useState } from "react";
import TeamIcon from "../../assets/TeamIcon";

const Admin: React.FC = () => {
  let location = useLocation();
  const state = location.state;

  const [teams, setTeams] = useState<[]>();

  const GetTeamsMutation = useMutation(() => GetTeams());

  useEffect(() => {
    GetTeamsMutation.mutateAsync().then((data) => {
      console.log(data);
      setTeams(data);
    });
  }, []);

  return (
    <div>
      <div className="flex">
        <h1 className="my-4 text-3xl mx-4 font-bold">Admin</h1>
        <h1 className="my-4 text-3xl ml-auto mr-4 font-bold">ID:{state.id}</h1>
      </div>

      <div className="flex flex-col">
        <div className="flex">
          <p className="my-4 text-xl mx-4 font-bold">Équipes</p>
          <TeamIcon></TeamIcon>
        </div>

        <ul className="m-auto max-h-[600px] overflow-scroll">
          {teams?.map((team: any) => (
            <li className={state.id == team.info.id ? "hidden" : "my-4"}>
              <div className="card w-96 bg-base-100 shadow-xl">
                <div className="card-body">
                  <div className="flex">
                    <h2 className="card-title">Équipe {team.info.id}</h2>
                    <h2 className="card-title ml-auto">
                      {team.info.work_time == "J" ? "Jour" : "Nuit"}
                    </h2>
                  </div>

                  <div className="card-actions">
                    <p className="m-auto">
                      Nids à traiter:{team.requests.length}
                    </p>
                    <Link
                      to="/team"
                      state={{
                        id: team.info.id,
                        from: window.location.pathname,
                      }}
                    >
                      <button className="btn btn-primary w-[80px]">Voir</button>
                    </Link>
                  </div>
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Admin;
