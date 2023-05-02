"""
    Authors: Jess Bunnag, Tiffany Lin, Anna Zuo
"""
import torch
import pandas as pd
import sys

def main(file_name):
    # read the probability prediction from a file
    pred = pd.read_csv(file_name)
    pred_tensor = torch.tensor(pred.values)

    # get the argmax prediction of each frame from the scores 
    pred_argmax = pred_tensor.argmax(dim=1)

    # get the prediction count frequency from all the frames
    unique, count = pred_argmax.unique(return_counts=True)

    # get the argmax prediction of each video
    max_pred = unique[count.argmax()].item()

    if max_pred == 0:
        print("NEGATIVE")
    elif max_pred == 1:
        print("NEUTRAL")
    elif max_pred == 2:
        print("POSITIVE")


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python parse_predictions.py pred.csv')
    else:
        file_name = sys.argv[1]
        main(file_name)

    