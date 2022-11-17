from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import read_pickle
from os.path import join, dirname, realpath

dir_path = dirname(realpath(__file__))
tone_model = read_pickle(join(dir_path, "models/tone_model.pkl"))
score_model = read_pickle(join(dir_path, "models/score_model.pkl"))
vocab = read_pickle(join(dir_path, "models/vect_vocab.pkl"))

print()

def predict(review):
    vectorizer = TfidfVectorizer(vocabulary=vocab)

    vectorized_review = vectorizer.fit_transform([review])
    tone_result = tone_model.predict(vectorized_review)
    score_result = score_model.predict(vectorized_review)

    tone_classification = str(tone_result[0])
    score_classification = str(score_result[0])

    return {
        'tone': tone_classification,
        "score": score_classification,
        "review": review
    }
