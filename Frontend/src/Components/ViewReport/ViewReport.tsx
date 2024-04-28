import { useState } from "react";
import { ReportObjectProps } from "../../Types/Types";
import { useLocation } from "react-router-dom";

const ViewReport:React.FC = () => {
    let location = useLocation();
    const [report, setReport] = useState<ReportObjectProps>(location.state.report);
    return (
      <div className="flex">
        <div className="card w-96 bg-base-100 shadow-xl m-auto">
          <div className="card-body">
            <p className="my-4 text-3xl mx-4 font-bold">
              Identifiant:{report.id}
            </p>
            <p className="my-4 text-3xl mx-4 font-bold flex">
              Dangereux:
              {report.is_dangerous ? (
                <input
                  type="checkbox"
                  className="checkbox m-auto"
                  checked
                  readOnly
                />
              ) : (
                <input type="checkbox m-auto" disabled className="checkbox" />
              )}
            </p>
            <p className="my-4 text-3xl mx-4 font-bold flex">
              Statut: {report.status}
            </p>

            <p className="my-4 text-l mx-4 font-bold flex">
              Date de création: {report.creation_date}
            </p>
            <p className=" text-l mx-4 font-bold flex">
              Date de réparation:{" "}
              {report.fix_date ? report.fix_date : "Indéfinie"}
            </p>
          </div>
        </div>
      </div>
    );
}

export default ViewReport;