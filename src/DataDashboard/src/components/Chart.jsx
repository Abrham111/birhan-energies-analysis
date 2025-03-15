import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, Legend } from 'recharts';

const Chart = () => {
  const [data, setData] = useState([]);

  const [prediction, setPrediction] = useState([]);

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

  useEffect(() => {
    fetch("http://localhost:5000/api/predictions")
      .then((res) => res.json())
      .then((fetchedData) => {
        // Convert string dates to Date objects for better formatting
        const refinedData = fetchedData.map((row) => ({
          ...row,
          Date: new Date(row.Date).toLocaleDateString(), // Format date
        }));
        setPrediction(refinedData);
      })
      .catch((err) => console.error("Error fetching predictions:", err));
  }, []);

  return (
    <div>
      <div className="bg-white shadow-md rounded-lg p-6 w-full mx-auto">
        <h2 className="text-2xl font-semibold mb-4">Oil Price Chart</h2>
        <ResponsiveContainer width="100%" height={400} margin={{ top: 20, right: 30, left: 20, bottom: 20 }}>
          <LineChart data={data}>
            <XAxis dataKey="date" tick={{ fontSize: 12 }} />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="price" stroke="#1E40AF" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="bg-white shadow-md rounded-lg p-6 w-full mx-auto">
        <h2 className="text-2xl font-semibold mt-8 mb-4">Price Distribution Chart</h2>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={data}>
            <XAxis dataKey="date" tick={{ fontSize: 12 }} />
            <YAxis />
            <Tooltip />
            <Bar dataKey="price" fill="#1E40AF" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="bg-white shadow-md rounded-lg p-6 w-full mx-auto">
        <h2 className="text-2xl font-semibold mb-4">Brent Oil Price Predictions and actual price using LSTM</h2>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={prediction}>
            <XAxis dataKey="Date" tick={{ fontSize: 12 }} angle={-30} textAnchor="end" />
            <YAxis domain={["auto", "auto"]} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="Actual_Price" stroke="#ff7300" strokeWidth={2} dot={false} name="Actual Price" />
            <Line type="monotone" dataKey="Predicted_Price" stroke="#387eff" strokeWidth={2} dot={false} name="Predicted Price" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default Chart;
