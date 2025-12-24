from typing import Dict

import pandas as pd


def analyze_feedback(file_path: str) -> Dict[str, int]:
    """
    Analyze student feedback data from a CSV file.

    Expected CSV format:
    - text: feedback text
    - sentiment: sentiment label (positive, neutral, negative)

    Returns a dictionary with sentiment counts.
    """
    df = pd.read_csv(file_path)

    if "sentiment" not in df.columns:
        raise ValueError("CSV file must contain a 'sentiment' column")

    sentiment_counts = df["sentiment"].value_counts().to_dict()
    return sentiment_counts
