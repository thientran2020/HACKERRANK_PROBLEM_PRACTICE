# Start Date: 12/14/2020
# PYTHON CODE CHALLENGES ON LINKEDIN LEARNING
# 1. Find prime factors
# 2. Identify a palindrome
# 3. Sort a string
# 4. Find all list items
# 5. Play the waiting game
# 6. Save a dictionary
# 7. Set an alarm
# 8. Send an email
# 9. Simulate dice
# 10. Count unique words
# 11. Generate a password
# 12. Merge CSV files.
# 13. Solve a Sudoku.
# 14. Build a ZIP archive
# 15. Download sequential files
import csv
import math
import pickle
import random
import time
import sched
import winsound as ws
import scipy
from scipy.stats import norm
import smtplib
from collections import Counter
from itertools import product
from PyQt5 import QtCore

# works similarly as random module
# since generally random module is not used for secure purpose...
import secrets

# Using for creating zip files
from zipfile import ZipFile

# working with operating system
import os
# working with regular expression
import re
# working with url
import urllib.parse
import urllib.request


def get_prime_factors(number):
    factors_list = []
    k = 2
    while number > 1:
        if number % k == 0:
            factors_list.append(k)
            number = number // k
        else:
            k += 1
    return factors_list


def is_palindrome(text):
    new_text = "".join([letter for letter in text.upper() if letter.isalpha()])
    return new_text[::-1] == new_text


def sort_words(text):
    words_list = text.split(' ')
    words_list = sorted(words_list, key=str.casefold)
    return " ".join(words_list)


def index_all(num_list, value):
    idxList = []
    for i in range(len(num_list)):
        if num_list[i] == value:
            idxList.append([i])
        elif isinstance(num_list[i], list):
            for j in index_all(num_list[i], value):
                idxList.append([i] + j)
    return idxList


def simulator(N, M, K):
    success = 0
    repetition = 10000
    for _ in range(repetition):
        total_hp = 0
        for _ in range(K):
            hp = random.randint(0, M)
            total_hp += hp
            if total_hp >= N:
                success += 1
                break
    return success / repetition


def probability(N, M, K):
    approx_mean = K * M / 2
    approx_var = K * (M ** 2 + 2 * M) / 12
    z_value = (N - 0.5 - approx_mean) / math.sqrt(approx_var)
    return 1 - scipy.stats.norm(0, 1).cdf(z_value)


def available_memory(N, M_array):
    def calculate(M1, M2):
        t = 0
        while M1 >= 0 and M2 >= 0:
            t += 1
            if M1 >= M2:
                M1 -= t
                M1 -= t
            else:
                M2 -= t
        if M1 < 0:
            M1 += t
        if M2 < 0:
            M2 += t
        return [t, M1, M2]

    for i in range(N):
        print(calculate(M_array[i][0], M_array[i][1]))


def waiting_game():
    target_time = random.randint(2, 4)
    print()
    print("Your target time is {} seconds.".format(target_time))
    pressedKey = input("---Press Enter to Begin (or s to Stop)---")
    if pressedKey == "":
        start_time = time.perf_counter()
        pressedKey = input("---Press Enter again after {} seconds".format(target_time))
        end_time = time.perf_counter()
        if pressedKey == "":
            process_time = end_time - start_time
            notice = "Elapsed time: {:.3f} seconds, ({:.3f} seconds too)" \
                .format(process_time, abs(process_time - target_time))
            if process_time < target_time:
                print(notice + " fast")
            elif process_time > target_time:
                print(notice + " slow")
            else:
                print("Perfect timing...Congratulations!!!")


# save a dictionary to file using pickle (Python object serialization)
def save_dictionary(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)


# retrieve a dictionary from file_path
def load_dictionary(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


# play a sound file at alarm_time and display a message
def set_alarm(alarm_time, sound_filename, message):
    # use sched module to initialize a schedule object
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(sound_filename, ws.SND_FILENAME))
    print('Alarm set for ', time.asctime(time.localtime(alarm_time)))
    s.run()


# Send an email
# Use smtplib module (SMTP protocol client)
def send_email(receiver_email, subject, body):
    SENDER_EMAIL = ''
    SENDER_PASSWORD = ''

    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)


# Simulate rolling multiple dices and calculate the probabilities
# EX: roll_dice(4,6,6) means rolling ONE 4-sided dice and TWO 6-sided dices
def roll_dice(*arguments, repetition=100000):
    t_sum = 0
    for number in arguments:
        t_sum += number
    table = [0 for _ in range(t_sum + 1)]
    for _ in range(repetition):
        num = 0
        for number in arguments:
            num += random.randint(1, number)
        table[num] += 1
    print("________PMF TABLE_______")
    for i in range(3, t_sum + 1):
        print('{} : {:0.2f}%'.format(i, table[i] / repetition * 100))


