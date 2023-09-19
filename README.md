# Ivy Connection - LinkedIn Automation

![LinkedIn Logo](https://brand.linkedin.com/content/dam/brand/site/img/logo/logo-tm.png)

Ivy Connection is a Python-based LinkedIn automation tool designed to connect with Ivy League university students on LinkedIn and collect their profile information for networking and professional purposes. This tool leverages the power of Selenium to perform automated tasks on the LinkedIn platform.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Customization](#customization)
- [Contribution](#contribution)
- [License](#license)

## Features

- **Automated LinkedIn Actions**: Connect with Ivy League students on LinkedIn automatically.
- **Profile Information**: Collect and store essential profile information, including name, gender, university, and profile link.
- **Dynamic Search**: Customize your search criteria to target specific profiles.
- **CSV Export**: Store the collected data in CSV format for easy analysis and reference.
- **User-Friendly**: Built with user-friendliness in mind, with simple configurations.

## Getting Started

### Prerequisites

Before using Ivy Connection, ensure you have the following:

- Python 3.x installed on your system.
- The Chrome web browser installed.
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and configured for your Chrome version.
- A valid LinkedIn account.

### Installation

1. Clone the Ivy Connection repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ivy-connection.git
   ```

2. Navigate to the repository's directory:

   ```bash
   cd ivy-connection
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Open the `config.py` file and update it with your LinkedIn username and password.

2. Customize the search query in the `IvyConnection` class to specify your criteria for Ivy League students.

3. Run the Ivy Connection script:

   ```bash
   python ivy_connection.py
   ```

   The script will perform the automated tasks and store the data in a CSV file.

## Customization

You can customize Ivy Connection for your specific requirements by modifying the search criteria and data collection in the script. Explore the script's comments and documentation for more details on customization options.

## Contribution

Contributions to Ivy Connection are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request. Please review our [Contribution Guidelines](CONTRIBUTING.md) for more information.

## License

Ivy Connection is open-source software licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

---

**Disclaimer**: Please use Ivy Connection responsibly and in compliance with LinkedIn's terms of service. Automated actions on LinkedIn may be subject to restrictions and policies, so exercise caution when using this tool.
```

You can copy and paste this template into a README.md file in your "ivy-connection" repository on GitHub and then customize it further to provide specific details about your project. Don't forget to update the links, descriptions, and any other information to match your project's specifics.
