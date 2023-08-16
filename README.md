# DirSearchPro

DirSearchPro is a Python script that helps you scan a given URL for directories and display the results using colored output. It's a useful tool for web exploration, analysis, and vulnerability assessment.

## Features

- Scans a target URL for directories and displays them with color-coded information.
- Provides response codes for each URL, highlighting 200 responses in green, non-reachable responses in red, and other responses in their respective colors.
- Enhances the scanning experience by presenting tool and creator names in stylish colors.
- Helps you identify hidden directories and analyze website structures quickly.

## Usage

1. Make sure you have Python 3.x installed.
2. Install the required dependencies using `pip install requests bs4 colorama`.
3. Run the script in your terminal by entering `python url.py`.
4. Enter the URL you want to scan for directories.
5. The script will display a color-enhanced report of the scanning process, indicating reachable directories and their response codes.

## Dependencies

- [requests](https://pypi.org/project/requests/): For sending HTTP requests and fetching response codes.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): For parsing HTML content and extracting URLs.
- [colorama](https://pypi.org/project/colorama/): For colorizing terminal output.

## Author

- **Abhishek1924** - [GitHub](https://github.com/Abhishek1924)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, open issues, and provide feedback. Happy directory scanning with DirSearchPro!
