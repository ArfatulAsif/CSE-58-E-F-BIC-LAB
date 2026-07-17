# **Bioinformatics Lab Guide: Motif Finding Algorithms**



## **1. Brute-Force Motif Search (Combination Search)**

**Problem Statement:**
Given an integer $k$ and a set of $t$ DNA sequences (each of length $n$), find a set of $k$-mers (exactly one from each sequence) that minimizes the overall consensus score. The score is calculated by determining the most frequent nucleotide in each column of the resulting motif matrix and summing the number of mismatches across all columns. This algorithm brute-forces all $(n - k + 1)^t$ possible combinations of starting indices.

**Expected Terminal Input:**

> 3
> ATGCGA TTCAGT CGATAC GGAATC

**Expected Terminal Output:**

> ATG TTC ATA ATC


---




## **2. Median String Algorithm**

**Problem Statement:**
Given an integer $k$ and a collection of space-separated DNA strings, find a $k$-mer (the "Median String") that minimizes the total Hamming distance between the $k$-mer and the collection of strings. The distance to a single string is the minimum mismatch count to any window within that string, and the total distance is the sum of these minimums across all strings.

**Expected Terminal Input:**

> 3
> AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG

**Expected Terminal Output:**

> AAT


**Solution Code**

```python
def generate_k_mers(k):
        if k == 1:
                return ['A', 'C', 'G', 'T']
        smaller_k_mers = generate_k_mers(k-1)
        kmers = []
        for kmer in smaller_k_mers:
                for nucle  in ['A', 'C', 'G', 'T']:
                        kmers.append(kmer + nucle)

        return kmers


def generate_3_mer():
        kmers = []

        for i in ['A', 'C', 'G', 'T']:
                for j in ['A', 'C', 'G', 'T']:
                        for k in ['A', 'C', 'G', 'T']:
                                kmers.append(i+j+k)
        return kmers


def hamming_distance(a, b):
        Distance=0
        for i in range(len(b)):
                if a[i] != b[i]:
                        Distance+=1
        return Distance


def distance(kmer, dna):
        k = len(kmer)
        total_distance = 0
        for seq in dna:
                min_dist = 99999999
                
                for i in range(len(seq) - k+1):
                        window = seq[i:i+k]
                        dist = hamming_distance(seq, kmer)

                        if dist < min_dist:
                                min_dist = dist
                total_distance += min_dist
        
        return total_distance
                        
        


def median_string(k, dna):
        all_kmers = generate_k_mers(k)
        min_total_distance = 99999999999
        best_median = ""

        for kmer in all_kmers:
                current_dis = distance(kmer, dna)

                if current_dis < min_total_distance:
                        min_total_distance = current_dis
                        best_median = kmer
        
        return best_median



if __name__ == "__main__":

        k = int(input().strip())

        dna = input().split()


        result = median_string(k, dna)

        print(result)

```

---








## **3. Consensus String Finding from $n$ Motifs of Length $k$**

**Problem Statement:**
Given a list of space-separated, aligned motifs (where all strings are of equal length $k$), construct a count matrix to determine the most frequent nucleotide at each column position. Output the resulting consensus string. Ties are broken by alphabetical order (A, C, G, T).

**Expected Terminal Input:**

> ATGCGA TTCAGT CGATAC GGAATC

**Expected Terminal Output:**

> AGAAGC



**Answer Code:**

```python

def consensust_string(Input):
        if len(Input) == 0:
                return ""
        
        t = len(Input)
        k = len(Input[0])

        ans = ""

        for i in range(k):
                counts = {'A' : 0, 'C': 0, 'G': 0, 'T': 0}

                for motif in Input:
                        nucle = motif[i]
                        if nucle == 'A' : 
                                counts['A'] += 1
                        elif nucle == 'C':
                                counts['C'] += 1
                        elif nucle == 'G':
                                counts['G'] += 1
                        elif nucle == 'T':
                                counts['T'] += 1
                
                mx_cnt = -1
                best_nucle = ""

                for nuc in ['A', 'C', 'G', 'T']:
                        if counts[nuc] > mx_cnt:
                                mx_cnt = counts[nuc]
                                best_nucle = nuc 
                
                ans += best_nucle
        
        return ans



if __name__ == "__main__":

        motifs = input().split()

        resuts = consensust_string(motifs)

        print(resuts)

```
