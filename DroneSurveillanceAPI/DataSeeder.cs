using DroneSurveillanceAPI.Models;

namespace DroneSurveillanceAPI;

using MongoDB.Driver;
using System;

public class DataSeeder(IMongoDatabase database)
{
    private readonly IMongoCollection<SensorData> _sensorDataCollection = database.GetCollection<SensorData>("SensorData");

    public void Seed()
    {
        var sensorData = new[]
        {
            new SensorData
            {
                SensorType = "Camera",
                Value = "Person detected",
                Timestamp = DateTime.Parse("2023-08-01T12:34:56Z")
            },
            new SensorData
            {
                SensorType = "Infrared",
                Value = "Temperature: 36.6",
                Timestamp = DateTime.Parse("2023-08-01T12:35:00Z")
            },
            new SensorData
            {
                SensorType = "GPS",
                Value = "Latitude: 40.7128, Longitude: -74.0060",
                Timestamp = DateTime.Parse("2023-08-01T12:35:10Z")
            },
            new SensorData
            {
                SensorType = "Camera",
                Value = "Person not detected",
                Timestamp = DateTime.Parse("2023-08-01T12:35:20Z")
            },
            new SensorData
            {
                SensorType = "Infrared",
                Value = "Temperature: 36.8",
                Timestamp = DateTime.Parse("2023-08-01T12:35:30Z")
            },
            new SensorData
            {
                SensorType = "GPS",
                Value = "Latitude: 40.7138, Longitude: -74.0065",
                Timestamp = DateTime.Parse("2023-08-01T12:35:40Z")
            }
        };

        _sensorDataCollection.InsertMany(sensorData);
    }
}

