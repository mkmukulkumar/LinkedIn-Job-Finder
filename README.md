# LinkedIn Job Finder

## Introduction
This Python script automates various LinkedIn tasks using Selenium, such as logging in, saving cookies for future sessions, fetching companies from the user's profile, and retrieving recommended and recent jobs for each company. The script is designed to assist in job hunting and keeping track of companies of interest on LinkedIn.

## Prerequisites
- Python 3.x
- Selenium library
- Chrome WebDriver

## Installation
1. Install Python: [Python Installation Guide](https://www.python.org/downloads/)
2. Install the Selenium library:
   ```bash
   pip install selenium
   ```
3. Download Chrome WebDriver: ChromeDriver Downloads
4. Update the webdriverpath variable in the script with the path to your Chrome WebDriver executable.
5. Create a credentials.py file with your LinkedIn username and password:
```bash
  secrets = {
      'username': 'your_username',
      'password': 'your_password'
  }
```
## Usage
1. Run the script: python script_name.py
2. The script will open LinkedIn, log in using your credentials, save cookies for future sessions, fetch companies from your profile, and retrieve recommended and recent jobs for each company.

## Important Note
- It is recommended to run the script only in accordance with LinkedIn's terms of service.
- Be cautious with automation to avoid any potential issues with LinkedIn's policies.
## Configuration
- Update the credentials.py file with your LinkedIn username and password.
- Adjust the file paths and structure as needed for your project.
## Disclaimer
This script is for educational and informational purposes only. Use the automation responsibly and at your own risk. The developer is not responsible for any consequences resulting from the use of this script.
