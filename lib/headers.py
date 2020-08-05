from email.utils import formatdate
from mimetypes import guess_type
from os import uname, path
from .file_contents import get_file_contents

def response_headers(file: str) -> list:
        headers = []
        file_contents = get_file_contents(file) # file contents
        headers.append('404 File not found') if not path.exists(file) else headers.append('200 OK') # status code
        headers.append('text/html' if guess_type(file)[0] == 'text/html' or not path.exists(file) else 'text/plain') # content type header
        headers.append(formatdate(timeval=None, localtime=None, usegmt=None)) # date header
        headers.append(uname()[1]) # Server header
        headers.append(len(file_contents)) # content-length header
        headers.append(file_contents) # append file contents
        return headers