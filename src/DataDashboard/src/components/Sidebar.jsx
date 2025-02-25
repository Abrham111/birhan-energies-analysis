import { useState } from "react";
import { FiBarChart2, FiDollarSign, FiMenu } from "react-icons/fi";

const Sidebar = ({ setActiveSection }) => {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <div className={`bg-gray-900 text-white h-screen p-4 transition-all ${isOpen ? "w-64" : "w-16"}`}>
      <button onClick={() => setIsOpen(!isOpen)} className="mb-4 text-xl">
        <FiMenu />
      </button>
      <ul>
        <li className="flex items-center space-x-2 p-3 cursor-pointer hover:bg-gray-700 rounded-lg" onClick={() => setActiveSection("summary")}>
          <FiDollarSign /> {isOpen && <span>Summary</span>}
        </li>
        <li className="flex items-center space-x-2 p-3 cursor-pointer hover:bg-gray-700 rounded-lg" onClick={() => setActiveSection("chart")}>
          <FiBarChart2 /> {isOpen && <span>Price Chart</span>}
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
