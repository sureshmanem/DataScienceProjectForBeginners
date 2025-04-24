import os


def create_folders_from_file(filepath):
    """
    Reads folder names from a text file and creates the folders.

    Args:
        filepath (str): The path to the text file containing folder names.
    """
    try:
        with open(filepath, "r") as file:
            folder_names = file.read().splitlines()  # Read lines and remove newlines

        if not folder_names:
            print("The file is empty. No folders to create.")
            return

        created_count = 0
        for folder_name in folder_names:
            # Remove leading/trailing whitespace and check if the name is not empty
            folder_name = folder_name.strip()
            if folder_name:
                try:
                    os.makedirs(folder_name, exist_ok=True)
                    # Create folder, no error if exists
                    print(f"Created folder: {folder_name}")
                    created_count += 1
                except OSError as e:
                    print(f"Error creating folder {folder_name}: {e}")
            else:
                print("Skipping empty folder name.")

        if created_count == 0:
            print("No folders were created.")
        else:
            print(f"Successfully created {created_count} folder(s).")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    filepath = input("Enter the path to the text file containing folder names: ")
    create_folders_from_file(filepath)
