import Router from "./Components/Router/Router";
import { BrowserRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "react-query";
import { Loader } from "@googlemaps/js-api-loader";
import { useEffect } from "react";
import { MAP_API_KEY } from "./Tools/Globals";

const queryClient = new QueryClient();

function App() {
  useEffect(()=>{
    const loader = new Loader({
      apiKey: "AIzaSyAYTcQYICvkJevt0kjlY6kOIoBVc6j6Vj0",
    });

    loader.importLibrary("places");
    loader.importLibrary("routes");
  },[])
  return (
    <QueryClientProvider client={queryClient}>
      <div className="roboto">
        <BrowserRouter>
          <Router></Router>
        </BrowserRouter>
      </div>
    </QueryClientProvider>
  );
}

export default App;
