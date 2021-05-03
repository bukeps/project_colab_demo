import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/monday.csv")
print(df.shape)


def explore():
    """Main function for analysis"""
    return "Awesome Analysis!"


if __name__ == "__main__":
    print(explore())
