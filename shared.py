import os

# Change path if needed
SHARED_FOLDER = r"D:\LAN_Messenger\shared"

# Ensure folder exists
os.makedirs(SHARED_FOLDER, exist_ok=True)


def safe_filename(filename: str):
    """Prevent directory traversal attacks"""
    return os.path.basename(filename)


def save_file(filename, content):
    filename = safe_filename(filename)
    path = os.path.join(SHARED_FOLDER, filename)

    with open(path, "wb") as f:
        f.write(content)

    return filename


def get_file_path(filename):
    filename = safe_filename(filename)
    return os.path.join(SHARED_FOLDER, filename)


def list_files():
    return os.listdir(SHARED_FOLDER)


def file_exists(filename):
    return os.path.exists(get_file_path(filename))