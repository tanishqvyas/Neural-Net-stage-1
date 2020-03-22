import csv
import os
import pandas as pd



class FileHandler:

	# Encoding
	encoding = "ISO-8859-1"

	# Function to get number of rows in the csv files
	def row_count(self, path):

		num_rows = 0

		for row in open(path,"rb"):
		    num_rows += 1

		return num_rows

	# Function to get the tweets and respective labels for taken dataset
	def extract_tweets_and_labels(self, path):

		# the columns that we need
		col_list = ["Label", "Tweets"]

		# Reading the csv
		df = pd.read_csv(path, encoding = self.encoding)

		# Giving column headers since current csv doesn't have any
		df.columns = ["Label", "Random","Timestamp","Topic","Id","Tweets"]
		
		# Extracting columns
		df1 = df[col_list]

		return df1

# var = FileHandler()
# print(var.extract_tweets_and_labels("test.csv"))