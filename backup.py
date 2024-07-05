import time
import sys
import os.path
import shutil

def backup(src, dst):
    # List all files in the source directory
    files = os.listdir(src)

    # Check if the destination is a directory
    if os.path.isdir(dst):
        # List all files in the destination directory
        dst_files = os.listdir(dst)
        if dst_files != []:
            # If destination directory is not empty, iterate through each file
            print(dst_files)
            for file in dst_files:
                # Check if the file exists in the destination directory
                file_exists = os.path.exists(dst + '/' + file)
                if file_exists:
                    print("exists")
                    # If the file exists, create a timestamped filename
                    ts = time.time()
                    file_name = os.path.basename(file).split('.')
                    new_file_name = file_name[0] + '_' + str(ts) + '.' + file_name[1]
                    try:
                        # Copy the file from source to destination with the new name
                        shutil.copy2(os.path.join(src, file), os.path.join(dst, new_file_name))
                    except Exception as e:
                        # Print any exceptions that occur during the copy process
                        print(f"exception: {e}")
        else:
            # If the destination directory is empty, copy all files from source to destination
            for file in files:
                try:
                    shutil.copy2(os.path.join(src, file), dst)
                except Exception as e:
                    # Print any exceptions that occur during the copy process
                    print(f"exception:  {e}")
    else:
        # If the destination is not a directory, attempt to copy the entire source directory
        try:
            shutil.copytree(src, dst, dirs_exist_ok=True)
        except Exception as e:
            # Print any exceptions that occur during the copy process
            print(f"exception:  {e}")

def main():
    # Get source and destination directories from command line arguments
    source = sys.argv[1]
    destination = sys.argv[2]
    try:
        # Check if the source is a directory and is not empty
        if os.path.isdir(source) and os.listdir(source) != []:
            backup(source, destination)
    except IsADirectoryError:
        return "source given is not a directory"
    except Exception as e:
        return f"error occured {e}"

if __name__ == "__main__":
    main()
