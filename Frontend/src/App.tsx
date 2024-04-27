import Router from "./Components/Router/Router";
import { BrowserRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "react-query";

const queryClient = new QueryClient();

function App() {
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
