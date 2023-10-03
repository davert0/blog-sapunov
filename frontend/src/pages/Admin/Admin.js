import { useDispatch, useSelector } from 'react-redux';
import './Admin.css';
// @ts-ignore
import React, { useState, useEffect } from 'react';
import { actions, thunks } from 'store/slices/session';


const Admin = () => {
    const [authenticated, setAuthenticated] = useState(false);
    // @ts-ignore
    // @ts-ignore
    const { user } = useSelector(state => state.session);
    const dispatch = useDispatch();
    useEffect(() => {
      // @ts-ignore
      dispatch(thunks.getUser());
      // eslint-disable-next-line
    }, []);
  
    const handleLogout = () => {
      localStorage.removeItem('access_token')
      dispatch(actions.setUser(null));
      setAuthenticated(false);
  }  
    useEffect(() => {
        if (user) {
          setAuthenticated(true);
        }
      }, [user]);
    const handleLoginFormSubmit = (event) => {
        event.preventDefault();
        const username = event.target.username.value;
        const password = event.target.password.value;
        const formData = new FormData()
        formData.append('username', username)
        formData.append('password', password)
        // @ts-ignore
        dispatch(thunks.getToken(formData))
        // @ts-ignore
        if (user) {
          setAuthenticated(true);
          // @ts-ignore
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
        <button onClick={handleLogout}>Logout</button>
      </div>
    );
  };
  
  export default Admin;