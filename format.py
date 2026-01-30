# This script reformats a username from "Last, First" to "First Last" and prints a greeting.

import re  # Import the regular expressions module for pattern matching

# Prompt the user to enter their username and strip any leading/trailing whitespace
username = input("Enter your username: ").strip()

# Use regex to search for the pattern "anything, anything" (Last, First format)
if matches := re.search(r"^(.+), *(.+)$", username):

    # If a match is found, reformat the username to "First Last"
    username = matches.group(2) + " " + matches.group(1)

# Print a greeting message with the formatted username
print(f"hello, {username}")
