from sklearn.feature_extraction.text import TfidfVectorizer


def extract_topics(texts, top_k=5):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(texts)
    scores = tfidf.sum(axis=0).A1
    terms = vectorizer.get_feature_names_out()

    ranked = sorted(zip(terms, scores), key=lambda x: x[1], reverse=True)
    return [term for term, _ in ranked[:top_k]]
