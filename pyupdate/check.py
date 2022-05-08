import typing
import requests


def check(local_path, server_address) -> bool:
    """
    Checks the local_path contents with the server_address contents,
    it is best to only check something small in size rather than the main program.

    Parameters
    ----------
    local_path (str) : 
        A relative or absolute path to the local file
    server_address (str) :
        The address of the web server
    
    Returns
    -------
    (bool) :
        Returns true if the file contents are different, and false if they are the same
    """

    # Getting local file
    try:
        with open(local_path, "rb") as file:
            local = file.read()
            file.close()
    except FileNotFoundError:
        return True # If the file doesn't exist, return true

    # Getting server file
    server = requests.get(server_address)
    
    # Comparing and returning result
    if local != server.content:
        return True
    return False
