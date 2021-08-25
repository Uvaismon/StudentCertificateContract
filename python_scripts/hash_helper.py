import hashlib
import os

def hash_from_file(filename):
    """
    This function takes a file object and returns the hash sha256 hash sum.
    """
    h = hashlib.sha256()
    filepath = os.path.join(r'.\file_buffer', filename)
    with open(filepath, 'rb') as file:
        while (chunk := file.read(h.block_size)):
            h.update(chunk)
    return h.hexdigest()