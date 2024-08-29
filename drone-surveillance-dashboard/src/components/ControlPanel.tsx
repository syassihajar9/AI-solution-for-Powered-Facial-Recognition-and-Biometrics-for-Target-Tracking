import React, { useState } from 'react';
import axios from 'axios';

const ControlPanel: React.FC = () => {
    // Zustand für Fehler und Ladeanzeige
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    const startSimulation = async () => {
        setIsLoading(true);  // Ladeanzeige aktivieren
        setError(null);      // Fehler zurücksetzen

        try {
            await axios.post('http://localhost:5012/api/simulation/start');
            // Optional: Erfolgsnachricht anzeigen oder andere Aktionen
        } catch (err) {
            // Fehlerbehandlung
            if (axios.isAxiosError(err) && err.response) {
                setError(`Fehler: ${err.response.status} - ${err.response.statusText}`);
            } else {
                setError('Ein unbekannter Fehler ist aufgetreten.');
            }
        } finally {
            setIsLoading(false); // Ladeanzeige deaktivieren
        }
    };

    return (
        <div>
            <h1>Control Panel</h1>
            <button onClick={startSimulation} disabled={isLoading}>
                {isLoading ? 'Starte Simulation...' : 'Start Simulation'}
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default ControlPanel;
