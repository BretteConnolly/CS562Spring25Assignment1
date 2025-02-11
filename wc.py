#Brette Fitzgibbon

import argparse
import os
import pickle
import sys
from string import punctuation

def wordfreq(fname, stripPunc=False, toLower=False, nonwords=False, separator=" ") :
    wordDict = {}
    with open(fname) as f:
        words = f.read().split(separator)
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if toLower :
                word = word.lower()
            if nonwords:
               if not word.isalpha():
                   continue
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    return wordDict

if __name__== '__main__':
    parser = argparse.ArgumentParser(description="Word Frequency")
    parser.add_argument("fname")
    parser.add_argument("-strip", "--strip_punc", action="store_true")
    parser.add_argument("-convert", "--to_lower", action="store_true")
    parser.add_argument("-nw", action="store_true")
    parser.add_argument("-sep", type=str)
    parser.add_argument("--save", type=str)
    args = parser.parse_args()

    print(wordfreq("submission.py"))

    combined_word_freq = {}
    for root, dirs, files in os.walk(args.fname):
        for file in files:
            try:
                full_name = os.path.join(root, file)
                wd = wordfreq(full_name, args.strip, args.convert, args.nw, args.sep)
                for word in wd.keys():
                    if word in combined_word_freq:
                        combined_word_freq[word] += 1
                    else:
                        combined_word_freq[word] = 1
            except Exception as e:
                print("Something went wrong.", e)
    print(combined_word_freq)

    pickled = False
    if args.save:
        ofile = args.split(", ")[1]
        pickle.dump(combined_word_freq, open(ofile, "wb"))
        pickled = True
    if not pickled:
        print(combined_word_freq)





