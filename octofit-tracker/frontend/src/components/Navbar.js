import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
        <div className="navbar-nav">
          <Link className="nav-link" to="/dashboard">Dashboard</Link>
          <Link className="nav-link" to="/activities">Activities</Link>
          <Link className="nav-link" to="/teams">Teams</Link>
          <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
          <Link className="nav-link" to="/login">Login</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;