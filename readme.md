# URL Fuzzer

URL Fuzzer is a Python GUI application that allows users to perform URL fuzzing using wordlists directly sourced from the SecLists GitHub repository. This tool is designed to help security professionals and enthusiasts test various endpoints by inserting words from a selected wordlist into the URL and observing the HTTP responses.

## Features

- **GUI Interface**: User-friendly interface built with Tkinter and enhanced with `ttkthemes` for a dark theme.
- **Dynamic Wordlist Selection**: Fetches and lists available wordlists directly from the SecLists GitHub repository.
- **Automated Fuzzing**: Automatically replaces `FUZZ` in the provided URL with words from the selected wordlist and displays the results.

## Prerequisites

- Python 3.x
- `requests` library
- `ttkthemes` library

You can install the required libraries using pip:


```sh
pip install requests ttkthemes

## Clone
```sh
git clone https://github.com/HelloByeLetsNot/URL-Fuzzer.git
cd URL-Fuzzer

## Run
```sh
python main.py


## Use the Application:
Enter the URL: Input the URL you want to fuzz. Use FUZZ in the URL where you want to insert words from the wordlist.Select a Wordlist: Choose a wordlist file from the dropdown menu. The program will download the selected wordlist from the GitHub repository.Start Fuzzing: Click "Start Fuzzing" to begin. The results, including HTTP response codes for each fuzzed URL, will be displayed in the text area below.



