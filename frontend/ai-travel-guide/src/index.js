import React from 'react';
import { Auth0Provider } from '@auth0/auth0-react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App'
import LoginButton from './App';
import Travel from './components/Travel';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Auth0Provider
    domain="dev-mbl774dckalmqvb3.us.auth0.com"
    clientId="04UXpjbiNK8G9sYdqq2c6w27KBt4BNBH"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}>
    <LoginButton />
    </Auth0Provider>
);
