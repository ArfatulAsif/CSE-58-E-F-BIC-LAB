
# BIC Rosalind Chapter 1 problems:



## Problem 1: Compute the Number of Times a Pattern Appears in a Text

**Statements:** A $k$-mer is a string of length $k$. We define $Count(Text, Pattern)$ as the number of times that a $k$-mer $Pattern$ appears as a substring of $Text$. For example, $Count(\text{ACAACTATGCATACTATCGGGAACTATCCT}, \text{ACTAT}) = 3$. We note that $Count(\text{CGATATATCCATAG}, \text{ATA})$ is equal to 3 (not 2) since we should account for overlapping occurrences of $Pattern$ in $Text$.




**Given:** DNA strings $Text$ and $Pattern$.

**Return:** $Count(Text, Pattern)$.

**Example Input:**

```text
GCGCG
GCG

```

**Example output:**

```text
2

```

---

## Problem 2: Find the Most Frequent Words in a String

**Statements:** We say that $Pattern$ is a most frequent $k$-mer in $Text$ if it maximizes $Count(Text, Pattern)$ among all $k$-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

**Frequent Words Problem:** Find the most frequent $k$-mers in a string.

**Given:** A DNA string $Text$ and an integer $k$.

**Return:** All most frequent $k$-mers in $Text$ (in any order).

**Example Input:**

```text
ACGTTGCATGTCGCATGATGCATGAGAGCT
4

```

**Example output:**

```text
CATG GCAT

```

---

## Problem 3: Find the Reverse Complement of a String

**Statements:** In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide $p$, we denote its complementary nucleotide as $p'$. The reverse complement of a DNA string $Pattern = p_1 \dots p_n$ is the string $Pattern' = p'_n \dots p'_1$ formed by taking the complement of each nucleotide in $Pattern$, then reversing the resulting string.

For example, the reverse complement of $Pattern = \text{GTCA}$ is $Pattern' = \text{TGAC}$.

**Reverse Complement Problem:** Find the reverse complement of a DNA string.

**Given:** A DNA string $Pattern$.

**Return:** $Pattern'$, the reverse complement of $Pattern$.

**Example Input:**

```text
AAAACCCGGT

```

**Example output:**

```text
ACCGGGTTTT

```

---

## Problem 4: Find All Occurrences of a Pattern in a String

**Statements:** In this problem, we ask a simple question: how many times can one string occur as a substring of another? Recall from “Find the Most Frequent Words in a String” that different occurrences of a substring can overlap with each other. For example, $\text{ATA}$ occurs three times in $\text{CGATATATCCATAG}$.

**Pattern Matching Problem:** Find all occurrences of a pattern in a string.

**Given:** Strings $Pattern$ and $Genome$.

**Return:** All starting positions in $Genome$ where $Pattern$ appears as a substring. Use 0-based indexing.

**Example Input:**

```text
ATAT
GATATATGCATATACTT

```

**Example output:**

```text
1 3 9

```
