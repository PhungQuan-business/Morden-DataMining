import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [predictions, setPredictions] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://api.example.com/predict', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    setPredictions(data);
    setIsLoading(false);
  };

  return (
    <div className="container">
      <h1>Leaf Disease Prediction</h1>
      <form onSubmit={handleSubmit} className="upload-form">
        <input type="file" onChange={handleFileChange} />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Predicting...' : 'Predict Disease'}
        </button>
      </form>
      {isLoading && <p>Loading...</p>}
      {!isLoading && predictions.length > 0 && (
        <div className="predictions">
          <h2>Predictions:</h2>
          {predictions.map((prediction) => (
            <div key={prediction.class} className="prediction">
              <p>
                Class: {prediction.class}, Confidence: {prediction.confidence}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;