// src/components/FaceRecognitionResults.tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface FaceRecognitionResult {
    id: string;
    name: string;
    confidence: number;
}

const FaceRecognitionResults: React.FC = () => {
    const [results, setResults] = useState<FaceRecognitionResult[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    const apiUrl = 'http://localhost:5012/api/facerecognition'; // Ihre API-URL

    useEffect(() => {
        const fetchResults = async () => {
            try {
                const response = await axios.get<FaceRecognitionResult[]>(apiUrl);
                setResults(response.data);
            } catch (err) {
                setError('Fehler beim Abrufen der Gesichtserkennungsergebnisse');
            } finally {
                setLoading(false);
            }
        };

        fetchResults();
    }, []);

    if (loading) return <p>Lade Gesichtserkennungsergebnisse...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div>
            <h1>Gesichtserkennung Ergebnisse</h1>
            <ul>
                {results.map((result) => (
                    <li key={result.id}>
                        Name: {result.name}, Vertrauen: {result.confidence.toFixed(2)}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FaceRecognitionResults;
