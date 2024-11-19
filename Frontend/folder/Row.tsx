import { useEffect, useState } from "react";
import { ReportObjectProps } from "../../Types/Types";
import { useMutation } from "react-query";
import {
  UpdateStatus,
  UpdateProps,
  GetTeams,
  TransferReport,
} from "../../Tools/AuthUtils";
import ServerError from "../../Types/Errors/ServerError";
import BaseDialog from "../Dialogs/BaseDialog";
import { Link } from "react-router-dom";
import EyeIcon from "../../assets/EyeIcon";

interface Props {
  report: ReportObjectProps;
  teamId: number;
}

const Row: React.FC<Props> = (props) => {
  const [report, setReport] = useState(props.report);
  const [status, setStatus] = useState("Changer");
  const [teams, setTeams] = useState<[]>();

  const [changed, setChanged] = useState(false);

  const TransferReportMutation = useMutation((report: ReportObjectProps) =>
    TransferReport(report)
  );

  const GetTeamsMutation = useMutation(() => GetTeams());

  const UpdateMutation = useMutation((credentials: UpdateProps) =>
    UpdateStatus(credentials)
  );

  const admin = localStorage.getItem("logged")?.split(",")[0] == "admin";

  const handleClick = (e: any) => {
    setStatus(e.target.value);
    setChanged(true);
    const elem = document.activeElement;
    if (elem) {
      (elem as HTMLElement).blur();
    }
  };

  async function transferReport(destTeamId: number) {
    var tempReport = report;
    tempReport.team_id = destTeamId;

    await TransferReport(tempReport)
      .then((resStatus) => {
        if (resStatus == 201) {
          setTimeout(() => {
            window.location.reload();
          }, 500);
        }
      })
      .catch((e) => {
        if (e instanceof ServerError) {
          (
            document.getElementById("ServerFail") as HTMLDialogElement
          ).showModal();
        } else {
          (
            document.getElementById("updateFail") as HTMLDialogElement
          ).showModal();
        }
      });
  }

  async function handleSave(
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) {
    e.preventDefault();
    await UpdateMutation.mutateAsync({ id: report.id, status: status })
      .then((resStatus) => {
        if (resStatus == 201) {
          setTimeout(() => {
            window.location.reload();
          },500);
        }
      })
      .catch((e) => {
        if (e instanceof ServerError) {
          (
            document.getElementById("ServerFail") as HTMLDialogElement
          ).showModal();
        } else {
          (
            document.getElementById("updateFail") as HTMLDialogElement
          ).showModal();
        }
      });
  }

  useEffect(() => {
    if (admin) {
      GetTeamsMutation.mutateAsync().then((data) => {
        setTeams(data);
      });
    }
  }, []);

  return (
    <div>
      <div className="flex">
        <div className="mr-auto my-auto w-1/3 flex">
          <Link
            to="/report"
            state={{
              report: report,
            }}
          >
            <button className="btn w-[90px]">
              {report.id}
              <EyeIcon></EyeIcon>
            </button>
          </Link>
        </div>

        <p className="m-auto w-1/3 text-center">{props.report.status}</p>

        <div className="w-1/3 flex">
          <div className="ml-auto flex gap-4 flex-col lg:flex-row">
            {admin ? (
              <div className="dropdown dropdown-end">
                <div
                  tabIndex={0}
                  role="button"
                  className="btn m-auto w-[100px] sm:w-[150px]"
                >
                  Transférer
                </div>
                <ul
                  tabIndex={0}
                  className="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52"
                >
                  {teams?.map((team: any) => (
                    <button
                      className={
                        team.info.id == props.teamId
                          ? "hidden"
                          : "btn m-2 flex w-full p-0"
                      }
                      value={team.info.id}
                      onClick={(e) => {
                        e.preventDefault();
                        transferReport(team.info.id);
                      }}
                    >
                      Team:<u>{team.info.id}</u> / N-d-p:
                      <b>{team.requests.length}</b>
                    </button>
                  ))}
                </ul>
              </div>
            ) : (
              <></>
            )}
            {changed ? (
              <button
                className="btn btn-success ml-auto w-[100px] sm:w-[150px]"
                onClick={handleSave}
              >
                Confirmer
              </button>
            ) : (
              <div className="dropdown dropdown-end ml-auto ">
                <div
                  tabIndex={0}
                  role="button"
                  className="btn m-auto  w-[100px] sm:w-[150px]"
                >
                  {status}
                </div>
                <ul
                  tabIndex={0}
                  className="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52"
                >
                  <button
                    className={
                      report.status == "En attente" ? "hidden" : "btn m-2"
                    }
                    onClick={handleClick}
                    value="En attente"
                  >
                    En attente
                  </button>
                  <button
                    className={
                      report.status == "En réparation" ? "hidden" : "btn m-2"
                    }
                    onClick={handleClick}
                    value="En réparation"
                  >
                    En réparation
                  </button>
                  <button
                    className={
                      report.status == "Complété" ? "hidden" : "btn m-2"
                    }
                    onClick={handleClick}
                    value="Complété"
                  >
                    Complété
                  </button>
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
      <BaseDialog
        componentName="updateFail"
        title="Oh no..."
        message="Nous n'avons pas pu changer le statut de ce nid-de-poule."
      ></BaseDialog>
      <BaseDialog
        componentName="ServerFail"
        title="Whoops!"
        message="Notre serveur n'a pas pu traiter votre demande. Veuillez réessayer plus tard."
      ></BaseDialog>
    </div>
  );
};

export default Row;
