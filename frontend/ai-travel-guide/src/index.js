import React from 'react';
import { Auth0Provider } from '@auth0/auth0-react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import App from './App'
import LoginButton from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Auth0Provider
    domain="dev-mbl774dckalmqvb3.us.auth0.com"
    clientId="04UXpjbiNK8G9sYdqq2c6w27KBt4BNBH"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}>
   
    <LoginButton />
    </Auth0Provider>

  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
