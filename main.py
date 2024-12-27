import urllib.request
import os
import time
import logging

# Logging configuration
logging.basicConfig(filename='file_extract.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
sysroot = os.path.expanduser("~")
log_file = "logs.txt"
def check_logs():
    try:
        open(log_file, "r")
    except FileNotFoundError:
        open(log_file, "w").write("raw 01")
        return True
    return False

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def validate_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        print(error_message)

def is_not_empty(value):
    return bool(value.strip())

def main():
    first_time = check_logs()
    
    if first_time:
        print("Welcome to FileExtract by rawbyte")
        print()
        time.sleep(0.8)
        print("""I will guide you because it's your first time using this tool
        Thanks for downloading FileExtract""")
        time.sleep(1)
        print("getting everything ready")
        clear_console()
        print(logo)

    username = validate_input("GitHub username: ", is_not_empty, "Username cannot be empty.")
    repo_name = validate_input("Repository name: ", is_not_empty, "Repository name cannot be empty.")
    path_to_file = validate_input("Path to file in GitHub: ", is_not_empty, "Path to file cannot be empty.")
    save_location = validate_input("Where to save download: ", is_not_empty, "Save location cannot be empty.")
    extract_url = f'https://raw.githubusercontent.com/{username}/{repo_name}/main/{path_to_file}'  # Assuming "main" branch
    
    print(f"Extracting {path_to_file} from https://github.com/{username}/{repo_name}")

    try:
        urllib.request.urlretrieve(extract_url, save_location)
        print(f"Saved in {save_location}")
        logging.info(f"File {path_to_file} from {repo_name} saved in {save_location}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Failed to download {path_to_file} from {repo_name}: {e}")

if __name__ == "__main__":
    main()
