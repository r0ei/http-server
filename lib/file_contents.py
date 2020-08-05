from os import path, getcwd

def get_file_contents(file: str) -> bytes:
        if path.exists(file):
            with open(file) as f:
                return f.read().encode()
        with open(getcwd() + '/html/not_found.html') as f:
            return f.read().encode()