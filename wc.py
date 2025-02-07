import argparse
import os
import pickle
#import sys
from string import punctuation

def wordfreq(fname, stripPunc=False, toLower=False, nonwords=False, separator=" ") :
    wordDict = {}
    with open(fname) as f:
        words = f.read().split(separator)
        print("These are the words: ", words)
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
    parser.add_argument("-nw", "--nonwords", action="store_true")
    parser.add_argument("-sep", "--separator", action="store_true")
    parser.add_argument("--save", type=str)
    args = parser.parse_args()

    #print(wordfreq("submission.py"))

    combined_word_freq = {}
    if os.path.isdir(args.fname):
        print("It's a directory!")
    for root, dirs, files in os.walk(args.fname):
        print("Trying to traverse...")
        for file in files:
            try:
                with open(file) as f:
                    wd = wordfreq(f, args.strip, args.convert, args.nw, args.sep, args.save)
                    print("This is wd: ", wd)
                    for word in wd.keys():
                        if word in combined_word_freq:
                            combined_word_freq[word] += 1
                        else:
                            combined_word_freq[word] = 1
            except:
                print("Something went wrong.")
    print(combined_word_freq)

    # for r, d, f in os.walk(path):
    #     wd = wordfreq(fname, stripPunc=strip, toLower=convert)

    pickled = False
    # for arg in sys.argv:
    #     if arg.startswith('--pfile'):
    #             ofile = arg.split('=')[1]
    #             pickle.dump(wd, open(ofile, 'w'))
    #             pickled = True
    #     if not pickled:
    #         print(wd)
    if args.save:
        ofile = args.split(", ")[1]
        pickle.dump(combined_word_freq, open(ofile, "wb"))
        pickled = True
    if not pickled:
        print(combined_word_freq)





