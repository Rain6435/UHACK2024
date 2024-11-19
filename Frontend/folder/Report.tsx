import { useState } from "react";
import "./Report.css";
import Autocomplete from "react-google-autocomplete";
import { CreateReport, ReportProps, TrackReport } from "../../Tools/AuthUtils";
import CheckIcon from "../../assets/CheckIcon";
import { useMutation } from "react-query";
import { fileToBase64 } from "../../Tools/FileUtils";
import ServerError from "../../Types/Errors/ServerError";
import BaseDialog from "../Dialogs/BaseDialog";
import PlusIcon from "../../assets/PlusIcon";
import { useNavigate } from "react-router-dom";
import { MAP_API_KEY } from "../../Tools/Globals";
interface Props {}

const Report: React.FC<Props> = () => {
  const [fname, setFname] = useState<string>("");
  const [lname, setLname] = useState<string>("");
  const [address, setAddress] = useState<any>();
  const [dangerous, setDangerous] = useState(false);
  const [image, setImage] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [tel, setTel] = useState<string>("");

  const [buttonState, setButtonState] = useState("default");

  const [reportId, setReportId] = useState<string>("");

  const navigate = useNavigate();

  const CreateReportMutation = useMutation((credentials: ReportProps) =>
    CreateReport(credentials)
  );

  const TrackReportMutation = useMutation((credentials: string) =>
    TrackReport(credentials)
  );

  async function handleUpload(event: React.FormEvent<HTMLInputElement>) {
    const target = event.target as HTMLInputElement & { files: FileList };

    if (target.files && target.files.length > 0) {
      const newImage: File = target.files[0];
      fileToBase64(newImage)
        .then((base64String) => {
          setImage(base64String);
        })
        .catch((error) => {
          console.error("Error converting file to Base64:", error);
        });
    }
  }

  async function handleReport(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setButtonState("reqSent");
    await CreateReportMutation.mutateAsync({
      userFname: fname,
      userLname: lname,
      potholeAddress: address,
      dangerous: dangerous,
      image: image,
      email: email,
      tel: tel,
    })
      .then(async (reportId) => {
        setButtonState("success");
        setReportId(reportId.payload);
        await TrackReportMutation.mutateAsync(reportId)
          .then((report) => {
            setButtonState("success");
            setTimeout(() => {
              navigate("/report", {
                state: { report: report },
              });
            }, 1000);
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
                document.getElementById("createFail") as HTMLDialogElement
              ).showModal();
            }
          });
      })
      .catch((e: any) => {
        setButtonState("default");
        if (e instanceof ServerError) {
          (
            document.getElementById("ServerFail") as HTMLDialogElement
          ).showModal();
        } else {
          // Show error dialog
          (
            document.getElementById("createFail") as HTMLDialogElement
          ).showModal();
        }
      });
  }

  return (
    <div className="m-auto card flex px-4">
      <p className="my-4 text-xl mx-4 font-bold">Signaler un nid-de-poule</p>
      <div className="card w-full m-auto bg-base-100 shadow-xl">
        <div className="card-body w-full">
          <form onSubmit={handleReport} className="flex flex-col m-auto gap-4">
            <label>
              <p className="m-auto">Prenom</p>
              <input
                className="input input-bordered ml-auto w-full"
                type="text"
                value={fname}
                onChange={(e) => setFname(e.target.value)}
                required
                autoComplete="off"
              />
            </label>
            <label>
              <p className="m-auto">Nom de famille</p>
              <input
                className="input input-bordered ml-auto w-full"
                type="text"
                value={lname}
                onChange={(e) => setLname(e.target.value)}
                required
                autoComplete="off"
              />
            </label>
            <label>
              <p className="m-auto">Adresse du nid-de-poule</p>
              <Autocomplete
                apiKey={MAP_API_KEY}
                onPlaceSelected={(place) => {
                  setAddress(place);
                }}
                className="input input-bordered ml-auto w-full"
                options={{
                  types: ["address"],
                  componentRestrictions: { country: "ca" },
                }}
                placeholder=""
                required
                onError={(e)=>{
                  console.log(e)
                }}
              ></Autocomplete>
            </label>
            <label>
              <p className="m-auto">Voulez vous être notifié?</p>
              <input
                className="input input-bordered ml-auto w-full"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                autoComplete="off"
                placeholder="Ajouter votre courriel"
              />
            </label>
            <label>
              <input
                className="input input-bordered ml-auto w-full"
                type="tel"
                value={tel}
                onChange={(e) => setTel(e.target.value)}
                autoComplete="off"
                placeholder="Ajouter votre telephone"
              />
            </label>
            <label className="flex">
              <p className="m-auto">
                <b>Dangeureux?</b>
              </p>
              <input
                type="checkbox"
                className="checkbox"
                onChange={() => setDangerous(!dangerous)}
              />
            </label>
            <label>
              <div className="flex">
                <p className="m-auto">Ajouter une image?</p>
                <button
                  className="btn btn-outline"
                  onClick={(e) => {
                    e.preventDefault();
                    (document.getElementById("getFile") as any).click();
                  }}
                >
                  <PlusIcon></PlusIcon>
                </button>
              </div>

              <input
                type="file"
                className="hidden"
                id="getFile"
                accept="image/*"
                capture="environment"
                onChange={handleUpload}
              />
            </label>
            <div className="p-2 w-full m-auto flex">
              {buttonState == "reqSent" ? (
                <span className="loading loading-infinity loading-lg m-auto my-1"></span>
              ) : buttonState == "success" ? (
                <button className="btn btn-success w-full my-2">
                  <CheckIcon></CheckIcon>
                </button>
              ) : (
                <input
                  className="btn btn-outline w-full"
                  type="submit"
                  value="Signaler"
                />
              )}
            </div>
          </form>
        </div>
      </div>
      <BaseDialog
        componentName="createFail"
        title="Il a y un ick!"
        message="Malheureusement, nous n'avons pas pu traiter votre demande. Il existe déjà un signalement avec les coordonnées insérées."
      ></BaseDialog>
      <BaseDialog
        componentName="ServerFail"
        title="Whoops!"
        message="Notre serveur n'a pas pu traiter votre demande. Veuillez réessayer plus tard."
      ></BaseDialog>
    </div>
  );
};

export default Report;
