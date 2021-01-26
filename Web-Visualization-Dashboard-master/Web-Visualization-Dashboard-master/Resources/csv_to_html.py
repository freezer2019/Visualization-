import pandas as pd

pd.read_csv('cities.csv').to_html('table.html',classes='table table-striped thead-dark bordered')