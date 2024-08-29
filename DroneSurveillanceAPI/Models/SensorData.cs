using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace DroneSurveillanceAPI.Models;

public class SensorData
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }
    public string SensorType { get; set; }
    public string Value { get; set; }
    public DateTime Timestamp { get; set; }
}