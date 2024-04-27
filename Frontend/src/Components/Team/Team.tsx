import { useLocation } from "react-router-dom";

interface Props {}

const Team: React.FC<Props> = () => {
  let location = useLocation();
  const state = location.state;
  const teamId = state.teamId;
  console.log(state);
  return <div>{teamId}</div>;
};

export default Team;
