#!/usr/bin/env python
import argparse

# Chech positive interger numbers


def check_positive(num):
    n = int(num)
    if (n <= 0):
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % num)
    return n

# Check the word only contains S and T


def only_s_t(word):
    if (word.count('S') + word.count('T') != len(word)):
        raise argparse.ArgumentTypeError(
            "%s is an invalid string value" % word)
    return word

# Convert s and t into Soft and Tough


def convert(c):
    s = "Soft"
    t = "Tough"

    if (c == "S"):
        return s
    else:
        return t

# Play with letters and positions in word


def repeat_word(word, n):
    stringArray = []
    m = len(word)
    y = n

    while (y >= m):
        for i in range(m):
            stringArray.append(convert(word[i]) + ",")
        y -= m

    if (y < m):
        for i in range(y):
            stringArray.append(convert(word[i]) + ",")

    if (len(stringArray) > 1):
        stringArray[-2] = stringArray[-2].strip(",") + \
            " and " + stringArray[-1].strip(",")
        stringArray.pop(-1)
    else:
        stringArray[-1] = stringArray[-1].strip(",")

    string = stringArray[0]
    for i in range(1, len(stringArray)):
        string = string + " " + stringArray[i]
    string = string + "."
    print(string)

# Input arguments as requirement
# First argument is pattern which includes only S and T
# Following arguments are the list of positive intergers


def get_args():
    parser = argparse.ArgumentParser(
        description='Repeat and Convert Letters to Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('pattern',
                        metavar='str',
                        type=only_s_t,
                        help="The first argument is a random pattern consisting of characters S and T. For example 'STTTS'")

    parser.add_argument('numbers',
                        metavar='N',
                        type=check_positive,
                        nargs='+',
                        help='The following arguments are N (N >= 1) number of integers. For example 1 5 8.')
    return parser.parse_args()

# -------------------------------------------


def main():
    args = get_args()
    nums = args.numbers
    word = args.pattern

    for n in nums:
        repeat_word(word, n)


# -------------------------------------------
if __name__ == "__main__":
    main()
