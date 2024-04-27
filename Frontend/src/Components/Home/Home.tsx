import Report from "../Report/Report";

const Home:React.FC = () => {
    return (
      <div className="flex flex-col">
        <h1 className="text-2xl m-auto">UHACK 2024</h1>
        <Report></Report>
      </div>
    );
}

export default Home;