from src.main import analyze_feedback


def test_analyze_feedback_returns_dict():
    result = analyze_feedback("data/sample.csv")
    assert isinstance(result, dict)


def test_analyze_feedback_contains_expected_keys():
    result = analyze_feedback("data/sample.csv")
    assert "positive" in result
    assert "negative" in result


def test_analyze_feedback_counts_correctly():
    result = analyze_feedback("data/sample.csv")
    assert result["positive"] == 2
    assert result["negative"] == 1
    assert result["neutral"] == 1
