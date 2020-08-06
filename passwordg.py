#!/usr/bin/env python3

import argparse
import string
import random
import sys


DEFAULT_PWD_LENGTH = 18

LETTERS = string.ascii_lowercase
DIGITS = string.digits  
PUNCTUATION = string.punctuation  
FRIENDLY_PUNCTUATION = "!#$%%&*+-_="


parser = argparse.ArgumentParser(
                    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-l", "--length", help = "Set password length", type = int,
                    default = DEFAULT_PWD_LENGTH)
parser.add_argument("-xu", "--excludeUpperCase", help = "Exclude all uppercases: ABCDEFGHIJKLMNOPQRSTUVWXYZ", action = 'store_true')
parser.add_argument("-xl", "--excludeLowerCase", help = "Exclude all lowercases: abcdefghijklmnopqrstuvwxyz", action = 'store_true')
parser.add_argument("-xd", "--excludeDigits", help = "Exclude all digits: 0123456789", action = 'store_true')
parser.add_argument("-xp", "--excludePunctuation", help = "Exclude all punctuation: !\"#$%%&'()*+,-./:;<=>?@[\]^_`{|}~", action = 'store_true')
parser.add_argument("-o", "--onlyFriendlyPunctuation", help = "Include only" + FRIENDLY_PUNCTUATION, action = 'store_true')

args = parser.parse_args()

password_chars = ""

if args.excludeUpperCase == False:
    password_chars = password_chars + LETTERS.upper()
if args.excludeLowerCase == False:
    password_chars = password_chars + LETTERS
if args.excludeDigits == False:
    password_chars = password_chars + DIGITS
if args.excludePunctuation == False:
    if args.onlyFriendlyPunctuation == True:
        password_chars = password_chars + FRIENDLY_PUNCTUATION
    else:
        password_chars = password_chars + PUNCTUATION
    
if password_chars == "":
    sys.exit('Invalid option. You have excluded everything!')


print('Password base chars: ' + password_chars + "\n")

password_chars = list(password_chars)
random.shuffle(password_chars)

random_password = random.choices(password_chars, k=args.length)
random_password = ''.join(random_password)

print('Generated random password: ', random_password)
