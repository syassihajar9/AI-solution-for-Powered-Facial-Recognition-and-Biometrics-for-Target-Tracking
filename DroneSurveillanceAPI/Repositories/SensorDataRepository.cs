using DroneSurveillanceAPI.Models;
using MongoDB.Driver;

namespace DroneSurveillanceAPI.Repositories;

public class SensorDataRepository(DataContext.DataContext context) : ISensorDataRepository
{
    public async Task AddSensorDataAsync(SensorData data)
    {
        await context.SensorData.InsertOneAsync(data);
    }

    public async Task<IEnumerable<SensorData>> GetSensorDataAsync()
    {
        return await context.SensorData.Find(_ => true).ToListAsync();
    }
}