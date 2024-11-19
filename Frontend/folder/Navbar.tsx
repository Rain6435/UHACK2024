import { Link, Outlet, useNavigate } from "react-router-dom";
import HomeIcon from "../../assets/HomeIcon";
import PersonIcon from "../../assets/PersonIconEmpty";

interface Props {}

const Navbar: React.FC<Props> = () => {
  const navigate = useNavigate();
  const handleClick = () => {
    const elem = document.activeElement;
    if (elem) {
      (elem as HTMLElement).blur();
    }
  };
  return (
    <div className="w-full">
      <div className="navbar bg-base-100 justify-center">
        <Link to="/" state={{}}>
          <div className="w-[50px] mr-auto">
            <button className="btn btn-square btn-ghost">
              <HomeIcon></HomeIcon>
            </button>
          </div>
        </Link>
        <div className="w-max m-auto">
          <a className="btn btn-ghost text-xl">Alerte Nid-de-Poule</a>
        </div>
        <div className="dropdown dropdown-hover dropdown-end">
          <div
            tabIndex={0}
            role="button"
            className="btn btn-ghost btn-circle avatar"
          >
            <PersonIcon></PersonIcon>
          </div>
          <ul
            tabIndex={0}
            className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52"
          >
            <li
              onClick={handleClick}
              className={
                localStorage.getItem("logged")?.split(",")[0] == "employe"
                  ? "hidden"
                  : localStorage.getItem("logged")?.split(",")[0] == "admin"
                  ? "hidden"
                  : "btn m-2"
              }
            >
              <Link to="/citoyen" state={{}}>
                <p>Citoyen</p>
              </Link>
            </li>
            <li
              onClick={handleClick}
              className={
                localStorage.getItem("logged")?.split(",")[0] == "citoyen"
                  ? "hidden"
                  : "btn m-2"
              }
            >
              <Link to="/employe" state={{}}>
                <p>Employé</p>
              </Link>
            </li>

            <li onClick={handleClick} className="btn m-2">
              <Link to="/track" state={{}}>
                <p className="w-full">Suivi</p>
              </Link>
            </li>
            <li
              onClick={() => {
                handleClick();
                localStorage.clear();
                navigate("/");
              }}
              className={
                localStorage.getItem("logged") != undefined
                  ? "btn btn-error m-2"
                  : "hidden"
              }
            >
              <p>Se déconnecter</p>
            </li>
          </ul>
        </div>
      </div>
      <Outlet></Outlet>
    </div>
  );
};

export default Navbar;
