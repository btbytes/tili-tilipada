#!/usr/bin/env python3
import argparse
import csv
import json

"""
﻿ಅರಿಮೆ ತಿಳಿಪದ ಪದನೆರಕೆ ಪದಗಳು - Arime Tiliapada Dictionary Words,,,
English words,Kannada words,Meaning Description  in Kannada(| separated),example of usage in Kannada(| separated)
,,,
anthracite,ಗಟ್ಟಿದ್ದಲು,,
"""


def main(infile, outfile):
    with open(infile, "r") as f:
        csvr = csv.reader(f)
        for _ in range(3):
            next(csvr)
        d = {}
        for line in csvr:
            print(line)
            eng, kan, meaning, example = line[0], line[1], line[2], line[3]
            example = example.split("|")
            meaning = meaning.split("|")
            if "," in eng:
                for en in eng.split(","):
                    d[en] = {"kan": kan, "meaning": meaning, "example": example}
            else:
                d[eng] = {"kan": kan, "meaning": meaning, "example": example}
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("infile", help="Input file")
    args.add_argument("outfile", help="Output file")
    args = args.parse_args()
    main(args.infile, args.outfile)
