import { useState } from "react";
import { TrackReport } from "../../Tools/AuthUtils";
import AlertIcon from "../../assets/AlertIcon";
import { useNavigate } from "react-router-dom";
import { useMutation } from "react-query";
import ServerError from "../../Types/Errors/ServerError";
import BaseDialog from "../Dialogs/BaseDialog";
import CheckIcon from "../../assets/CheckIcon";

interface Props {}
const TrackReportComponent: React.FC<Props> = () => {
  const [reportId, setReportId] = useState<string>("");
  const [buttonState, setButtonState] = useState("default");
  const navigate = useNavigate();

  const TrackReportMutation = useMutation((credentials: string) =>
    TrackReport(credentials)
  );

  async function handleTrack(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setButtonState("reqSent");
    console.log(reportId)
    await TrackReportMutation.mutateAsync(reportId)
      .then((report) => {
        console.log(report);
        setButtonState("success");
        //setTimeout(() => {
        //  navigate("/report", {
        //    state: { report: report },
        //  });
        //}, 1000);
      })
      .catch((e) => {
        setButtonState("default");
        if (e instanceof ServerError) {
          (
            document.getElementById("ServerFail") as HTMLDialogElement
          ).showModal();
        } else {
          // Show error dialog
          (
            document.getElementById("trackFail") as HTMLDialogElement
          ).showModal();
        }
      });
  }

  return (
    <div className="card flex flex-col w-96 mt-2 mb-10 m-auto h-1/2">
      <h2 className="my-4 text-3xl mx-4 font-bold m-auto">
        Veuillez insérer le numéro d'identifiant de votre signalement.
      </h2>
      <form onSubmit={handleTrack}>
        <label className="input input-bordered flex items-center gap-2 m-2">
          <AlertIcon></AlertIcon>
          <input
            type="text"
            className="grow"
            placeholder="#12AS34DE"
            required
            autoComplete="off"
            onChange={(e) => {
              setReportId(e.target.value);
            }}
            value={reportId}
          />
        </label>
        <div className="p-2 w-full m-auto flex">
          {buttonState == "reqSent" ? (
            <span className="loading loading-infinity loading-lg m-auto my-1"></span>
          ) : buttonState == "success" ? (
            <button className="btn btn-primary w-full my-2">
              <CheckIcon></CheckIcon>
            </button>
          ) : (
            <input
              className="btn btn-outline w-full"
              type="submit"
              value="Retrouver le signalement"
            />
          )}
        </div>
      </form>
      <BaseDialog
        componentName="trackFail"
        title="Il y a un soucis..."
        message="Nous n'avons pas pu retrouver le signalement lié à ce numéro de d'identifiant. Assurez vous de l'avoir bien écris, sinon, veuillez contacter le 311 pour plus de support."
      ></BaseDialog>
      <BaseDialog
        componentName="ServerFail"
        title="Whoops!"
        message="Notre serveur n'a pas pu traiter votre demande. Veuillez réessayer plus tard."
      ></BaseDialog>
    </div>
  );
};

export default TrackReportComponent;
