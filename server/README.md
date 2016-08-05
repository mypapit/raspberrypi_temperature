# Automatic Raspberry pi CPU temperature reporting
Copyright (c) 2016 Mohammad Hafiz bin Ismail <mypapit@gmail.com>

This packages contains a quick and dirty hack for raspberry pi to report its CPU temperature to a remote server.
The package has client-side code and server-side code

The client-side is written in Python (tested with  Python 2.7.9 under Raspbian Jessie 8)
and is stored in "python-code" directory

The server-side is written in PHP (tested with  PHP 5.5.9 under Ubuntu 14.04 LTS)


## Server Side requirements
python 2.7.9 (tested)
python-pip
Python HTTP Requests libary (python-requets.org)


I install the requests library by installing python-pip via apt-get on Raspbian,
then I install Python HTTP Requests:

pip install requests


## Client Side requirements
php 5.5.9 (tested)
php-sqlite3


make sure that the 'duke.db' sqlite3 file is writable for web server user

