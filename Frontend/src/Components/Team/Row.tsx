import { useState } from "react";
import { ReportObjectProps } from "../../Types/Types";
import { useMutation } from "react-query";
import { UpdateStatus, UpdateProps } from "../../Tools/AuthUtils";
import ServerError from "../../Types/Errors/ServerError";
import BaseDialog from "../Dialogs/BaseDialog";

interface Props {
  report: ReportObjectProps;
  index: number;
}

const Row: React.FC<Props> = (props) => {
  const [report, setReport] = useState(props.report);
  const index = props.index;
  const [status, setStatus] = useState("Changer");
  
  const [changed, setChanged] = useState(false);

  const UpdateMutation = useMutation((credentials: UpdateProps) =>
    UpdateStatus(credentials)
  );

  const handleClick = (e: any) => {
    setStatus(e.target.value);
    setChanged(true);
    const elem = document.activeElement;
    if (elem) {
      (elem as HTMLElement).blur();
    }
  };

  async function handleSave(
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) {
    e.preventDefault();
    await UpdateMutation.mutateAsync({ id: report.id, status: status })
      .then((resStatus) => {
        if (resStatus == 201) {
          setTimeout(() => {
            setReport({...report,status:status})
            window.location.reload();
          });
        }
      })
      .catch((e) => {
        if (e instanceof ServerError) {
          (
            document.getElementById("ServerFail") as HTMLDialogElement
          ).showModal();
        }else{
            (
              document.getElementById("updateFail") as HTMLDialogElement
            ).showModal();
        }
      });
  }

  return (
    <div key={index}>
      <li key={index} className="flex">
        <p className="mr-auto my-auto w-1/3">{report.id}</p>
        <p className="m-auto w-1/3 text-center">{props.report.status}</p>
        <div className="w-1/3 flex">
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
                  className={report.status == "Complété" ? "hidden" : "btn m-2"}
                  onClick={handleClick}
                  value="Complété"
                >
                  Complété
                </button>
              </ul>
            </div>
          )}
        </div>
      </li>
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
