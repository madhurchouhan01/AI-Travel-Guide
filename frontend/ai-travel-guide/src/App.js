import React from "react";
import { useAuth0 } from "@auth0/auth0-react";


function App(){
  return <h1>Hello</h1>
}


function LoginButton() {
  const { user, loginWithRedirect, logout, isAuthenticated } = useAuth0();
  console.log('current user', user)
  if (isAuthenticated){
  const userData = {
    auth0_user_id: user.sub,
    email : user.email,
    email_verified : user.email_verified || false,
    phone_number : user.phone_number || "",
    profile_picture: user.picture || "",
    name : user.name  || "Anonymous",
  }
  console.log("User data being sent:", userData);
  const jsonData = JSON.stringify(userData);
  console.log('its working1')
  console.log(jsonData)
  console.log('its working2')
  fetch('http://localhost:8000/api/register/', { 
    method: 'POST', 
    headers: {
        'Content-Type': 'application/json', 
    },
    body: jsonData, 
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json(); 
})
.then(data => {
    // Handle the response from the Django backend 
    console.log('Data sent to backend:', data); 
})
.catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
});

  }
  return (
    <div className="authentication">
      <header className="auth-header">
       { isAuthenticated && <h1>Hello, {user.name} 👋 </h1>}
        {isAuthenticated ? (
          <button onClick={(e) => logout()}>Logout</button>
        ): (
          <button onClick={(e)=> loginWithRedirect()}>Login Button</button>
        )}
      </header>
    </div>
);
}
export default LoginButton;
