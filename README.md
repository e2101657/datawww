# Weather Data Lakehouse Pipeline

This project implements an end-to-end data pipeline using a modern lakehouse architecture. The pipeline processes real-time API data and historical data. The system supports both batch and streaming ingestion, and simple machine learning predictions.

## Architecture

The pipeline follows the Medallion Architecture.

Bronze Layer – raw ingested data from API and historical CSV
Silver Layer – cleaned and standardized data
Gold Layer – aggregated data

## Data Sources

## Real-time Data
Source: WeatherAPI
Data is fetched using an API key
Includes: temperature, humidity, wind speed, timestamp
City used: Vaasa

## Historical Data
Data includes daily temperature and past weather data for Vaasa
Source: Open-Meteo API

## Data Ingestion

## Batch Ingestion
Historical data is loaded from CSV files
Script: ingestion/batch.py
Output stored in: data/bronze/

## Real-time Ingestion
Data is fetched from WeatherAPI
Script: ingestion/stream.py

## Data Processing

## Silver Layer
Merges historical and real-time data
Output: data/silver/clean_weather.csv

## Gold Layer
Aggregates data such as average temperature
Output: data/gold/avg_temp.csv

## Machine Learning

A simple machine learning model is implemented to predict temperature trends.

Model: Linear Regression
Input: cleaned weather data
Output: predicted temperature values
Script: ml/model.py

## Snowflake Integration

Processed data from the Silver layer was uploaded to Snowflake.

Database: WEATHER_DB
Schema: PUBLIC
Table: WEATHER_DATA

Example query:
SELECT * FROM WEATHER_DB.PUBLIC.WEATHER_DATA;

<img width="1270" height="427" alt="image" src="https://github.com/user-attachments/assets/0975bd9b-92d0-4756-b2be-ee0353c3bda2" />



## How to run

Run batch ingestion:
python ingestion/batch_api.py

Run real-time ingestion:
python ingestion/stream_api.py

Run processing:
python processing/etl.py
python processing/gold.py

Run machine learning model:
python ml/model.py

## Features Implemented

Batch data ingestion using CSV
Real-time data ingestion using API
ETL pipeline for cleaning and transformation
Medallion architecture with Bronze Silver Gold layers
Simple machine learning model
Snowflake integration

## Conclusion

This project demonstrates a scalable data engineering solution using lakehouse architecture. It integrates multiple data sources, processes them, and enables both analytical and predictive use cases.
