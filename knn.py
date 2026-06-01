import os
import urllib.request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
import matplotlib.pyplot as plt
import seaborn as sns

# Download dataset automatically if not found
if not os.path.exists("magic04.data"):
    print("Downloading MAGIC Gamma Telescope dataset...")
    urllib.request.urlretrieve(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data",
        "magic04.data"
    )
    print("Dataset downloaded successfully.")

file_path = "magic04.data"

# Load dataset
df = pd.read_csv(file_path, header=None)