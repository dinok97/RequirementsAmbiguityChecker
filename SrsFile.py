class SrsFile:

    file_name = ''
    correction_time = ''
    normal_req = 0
    ambiguous_req = 0
    total_req = 0
    detection_result = []

    # constractor method
    def __init__(self, file_name, correction_time, detection_result):

        self.file_name = file_name
        self.correction_time = correction_time
        self.set_detection_result(detection_result)

    # Setter method
    def set_file_name(self, fn):
        self.file_name = fn

    def set_correction_time(self, ct):
        self.correction_time = ct

    # method to set and adjust data structure of detection_result variable
    def set_detection_result(self, data):
        self.detection_result.clear()

        for i in range(len(data)):
            temp_data = []
            id_req = data[i][0]
            req_sentences = data[i][1]

            temp_data.append(i+1)
            temp_data.append(id_req)
            temp_data.append(req_sentences)
            temp_data.append("-")
            temp_data.append("-")
            temp_data.append("-")

            self.detection_result.append(temp_data)

    # Update method
    # this method used to update element in detection_result variable
    #def update_detection_result(self, index_1, index_2, data):
    #    self.detection_result[index_1][index_2] = data

    def update_detection_result(self, det_result):
        self.detection_result = det_result

    # Getter method
    def get_file_name(self):
        return self.file_name

    def get_correction_time(self):
        return self.correction_time

    # return number of normal system-requirements
    def get_normal_req(self):
        number = 0
        for i in range(len(self.detection_result)):
            if self.detection_result[i][3] == "-":
                number += 1
        self.normal_req = number
        return self.normal_req

    # return number of ambiguous system-requirements
    def get_ambiguous_req(self):
        number = 0
        for i in range(len(self.detection_result)):
            if self.detection_result[i][3] != "-":
                number += 1
        self.ambiguous_req = number
        return self.ambiguous_req

    # return number of total system-requirements
    def get_total_req(self):
        self.total_req = len(self.detection_result)
        return self.total_req

    def get_detection_result(self, index=None):
        if index is None:
            return self.detection_result
        else:
            return self.detection_result[index-1]

    def get_requirement_list(self):
        return self.detection_result