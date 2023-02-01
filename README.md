
# Aggregated Access Log Stats

## Introduction

This is a flask application that parses access log files and provides aggregated statistics about the log data.

## Running the Application

### Option 1: Running with Docker
**Prerequisites**: Docker

1.  Clone the repository and navigate to the project directory.
2.  Build the Docker image using the following command 
`docker build -t access-log-stats .`
3.  Run the Docker container using the command: 
```docker run -p 5001:5000 -v <host file path>:/app/access.log access-log-stats```
**Please Note**: Make sure to replace `<host file path>` with the path of Access Log file.
4.  Access the aggregated logs stats at `http://localhost:5001/stats`.

### Option 2: Running Locally
**Prerequisites**: Python 3.9 or above, Flask

1.  Clone the repository and navigate to the project directory.
2.  Set the `LOG_FILE_PATH` environment variable with the path to your log access file:
`export LOG_FILE_PATH=<host file path>`
3.  Start the flask application using the command `flask run`.
4. Access the aggregated logs stats at `http://localhost:5000/stats`.

## Parsing Log Access Files

The function `parse_log_file` in `app.py` takes the access log file path as an input and returns the following statistics:

-   Number of unique IP addresses
-   Number of requests per IP address
-   Distribution of status codes in the log access file
-   Top 5 referrers

## API Endpoint

The API endpoint for the aggregated log access stats is `/stats` and it can be accessed via a GET request. The API returns the parsed log access data in JSON format.
