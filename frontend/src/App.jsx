import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';

// Components
import Header from './components/Header';
import Login from './components/Login';
import HelpInfo from './components/HelpInfo';
import Contact from './components/Contact';
import Dashboard from './components/Dashboard';
import Registration from './components/Registration';
import ForgotPassword from './components/ForgotPassword';
import GlucoseLogs from './components/GlucoseLogs';
import Profile from './components/Profile';
import Appointment from './components/Appointment';
import Notifications from './components/Notifications';
import MedicalForms from './components/MedicalForms';
import Products from './components/Products';

export default function AimPlusMedicalSupplies() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [jwtToken, setJwtToken] = useState('');

  return (
    <Router>
      <div>
        <Header isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} setJwtToken={setJwtToken} />
        <Routes>
          <Route path="/" element={isLoggedIn ? <Navigate to='/dashboard'/> : <Login setIsLoggedIn={setIsLoggedIn} setJwtToken={setJwtToken} />} />
          <Route path="/dashboard/*" element={isLoggedIn ? <Dashboard jwtToken={jwtToken}/> : <Navigate to="/" />} >
            <Route path="profile" element={<Profile />} />
            <Route path="glucose-logs" element={<GlucoseLogs />} />
            <Route path="appointments" element={<Appointment />} />
            <Route path="notifications" element={<Notifications />} />
            <Route path="medical-forms" element={<MedicalForms />} />
            <Route path="products" element={<Products />} />
          </Route>
          <Route path="/help" element={<HelpInfo />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  )
}