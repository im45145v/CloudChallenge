# Weather Dashboard
```
Warm up to the month long DevOps Challenge
```
## Technologies
- Python
- AWS S3
## Objective
- Connect to S3 bucket via python and store json files in it
- Using basic API Get call to fetch Weather Details from Open Weather API
## Flow
### 1. API provider
- Create an account in openweather and create and API key
### 2. Project Structure
```
weather-dashboard/
├── src/
│   ├── __init__.py
│   └── weather_dashboard.py
├── .env
├── .gitignore
├── Dockerfile
└── README.md
```
### 3. GitIgnore
- Ignore files that are not part of code
- Ignore Environment Variables files
You can do this by adding their paths to `.gitignore` file
### 4. Environment file
- Create .env file in your project directory
```.env
OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=weather-dashboard-Uniqe
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_DEFAULT_REGION=your_aws_default_region
```
### 5. Code
You can find the code [here](src/weather_dashboard.py)
### 6. Docker Build File
Optional Setup done by [Rene Mayhrem](https://github.com/Rene-Mayhrem)
```
FROM python:3.9-slim

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install AWS CLI
RUN apt-get update && apt-get install -y awscli

COPY .env .
COPY src/ ./src  

CMD ["python", "src/__init__.py"]
```
### How to run
#### Running python file
`Python weather_dashboard.py`
#### Building Docker image
`docker build -t weather-dashboard .`
#### Running Docker image
`docker run weather-dashboard --name aws-app`
## Resources
- [Docker Installation Guide](https://docs.docker.com/get-docker/): Follow this guide to install Docker on your machine.
- [OpenWeather API Documentation](https://openweathermap.org/api): Learn more about the OpenWeather API.
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html): Comprehensive guide to using AWS S3.
- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html): Guide to configuring the AWS CLI.
