# http-server

Simple Multi threaded HTTP Web Server in Python over TCP. Scroll down for a list of supported HTTP methods, headers, and status codes. The server displays  the `not_found.html` if the requested file not found. The Server displayes `index.html` when the requested file is a directory.

## Status Codes

_404_ File not found
_200_ OK

## Methods

_GET_

## installation

```bash
$ git clone https://github.com/r0eilevi/http-server
$ cd http-server
$ pip install -r requirements.txt
$ python3 main.py
```

## Headers

```
Status Code
Mime type
Date
Server
Content Length
Content
```
