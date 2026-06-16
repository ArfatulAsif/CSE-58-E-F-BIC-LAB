from collections import defaultdict


def hamming_distance(a, b):
    mismatch = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch += 1

    return mismatch


def neighbors(pattern, d):

    if d == 0:
        return [pattern]

    if len(pattern) == 1:
        return ["A", "C", "G", "T"]

    result = []

    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:

        if hamming_distance(pattern[1:], text) < d:

            for x in "ACGT":
                result.append(x + text)

        else:
            result.append(pattern[0] + text)

    return result


def frequent_words_mismatch(text, k, d):

    frequency = defaultdict(int)

    for i in range(len(text) - k + 1):

        pattern = text[i:i + k]

        nearby = neighbors(pattern, d)

        for n in nearby:
            frequency[n] += 1

    maximum = max(frequency.values())

    answer = []

    for key in frequency:

        if frequency[key] == maximum:
            answer.append(key)

    return answer


# INPUT
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

result = frequent_words_mismatch(text, k, d)

print(*result)
