import { Link, Outlet } from "react-router-dom";
import HomeIcon from "../../assets/HomeIcon";
import PersonIcon from "../../assets/PersonIconEmpty";

interface Props {}

const Navbar: React.FC<Props> = () => {
  const handleClick = () => {
    const elem = document.activeElement;
    if (elem) {
      (elem as HTMLElement).blur();
    }
  };

  return (
    <div className="w-full">
      <div className="navbar bg-base-100 justify-center">
        <Link to="/">
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
            <li onClick={handleClick}>
              <a className="justify-between">Retracer un report</a>
            </li>
            <li onClick={handleClick}>
              <Link to="/login">
                <p>Employé</p>
              </Link>
            </li>
          </ul>
        </div>
      </div>
      <Outlet></Outlet>
    </div>
  );
};

export default Navbar;
