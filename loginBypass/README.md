# SQL Injection Login Bypass Script

This script demonstrates an SQL injection attack on a vulnerable web application in PortSwigger. It uses Python's `requests` library to handle HTTP requests and `BeautifulSoup` for HTML parsing.

## Features

- Obtains and utilizes CSRF tokens for the login form.
- Executes SQL injection to gain administrator access.
- Displays the payload and results of the injection attempt.

## Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup4` library

You can install the required libraries using:
```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script.
2. Run the script with Python.
3. Enter the URL of the lab login page when prompted.

## Example Run

1. Run the script:

```bash
python sql_injection_script.py
```

2. Enter your lab login URL:
```bash
Enter your lab login URL: https://0af4008404596280802ae92400d700c9.web-security-academy.net/login
```

3. The script will obtain the CSRF token, display it for verification, and execute the SQL injection payload.

4. It will display the used payload and the result of the injection attempt.

## Disclaimer

This script is for educational purposes only. Unauthorized use of this script on any web application without permission is illegal and unethical. Always ensure you have explicit permission before testing any web application for vulnerabilities.

## License
This project is licensed under the MIT License - see the LICENSE file for details.