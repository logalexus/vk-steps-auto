# Auto VK Steps

## Description

This project is intended to automatically generate steps and distance for the VK Run app.

## How it works

The code does the following:
1. Generate random steps and distance
2. Get current date in YYYY-MM-DD format
3. Build request to VK API with these parameters and access token
4. Send request and get response
5. Pause for 1 day before next request
6. This allows automatically submitting stats to VK Run app every day.

## Usage
To use this you need:

- [Obtain](https://vkhost.github.io/) VK API access token and set it in **ACCESS_TOKEN** variable 
- Configure range for random steps and distance values
- Set wait time between requests in **WAIT_TIME** (currently 1 day)

You can just run the script in Python
````
python main.py
````
But it is better to set up automatic generation of steps, for this you need Docker

In the directory with the docker-compose execute command
````
docker-compose up
````

## License

MIT License



