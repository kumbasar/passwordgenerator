# Password Generator
A simple password generator

## Setup

```bash
pip3 install -r requirements.txt
```

## Usage

See help

```bash
# ./passwordg.py --help                                                               
usage: passwordg.py [-h] [-l LENGTH] [-xu] [-xl] [-xd] [-xp] [-o]

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Set password length (default: 18)
  -xu, --excludeUpperCase
                        Exclude all uppercases: ABCDEFGHIJKLMNOPQRSTUVWXYZ (default: False)
  -xl, --excludeLowerCase
                        Exclude all lowercases: abcdefghijklmnopqrstuvwxyz (default: False)
  -xd, --excludeDigits  Exclude all digits: 0123456789 (default: False)
  -xp, --excludePunctuation
                        Exclude all punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (default: False)
  -o, --onlyFriendlyPunctuation
                        Include only!#$%&*+-_= (default: False)
```

## Example

To generate a 128 length `friendly` password:

```bash
./passwordg.py -o -l 128
Password base chars: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%%&*+-_=

Generated random password:  e9VK+w&JI6r2=5QgR6UNc7KNvGWFErtH-5LVH++g7Mf8UzslGyPXiDcuc_jI6kF+FWEgNx$-1MD$fS1q3mhBM%_O&tSjWjZ4!jx511ImnZdb&jCmMa_g6qZDU19IEsPt
```