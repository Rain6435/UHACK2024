import { useEffect, useState } from "react";
import { TeamLogIn } from "../../Tools/AuthUtils";
import { useMutation } from "react-query";
import { useNavigate } from "react-router-dom";
import PersonIconFilled from "../../assets/PersonIconFilled";
import ServerError from "../../Types/Errors/ServerError";
import CheckIcon from "../../assets/CheckIcon";
import BaseDialog from "../Dialogs/BaseDialog";

interface Props {}

const Login: React.FC<Props> = () => {
  const [teamId, setTeamId] = useState<string>("");
  const navigate = useNavigate();
  const [buttonState, setButtonState] = useState("default");
  const TeamLogInMutation = useMutation((credentials: string) =>
    TeamLogIn(credentials)
  );

  async function handleLogIn(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setButtonState("reqSent");
    await TeamLogInMutation.mutateAsync(teamId)
      .then((data) => {
        setButtonState("success");
        localStorage.setItem("logged","employe,"+{teamId})
        setTimeout(() => {
          navigate("/team", {
            state: { id: teamId },
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

  useEffect(()=>{
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
  })

  return (
    <div className="card flex flex-col w-96 mt-2 mb-10 m-auto h-1/2">
      <h2 className="my-4 text-3xl mx-4 font-bold">
        Veuillez insérer le numéro d'identifiant de votre équipe.
      </h2>
      <form
        onSubmit={handleLogIn}
        className="flex flex-col m-auto bg-base-200 shadow-xl gap-4 rounded-2xl"
      >
        <label className="input input-bordered flex items-center gap-2 m-2">
          <PersonIconFilled></PersonIconFilled>
          <input
            type="text"
            className="grow"
            placeholder="Team ID"
            value={teamId}
            onChange={(e) => setTeamId(e.target.value)}
            required
            autoComplete="off"
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
              value="Se connecter"
            />
          )}
        </div>
      </form>
      <BaseDialog
        componentName="loginFail"
        title="Log in failed"
        message="Oops, there seems to be an error in your email or your password. Please try again."
      ></BaseDialog>
      <BaseDialog
        componentName="ServerFail"
        title="Whoops!"
        message="Notre serveur n'a pas pu traiter votre demande. Veuillez réessayer plus tard."
      ></BaseDialog>
    </div>
  );
};

export default Login;
