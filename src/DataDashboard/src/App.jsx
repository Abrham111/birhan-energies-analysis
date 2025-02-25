import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Summary from './components/Summary';
import Chart from './components/Chart';
import './App.css';

function App() {
  return (
    <Router>
      <div className="min-h-screen">
        <Header />
        <div className="flex">
          <Sidebar />
          <main className="flex-1 bg-gray-50 ml-48 mt-16">
            <Routes>
              <Route path="/" element={<Summary />} />
              <Route path="/chart" element={<Chart />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;