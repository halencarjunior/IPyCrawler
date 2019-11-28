# IPyCrawler

Simple Script for Lookup hostnames in IP Ranges.

This tool is based in the Old and Super Useful ipcrawl.

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

## Requirements:

- python3+
- ipaddress
  
  * $ pip install ipaddress

## Usage

  $ python3 ipcrawl.py -s 1.1.1.1 -e 1.1.1.2 -o results.txt

optional arguments:

  -h, --help show this help message and exit
  
  -s [STARTIP], --startip [STARTIP] Start IP (This argument is required)
  
  -e [ENDIP], --endip [ENDIP] End IP 
  (Optional argument. For single lookup use only -s or --startip. -o option is not allowed for single lookup)
  
  -o [OUTPUT], --output [OUTPUT] Output results to a file e.g results.txt
  
  --version             show program's version number and exit

## Screenshots

![IPyCrawler](https://imgur.com/N2tHobe.jpg)
