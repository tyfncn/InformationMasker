"""More Helper Classes"""


class SimpleStatistics:
    """
    Very simple statistics module.
    Can be used to calculate stats while reading one by one.
    """
    def __init__(self, columns):
        self.columns = {}
        for key in columns:
            self.columns[key] = {
                "min": 2**32,   # biggest possible 64 bit integer
                "max": -2**32,  # smallest possible 64 bit integer
                "sum": 0,
                "count": 0
            }

    def process(self, column, value):
        if type(value) == str:
            return
        self.columns[column]["min"] = min(self.columns[column]["min"], value)
        self.columns[column]["max"] = max(self.columns[column]["max"], value)
        self.columns[column]["sum"] += value
        self.columns[column]["count"] += 1

    def get_average(self, column):
        if self.columns[column]["count"] == 0:
            return nan
        return self.columns[column]["sum"] / self.columns[column]["count"]

    def column_info(self, column):
        return "Min:{:0.2f} Max:{:0.2f} Avg:{:0.2f} Count:{}".format(
            self.columns[column]["min"],
            self.columns[column]["max"],
            self.get_average(column),
            self.columns[column]["count"]
        )
