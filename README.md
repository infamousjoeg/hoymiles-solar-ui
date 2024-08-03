# Hoymiles Solar UI <!-- omit from toc -->

![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Flask web application to visualize solar panel data using a dashboard. This app fetches data from the Hoymiles API and displays it in an interactive dashboard.

## Table of Contents <!-- omit from toc -->

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [Security](#security)
  - [Secret Key](#secret-key)
  - [Other Considerations](#other-considerations)
- [License](#license)

## Description

The Hoymiles Solar UI is a web application built with Flask to display real-time and historical data from solar panels. It fetches data from the Hoymiles API and provides various dashboards to visualize the data, including:

- Main page displaying current solar power data
- Plant details page
- Device list page with details for each device

## Features

- Fetch and display real-time solar data
- View detailed plant information
- List and view details for individual devices (microinverters)
- Mock tests for testing the app without accessing the live API
- Login and Logout functionality
- Dark mode toggle for better user experience

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/hoymiles-solar-ui.git
    cd hoymiles-solar-ui
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root and add the following variables:

    ```env
    SECRET_KEY=your_secret_key
    ```

5. **Run the Flask application:**

    ```bash
    python run.py
    ```

    The application will be accessible at `http://localhost:8000`.

## Usage

1. **Navigate to the Login Page:** Open your browser and go to `http://localhost:8000/login`.
2. **Enter Credentials:** Provide your username, password, and plant ID to log in.
3. **Dashboard:** After logging in, you will be redirected to the dashboard displaying the solar data.
4. **Logout:** Use the "Logout" button in the navigation bar to log out and clear the session.
5. **Dark Mode:** Use the toggle switch in the navigation bar to enable or disable dark mode.

- **Main Page:** Displays the current solar power data.
- **Plant Details:** Navigate to `/plant` to view detailed information about the plant.
- **Device List:** Navigate to `/devices` to view a list of all devices (microinverters). Click on a device to view its details.

## Testing

Mock tests are provided to test the application without accessing the live API.

1. **Run the tests:**

    ```bash
    python -m unittest discover -s tests
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## Security

### Secret Key

- **Purpose**: The secret key is used by Flask to encrypt session cookies and other security-related operations.
- **Configuration**: Set the `SECRET_KEY` environment variable in the `.env` file. Use a strong, random value for this key.
- **Example**: You can generate a secret key using Python:

    ```python
    import os
    os.urandom(24)
    ```

- **.env File**: Ensure that your `.env` file is not tracked by version control by including it in your `.gitignore`.

### Other Considerations

- **Environment Variables**: Do not hardcode sensitive information. Always use environment variables.
- **HTTPS**: Use HTTPS to encrypt data in transit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
