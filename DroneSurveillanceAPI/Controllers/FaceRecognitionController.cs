using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace DroneSurveillanceAPI.Controllers;

[ApiController]
    [Route("api/[controller]")]
    public class FaceRecognitionController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public FaceRecognitionController(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri("http://localhost:8501"); // Ensure this is correct
        }

        [HttpPost("predict")]
        public async Task<IActionResult> Predict([FromBody] ImageData imageData)
        {
            // Validate input
            if (imageData == null || imageData.Image == null)
            {
                return BadRequest("Image data is missing.");
            }

            // Create the payload for TensorFlow Serving
            var requestPayload = new
            {
                instances = new[]
                {
                    new
                    {
                        inputs = imageData.Image // Ensure this key matches the model's expected input name
                    }
                }
            };

            var jsonContent = new StringContent(JsonConvert.SerializeObject(requestPayload), Encoding.UTF8, "application/json");

            // Send the request to TensorFlow Serving
            var response = await _httpClient.PostAsync("/v1/models/face_recognition_model:predict", jsonContent);

            // Check the response status and return appropriate results
            if (!response.IsSuccessStatusCode)
            {
                var errorContent = await response.Content.ReadAsStringAsync();
                return StatusCode((int)response.StatusCode, errorContent);
            }

            var result = await response.Content.ReadAsStringAsync();
            return Ok(result);
        }

    }

    public class ImageData
    {
        public float[][][][] Image { get; set; } // Ensure this matches the input tensor shape expected by the model
    }
