

# Sales and Marketing Analysis

## Overview

This project involves generating and analyzing sales and marketing data. The data includes randomly generated information about products, customers, sales, and regions. The data is first generated using Python, transferred to a MySQL database, and then analyzed using Jupyter Notebook. This analysis aims to provide insights into sales patterns and customer behavior.

## Project Structure

- **generate_data.py**: Python script for generating random data for products, customers, sales, and regions.
- **populate_database.py**: Python script for transferring the generated data to the MySQL database.
- **Ecommerce.ipynb**: Jupyter Notebook containing the analysis and visualizations of the data.
- **shoppy.sql**: SQL script for setting up the MySQL database and tables (named `shoppy_db`).
- **requirements.txt**: List of Python dependencies required for the project.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Yvokim/Sales-Marketing-Analysis.git
    cd Sales-Marketing-Analysis
    ```

2. **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MySQL:**

    - Create a new MySQL database named `shoppy_db` and a user as per your configuration.
    - Run the `shoppy.sql` script to create the necessary tables:

    ```bash
    mysql -u your_username -p shoppy_db < shoppy.sql
    ```

5. **Generate Data:**

    Run the `generate_data.py` script to populate the MySQL database with random data:

    ```bash
    python generate_data.py
    ```

6. **Run the Analysis:**

    Open `Ecommerce.ipynb` in Jupyter Notebook and execute the cells to perform the analysis.

## Usage

- Modify the `generate_data.py` script if you need to change the data generation parameters.
- Use the Jupyter Notebook to explore different aspects of the data and perform various analyses.
- The project can be extended with additional features or more detailed analysis as needed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the existing code style and include relevant tests.

## License

This project is licensed under the MIT License


