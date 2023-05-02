import torch
import pandas as pd
import sys

def main(file_name):
    pred = pd.read_csv(file_name)
    pred_tensor = torch.tensor(pred.values)

    pred_argmax = pred_tensor.argmax(dim=1)

    unique, count = pred_argmax.unique(return_counts=True)

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

    