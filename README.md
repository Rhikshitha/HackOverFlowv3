# VoyageShare - Travel as one, Save as all

## Description

Simplifying daily commutes,VoyageShare is a dynamic carpooling and ride-sharing platform that seamlessly links users with similar travel routes, fostering cost-effective and secure travel while promoting a sustainable and collaborative community
## Table of Contents

- [VoyageShare](#voyageshare)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
  - [Configuration](#configuration)

## Features

- 
- 
- 
- 

## Tech Stack

- **Django**: Used for backend server 
- **SQLite**: A relational database for storing subscription and payment data.
- **ClickHouse**: A columnar database for efficient and scalable data analysis.


## Installation

To get started with this project, follow these steps

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   ```

2. **Install Python Dependencies**:

   Navigate to the project directory and set up your Python environment by installing the required packages. It's recommended to use a virtual environment.

   ```bash
   cd <project-directory>
   pip install virtualenv # Install Virtualenv package
   virtualenv venv # Create a virtual environment

   source venv/bin/activate # Activate the virtual environment (Linux/macOS)
   # OR
   venv\Scripts\activate # Activate the virtual environment (Windows)

   pip install -r requirements.txt
   ```

3. **Configure the project** (see [Configuration](#configuration) below).

4. **Make Migrations and Migrate:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
5. **Start the Django server**:
   ```bash
   python manage.py runserver
   ```

## Configuration

1. Set the following environment varables in developement:
   Note the following values are dummy values and use the actual values to configure
   ```bash
    

   ```
