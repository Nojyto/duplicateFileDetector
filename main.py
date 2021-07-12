import os
import filecmp as file

if __name__ == "__main__":
    WORK_DIR = input("Input a working dir: ")
    if not os.path.isdir(WORK_DIR):
        print("Cannot lock onto directory.\nAborting.")
        exit(-1)

    dirpath, dirnames, filenames = next(os.walk(WORK_DIR), (None, None, []))
    fileCount = len(filenames)
    duplicates = []

    print(f"Dir locked. {fileCount} files found.")
    print("Searching for duplicates...\n")

    for i in range(0, fileCount - 1):
        for j in range(i + 1, fileCount):
            f1 = os.path.join(WORK_DIR, filenames[i])
            f2 = os.path.join(WORK_DIR, filenames[j])
            if(file.cmp(f1, f2)):
                duplicates.append((filenames[i], f1))

    if(len(duplicates) == 0):
        print("No duplicates found.\nExiting.")
        exit(-1)
    
    print("Duplicates found:")
    for name, path in duplicates:
        print(name)
    
    if input("\nDo you wish to delete the duplicates?(y/n) ") == "y":
        print("\nDeletion started:")
        for name, path in duplicates:
            os.remove(path)
            print(f"{name} has been deleted.")
        print("\nDeletion finished.\nExiting.")
    else:
        print("Deletion aborted.\nExiting.")