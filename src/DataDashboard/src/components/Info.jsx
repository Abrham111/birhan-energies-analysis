import React from 'react';

const Info = () => {
  return (
    <div className="bg-white shadow-md rounded-lg p-6 w-full mx-auto mt-6 h-screen">
      <h1 className="text-3xl font-bold mb-4 text-center">10 Academy: Artificial Intelligence Mastery</h1>
      <h2 className="text-xl font-semibold mb-2 text-center">Week 10 Challenge</h2>
      <p className="text-gray-700 mb-4 text-center">Date: 25 Feb 2025</p>
      <h3 className="text-2xl font-semibold mb-4">Change Point Analysis and Statistical Modelling of Time Series Data</h3>
      <p className="text-gray-700 mb-4">
        The main goal of this analysis is to study how important events affect Brent oil prices. This focuses on finding out how changes in oil prices are linked to big events like political decisions, conflicts in oil-producing regions, global economic sanctions, and changes in Organization of the Petroleum Exporting Countries (OPEC) policies. The aim is to provide clear insights that can help investors, analysts, and policymakers understand and react to these price changes better.
      </p>
      <h3 className="text-2xl font-semibold mb-4">Business Objective</h3>
      <p className="text-gray-700 mb-4">
        As a data scientist at Birhan Energies, a leading consultancy firm specializing in providing data-driven insights and strategic advice to stakeholders in the energy sector, the task is analyzing how big political and economic events affect Brent oil prices. Understand how political decisions, conflicts in oil-producing areas, international sanctions, and OPEC policy changes affect the market.
      </p>
      <h3 className="text-2xl font-semibold mb-4">Data</h3>
      <p className="text-gray-700 mb-4">
        The data set contains historical Brent oil prices. It includes daily prices from May 20, 1987, to September 30, 2022.
      </p>
    </div>
  );
};

export default Info;