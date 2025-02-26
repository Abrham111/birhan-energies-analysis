import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Info from './components/Info';
import Summary from './components/Summary';
import Chart from './components/Chart';
import './App.css';

const App = () => {
  const location = useLocation();
  const [showInfo, setShowInfo] = useState(true);

  useEffect(() => {
    if (location.pathname === '/summary' || location.pathname === '/chart') {
      setShowInfo(false);
    } else {
      setShowInfo(true);
    }
  }, [location]);

  return (
    <div className="flex">
      <Sidebar />
      {showInfo && <Info />}
      <div className="flex-grow p-4">
        <Routes>
          <Route path="/summary" element={<Summary />} />
          <Route path="/chart" element={<Chart />} />
        </Routes>
      </div>
    </div>
  );
};

const AppWrapper = () => (
  <Router>
    <App />
  </Router>
);

export default AppWrapper;