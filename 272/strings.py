from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length first, then alaphbetic.
    """
    # Convert to lowercase
    sentence1_set = set([word.lower() for word in sentence1])
    sentence2_set = set([word.lower() for word in sentence2])

    # Sorted list of intersection of two sets
    common = list(sentence1_set.intersection(sentence2_set))
    common.sort(key=lambda item: (len(item), item))

    return common
