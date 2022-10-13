# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Unit3-02.py File, learning if statements in python.

import constants


def main():

    # input
    guess_number = int(input("Guess the number from 0 to 9: "))

    # process and output
    if guess_number == constants.CONSTANT_NUMBER:
        print("\nYou guessed right.")
    if guess_number != constants.CONSTANT_NUMBER:
        print("\nYou guessed wrong, try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
