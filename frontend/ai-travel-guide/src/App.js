import React, { useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import Travel from "./components/Travel";


function AuthHandler() {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return isAuthenticated ? (
    <button onClick={() => logout()} className="bg-green-400 text-black p-4 rounded xl">Logout</button>
  ) : (
    <button onClick={() => loginWithRedirect()}className="bg-green-400 text-black p-4 rounded xl">Login</button>
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
    <>
        <div className="authentication">
      <header className="auth-header">
        {isAuthenticated && <>
        <h1>Hello, {user.name}👋</h1>
        <Travel/>
        </>}
        
        <AuthHandler />
        
      </header>
    </div>
    </>

  );
}

export default LoginButton;
