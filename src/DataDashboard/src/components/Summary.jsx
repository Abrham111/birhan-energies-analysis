import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Summary() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/summary')
      .then(response => setSummary(response.data));
  }, []);

  if (!summary) return <div>Loading...</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-6">
      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <h3 className="text-gray-500 text-sm font-medium">Latest Price</h3>
        <p className="text-3xl font-bold text-gray-900 mt-2">
          {summary.latest_price.toFixed(2)}
        </p>
      </div>
      {/* Repeat similar blocks for max, min, avg */}
      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <h3 className="text-gray-500 text-sm font-medium">Maximum Price</h3>
        <p className="text-3xl font-bold text-gray-900 mt-2">
          {summary.max_price.toFixed(2)}
        </p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <h3 className="text-gray-500 text-sm font-medium">Minimum Price</h3>
        <p className="text-3xl font-bold text-gray-900 mt-2">
          {summary.min_price.toFixed(2)}
        </p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <h3 className="text-gray-500 text-sm font-medium">Average Price</h3>
        <p className="text-3xl font-bold text-gray-900 mt-2">
          {summary.avg_price.toFixed(2)}
        </p>
      </div>
    </div>
  );
}