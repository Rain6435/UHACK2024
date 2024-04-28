import { Link } from "react-router-dom";

const Home: React.FC = () => {
  return (
    <div className="m-auto card flex px-4 h-full">
      <figure>
        <img
          src="https://www.gatineau.ca/docs/guichet_municipal/identite_visuelle/logo.gif"
          alt="Shoes"
          width={200}
        />
      </figure>
      <div className="card-body">
        <h2 className="card-title m-2 text-3xl font-bold">
          Bienvenue à la ville de Gatineau
        </h2>
        <p>
          Cette application vous permet de signaler un nid-de-poule ainsi que
          retracer l'avancement de la réparation.
          <br />
          <br />
          De plus, bénificier de récompenses tels dont des rabais sur des
          services offerts par la ville ou sur des attractions touristiques.
          <br />
          <br />
          Commencez à accumuler des récompenses dès maintenant!
        </p>
        <div className="card-actions justify-center my-4">
          <Link to="/signaler">
            <button className="btn btn-primary">
              Signaler un nid-de-poule
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
