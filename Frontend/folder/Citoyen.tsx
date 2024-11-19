import { useEffect, useState } from "react";
import CheckIcon from "../../../assets/CheckIcon";
import { useMutation } from "react-query";
import { CitoyenLogIn } from "../../../Tools/AuthUtils";
import { Link, useLocation, useNavigate } from "react-router-dom";
import ServerError from "../../../Types/Errors/ServerError";
import BaseDialog from "../../Dialogs/BaseDialog";

const Citoyen: React.FC = () => {
  const [tel, setTel] = useState("");
  const [fname, setFname] = useState<string>("");
  const [lname, setLname] = useState<string>("");
  const [buttonState, setButtonState] = useState("default");
  const navigate = useNavigate();

  let location = useLocation();

  const CitoyenLogMutation = useMutation(
    (credentials: { tel: string; fname: string; lname: string }) =>
      CitoyenLogIn(credentials)
  );

  async function handleLogIn(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setButtonState("reqSent");
    await CitoyenLogMutation.mutateAsync({ tel, fname, lname })
      .then((data) => {
        setButtonState("success");
        localStorage.setItem("logged", "citoyen," + data.id);
        setTimeout(() => {
          navigate("/user", {
            state: { id: data.id },
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
            document.getElementById("loginFail") as HTMLDialogElement
          ).showModal();
        }
      });
  }

  useEffect(() => {
    if (localStorage.getItem("logged")?.split(",")[0] == "citoyen") {
      navigate("/user", {
        state: { id: localStorage.getItem("logged")?.split(",")[1] },
      });
    }
    if (localStorage.getItem("logged")?.split(",")[0] == "employe") {
      navigate("/team", {
        state: { id: localStorage.getItem("logged")?.split(",")[1] },
      });
    }
  });

  return (
    <div>
      <div className="flex w-full">
        <h1 className="my-4 text-3xl mx-4 font-bold m-auto">Connexion</h1>
      </div>

      <h1 className="my-4 text-m mx-4 ">
        Veuillez notez que si vous n'avez jamais signalé de nid-de-poule, vous
        n'avez pas de compte dans notre système.
      </h1>
      <div className="card w-max m-auto bg-base-100 shadow-xl">
        <div className="card-body">
          <form className="flex flex-col m-auto gap-4" onSubmit={handleLogIn} autoComplete="true">
            <div className="border-b-4 pb-4">
              <p>Numéro de téléphone</p>
              <label>
                <input
                  className="input input-bordered ml-auto w-full"
                  type="tel"
                  placeholder=""
                  onChange={(e) => setTel(e.target.value)}
                  autoComplete="true"
                />
              </label>
            </div>

            <div>
              <label>
                <p className="m-auto">Prenom</p>
                <input
                  className="input input-bordered ml-auto w-full"
                  type="text"
                  value={fname}
                  onChange={(e) => setFname(e.target.value)}
                  required
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
            </div>
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
                  value="Se connecter"
                />
              )}
            </div>
          </form>
        </div>
      </div>
      <BaseDialog
        componentName="loginFail"
        title="Il y a un soucis..."
        message="Nous n'avons pas pu retrouver de dossier avec les coordonnées que vous avez inscrit. Veuillez changer de méthode d'identification ou réessayer plus tard."
      ></BaseDialog>
      <BaseDialog
        componentName="ServerFail"
        title="Whoops!"
        message="Notre serveur n'a pas pu traiter votre demande. Veuillez réessayer plus tard."
      ></BaseDialog>
    </div>
  );
};

export default Citoyen;
