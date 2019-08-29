import xml.etree.cElementTree as ET


class Rule:

    tree = ET
    root = ''

    def __init__(self, rule_directory):

        self.tree = ET.parse(rule_directory)
        self.root = self.tree.getroot()

        # print(self.data)
        # print(self.get_rule(1))
        # print(self.get_suggestions_by_rule_name("beberapa"))
        # print(self.get_string_suggestions_by_rule_name("beberapa"))
        # print(self.get_all_rule())
        # print("\n")
        # self.get_all_rule()
        # print(self.get_preface_by_rule_name("beberapa"))

    # get all rule in list data type
    def get_all_rule(self):
        rule_list = []
        m_rule_list = [rule.attrib for rule in self.root.findall(".rule")]

        # loop to change data type from dict to array
        for i in range(len(m_rule_list)):
            temp = m_rule_list[i]
            m_rule = temp["name"]
            rule_list.append(m_rule)

        # return rule list
        return rule_list

    # get rule by rule_id
    def get_rule_by_id(self, rule_id):
        var = {}
        for rule in self.root.findall(".rule[@id='%s']" % rule_id):
            var = rule.attrib

        # return the rule
        return var["name"]

    # get rule by rule_id
    def get_rule_by_name(self, rule_name):
        var = {}
        for rule in self.root.findall(".rule[@name='%s']" % rule_name):
            var = rule.attrib

        # return the rule
        return var["name"]

    def get_preface_by_rule_id(self, rule_id):
        string_preface = " "
        for preface in self.root.findall(".rule[@id='%s']/preface" % rule_id):
            string_preface = preface.text
        return string_preface

    def get_preface_by_rule_name(self, rule_name):
        string_preface = " "
        for preface in self.root.findall(".rule[@name='%s']/preface" % rule_name):
            string_preface = preface.text
        return string_preface

    # get recommendation by rule_id
    def get_recommendations_by_rule_id(self, rule_id):
        # return list of recommendations
        return [recommendations.text for recommendations in self.root.findall(".rule[@id='%s']/suggestions/suggestion" % rule_id)]

    # get recommendations by rule_name
    def get_recommendations_by_rule_name(self, rule_name):
        # return list of recommendations
        return [recommendations.text for recommendations in self.root.findall(".rule[@name='%s']/suggestions/suggestion" % rule_name)]

    def get_string_recommendations_by_rule_id(self, rule_id):
        list_recommendations = self.get_recommendations_by_rule_id(rule_id)
        string_recommendations = ", ".join(list_recommendations)
        return string_recommendations

    def get_string_recommendations_by_rule_name(self, rule_name):
        list_recommendations = self.get_recommendations_by_rule_name(rule_name)
        string_recommendations = ", ".join(list_recommendations)
        return string_recommendations


