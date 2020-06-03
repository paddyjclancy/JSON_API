# API, JSON and PostCodes.io


This repo explores using the package Requests, to make GET and POST request to a simple api end-point. 

## Task 
- Make 2 GET request
- Complete this README.md

## What is an API
- Application Programming Interface
- Set of functions / procedures
- Defines interactions between internal systems - computers, servers, etc
- Allows applications to "talk to each other" by dealing with requests
- eg Amazon S3, Google Maps

- Formats: JSON, XML

##### url_target = path + arguments
##### path = 'http://api.postcodes.io/postcodes/'
##### arguments = 'e147le'

## What is JSON
- JavaScript Object Notation
- File format, for storing, parsing and transferring data with ease
- Dictionaries / Arrays
- Became web standard for front-end development because of simplicity, and as browsers only use HTML, CSS or JS <-- 

- Receiving info in JSON from API:
    - API Response --> JSON --> Python JSON. library (parsing) --> JSON --> Python dict object
- Sending info using API:
    - Python dict object --> Python JSON. library (parsing)  --> JSON --> API Destination


## HTTP GET VS POST

Get:
- Requests data from specified resource (eg website)
- Visible, and cached
    - Should not contain sensitive info
- Shouldn't modify data
- eg search page

Post:
- Used when changing something, not limited to
- Contains info in body
- Not cached or stored
- May insert a new, or update resource
- eg changing a password
 

### Main status codes 

200 - 299   = GOOD
300 - 399   = UNDERSTOOD (resource maybe located elsewhere)
400 - 499   = ERROR (client side)
500 - 599   = ERROR (server)

-----------////------------

## Package managers

Software tools that automate the process of installing, upgrading, configuring, and removing computer programs for a computer's operating system in a consistent manner.

- eg app stores, Steam, Google Play

### list the package managers

Package managers for:
- python: pip, Anaconda, EasyInstall 
    - pycharm: pip
- ruby: rubygems
- js: npm, Yarn

at an operating system you can also have a package manager:
- linux - unbuntu: GNOME Software, APT, dpkg, Snappy, flatpak
- Windows: Windows Installer, executable file (.exe), Universal Windows Platform
- IOS: Swift


### what is https://pypi.org/?

- Python Package Index - PyPI
- Official third-party software repo for Python
- Source / host of packages for managers eg pip
