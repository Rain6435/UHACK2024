import { useLocation } from "react-router-dom";
import { ReportObjectProps, TeamInfo } from "../../Types/Types";
import { useState } from "react";
import Row from "./Row";

interface Props {}

const Team: React.FC<Props> = () => {
  let location = useLocation();
  const state = location.state;
  var reports: ReportObjectProps[] = state.reports;
  const info:TeamInfo = state.info;

  function updateReport(report:ReportObjectProps){
    const f = reports.filter((reportO:ReportObjectProps)=>{
      return report.id = reportO.id
    })[0];
  }

  return (
    <div className="flex m-4 flex-col">
      <div className="flex">
        <h1 className="my-4 text-3xl mx-4 font-bold">Team {info.id}</h1>
        <h1 className="my-4 text-3xl mx-4 font-bold ml-auto">{info.secteur}</h1>
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
          <Row index={index} report={report} change = {updateReport}></Row>
        ))}
      </ul>
    </div>
  );
};

export default Team;
