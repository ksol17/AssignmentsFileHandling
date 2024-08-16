import os

def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f'File: {entry.name}')
                elif entry.is_dir():
                    print(f'Directory: {entry.name}')
    except FileNotFoundError:
        print("The specified path does not exist.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Please enter the directory path: ")
    list_directory_contents(directory_path)
