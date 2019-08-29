from Detection import RuleBaseDetection


class Testing01:
    def __init__(self):
        # requirement sentence is None
        requirement_sentence = []
        rule_base = RuleBaseDetection(requirement_sentence)
        rule_base.set_rule('rule.xml')
        rule_base.start_detection()


class Testing02:
    def __init__(self):
        requirement_sentence = [[1, "RAC-01", "Sistem harus dapat menampilkan beberapa gambar pengguna pada layar Home", "-", "-", "-"]]
        rule_base = RuleBaseDetection(requirement_sentence)
        # rule.xml is None
        rule_base.set_rule('rule_base_testing_02.xml')
        rule_base.start_detection()


class Testing03:
    def __init__(self):
        requirement_sentence = [[1, "RAC-01", "Sistem harus dapat menampilkan beberapa gambar pengguna pada layar Home", "-", "-", "-"]]
        rule_base = RuleBaseDetection(requirement_sentence)
        rule_base.set_rule('rule.xml')
        rule_base.start_detection()


class Testing04:
    def __init__(self):
        requirement_sentence = [[1, "RAC-01", "Sistem harus dapat mengonversi suhu dari Celsius ke Fahrenheit", "-", "-", "-"]]
        rule_base = RuleBaseDetection(requirement_sentence)
        rule_base.set_rule('rule.xml')
        rule_base.start_detection()


if __name__ == '__main__':
    Testing01()
    # Testing02()
    # Testing03()
    # Testing04()