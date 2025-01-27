import React, { useState } from 'react';
import { useAuth0 } from '@auth0/auth0-react'; // Import useAuth0
import './Navbar.css';

const Navbar = () => {
  const [isDropdownOpen, setDropdownOpen] = useState(false);
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  const toggleDropdown = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">Travel Buddy</div>
      <ul className="navbar-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#recommendations">Recommendations</a></li>
        <li className="dropdown">
          <button className="dropdown-btn" onClick={toggleDropdown}>
            Plan Your Trip ▼
          </button>
          {isDropdownOpen && (
            <ul className="dropdown-menu">
              <li><a href="#planner">Trip Planner</a></li>
              <li><a href="#checklist">Packing Checklist</a></li>
              <li><a href="#updates">Weather & Updates</a></li>
            </ul>
          )}
        </li>
        <li><a href="#saved">Saved Trips</a></li>
        <li><a href="#about">About Us</a></li>
        <li><a href="#help">Help</a></li>
        <li>
          {isAuthenticated ? (
            <button className="auth-btn" onClick={() => logout({ returnTo: window.location.origin })}>
              Logout
            </button>
          ) : (
            <button className="auth-btn" onClick={() => loginWithRedirect()}>
              Login
            </button>
          )}
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
