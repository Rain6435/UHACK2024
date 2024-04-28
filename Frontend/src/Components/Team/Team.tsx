import { useLocation, useNavigate } from "react-router-dom";
import { ReportObjectProps, TeamInfo } from "../../Types/Types";
import Row from "./Row";
import { useEffect, useState } from "react";
import { TeamLogIn } from "../../Tools/AuthUtils";
import { useMutation } from "react-query";

interface Props {}

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
    TeamLogInMutation.mutateAsync(teamId).then((data)=>{
      setInfo(data.info)
      setReports(data.requests)
    }).catch(()=>{})
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

      <ul className="flex flex-col gap-4">
        {reports.map((report: ReportObjectProps, index: number) => (
          <Row index={index} report={report}></Row>
        ))}
      </ul>
    </div>
  );
};

export default Team;
