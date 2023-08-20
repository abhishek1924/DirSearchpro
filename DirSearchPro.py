import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque
from colorama import Fore, Style

def display_disclaimer():
    disclaimer = """
    DISCLAIMER: DirSearchPro is created solely for educational and ethical purposes.
    The tool's primary objective is to assist users in understanding web directory structures
    and practicing responsible website exploration. It is not intended for any malicious
    or unauthorized use.
    """
    print(Fore.RED + Style.BRIGHT + disclaimer + Style.RESET_ALL)

def find_all_directories(url):
    try:
        visited = set()
        queue = deque([url])
        directories = set()

        while queue:
            current_url = queue.popleft()
            if current_url in visited:
                continue

            visited.add(current_url)

            if not current_url.startswith('http://') and not current_url.startswith('https://'):
                print(f"Skipping URL: {current_url} (Not an HTTP/HTTPS URL)")
                continue

            response = requests.get(current_url)
            response_code = response.status_code

            tool_name = f"{Fore.CYAN}{Style.BRIGHT}DirSearchPro{Style.RESET_ALL}"
            creator_name = f"{Fore.WHITE}{Style.BRIGHT}Abhishek1924{Style.RESET_ALL}"
            response_text = (
                f"{Fore.GREEN if response_code == 200 else Fore.RED}Response Code: {response_code}{Style.RESET_ALL}"
            )
            scanning_text = f"{Fore.MAGENTA}Scanning: {current_url}{Style.RESET_ALL}"

            print(tool_name, "by", creator_name)
            print("=" * 50)
            print(scanning_text)
            print(response_text)
            print("-" * 50)

            if response_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                for link in soup.find_all('a', href=True):
                    href = link.get('href')
                    full_url = urljoin(current_url, href)
                    if full_url.endswith('/'):
                        directories.add(full_url)
                        queue.append(full_url)

        return directories

    except requests.exceptions.RequestException as e:
        error_text = f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}"
        print(error_text)
        return []

if __name__ == "__main__":
    display_disclaimer()

    target_url = input(f"{Fore.YELLOW}Enter the URL to search for directories: {Style.RESET_ALL}")

    found_directories = find_all_directories(target_url)

    if found_directories:
        print("\nFound directories:")
        for directory in found_directories:
            print(directory)
    else:
        print("No directories found.")
