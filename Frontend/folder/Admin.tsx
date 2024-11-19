import { useMutation } from "react-query";
import { Link, useLocation } from "react-router-dom";
import { GetTeams } from "../../Tools/AuthUtils";
import { useEffect, useState } from "react";
import TeamIcon from "../../assets/TeamIcon";
import Row from "../Team/Row";
import { ReportObjectProps } from "../../Types/Types";

const Admin: React.FC = () => {
  let location = useLocation();
  const state = location.state;

  const [activeView, setActive] = useState("equipes");

  const [teams, setTeams] = useState<[]>();

  const GetTeamsMutation = useMutation(() => GetTeams());

  useEffect(() => {
    GetTeamsMutation.mutateAsync().then((data) => {
      setTeams(data);
    });
  }, []);

  return (
    <div className="">
      <div className="flex">
        <h1 className="my-4 text-3xl mx-4 font-bold">Admin</h1>
        <h1 className="my-4 text-3xl ml-auto mr-4 font-bold">ID:{state.id}</h1>
      </div>
      <div className="flex gap-4">
        <button
          className="btn m-auto btn-outline"
          onClick={(e) => {
            e.preventDefault();
            setActive("equipes");
          }}
        >
          Mes Équipes
        </button>
        <button
          className="btn m-auto btn-outline"
          onClick={(e) => {
            e.preventDefault();
            setActive("moi");
          }}
        >
          Mes Requetes
        </button>
      </div>
      <div className="flex flex-col">
        <div className="flex flex-col">
          <div className="flex">
            <p className="mt-4 text-xl mx-4 font-bold">Équipes</p>
            <TeamIcon></TeamIcon>
          </div>
          {activeView == "equipes" ? (
            <ul className="m-auto max-h-[600px] overflow-scroll p-4">
              {teams?.map((team: any, index: number) => (
                <li
                  className={state.id == team.info.id ? "hidden" : "my-4"}
                  key={index}
                >
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
                          <button className="btn btn-primary  w-[80px]">
                            Voir
                          </button>
                        </Link>
                      </div>
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          ) : activeView == "moi" ? (
            <ul className="flex flex-col gap-4 h-[400px] overflow-scroll w-full p-4">
              <div className="flex justify-center border-b-4">
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
              {teams?.map((team: any, index: number) => (
                <div className={state.id != team.info.id ? "hidden" : ""}>
                  {state.id == team.info.id ? (
                    <li
                      key={index}
                      className={state.id == team.info.id ? "my-4" : ""}
                    >
                      {(team.requests as []).map(
                        (request: ReportObjectProps) => (
                          <div>
                            <Row report={request} teamId={team.info.id}></Row>
                          </div>
                        )
                      )}
                    </li>
                  ) : (
                    <></>
                  )}
                </div>
              ))}
            </ul>
          ) : (
            <div>
              <h1>Il n'y a rien à voir.</h1>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Admin;
