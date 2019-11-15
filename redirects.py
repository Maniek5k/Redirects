import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from termcolor import colored

start_time = time.time()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(options=options)


def compare():
    if driver.current_url == row[1]:
        print("Redir ok at line: " + str(line_count))
        print("Base URL in " + str(line_count) + ": " + row[0])
        print("Redirected URL in " + str(line_count) + ": " + row[1])
    else:
        file = open("errors.log", "a")
        file.write("*******************" + "\n" +
                   "ERROR at line: " + str(line_count) + "\n" +
                   "Base URL: " + str(line_count) + ": " + row[0] + "\n" +
                   "Expected URL: " + str(line_count) + ": " + row[1] + "\n" +
                   "Current URL: " + driver.current_url + "\n" +
                   "*******************" + "\n" + "\n")
        print(colored("ERROR at line: " + str(line_count) + " saved in errors.log file", "red"))


with open('redirs.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        driver.implicitly_wait(1)
        driver.get(row[0])
        driver.implicitly_wait(1)
        compare()
        line_count += 1
    print(f'Processed {line_count} lines.')

end_time = time.time()

print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))
