from service.data_service import DataService
from service.plot_service import PlotService
from service.reports_service import ReportsService
from sklearn.linear_model import LinearRegression


class Runner:

    def __init__(self):
        self.learning_rate = 0.0001

    def run(self):

        data = DataService.load_csv("data/blood_pressure_cengage.csv")
        feature_data = data[:, :-1]
        labels = data[:, -1].reshape(feature_data.shape[0], 1)

        lin_reg = LinearRegression()
        lin_reg_model = lin_reg.fit(feature_data, labels)
        predictions = lin_reg_model.predict(feature_data)

        ReportsService.print_results_table(data, predictions, labels)

        PlotService.plot3d_scatter_compare(feature_data, labels, predictions,
                                           labels=['Age', 'Weight', 'BP'],
                                           title="Actual vs Projected LinearRegressor")


if __name__ == "__main__":

    Runner().run()
