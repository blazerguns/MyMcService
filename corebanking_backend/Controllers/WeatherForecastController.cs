using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace TodoApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WeatherForecastController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ILogger<WeatherForecastController> _logger;

        public WeatherForecastController(ILogger<WeatherForecastController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<WeatherForecast> Get([FromQuery]string[] rid)
        {
            var rng = new Random();
            List<WeatherForecast> selectn = new List<WeatherForecast>();
            foreach (string s in rid)
            {
                if (s.Contains(",")) {
                    string[] ls = s.Split(',');
                    foreach (string v in ls) {
                        selectn.Add(new WeatherForecast {
                            CustomerId = Int32.Parse(v),
                            CustomerValue = rng.Next(-20, 55),
                            Summary = "No value found"
                        });
                    }
                } else {
                    selectn.Add(new WeatherForecast {
                        CustomerId = Int32.Parse(s),
                        CustomerValue = rng.Next(-20, 55),
                        Summary = "No value found"
                    });
                }
            }
            return selectn.ToArray();
        }
    }
}
