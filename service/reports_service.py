import numpy as np


class ReportsService:

    def __init__(self):
        pass

    @staticmethod
    def print_results_table(data, predictions, labels):

        print("|Age|Weight|Actual Blood Pressure|Predicted Blood Pressure|Loss|")
        print("|:-------:|:---:|:--------------------:|:---------------------:|:-------:|")

        train_records = data[:, :-1]
        predicted_labels = []
        loss_list = []
        for record_index, prediction in enumerate(predictions):
            age = train_records[record_index, 0]
            weight = train_records[record_index, 1]
            label = labels[record_index][0]
            predicted_label = np.rint(prediction[0])
            predicted_labels.append(predicted_label)
            loss = np.abs(label - predicted_label)
            loss_list.append(loss)

            print("|{0}|{1}|{2}|{3}|{4}|".format(age, weight, label, predicted_label, loss))

        print("Mean Absolute Loss: ", np.round(np.mean(loss_list), 2))