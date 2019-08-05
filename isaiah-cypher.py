#!/usr/bin/python3

import argparse
import logging

argParser = argparse.ArgumentParser()

argParser.add_argument('-i', '--input', help='Input string to cypher')

logLevel = logging.DEBUG
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'

dailyShift = [3, 1, 18]

letterToNum = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
               "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
               "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
               "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ".": 27, " ": 28}

numToLetter = {"a": 14, "b": 17, "c": 3, "d": 7, "e": 9, "f": 11, "g": 16,
               "h": 8, "i": 25, "j": 23, "k": 19, "l": 15, "m": 18, "n": 1,
               "o": 2, "p": 5, "q": 10, "r": 12, "s": 20, "t": 22, "u": 6,
               "v": 4, "w": 24, "x": 13, "y": 26, "z": 21, ".": 27, " ": 28}

layer1 = [3, 17, 11, 25, 4, 7, 6, 12, 8, 9, 19, 24, 14, 18, 26, 10, 2, 5, 1,
          23, 13, 21, 15, 16, 28, 27, 20, 22, 3, 17, 11, 25, 4, 7, 6, 12, 8,
          9, 19, 24, 14, 18, 26, 10, 2, 5, 1, 23, 13, 21, 15, 16, 28, 27, 20,
          22]

layer2 = [18, 7, 21, 17, 14, 9, 26, 20, 10, 1, 5, 23, 2, 19, 25, 13, 24, 28,
          4, 16, 6, 27, 12, 15, 22, 3, 11, 8, 18, 7, 21, 17, 14, 9, 26, 20, 10,
          1, 5, 23, 2, 19, 25, 13, 24, 28, 4, 16, 6, 27, 12, 15, 22, 3, 11, 8]

layer3 = [11, 21, 6, 9, 1, 7, 24, 13, 10, 5, 27, 19, 28, 3, 22, 8, 12, 25, 17,
          20, 16, 23, 4, 15, 26, 14, 2, 18, 11, 21, 6, 9, 1, 7, 24, 13, 10, 5,
          27, 19, 28, 3, 22, 8, 12, 25, 17, 20, 16, 23, 4, 15, 26, 14, 2, 18]


def main():

    args = argParser.parse_args()

    logging.basicConfig(level=logLevel, format=FORMAT, filemode='a')

    logging.debug('All command line arguments: [%s]', args)

    cypherText(args.input)


def cypherText(inputText):

    logging.debug("Cyphering input text: [%s]", inputText)

    output = ''.join(executeCypher(letter) for letter in inputText)

    print(output)


def executeCypher(letter):

    logging.debug('Cyphering input letter: [%s]', letter)

    result = layer1[layer1.index(letterToNum[letter]) + dailyShift[0]]

    result = layer2[layer2.index(result) + dailyShift[1]]

    result = layer3[layer3.index(result) + dailyShift[2]]

    inverseNumToLetter = {v:k for k, v in numToLetter.items()}

    result = inverseNumToLetter[result]

    logging.debug('Result of cyphering input letter: [%s] = [%s]', letter, result)

    return result


if __name__ == '__main__':
    main()