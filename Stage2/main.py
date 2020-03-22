from handler import FileHandler
import os

# Making an object for our Filehandler class
var = FileHandler()

# File paths
train_file_path = os.path.join("data","testtraindata","train.csv")
test_file_path = os.path.join("data","testtraindata","test.csv")


# Printing the number of rows in testing and training data
print("Number of rows for Datasets :\n")
print("Training dataset : ", var.row_count(train_file_path))
print("Testing dataset : ", var.row_count(test_file_path))
print("Label Encoding -> ", "0 : Negative,  2 : Neutral,  4 : Positive")

# Printing the Dataframe
print("\nDataframe (train) : \n\n", var.extract_tweets_and_labels(train_file_path) )
print("\nDataframe (test) : \n\n", var.extract_tweets_and_labels(test_file_path))
