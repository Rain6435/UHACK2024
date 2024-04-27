import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import NotFound from "../404/NotFound";
import Login from "../LogIn/Login";
import Navbar from "../NavigationBar/Navbar";
import Team from "../Team/Team";
import TrackReportComponent from "../TrackReport/TrackReport";

const Router: React.FC = () => {
  return (
    <div className="h-screen w-screen overflow-hidden" data-theme="light">
      <Navbar></Navbar>
      <Routes>
        <Route path="/" element={<Home></Home>}></Route>
        <Route path="/login" element={<Login></Login>}></Route>
        <Route path="/team" element={<Team></Team>}></Route>
        <Route path="/track" element={<TrackReportComponent></TrackReportComponent>}></Route>
        <Route path="*" element={<NotFound></NotFound>}></Route>
      </Routes>
    </div>
  );
};

export default Router;
