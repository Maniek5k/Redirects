##REDIRECTS TESTING TOOL   

This is 301 redirects testing tool, for general testing purpose.

This tool supports CSV file type, as most popular.

How it works:
- in redirects.py file we can setup which file should be opened:
    "with open('redirs.txt') as csv_file:" -> put your file instead of redirs.txt and it should read this file
- after correct path to our file is provided, we can just run script
- script will push logs into console after each row of CSV is checked
- every error found will be logged as ERROR in console + additionally all info will be pushed to errors.log file
- execution timer is applied for checking how much time it took to work out all redirects provided