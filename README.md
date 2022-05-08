# Pyupdate
## About
Pyupdate is a pure-python module for writing update routines for your application. 

Using pyupdate you can compare a local file to one on a server, and then you can replace the potentially outdated file with the contents of the server.

## Use
Pyupdate is very lightweight and very easy to learn - there are only 2 methods.

### pyupdate.check(local_path, server_address)
This compares the contents of a local file with one from a server. If this returns true then the contents are different.

Example:
```py
new_version = pyupdate.check("./example.png", "https://example.com/example.png")
print(new_version)
```

```
>>> True
```

It is recommended to check small files, as running this function still requests the full file from the server. 

### pyupdate.download(local_path, server_address)
This function requests a file from the server and writes the contents to a local path. If the path already exists, it will overwrite the contents of the file. If not, it will create a new file.

Example:
```py
pyupdate.download("./example.png", "https:/example.com/example.png")
```
