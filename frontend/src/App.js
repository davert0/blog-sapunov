import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home/Home';
import About from './pages/About/About';
import Admin from './pages/Admin/Admin';

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route exact path="/" element={<Home/>} />
        <Route exact path="/about" element={<About/>} />
        <Route exact path="/admin" element={<Admin/>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
};

export default App;