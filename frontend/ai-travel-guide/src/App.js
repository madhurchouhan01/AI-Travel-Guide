import React, { useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import "./App.css";
import Travel from "./components/Travel";
import Navbar from "./components/Navbar";
import Chatbot from "./components/TravelBot";
import Landing from "./components/Landing";
import "./components/TravelBot.css";

function AuthHandler() {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return isAuthenticated ? (
    <button onClick={() => logout()} >Logout</button>
  ) : (
    <button onClick={() => loginWithRedirect()}>Login</button>
  );
}

function LoginButton() {

  const { user, isAuthenticated } = useAuth0();

  useEffect(() => {
    if (isAuthenticated) {
      const userData = {
        auth0_user_id: user.sub,
        email: user.email,
        email_verified: user.email_verified || false,
        phone_number: user.phone_number || "",
        profile_picture: user.picture || "",
        name: user.name || "Anonymous",
      };

      fetch("http://localhost:8000/api/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          console.log("Data sent to backend:", data);
        })
        .catch((error) => {
          console.error("Fetch error:", error);
        });
    }
  }, [isAuthenticated, user]);

  return (
    <div className="app">
      <div className="authentication">
        <header className="auth-header">
          <Navbar />
          {!isAuthenticated && <Landing />}
          {isAuthenticated && <>
            {/* <h1>Hello, {user.name}👋</h1> */}
            <div id="main">
              <div id="mainContent">
                <Travel />
              </div>
              <div id="sideContent">
                <Chatbot />
              </div>
            </div>
          </>}

        </header>
      </div>
    </div>

  );
}

export default LoginButton;
