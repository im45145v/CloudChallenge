import boto3
import json
import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()

Config={
    "region":"ap-south-1",
    "bucket_name":"sports-analytics-data-lake",
    "glue_database_name":"glue_nba_data_lake",
    "athena_output_location":f"s3://{Config["bucket_name"]}/athena-results/",
    "api_key":os.getenv("SPORTS_DATA_API_KEY"),
    "nba_endpoint":os.getenv("NBA_ENDPOINT")
}
s3_client = boto3.client("s3", region_name=region)
glue_client = boto3.client("glue", region_name=region)
athena_client = boto3.client("athena", region_name=region)

def make_s3_bucket():
    try:
        if region=="ap-south-1":
            s3_client.create_bucket(Bucket=Config["bucket_name"])
        else:
            s3_client.create_bucket(Bucket=Config["bucket_name"],CreateBucketConfiguration={"LocationConstraint": Config["region"])
        print(f"{Config['bucket_name']} bucket has been suceesfully created")
    except Exception as e:
        print(f"{e}")

def make_glue_db():
    try:
        glue_client.create_database(
            DatabaseInput={
                "Name":Config["glue_database_name"],
                "Description":"Glue database for NBA sports analytics.",
            }
        )
        print(f"Glue database '{glue_database_name}' created successfully.")
    except Exception as e:
        print(f"{e}")

def get_nba_data():
    try:
        headers = {"Ocp-Apim-Subscription-Key": api_key}
        response = requests.get(nba_endpoint, headers=headers)
        response.raise_for_status() 
        print("Fetched NBA data successfully.")
        return response.json()
    except Exception as e:
        print(f"Error fetching NBA data: {e}")
        return []

def push_data_into_bucket():
    try:
        file_key="raw-data/nba_player_data.json"
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=json.dumps(data)
        )
        print(f"Uploaded data to S3: {file_key}")
    except Exception as e:
        print(f"{e}")

def make_glue_table():
    try:
        glue_client.create_table(
            DatabaseName=Config["glue_database_name"],
            TableInput={
                "Name": "nba_players",
                "StorageDescriptor": {
                    "Columns": [
                        {"Name": "PlayerID", "Type": "int"},
                        {"Name": "FirstName", "Type": "string"},
                        {"Name": "LastName", "Type": "string"},
                        {"Name": "Team", "Type": "string"},
                        {"Name": "Position", "Type": "string"},
                    ],
                    "Location": f"s3://{Config["bucket_name"]}/raw-data/",
                    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
                    "SerdeInfo": {
                        "SerializationLibrary": "org.openx.data.jsonserde.JsonSerDe"
                    },
                },
                "TableType": "EXTERNAL_TABLE",
            },
        )
        print(f"Glue table 'nba_players' created successfully.")
    except Exception as e:
        print(f"{e}")

def configure_athena():
    try:
        athena_client.start_query_execution(
            QueryString="CREATE DATABASE IF NOT EXISTS nba_analytics",
            QueryExecutionContext={"Database": Config["glue_database_name"]},
            ResultConfiguration={"OutputLocation": Config["athena_output_location"]},
        )
        print("Athena output location configured successfully.")
    except Exception as e:
        print(f"{e}")

def main():
    print("Setting up data lake for NBA sports analytics...")
    make_s3_bucket()
    time.sleep(5)
    make_glue_db()
    nba_data=get_nba_data()
    if nba_data:
        push_data_into_bucket(nba_data)
    make_glue_table()
    configure_athena()
    print("Data lake setup complete.")

if __name__=="__main__":
    main()