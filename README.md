# Labatt Data Pipeline

## Overview

This repository contains a data pipeline project designed to analyze alcohol consumption per country. The pipeline retrieves, cleans, and stores data in a Snowflake data warehouse, enabling further analysis and visualization using Tableau.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hamzah023/LabattDataPipeline.git
   cd LabattDataPipeline
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows
Install required packages:

bash
Copy code
pip install -r requirements.txt
Create a .env file for your environment variables. Ensure to add .env to your .gitignore to prevent it from being pushed to the repository.

Usage
Run the main script:

bash
Copy code
python src/main.py
Follow the prompts to download, inspect, clean, and upload the dataset to Snowflake.

Data Sources
The dataset represents average beer consumption per person, sourced from various aggregators.

Features
Downloading and cleaning the dataset
Uploading cleaned data to Snowflake
Visualizing data using Tableau
Contributing
Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.






