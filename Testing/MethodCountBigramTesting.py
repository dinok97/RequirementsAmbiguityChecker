from Detection import StatisticalBaseRecommendation


class Testing01:
    def __init__(self):
        # requirement text is None
        statistical_base = StatisticalBaseRecommendation([])
        statistical_base.set_corpus('count_bigram_corpus.txt')
        statistical_base.count_bigram("")


class Testing02:
    def __init__(self):
        # requirement text is None
        statistical_base = StatisticalBaseRecommendation([])
        statistical_base.set_corpus('count_bigram_corpus.txt')
        statistical_base.count_bigram("banyak data")


class Testing03:
    def __init__(self):
        # requirement text is None
        statistical_base = StatisticalBaseRecommendation([])
        statistical_base.set_corpus('count_bigram_corpus.txt')
        statistical_base.count_bigram("banyak kata")


class Testing04:
    def __init__(self):
        # requirement text is None
        statistical_base = StatisticalBaseRecommendation([])
        statistical_base.set_corpus('count_bigram_corpus.txt')
        statistical_base.count_bigram("tepuk tangan")


if __name__ == '__main__':
    Testing01()
    # Testing02()
    # Testing03()
    # Testing04()