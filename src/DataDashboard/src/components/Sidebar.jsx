import React from 'react';
import { useState } from "react";
import { FiBarChart2, FiDollarSign, FiMenu } from "react-icons/fi";
import { FaHome } from "react-icons/fa";
import { Link } from 'react-router-dom';

const Sidebar = ({ setActiveSection }) => {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <div className={`bg-gray-900 text-white h-screen p-4 transition-all ${isOpen ? "w-64" : "w-16"}`}>
      <button onClick={() => setIsOpen(!isOpen)} className="mb-4 text-xl">
        <FiMenu />
      </button>
      <ul>
      <li className="flex items-center space-x-2 p-3 cursor-pointer hover:bg-gray-700 rounded-lg">
          <Link to="/" className="flex items-center space-x-2" onClick={() => setActiveSection("home")}>
          <FaHome /> {isOpen && <span>Home</span>}
          </Link>
        </li>
        <li className="flex items-center space-x-2 p-3 cursor-pointer hover:bg-gray-700 rounded-lg">
          <Link to="/summary" className="flex items-center space-x-2" onClick={() => setActiveSection("summary")}>
            <FiDollarSign /> {isOpen && <span>Summary</span>}
          </Link>
        </li>
        <li className="flex items-center space-x-2 p-3 cursor-pointer hover:bg-gray-700 rounded-lg">
          <Link to="/chart" className="flex items-center space-x-2" onClick={() => setActiveSection("chart")}>
            <FiBarChart2 /> {isOpen && <span>Price Chart</span>}
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;