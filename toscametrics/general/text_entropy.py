import re
from math import log2

from toscametrics import utils
from toscametrics.blueprint_metric import BlueprintMetric


class TextEntropy(BlueprintMetric):
    """ This class measures the blueprint's Shannon entropy for keywords frequencies """

    def count(self):
        words_list = utils.all_keys(self.blueprint)
        words_list.extend(utils.all_values(self.blueprint))

        splitter = lambda x: re.sub(r'\s+', ' ', str(x)).split(' ')
        words_list = [item for sublist in list(map(splitter, words_list)) for item in sublist]

        words_set = set(words_list)

        freq = {w: words_list.count(w) for w in words_set}

        entropy = 0
        for word in words_set:
            p = freq[word] / len(words_list)
            entropy -= p * log2(p)

        return round(entropy, 2)
