using DroneSurveillanceAPI.Models;

namespace DroneSurveillanceAPI.Repositories;

public interface ISensorDataRepository
{
    Task AddSensorDataAsync(SensorData data);
    Task<IEnumerable<SensorData>> GetSensorDataAsync();
}