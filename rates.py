import csv


class Rates:
    def __init__(self):
        """
        Reads the currency conversion rate spreadsheet and builds the data
        structures necessary to get the conversion rate of different currencies
        at different times
        """
        self.currency_to_series_id = {}
        self.series = {}
        with open("FX_RATES_MONTHLY-sd-2017-01-01.csv") as csvfile:
            csv_contents = list(csv.reader(csvfile))
            line_idx = 0
            while line_idx < len(csv_contents):
                line = csv_contents[line_idx]
                # Parse the contents under the SERIES header
                if len(line) > 0 and line[0] == "SERIES":
                    # Start at the first row of the SERIES data
                    line_idx = line_idx + 2
                    line = csv_contents[line_idx]
                    while len(line) > 0:
                        id = line[0]
                        label = line[1]
                        description = line[2]
                        self.series[id] = {
                            "label": label,
                            "description": description,
                        }
                        currency = label.split("/")[0]
                        self.currency_to_series_id[currency] = id
                        line_idx = line_idx + 1
                        line = csv_contents[line_idx]
                    # Once we are done parsing the SERIES data, continue parsing
                    # the rest of the CSV
                    continue
                # Unimportant line, continue parsing the CSV
                line_idx = line_idx + 1