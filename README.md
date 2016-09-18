# Wercker GKE Demo: Get IP address HTTP API

A simple Python application that uses the Bottle framework to serve a JSON encoded client IP address of a user who makes a GET request to /.

Used as an example application for a tutorial on Wercker I am writing.

```
usage: get_ip.py [-h] hostname port

HTTP API for returning a visitor's IP address.

positional arguments:
  hostname    The host IP to listen on.
  port        The port to listen on.

optional arguments:
  -h, --help  show this help message and exit
```

Requires `Python 2` `pip` & `virtualenv` to run.

