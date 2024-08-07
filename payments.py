

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls"
df = pd.read_excel(url, header=1, engine='xlrd')

# Print the result to the console
print(df.head())    

# Rename the target column for clarity
df.rename(columns={'default payment next month': 'default'}, inplace=True)


# raul0230

INSERT INTO red VALUES (1, '335095070', 'SOL123', 'PA123');
INSERT INTO res VALUES (1, 'MTG');
INSERT INTO cli VALUES ('335095070', 925, '20240600000000000000');
INSERT INTO sis VALUES ('335095070', '20240601');
INSERT INTO sol VALUES ('SOL123');
INSERT INTO fcl VALUES ('PA123', 'MTG');
INSERT INTO ha VALUES ('APP1', '33509507024062000000000000000000000000000000000000000', 'CSL', 'SYS1');
INSERT INTO hci VALUES ('HCI1', '1', 'CSL');
