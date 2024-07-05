# My Tkinter GUI Project

## Project Overview

This project is a desktop application built using Tkinter in Python. It includes various functionalities such as recording registration details, generating random advice, and fetching location details. The project is structured to ensure modularity and ease of understanding.

## Project Structure

- **My_App1.py**: The main logic file of the Tkinter-based GUI application.
- **api.py**: This file includes two APIs:
  - A random advice generator.
  - A location details fetcher, which could also fetch weather details, but for simplicity, we are filtering out the weather details.
- **database.py**: Handles all database interactions. It directly interacts with the `db.json` file.
- **db.json**: Acts as the database for the application, storing all necessary data.
- **resources.properties**: Includes the icon of the app and acts as resource storage for the application.

## Features

### Tkinter Desktop Application

- **Main Logic (My_App1.py)**: The Tkinter-based GUI application allows users to interact with the system.
- **Functionalities**:
  - **Registration Details**: Users can record and save their registration details.
  - **Random Advice Generator**: Displays random advice fetched from an external API.
  - **Location Details Fetcher**: Fetches and displays location details based on user-provided latitude and longitude.

### APIs

- **api.py**:
  - **Random Advice Generator**: Fetches random advice from an external API.
  - **Location Details Fetcher**: Retrieves location details such as city, principal subdivision, and country name based on latitude and longitude.

### Database

- **database.py**: Manages the interaction with `db.json`.
  - **Functions**:
    - `load_database()`: Loads the database from the JSON file.
    - `save_database(data)`: Saves the database to the JSON file.
    - `get_all_entries()`: Retrieves all stored entries.
    - `add_entry(entry)`: Adds a new entry to the database.
    - `get_entry(entry_id)`: Retrieves a specific entry based on its ID.

## Installation and Setup

### Prerequisites

- Python 3.x
- Requests library (for making API calls)

### Installation

 **Install Dependencies**:
   ```bash
   pip install requests
   ```

### Running the Application

 **Run the Tkinter Desktop Application**:
   ```bash
   python My_App1.py
   ```

## Usage

- **Registration**: Fill in the registration details and submit.
- **Random Advice**: Click the button to receive random advice.
- **Location Details**: Enter latitude and longitude to get location details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Thanks to the developers of Tkinter for their amazing library.
- Special thanks to the providers of the external APIs used in this project.
