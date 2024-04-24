import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import NotFound from "../404/NotFound";

const Router: React.FC = () => {
  return (
    <div className="h-screen w-full" data-theme="light">
      <Routes>
        <Route path="/" element={<Home></Home>}></Route>
        <Route path="*" element={<NotFound></NotFound>}></Route>
      </Routes>
    </div>
  );
};

export default Router;
