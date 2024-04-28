import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import NotFound from "../404/NotFound";
import Login from "../LogIn/Login";
import Navbar from "../NavigationBar/Navbar";
import Team from "../Team/Team";
import TrackReportComponent from "../TrackReport/TrackReport";
import ViewReport from "../ViewReport/ViewReport";
import Citoyen from "../Citoyen/Citoyen";
import CitoyenView from "../Citoyen/CitoyenView";
import Admin from "../Admin/Admin";
import Report from "../Report/Report";

const Router: React.FC = () => {
  return (
    <div
      className="min-h-screen overflow-auto flex flex-col"
      data-theme="light"
    >
      <header>
        <Navbar></Navbar>
      </header>
      <div className="flex-grow">
        <Routes>
          <Route path="/" element={<Home></Home>}></Route>
          <Route path="/employe" element={<Login></Login>}></Route>
          <Route path="/team" element={<Team></Team>}></Route>
          <Route
            path="/track"
            element={<TrackReportComponent></TrackReportComponent>}
          ></Route>
          <Route path="/report" element={<ViewReport></ViewReport>}></Route>
          <Route path="/citoyen" element={<Citoyen></Citoyen>}></Route>
          <Route path="/user" element={<CitoyenView></CitoyenView>}></Route>
          <Route path="/admin" element={<Admin></Admin>}></Route>
          <Route path="/signaler" element={<Report></Report>}></Route>
          <Route path="*" element={<NotFound></NotFound>}></Route>
        </Routes>
      </div>

      <footer className="m-auto flex">
        <p className="card-title m-auto my-4 text-xl font-bold w-[350px] text-center">
          Signaler, c'est prévenir et protéger, et aussi gagner!
        </p>
      </footer>
    </div>
  );
};

export default Router;
