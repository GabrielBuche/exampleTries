from flask import Flask, render_template, request
from trie import Trie

app = Flask(__name__)
trie = Trie()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        if trie.search(query):
            message = f"'{query}' foi encontrado na trie!"
        else:
            message = f"'{query}' não foi encontrado na trie."
        words = trie.starts_with(query)
        if words:
            message += f" As seguintes palavras começam com '{query}': " + ", ".join(words)
        else:
            message += f" Nenhuma palavra começa com '{query}'."
        return render_template("result.html", message=message)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    trie.insert("hello")
    trie.insert("world")
    trie.insert("he")
    app.run(debug=True)