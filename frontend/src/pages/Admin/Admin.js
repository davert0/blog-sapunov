import './Admin.css';
import React, { useState, useEffect } from 'react';

const Admin = () => {
    const [authenticated, setAuthenticated] = useState(false);
    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
          setAuthenticated(true);
        }
      }, []);
    const handleLoginFormSubmit = (event) => {
        event.preventDefault();
        const username = event.target.username.value;
        const password = event.target.password.value;
        if (username === 'admin' && password === 'password') {
          setAuthenticated(true);
          localStorage.setItem('token', 'yourTokenValue');
        }
      };

      if (!authenticated) {
        return (
            <div>
              <h1 className='admin-heading'>Login</h1>
              <form onSubmit={handleLoginFormSubmit} className="admin-form">
                <input type="text" name="username" placeholder="Username" className="admin-input" />
                <input type="password" name="password" placeholder="Password" className="admin-input" />
                <button type="submit" className="admin-button">Login</button>
              </form>
            </div>
          );
        }
    
    return (
      <div className="container">
        <h1 className="title">Admin</h1>
        <p className="description">Welcome to admin page.</p>
      </div>
    );
  };
  
  export default Admin;