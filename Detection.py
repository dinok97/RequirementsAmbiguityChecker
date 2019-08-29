from SrsFile import SrsFile
import nltk
from Corpus.Corpus import Corpus
from Rule.Rule import Rule


class TextProcessing:
    list_requirements_sentences = []

    def __init__(self, detection_data):
        self.list_requirements_sentences = []

        self.extract_requirements_sentence(detection_data)
        self.pre_processing(self.list_requirements_sentences)

        # print("\ndetection result before detection: ")
        # for d_result in detection_data:
            # print(d_result)

    def extract_requirements_sentence(self, detection_data):
        # loop to insert value of list_requirements_sentence
        for i in range(len(detection_data)):
            self.list_requirements_sentences.append(detection_data[i][2])

    # before start detection ambiguity, every requirements must be pre-processing
    # pre-processing in this method is to lower case all requirements sentence
    def pre_processing(self, list_requirements_sentences):
        #print("\npreprocessing:")
        for i in range(len(list_requirements_sentences)):
            self.list_requirements_sentences[i] = list_requirements_sentences[i].lower()
            #print(i+1, self.list_requirements_sentences[i])


class RuleBaseDetection(TextProcessing):

    rule = Rule
    list_rule = []
    list_detection_data = []
    list_detection_result = []

    def __init__(self, detection_data):
        TextProcessing.__init__(self, detection_data)

        self.list_detection_data = detection_data
        self.list_detection_result = []

    def set_rule(self, rule_directory):
        self.rule = Rule(rule_directory)

    def start_detection(self):
        '''print("method start_detection show message:")
        test_message = ""'''
        # get all rule
        self.list_rule = self.rule.get_all_rule()
        number_of_requirements = len(self.list_requirements_sentences)

        # detection begin
        # print("\nrule base detection process:")
        for i in range(number_of_requirements):
            req_sentences = self.list_requirements_sentences[i]
            for m_rule in self.list_rule:
                if self.is_ambiguous(m_rule, req_sentences):
                    # print("found ambiguous:", m_rule, "@", self.list_requirements_sentences[i])
                    '''test_message = "kalimat kebutuhan teridentifikasi ambigu"'''
                    self.list_detection_data[i][3] = "ambigu"
                    self.list_detection_data[i][4] = m_rule
                    self.list_detection_data[i][5] = self.rule.get_string_recommendations_by_rule_name(m_rule)
                    break
                else:
                    '''test_message = "kalimat kebutuhan teridentifikasi tidak ambigu"'''
                    self.list_detection_data[i][3] = "-"
            self.list_detection_result.append(self.list_detection_data[i])
        '''print(test_message)'''

    def get_detection_result(self):
        return self.list_detection_result

    def is_ambiguous(self, m_rule, sentences):
        words = sentences.split()
        for word in words:
            if word == m_rule:
                return True
        return False


