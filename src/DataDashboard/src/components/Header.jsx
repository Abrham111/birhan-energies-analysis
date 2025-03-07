import React from "react";
import { FaMoon, FaSun } from "react-icons/fa";

export default function Header({ onToggle, isDarkMode }) {
  return (
    <header className="dark:bg-gray-900 text-white p-4 flex justify-between">
      <h1 className="text-2xl text-green-600 font-bold">Brent Oil Price Dashboard</h1>
      <button
        onClick={onToggle}
        className="bg-gray-800 dark:bg-yellow-500 px-4 py-2 rounded"
      >
        {isDarkMode ? <FaSun /> : <FaMoon />}
      </button>
    </header>
  );
}
