// SensorDataDisplay.tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Definieren Sie den Typ für die Sensordaten
interface SensorData {
  Id: string;
  SensorType: string;
  Value: string;
  Timestamp: string;
}

const SensorDataDisplay: React.FC = () => {
  // Zustand für Sensordaten
  const [sensorData, setSensorData] = useState<SensorData[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // API-URL für die Sensordaten
  const apiUrl = 'http://localhost:5012/api/sensordata';

  // Funktion zum Abrufen der Sensordaten
  const fetchSensorData = async () => {
    try {
      const response = await axios.get<SensorData[]>(apiUrl);
      setSensorData(response.data);
    } catch (err) {
      setError('Fehler beim Abrufen der Sensordaten');
    } finally {
      setLoading(false);
    }
  };

  // Daten abrufen, wenn die Komponente gemountet wird
  useEffect(() => {
    fetchSensorData();
  }, []);

  // Fehlerbehandlung und Ladeanzeige
  if (loading) return <p>Lade Sensordaten...</p>;
  if (error) return <p>{error}</p>;

  // Komponenten-Rendering
  return (
    <div>
      <h1>Sensor Daten</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Sensor Typ</th>
            <th>Wert</th>
            <th>Zeitstempel</th>
          </tr>
        </thead>
        <tbody>
          {sensorData.map((data) => (
            <tr key={data.Id}>
              <td>{data.Id}</td>
              <td>{data.SensorType}</td>
              <td>{data.Value}</td>
              <td>{new Date(data.Timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SensorDataDisplay;
