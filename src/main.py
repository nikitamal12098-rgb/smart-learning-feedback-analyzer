import pandas as pd

from analyzer.language import detect_language
from analyzer.sentiment import analyze_sentiment
from analyzer.topics import extract_topics
from report.generator import generate_report
from pathlib import Path



def analyze_feedback(csv_path: str) -> dict:
    df = pd.read_csv(csv_path)

    if "text" not in df.columns:
        raise ValueError("CSV must contain 'text' column")

    results = []
    texts = df["text"].astype(str).tolist()

    for text in texts:
        result = {
            "text": text,
            "language": detect_language(text),
            "sentiment": analyze_sentiment(text),
        }
        results.append(result)

    topics = extract_topics(texts)
    report = generate_report(results)

    docs_path = Path("docs")
    docs_path.mkdir(exist_ok=True)

    report_path = docs_path / "report.md"
    report_path.write_text(report, encoding="utf-8")

    return {
        "results": results,
        "topics": topics,
        "report": report,
        "report_path": str(report_path),
    }


if __name__ == "__main__":
    output = analyze_feedback("data/sample.csv")
    print(f"Report generated at: {output['report_path']}")

