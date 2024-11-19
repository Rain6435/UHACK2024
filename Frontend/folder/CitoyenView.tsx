import { useEffect, useState } from "react";
import { useMutation } from "react-query";
import { Link, useLocation } from "react-router-dom";
import { CitoyenReports } from "../../../Tools/AuthUtils";
import { ReportObjectProps } from "../../../Types/Types";
import ArrowIcon from "../../../assets/ArrowIcon";
import GiftIcon from "../../../assets/GiftIcon";
import Preview from "../../ImagePreview/Preview";
const CitoyenView: React.FC = () => {
  let location = useLocation();
  const state = location.state;

  const [reports, setReports] = useState<ReportObjectProps[]>([]);

  const CitoyenReportsMutation = useMutation((credentials: number) =>
    CitoyenReports(credentials)
  );
  useEffect(() => {
    CitoyenReportsMutation.mutateAsync(state.id).then((data) => {
      setReports(data.requests);
    });
  }, []);
  return (
    <div className="flex flex-col">
      <div className="flex flex-col m-auto">
        <div className="flex">
          <h1 className="my-4 text-m mx-4 font-bold">
            Vous êtes à {((reports.length * 3) / 25) * 100}% de réclamer votre
            prochaine récompense.
          </h1>
        </div>

        <div className="m-auto flex gap-10">
          <div
            className="radial-progress  bg-gray-100 m-auto"
            // @ts-ignore comment
            style={{ "--value": ((reports.length * 3) / 25) * 100 }}
            role="progressbar"
          >
            {((reports.length * 3) / 25) * 100}%
          </div>
          <div className="m-auto">
            <ArrowIcon></ArrowIcon>
          </div>
          <div className="m-auto">
            <GiftIcon></GiftIcon>
          </div>
        </div>
      </div>
      <div className="my-4 flex flex-col">
        <h1 className="text-3xl font-bold m-auto text-left">Signalements</h1>
        <div className="flex">
          <ul className="h-[700px] overflow-scroll overflow-x-hidden m-auto rounded-xl">
            {reports.map((report: ReportObjectProps, index: number) => (
              <li key={index} className="">
                <div className="card w-96 bg-blue-50 m-4">
                  <div className="card-body ">
                    <h2 className="card-title text-m font-bold">
                      {report.adresse}
                    </h2>
                    <p>Statut:{report.status}</p>
                    <div className="flex">
                      <div className="card-actions justify-end my-auto">
                        <Link
                          to="/report"
                          state={{
                            report: report,
                          }}
                        >
                          <button className="btn btn-primary">Détails</button>
                        </Link>
                      </div>
                      <div className="ml-auto">
                        {report.image ? (
                          <Preview
                            image={report.image}
                            width={100}
                            height={100}
                          ></Preview>
                        ) : (
                          <></>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default CitoyenView;
