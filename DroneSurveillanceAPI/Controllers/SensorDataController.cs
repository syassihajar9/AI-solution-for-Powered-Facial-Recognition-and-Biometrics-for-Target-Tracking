using DroneSurveillanceAPI.Models;
using DroneSurveillanceAPI.Repositories;
using Microsoft.AspNetCore.Mvc;

namespace DroneSurveillanceAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class SensorDataController(ISensorDataRepository repository, ILogger<SensorDataController> logger)
    : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> AddSensorData([FromBody] SensorData data)
    {
        try
        {
            await repository.AddSensorDataAsync(data);
            return Ok();
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "An error occurred while adding sensor data.");
            return StatusCode(500, "Internal server error.");
        }
    }

    [HttpGet]
    public async Task<IActionResult> GetSensorData()
    {
        try
        {
            var data = await repository.GetSensorDataAsync();
            if (!data.Any())
            {
                return NotFound("No sensor data found.");
            }
            return Ok(data);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "An error occurred while retrieving sensor data.");
            return StatusCode(500, "Internal server error.");
        }
    }
}