from Detection import RuleBaseDetection
from Detection import StatisticalBaseRecommendation


class Testing01:
    def __init__(self):
        # detection data is None
        detection_data = []
        statistical_base = StatisticalBaseRecommendation(detection_data)
        statistical_base.set_corpus('start_recommendation_corpus.txt')
        statistical_base.start_recommendation()


class Testing02:
    def __init__(self):
        detection_data = [[1, "RAC - 01", "Sistem harus dapat mengonversi suhu dari Celsius ke Fahrenheit", "-", "-", "-"]]
        statistical_base = StatisticalBaseRecommendation(detection_data)
        statistical_base.set_corpus('start_recommendation_corpus.txt')
        statistical_base.start_recommendation()


class Testing03:
    def __init__(self):
        detection_data = [[1, "RAC - 01", "Pada halaman peringkat, sistem dapat menampilkan sepuluh nama siswa dengan nilai tinggi", "ambigu", "tinggi", "-"]]
        statistical_base = StatisticalBaseRecommendation(detection_data)
        statistical_base.set_corpus('start_recommendation_corpus.txt')
        statistical_base.start_recommendation()


class Testing04:
    def __init__(self):
        detection_data = [[1, "RAC - 01", "Pada halaman evaluasi, sistem dapat menampilkan sepuluh nama siswa dengan nilai rendah", "ambigu", "rendah", "-"]]
        statistical_base = StatisticalBaseRecommendation(detection_data)
        statistical_base.set_corpus('start_recommendation_corpus.txt')
        statistical_base.start_recommendation()


class Testing05:
    def __init__(self):
        detection_data = [[1, "RAC - 01", "Pada halaman peringkat, sistem dapat menampilkan sepuluh nama siswa dengan nilai tinggi", "ambigu", "tinggi2", "-"]]
        statistical_base = StatisticalBaseRecommendation(detection_data)
        statistical_base.set_corpus('start_recommendation_corpus.txt')
        statistical_base.start_recommendation()


class Testing06:
    def __init__(self):
        detection_data = [[1, "RAC - 01", "Pada halaman evaluasi, sistem dapat menampilkan sepuluh nama siswa dengan nilai rendah", "ambigu", "rendah2", "-"]]
        statistical_base = StatisticalBaseRecommendation(detection_data)
        statistical_base.set_corpus('start_recommendation_corpus.txt')
        statistical_base.start_recommendation()


if __name__ == '__main__':
    Testing01()
    # Testing02()
    # Testing03()
    # Testing04()
    # Testing05()
    # Testing06()