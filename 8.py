def copy_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            content = input_file.read().upper()
        with open(output_file_path, 'w') as output_file:
            output_file.write(content)
        print(f"File contents copied and converted to uppercase successfully.")
    except FileNotFoundError:
        print("Error: The specified input file was not found.")
    except IOError as e:
        print(f"Error: An IO error occurred - {e}")
    except Exception as e:
        print(f"Error: {e}")
input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")
copy_file(input_file_path, output_file_path)
