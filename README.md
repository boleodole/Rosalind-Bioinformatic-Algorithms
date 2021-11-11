# BioInfoAlgos

This repository contains Rosalind problems which i have solved in Python, including the mid-steps for the final solution. It also follows the book Bioinformatics Algorithms by Pavel Pevzner & Phillip Compeau. <br />
Every individual python file does some form of processing of the genome sequence, and gives back an output.

List of python files with description:

-DNAtoRNA.py - Takes a DNA string input and returns a RNA string output <br />
-RevComp.py - Takes a DNA string input and returns the reverse complement DNA string <br />
-pattern_match_indexing.py - Takes a DNA pattern and DNA sequence input, returns the indexes of the patterns inside the sequence <br />
-pattern_search.py - Takes a pattern input and tries to find it in a string input. Outputs how many times said string containts the pattern. <br />
-frequencymap.py - Takes a DNA sequence and a k-mer as input, returns a dictionary with the k-mer:frequency relation <br />
-FrequentWords.py - First part finds frequent k-mers in a string input, and the second part maps their frequency <br />
-ClumpFind.py - Slides a 'window' of a certain length (L) trough the DNA sequence input (Text) and tries to find certain k-mers (k), and finally outputs the k-mers if they appear (t) or more times. <br />
-hamming_distance.py - This function matches 2 strings of the same length and searches for mismatches. If there are more mismatches than imposed, then the string is filtered. <br />
-app_pattern_match.py - Takes a k-mer (DNA pattern) and a DNA sequence input and tries to find the k-mer frequency within the sequence with a limited number of mismatches. <br />
-skewdiagram.py - 
