using DroneSurveillanceAPI.Models;
using Microsoft.Extensions.Options;
using MongoDB.Driver;

namespace DroneSurveillanceAPI.DataContext;

public class DataContext
{
    private readonly IMongoDatabase _database;

    public DataContext(IOptions<MongoSettings> settings)
    {
        var client = new MongoClient(settings.Value.ConnectionString);
        _database = client.GetDatabase(settings.Value.Database);
    }

    public IMongoCollection<SensorData> SensorData => _database.GetCollection<SensorData>("SensorData");
}