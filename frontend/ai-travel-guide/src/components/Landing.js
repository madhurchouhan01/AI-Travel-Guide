import React from "react";
import "./Landing.css"; 
import { useAuth0 } from '@auth0/auth0-react'; // Import useAuth0

const Landing = () => {
  const { loginWithRedirect} = useAuth0();
  
  return (
    <div className="landing">
      <div className="landing-content">
        <h1>Welcome to Travel Buddy 🌴🚎</h1>
        <p>Your ultimate travel companion powered by AI. <br></br>
          Build, personalize, and optimize your itineraries with our free AI trip planner. Designed for vacations, workations, and everyday adventures.</p>
        <button className="button-81" onClick={() => loginWithRedirect()}>Create a New Trip ✈</button>
      </div>
    </div>
  );
};

export default Landing;

