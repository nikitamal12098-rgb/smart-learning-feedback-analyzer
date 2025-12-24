import os
from main import analyze_feedback

def test_full_pipeline():
    result = analyze_feedback("data/sample.csv")

    assert "results" in result
    assert "topics" in result
    assert "report" in result

    assert len(result["results"]) > 0
    assert isinstance(result["topics"], list)
    assert "Feedback Report" in result["report"]