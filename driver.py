import pandas as pd
import numpy as np
import utils

# Removing the garbage data of missing values
def clean(data):
	data.replace("missing", np.nan, inplace=True)
	data.replace("na", np.nan, inplace=True)
	data.iloc[:, 1:-2] = data.iloc[:, 1:-2].astype(float)


data = pd.read_csv("train_full.csv")
dataLeader = pd.read_csv("leaderboard_full.csv")

clean(data)
clean(dataLeader)

meanValues = data.iloc[:, 1:47].mean()

data = data.fillna(meanValues)
dataLeader = dataLeader.fillna(meanValues)

data.to_csv("train_filled.csv", index=False)
dataLeader.to_csv("leaderboard_filled.csv", index=False)
