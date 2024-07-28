# Assignment Tasks

This repository contains a Python script that scrapes data from Speedtest Global Index for mobile and fixed broadband connections of all countries, displays the data, stores it in separate CSV files, and also stores the same data in two different tables in a MySQL database. Additionally, an `.sql` backup file is provided to restore the database tables.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [MySQL Database Backup](#mysql-database-backup)
- [Files](#files)

## Overview

The script performs the following tasks:
1. Scrapes data from [Speedtest Global Index](https://www.speedtest.net/global-index).
2. Displays the data for mobile and fixed broadband connections.
3. Stores the data in separate CSV files (`mobile_info.csv` and `broadband_info.csv`).
4. Stores the data in two different tables in a MySQL database.
5. Provides an `.sql` backup file to recreate the MySQL database tables with the scraped data.

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests
- MySQL Server
- MySQL Connector for Python
- Tabulate (for displaying data in a tabular format)

## Setup

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/TanishqSadanala/Assignment_Tasks.git
    cd Assignment_Tasks
    ```

2. **Install Python Packages:**

    ```sh
    pip install requests beautifulsoup4 mysql-connector-python tabulate
    ```

3. **Set Up MySQL Database:**

    - Create a new database in MySQL and set up the tables:

        ```sql
        CREATE DATABASE network_data;

        USE network_data;

        CREATE TABLE mobile_info (
            ranking INT PRIMARY KEY,
            Country VARCHAR(255),
            Speed_Mbps DECIMAL(10, 2)	
        );

        CREATE TABLE broadband_info (
            ranking INT PRIMARY KEY,
            Country VARCHAR(255),
            Speed_Mbps DECIMAL(10, 2)	
        );
        ```

    - Load the data from CSV files into the tables:

        ```sql
        LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/mobile_info.csv'
        INTO TABLE mobile_info
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (ranking, Country, Speed_Mbps);

        LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/broadband_info.csv'
        INTO TABLE broadband_info
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (ranking, Country, Speed_Mbps);
        ```

## Usage

1. **Run the Python Script:**

    ```sh
    Assignment_1.py
    ```

    This will scrape the data, display it, and store it in the specified CSV files and MySQL tables.

2. **Check the Output:**

    - The data will be displayed in the terminal.
    - CSV files (`mobile_info.csv` and `broadband_info.csv`) will be created in the repository directory.
    - The MySQL tables (`mobile_info` and `broadband_info`) will be populated with the scraped data.

## MySQL Database Backup

The `backup.sql` file is provided to restore the database tables with the scraped data. To restore the database, run the following command:

```sh
mysql -u username -p network_data < backup.sql
