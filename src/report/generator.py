from collections import Counter, defaultdict
from datetime import datetime, timezone


def generate_report(results: list) -> str:
    sentiments = Counter(r["sentiment"] for r in results)
    languages = Counter(r["language"] for r in results)

    by_language = defaultdict(list)
    for r in results:
        by_language[r["language"]].append(r["sentiment"])

    report = [
        "# 📊 Smart Learning Feedback Report",
        f"_Generated on {datetime.now(timezone.utc).isoformat()}_",
        "",
        "## 🌍 Language Distribution",
    ]

    for lang, count in languages.items():
        report.append(f"- **{lang.upper()}**: {count}")

    report.append("\n## 😊 Sentiment Distribution")
    for sentiment, count in sentiments.items():
        report.append(f"- **{sentiment.capitalize()}**: {count}")

    report.append("\n## 🧩 Sentiment by Language")
    for lang, sentiments_list in by_language.items():
        counts = Counter(sentiments_list)
        report.append(f"\n### Language: {lang.upper()}")
        for sentiment, count in counts.items():
            report.append(f"- {sentiment}: {count}")

    return "\n".join(report)
