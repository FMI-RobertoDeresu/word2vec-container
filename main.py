from flask import Flask, request, jsonify
import gensim
import nltk
import time

app = Flask(__name__)
app.debug = False

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')


@app.route("/")
def hello():
    return "This is a word2vec container. Call method word-vec (POST) to get words embeddings. " \
           "Request body: { 'texts': ['Romania Bucharest'], 'useNorm': false }."


@app.route("/word-vec", methods=["POST"])
def word_vec():
    start_time = time.time()

    output = []
    content = request.json

    for text in content["texts"]:
        words = tokenizer.tokenize(text)
        words_embeddings = []

        for word in words:
            if word in word_vec_model.vocab:
                word_embedding = word_vec_model.word_vec(word, content["useNorm"])
                words_embeddings.append([x.item() for x in word_embedding])
            else:
                words_embeddings.append([])

        output.append(words_embeddings)

    end_time = time.time()
    print("Request processed! Elapsed:" + str(end_time - start_time))

    return jsonify(output)


if __name__ == '__main__':
    # Load word2vec model
    print("Loading model...")
    start_time_model = time.time()

    word_vec_model_path = './models/GoogleNews-vectors-negative300.bin'
    word_vec_model = gensim.models.KeyedVectors.load_word2vec_format(word_vec_model_path, binary=True)

    end_time_model = time.time()
    print("Model loaded! Elapsed: " + str(end_time_model - start_time_model))

    # Run app
    print("Running app...")
    app.run(port=8001, use_reloader=False)
