from os import getcwd

def extract_file(request: str) -> str:
        return getcwd() + request.split('\n')[0].split(' ')[1] # full path