using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var tokenEndpoint = "https://api.prd.azure.us.allvuecloud.com/fund-accounting/v1/oauth2/token";
        var clientId = "your_client_id";
        var clientSecret = "your_client_secret";

        using (HttpClient client = new HttpClient())
        {
            var content = new FormUrlEncodedContent(new
            {
                grant_type = "client_credentials",
                client_id = clientId,
                client_secret = clientSecret
            });

            var response = await client.PostAsync(tokenEndpoint, content);
            var responseContent = await response.Content.ReadAsStringAsync();

            // Deserialize the response content to extract the access token
            // (Use a JSON parsing library such as Newtonsoft.Json)
            if (response.IsSuccessStatusCode)
            {
                JObject tokenData = JObject.Parse(responseContent);
                string accessToken = tokenData["access_token"].ToString();

                Console.WriteLine($"Access Token: {accessToken}");
            }
            else
            {
                Console.WriteLine($"Token request failed: {responseContent}");
            }
        }
    }
}