class StatisticalBaseRecommendation(TextProcessing):

    rule = Rule
    list_rule = []
    corpus = Corpus
    corpus_data = []
    list_detection_data = []
    recommendations = []
    list_recommendation_result = []

    def __init__(self, detection_data):
        TextProcessing.__init__(self, detection_data)

        self.rule = Rule('Rule\\rule_real.xml')
        '''self.rule = Rule('rule.xml')'''
        self.list_rule = self.rule.get_all_rule()
        self.list_detection_data = detection_data
        self.list_recommendation_result = []
        # print("\ncorpus data:")
        # print(self.corpus.get_data())

    def set_corpus(self, corpus_directory):
        self.corpus = Corpus(corpus_directory)
        self.corpus_data = self.corpus.get_data()

    def start_recommendation(self):
        '''print("method start_recommendation show message:")
        test_message = ""'''
        # print("\nstart statistical recommendation:")
        for i in range(len(self.list_detection_data)):
            if self.list_detection_data[i][3] == "ambigu":
                # print(self.list_requirements_sentences[i], "= AMBIGU")
                rule_name = self.list_detection_data[i][4]
                list_recommendation = self.rule.get_recommendations_by_rule_name(rule_name)
                preface = self.rule.get_preface_by_rule_name(rule_name)

                if len(list_recommendation) > 1:
                    candidates = self.populate_req_sentences(i, list_recommendation)
                    self.recommendations = []
                    self.recommendations = self.get_probability(candidates, list_recommendation)
                    # print("Sebelum urut:\n", self.recommendations)
                    self.sort_recommendations()
                    # print("Sesudah urut:\n", self.recommendations)
                    # print("Buat String:\n", self.produce_string_sorted_recommendations(self.recommendations))
                    string_recommendation = self.produce_string_sorted_recommendations(self.recommendations)
                    if preface == "-":
                        string_recommendation = self.produce_string_sorted_recommendations(self.recommendations)
                        '''test_message = "rekomendasi perbaikan berhasil diberikan.\nkalimat kebutuhan memiliki beberapa rekomendasi perbaikan yang sudah diurutkan dan tidak memiliki preface"'''
                    else:
                        string_recommendation = ("%s: %s" % (preface, string_recommendation))
                        '''test_message = "rekomendasi perbaikan berhasil diberikan.\nkalimat kebutuhan memiliki beberapa rekomendasi perbaikan yang sudah diurutkan dan memiliki satu preface"'''
                    self.list_detection_data[i][5] = string_recommendation

                else:
                    # print(">>>>> masuk ke else untuk:", list_recommendation[0])
                    if preface == "-":
                        string_recom = list_recommendation[0]
                        '''test_message = "rekomendasi perbaikan berhasil diberikan.\nkalimat kebutuhan hanya memiliki satu rekomendasi perbaikan dan tidak memiliki preface"'''
                    else:
                        string_recom = ("%s: %s" % (preface, list_recommendation[0]))
                        '''test_message = "rekomendasi perbaikan berhasil diberikan.\nkalimat kebutuhan hanya memiliki satu rekomendasi perbaikan dan memiliki preface"'''
                    self.list_detection_data[i][5] = string_recom
            else:
                '''test_message = "kalimat kebutuhan tidak ambigu. Tidak perlu diberikan rekomendasi perbaikan"'''
                # print(self.list_requirements_sentences[i], "= TIDAK AMBIGU")
            self.list_recommendation_result.append(self.list_detection_data[i])
        '''print(test_message)'''

    def populate_req_sentences(self, index, list_recommendation):
        list_req_sentences_candidate = []
        for i in range(len(list_recommendation)):
            ambiguous_word = self.list_detection_data[index][4]
            temp = self.list_requirements_sentences[index].replace(ambiguous_word, list_recommendation[i])
            list_req_sentences_candidate.append(temp)
            # print(temp)

        return list_req_sentences_candidate

    def count_bigram(self, text):
        '''print("method count_bigram show message:")
        test_message = "tidak ada teks yang akan dihitung peluang bigramnya"'''

        pw = []
        tokens = nltk.word_tokenize(text)
        bigram = nltk.bigrams(tokens)
        #print(tokens)

        for words in bigram:

            w_1 = 0
            w_1_2 = 0
            pw_temp = 0
            #print(words)

            w_1_2 = self.count_prior(words)
            w_1 = self.corpus_data.count(words[0])
            # print(w_1_2, w_1, len(tokens))

            if (w_1 != 0) & (w_1_2 != 0):
                pw_temp = w_1_2 / w_1
                '''test_message = "peluang bigram berhasil dihitung"'''
            else:
                pw_temp = self.add_one_laplapre(w_1, w_1_2, len(tokens))
                '''if w_1 == 0:
                    test_message = "kata ke 1 tidak pernah muncul dalam korpus sehingga bigram dihitung dengan add one laplace"
                    if w_1_2 == 0:
                        test_message = "kata ke 1 diikuti kata ke 2 tidak pernah muncul dalam korpus sehingga bigram dihitung dengan add one laplace"'''

            # print("PW TEMP", pw_temp)
            pw.append(pw_temp)

        bigram_result = self.total_bigram(pw)
        # print(bigram_result)
        '''print(test_message)'''
        return bigram_result

    def add_one_laplapre(self, w_1, w_1_2, v):
        # laplace formula:
        # (count(w_1_2) + 1) / (count(w_1) + v)
        laplapce = (w_1_2 + 1) / (w_1 + v)

        return laplapce

    def sort_recommendations(self):
        for i in range(len(self.recommendations)):
            index = i
            for j in range(i+1, len(self.recommendations)):
                if self.recommendations[index][0] < self.recommendations[j][0]:
                    index = j
            temp = self.recommendations[index]
            self.recommendations[index] = self.recommendations[i]
            self.recommendations[i] = temp

    def get_probability(self, candidates, list_recommendation):
        recommendations = []
        for j in range(len(candidates)):
            temp = []
            # buat satu tipe data baru dengan isi [rekomendasi, hasil]
            text = candidates[j]
            bigram = self.count_bigram(text)
            temp.append(bigram)
            temp.append(list_recommendation[j])
            recommendations.append(temp)
        return recommendations

    def count_prior(self, words):
        w_1_2 = 0
        for i in range(0, len(self.corpus_data)):
            if i == len(self.corpus_data) - 1:
                break
            else:
                if self.corpus_data[i].lower() == words[1].lower() and self.corpus_data[i - 1].lower() == words[0].lower():
                    w_1_2 += 1
        return w_1_2

    def total_bigram(self, pw):
        bigram_result = 1
        for k in range(len(pw)):
            bigram_result = bigram_result * pw[k]
        return bigram_result

    def produce_string_sorted_recommendations(self, list_recommendations):
        temp = []
        for i in range(len(list_recommendations)):
            temp.append(list_recommendations[i][1])
        string_recom = ", ".join(temp)
        return string_recom

    def get_recommendation_result(self):
        return self.list_recommendation_result










'''data_s = [['RAC-01', 'Sistem harus dapat menampilkan beberapa gambar pengguna pada layar Home'],
          ['RAC-02', 'Sistem harus dapat menghitung banyak data'],
          ['RAC-03', 'Sistem menghitung data dengan menggunakan rumus statistik'],
          ['RAC-04', 'Sistem menghitung data dengan cepat']
          ]
file = SrsFile("Ini file", "Kamis", data_s)
# bb = file.get_detection_result(2)
det_data = file.get_detection_result()
rule_base = RuleBaseDetection(det_data)
rule_base.set_rule('rule.xml')
rule_base.start_detection()

rule_base_result = rule_base.get_detection_result()

print("\nfinal detection result:")
for result in rule_base.get_detection_result():
    print(result)

statistical_base = StatisticalBaseRecommendation(rule_base_result)
statistical_base.set_corpus('Corpus\\leipzig.txt')
statistical_base.start_recommendation()

print("\nfinal detection result - statistic:")
for result in statistical_base.get_recommendation_result():
    print(result)

print("\nbefore detection result - srs_file:")
for ii in file.get_detection_result():
    print(ii)

file.update_detection_result(statistical_base.get_recommendation_result())
print("\nfinal detection result - srs_file:")
for ii in file.get_detection_result():
    print(ii)'''

'''keyword_list = ['motorcycle', 'bike', 'cycle', 'dirtbike']
all_text = input("what kind of bike do you like?")
for item in keyword_list:
    if item in all_text:
        print('found one of em', item)
        break'''