import os

def find_large_files(directory, size_in_mb=100):
    size_in_bytes = size_in_mb * 1024 * 1024  # 100 MB in Bytes
    large_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_in_bytes:
                large_files.append(file_path)

    return large_files

if __name__ == "__main__":
    directory_to_search = "C:\\Users\\anass\\RiderProjects\\dronesurveillance-app"  # Ersetzen Sie dies durch den gewünschten Pfad
    large_files = find_large_files(directory_to_search)
    
    if large_files:
        print("Dateien größer als 100 MB:")
        for file in large_files:
            print(file)
    else:
        print("Keine Dateien größer als 100 MB gefunden.")
