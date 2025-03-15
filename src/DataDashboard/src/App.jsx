import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Info from './components/Info';
import Summary from './components/Summary';
import Chart from './components/Chart';
import CorrelationHeatmap from './components/CorrelationHeatmap';
import './App.css';

const App = () => {
  const location = useLocation();
  const [showInfo, setShowInfo] = useState(true);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (location.pathname === '/summary' || location.pathname === '/chart' || location.pathname === '/heatmap') {
      setShowInfo(false);
    } else {
      setShowInfo(true);
    }
  }, [location]);

  return (
    <div className={darkMode ? 'dark' : ''}>
      <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
        <Header onToggle={() => setDarkMode(!darkMode)} isDarkMode={darkMode} />
        <div className="flex">
          <Sidebar />
          {showInfo && <Info />}
          <div className="flex-grow p-4">
            <Routes>
              <Route path="/summary" element={<Summary />} />
              <Route path="/chart" element={<Chart />} />
              <Route path="/heatmap" element={<CorrelationHeatmap />} />
            </Routes>
          </div>
        </div>
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