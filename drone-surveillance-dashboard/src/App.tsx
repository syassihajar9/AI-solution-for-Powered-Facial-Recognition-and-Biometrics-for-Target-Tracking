import React from 'react';
import SensorDataList from './components/SensorDataList';
import ControlPanel from './components/ControlPanel';
import FaceRecognitionResults from './components/FaceRecognitionResults';

const App: React.FC = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h1>Welcome to the Dashboard</h1>
            <ControlPanel />
            <SensorDataList />
            <FaceRecognitionResults />
        </div>
    );
};

export default App;
