import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts';

const Chart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/data")
      .then((res) => res.json())
      .then((data) => {
        const formattedData = data.dates.map((date, index) => ({
          date,
          price: data.prices[index],
        }));
        setData(formattedData);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="bg-white shadow-md rounded-lg p-6 w-full mx-auto">
      <h2 className="text-2xl font-semibold mb-4">Oil Price Chart</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data}>
          <XAxis dataKey="date" tick={{ fontSize: 12 }} />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#1E40AF" strokeWidth={2} />
        </LineChart>

        <h2 className="text-2xl font-semibold mt-8 mb-4">Price Distribution Chart</h2>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={data}>
            <XAxis dataKey="date" tick={{ fontSize: 12 }} />
            <YAxis />
            <Tooltip />
            <Bar dataKey="price" fill="#1E40AF" />
          </BarChart>
        </ResponsiveContainer>

      </ResponsiveContainer>
    </div>
  );
};

export default Chart;
