using Microsoft.AspNetCore.Mvc;
using System.Text;
using DroneSurveillanceAPI.Models;
using DroneSurveillanceAPI.Repositories;
using Newtonsoft.Json;

namespace DroneSurveillanceAPI.Controllers;

[ApiController]
    [Route("api/[controller]")]
    public class SimulationController : ControllerBase
    {
        private readonly ISensorDataRepository _repository;
        private readonly HttpClient _httpClient;

        public SimulationController(ISensorDataRepository repository, HttpClient httpClient)
        {
            _repository = repository;
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri("http://localhost:8501");
        }

        [HttpPost]
        public async Task<IActionResult> StartSimulation()
        {
            // Simulate data creation and insertion into the database
            await SimulateSensorData();
            await SimulateFacialRecognition();

            return Ok(new { message = "Simulation started successfully" });
        }

        private async Task SimulateSensorData()
        {
            // Simulate generating sensor data
            var random = new Random();

            for (int i = 0; i < 10; i++) // Simulating 10 sensor data entries
            {
                var sensorData = new SensorData
                {
                    SensorType = "Camera",
                    Value = random.Next(0, 2) == 0 ? "Person detected" : "No person detected",
                    Timestamp = DateTime.UtcNow.AddSeconds(-i * 10) // Generating timestamps in the past
                };

                await _repository.AddSensorDataAsync(sensorData);
            }
        }

        private async Task SimulateFacialRecognition()
        {
            for (int i = 0; i < 10; i++)
            {
                // Simulate image data
                var imageData = new
                {
                    inputs = GenerateRandomImage() // Adjust to the expected input name
                };

                var content = new StringContent(JsonConvert.SerializeObject(new
                {
                    instances = new[] { imageData } // Adjust to the expected input name
                }), Encoding.UTF8, "application/json");

                var response = await _httpClient.PostAsync("/v1/models/face_recognition_model:predict", content);
        
                if (!response.IsSuccessStatusCode)
                {
                    var errorResponse = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Model API Error: {errorResponse}");
                    throw new Exception($"Error from model: {errorResponse}");
                }

                var jsonResponse = await response.Content.ReadAsStringAsync();
                var result = JsonConvert.DeserializeObject<FacialRecognitionResult>(jsonResponse);

                // Save the prediction result to the database
                var sensorData = new SensorData
                {
                    SensorType = "FacialRecognition",
                    Value = $"Person detected: {result?.PredictedLabel}",
                    Timestamp = DateTime.UtcNow
                };

                await _repository.AddSensorDataAsync(sensorData);
            }
        }


        private float[][][] GenerateRandomImage()
        {
            // Simulate generating a random image as a 3D array (224x224 RGB image)
            var random = new Random();
            var image = new float[224][][];

            for (int i = 0; i < 224; i++)
            {
                image[i] = new float[224][];
                for (int j = 0; j < 224; j++)
                {
                    image[i][j] = new float[3];
                    for (int k = 0; k < 3; k++)
                    {
                        image[i][j][k] = (float)random.NextDouble();
                    }
                }
            }

            return image;
        }
    }