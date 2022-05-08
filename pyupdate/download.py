from http import server
import typing

import os
import sys
import requests

def download(local_file, server_address) -> None:
    """
    Downloads a file from the server_address and overwrites the local_file with the contents.
    If the local_file doesn't exist, it will create it.

    Parameters
    ----------
    local_path (str) : 
        A relative or absolute path to the local file
    server_address (str) :
        The address of the web server
    """

    # Getting server file
    server = requests.get(server_address)

    # Writing contents to a local file
    with open(local_file, "wb") as file:
        file.write(server.content)
        file.close()