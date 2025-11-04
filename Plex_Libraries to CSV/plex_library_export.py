#!/usr/bin/env python3

### Explanation ###
# xlsxwriter library handles the creation of the Excel file with multiple worksheets.
# Define a helper function, get_subfolders(), to list only the folder names (ignoring files).
# Create a workbook with xlsxwriter.Workbook and add three worksheets (Movies, Movies 4K, and Shows).
# For each folder list, we write them in the corresponding worksheet.

###  Installing Python & xlsxwriter on Unraid ###
# Install Python 3 via the NerdTools/NerdPack plugin
# Install xlsxwriter 
## Copy this code into Unraid Terminal. You need to create a new script and paste this code. Schedule it to run at first Array startup only ##
# pip install xlsxwriter


import os
import xlsxwriter

# Directories to scan
MOVIES_DIR = "YOUR LIBRARY"    ############## YOUR LIBRARY ###############
MOVIES_4K_DIR = "YOUR LIBRARY" ############## YOUR LIBRARY ###############
SHOWS_DIR = "YOUR LIBRARY"     ############## YOUR LIBRARY ###############

# Output .xlsx file
OUTPUT_XLSX = "OUTPUT FILE"    ############## OUTPUT FILE ###############

def get_subfolders(path):
    """
    Return a sorted list of subfolder names in the given directory.
    """
    if not os.path.isdir(path):
        return []
    folders = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            folders.append(item)
    return sorted(folders)

def main():
    # Create an Excel workbook
    workbook = xlsxwriter.Workbook(OUTPUT_XLSX)

    # Create one worksheet per library
    ws_movies   = workbook.add_worksheet("Movies")
    ws_movies_4k = workbook.add_worksheet("Movies 4K")
    ws_shows    = workbook.add_worksheet("Shows")

    # Write headers
    ws_movies.write(0, 0, "Title")
    ws_movies_4k.write(0, 0, "Title")
    ws_shows.write(0, 0, "Title")

    # Gather folder names
    movie_folders = get_subfolders(MOVIES_DIR)
    movie_4k_folders = get_subfolders(MOVIES_4K_DIR)
    show_folders = get_subfolders(SHOWS_DIR)

    # Fill the Movies sheet
    for row, folder_name in enumerate(movie_folders, start=1):
        ws_movies.write(row, 0, folder_name)

    # Fill the Movies 4K sheet
    for row, folder_name in enumerate(movie_4k_folders, start=1):
        ws_movies_4k.write(row, 0, folder_name)

    # Fill the Shows sheet
    for row, folder_name in enumerate(show_folders, start=1):
        ws_shows.write(row, 0, folder_name)

    # Save and close the workbook
    workbook.close()
    print(f"Export complete! File created at: {OUTPUT_XLSX}")

if __name__ == "__main__":
    main()

### Automating the Script ###
# Create a folder in /mnt/user/appdata/python_scripts
# Put the .py file in it
# Use the User Scripts plugin in Unraid
## Copy this code ##

#!/bin/bash

# python3 /mnt/user/appdata/python_scripts/plex_library_export.py
# if [ $? -ne 0 ]; then
#   send_discord_message "Python script (plex_library_export.py) **failed**!"
# fi