# Same as above function but using python list comprehension & Counter module to simulate
def roll_dice_2nd_way(*arguments, repetition=100000):
    counts = Counter()
    for roll in range(repetition):
        counts[sum((random.randint(1, sides) for sides in arguments))] += 1

    print('\n_______PMF TABLE_______')
    for outcome in range(len(arguments), sum(arguments) + 1):
        print('{} : {:0.2f}%'.format(outcome, counts[outcome] / repetition * 100))


# Take a path to a text file
# Output the total number of words
# Output top 20 most frequent words and their number of occurrences
def count_words(filepath):
    with open(filepath) as file:
        word_list = re.findall(r"[0-9a-zA-Z-']+", file.read())
        word_list = [word.upper() for word in word_list]
        print('\nTotal Words: ', len(word_list))

        my_dict = {}
        for word in word_list:
            if word not in my_dict.keys():
                my_dict[word] = 1
            else:
                my_dict[word] += 1
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        count = 0
        for item in sorted_dict:
            print(item[0], ":", item[1])
            count += 1
            if count == 20:
                break


# Generate a random password with a specific number pf words
# Use Diceware word list - a 5-digit number represents for a word
def generate_password(numWords):
    with open('eff_large_wordlist.txt') as file:
        lines = file.readlines()
        word_list = [line.split()[1] for line in lines]
    password = [secrets.choice(word_list) for _ in range(numWords)]
    return ' '.join(password)


# Merge multiple CSV files
def merge_csv(csv_list, output_path):
    fieldnames = []
    for in_file in csv_list:
        with open(in_file, 'r') as file:
            content = csv.DictReader(file).fieldnames
            fieldnames.extend(row for row in content if row not in fieldnames)

    with open(output_path, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as in_file:
                reader = csv.DictReader(in_file)
                for row in reader:
                    writer.writerow(row)


# Check a sudoku p at position [x][y] if it is a valid step to set p[x][y] = value
def isValid(x, y, p, value):
    for i in range(0, 9):
        if p[x][i] == value or p[i][y] == value:
            return False
    for (i, j) in product(range(0, 3), repeat=2):
        if p[x - x % 3 + i][y - y % 3 + j] == value:
            return False
    return True


# Solve a sudoku by using backtracking method
# Loop through each row and column - assign each box to a possible number from 1-9
# Recursively do it until cant continue, go back and set puzzle[row][col] = 0
# Use Cartesian product here (from itertools module) & new assignment operator :=
def solve(puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:
            for number in range(1, 10):
                if isValid(row, col, puzzle, number):
                    puzzle[row][col] = number
                    if trial := solve(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
    return puzzle


def print_sudoku(p):
    for row in range(0, 9):
        for col in range(0, 9):
            print(p[row][col], end='  ')
        print()


def solve_sudoku(puzzle):
    solved = solve(puzzle)
    if not solved:
        print("NO SOLUTION...")
    else:
        print("________ SUDOKU ________")
        print_sudoku(puzzle)


# Create a zip files from a search_directory with files in extension_list
# and keep other sub_directories in the search_directory
def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as out_file:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    out_file.write(os.path.join(root, file), arcname=os.path.join(rel_path, file))


def download_sequential_files(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    url_head, url_tail = os.path.split(first_url)
    first_idx = re.findall(r'[0-9]+', url_tail)[-1]
    idx_count, error_count = 0, 0
    while error_count < 4:
        next_idx = str(int(first_idx) + idx_count)
        if first_idx[0] == '0':
            next_idx = '0' * (len(first_idx) - len(next_idx)) + next_idx
        next_url = urllib.parse.urljoin(url_head, re.sub(first_idx, next_idx, url_tail))
        try:
            out_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, out_file)
            print('Successfully downloaded {}'.format(os.path.basename(next_url)))
        except IOError:
            print('Could not retrieve {}'.format(next_url))
            error_count += 1
        idx_count += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(get_prime_factors(630))
    # print(is_palindrome ("Go hang a salami - I'm a lasagna hog."))
    # print(sort_words("banana ORANGE apple"))
    # print(probability(2, 1, 3))
    # available_memory(2, [[2, 2], [8, 11]])
    # t = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    # print(index_all(t, 2))
    # waiting_game()
    # roll_dice_2nd_way(4, 5, 6, repetition=10000)
    # count_words('shakespeare.txt')
    # print(generate_password(7))
    test_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    # print_puzzle(puzzle)
    # print(possible_values(2, 4, puzzle))
    # solve_sudoku(test_puzzle)
    # url = 'http://699340.youcanlearnit.net/image001.jpg'
    # download_sequential_files(url, '.\\test_images')
