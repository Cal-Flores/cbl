import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import AllTeams from "./components/AllTeams/allTeams";
import SingleTeam from "./components/SingleTeam/singleTeam";
import SingleFighter from "./components/SingleFighter/singleFighter";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/teams/:teamId" >
            <SingleTeam />
          </Route>
          <Route exact path="/" >
            <AllTeams />
          </Route>
          <Route exact path="/fighter/:fightId" >
            <SingleFighter />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
