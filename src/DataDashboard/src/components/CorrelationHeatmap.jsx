import React, { useEffect, useState } from "react";
import colormap from "colormap";

const CorrelationHeatmap = () => {
  const [correlationMatrix, setCorrelationMatrix] = useState([]);
  const [commodities, setCommodities] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/correlation")
      .then((res) => res.json())
      .then((data) => {
        console.log("Fetched data:", data);

        const keys = Object.keys(data);
        setCommodities(keys);

        // Convert JSON object into a 2D array format for rendering
        const matrix = keys.map((row) =>
          keys.map((col) => ({
            row,
            col,
            value: data[row][col], // Extract correlation value
          }))
        );

        setCorrelationMatrix(matrix);
      })
      .catch((error) => console.error("Error fetching correlation data:", error));
  }, []);

  // Generate color scale for heatmap
  const colors = colormap({
    colormap: "jet",
    nshades: 100,
    format: "hex",
  });

  const getColor = (value) => {
    if (value === undefined) return "#fff"; // Handle missing values
    const index = Math.floor(((value + 1) / 2) * (colors.length - 1)); // Normalize (-1 to 1) to (0 to 100)
    return colors[index];
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6 w-full mx-auto">
      <h2 className="text-2xl font-semibold mb-4">Commodity Correlation Heatmap</h2>
      <div className="overflow-x-auto">
        <table className="border-collapse border border-gray-300 w-full">
          <thead>
            <tr>
              <th className="border border-gray-300 px-4 py-2">Commodity</th>
              {commodities.map((col, index) => (
                <th key={index} className="border border-gray-300 px-4 py-2">
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {commodities.map((row, rowIndex) => (
              <tr key={rowIndex}>
                <td className="border border-gray-300 px-4 py-2 font-semibold">{row}</td>
                {commodities.map((col, colIndex) => {
                  const value = correlationMatrix[rowIndex]?.[colIndex]?.value; // Access correct value
                  return (
                    <td
                      key={colIndex}
                      className="border border-gray-300 px-4 py-2 text-center"
                      style={{
                        backgroundColor: value !== undefined ? getColor(value) : "#fff",
                        color: Math.abs(value) > 0.6 ? "#fff" : "#000",
                      }}
                    >
                      {value !== undefined ? value.toFixed(3) : "-"}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CorrelationHeatmap;