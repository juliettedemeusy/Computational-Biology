#!/usr/bin/env python3


from Bio import SeqIO
import matplotlib.pyplot as plt


def main():
    dictionnaire = {}
    list_seq = list(SeqIO.parse('salmonella-enterica.reads.fna', 'fasta'))
    k = 4
    count = 0
    for elt in list_seq:
        if count % 1000 == 0:
            print(count)
        for i in range(len(elt.seq)):
            seq_cour = elt.seq[i:i+k]
            if seq_cour in dictionnaire:
                dictionnaire[seq_cour] += 1
            else:
                dictionnaire[seq_cour] = 1
        count += 1

    plt.hist(dictionnaire.values(), bins='auto', range=(0, 100))
    plt.show()


main()
