# Import the 're' module for regular expression operations, which may be used later for URL validation or extraction
import re

# Prompt the user to enter a URL, then strip any leading or trailing whitespace from the input
url = input("Enter URL: ").strip()

#re.sub(    # Pattern to match 'http://' or 'https://' at the beginning of the URL
#    r"^https?://",)
# re.removeprefix  # Remove the 'http://' or 'https://' prefix from the URL if it exists
# re.replace  # Replace 'http://' or 'https://' with an empty string to remove it from the URL