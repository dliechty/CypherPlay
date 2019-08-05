#!/usr/bin/python3

import argparse
import logging

argParser = argparse.ArgumentParser()

argParser.add_argument('-e', '--encrypt', help='String to cypher')
argParser.add_argument('-d', '--decrypt', help='String to decypher')

logLevel = logging.DEBUG
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'

dailyShift = [23, 8, 2]

letterToNum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,
               "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
               "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20,
               "v": 21, "w": 22, "x": 23, "y": 24, "z": 25, ".": 26, " ": 27}

numToLetter = {"a": 13, "b": 16, "c": 2, "d": 6, "e": 8, "f": 10, "g": 15,
               "h": 7, "i": 24, "j": 22, "k": 18, "l": 14, "m": 17, "n": 0,
               "o": 1, "p": 4, "q": 9, "r": 11, "s": 19, "t": 21, "u": 5,
               "v": 3, "w": 23, "x": 12, "y": 25, "z": 20, ".": 26, " ": 27}

layer1 = [2, 16, 10, 24, 3, 6, 5, 11, 7, 8, 18, 23, 13, 17, 25, 9, 1, 4, 0,
          22, 12, 20, 14, 15, 27, 26, 19, 21]

layer2 = [17, 6, 20, 16, 13, 8, 25, 19, 9, 0, 4, 22, 1, 18, 24, 12, 23, 27,
          3, 15, 5, 26, 11, 14, 21, 2, 10, 7]

layer3 = [10, 20, 5, 8, 0, 6, 23, 12, 9, 4, 26, 18, 27, 2, 21, 7, 11, 24, 16,
          19, 15, 22, 3, 14, 25, 13, 1, 17]


def main():

    args = argParser.parse_args()

    logging.basicConfig(level=logLevel, format=FORMAT, filemode='a')

    logging.debug('All command line arguments: [%s]', args)

    cypher(args.encrypt)


def cypher(text):

    logging.debug("Cyphering input text: [%s]", text)

    output = ''
    previousLetter = ''

    for letter in text:
        previousLetter = encrypt(letter, previousLetter)
        output = output + previousLetter

    print(output)


def uncypher(text):

    logging.debug("Cyphering input text: [%s]", text)

    output = ''.join(decrypt(letter) for letter in text)

    print(output)


def encrypt(letter, previousLetter):

    logging.debug('Encrypting input letter: [%s]', letter)

    i = (layer1.index(letterToNum[letter]) + dailyShift[0]) % len(layer1)

    result = layer1[i]

    i = (layer2.index(result) + dailyShift[1]) % len(layer2)

    result = layer2[i]

    i = (layer3.index(result) + dailyShift[2]) % len(layer3)

    result = layer3[i]

    inverseNumToLetter = {v: k for k, v in numToLetter.items()}

    if previousLetter:
        result = (result + numToLetter[previousLetter]) % len(layer1)

    result = inverseNumToLetter[result]

    logging.debug('Result of cyphering input letter: [%s] = [%s]',
                  letter, result)

    return result


def decrypt(letter):

    logging.debug('Decrypting input letter: [%s]', letter)

    i = layer1.index(letterToNum[letter]) + dailyShift[0] % len(layer1)

    result = layer1[i]

    i = layer2.index(result) + dailyShift[1] % len(layer2)

    result = layer2[i]

    i = layer3.index(result) + dailyShift[2] % len(layer3)

    result = layer3[i]

    inverseNumToLetter = {v: k for k, v in numToLetter.items()}

    result = inverseNumToLetter[result]

    logging.debug('Result of cyphering input letter: [%s] = [%s]',
                  letter, result)

    return result


if __name__ == '__main__':
    main()
