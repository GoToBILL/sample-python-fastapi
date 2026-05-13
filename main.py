"""Random Quotes API - AppPaaS Pivot sample service."""
import random
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="Random Quotes API")

QUOTES = [
    {"id": 1, "text": "The only true wisdom is in knowing you know nothing.", "author": "Socrates", "tags": ["wisdom"]},
    {"id": 2, "text": "I think, therefore I am.", "author": "René Descartes", "tags": ["wisdom", "life"]},
    {"id": 3, "text": "That which does not kill us makes us stronger.", "author": "Friedrich Nietzsche", "tags": ["life", "wisdom"]},
    {"id": 4, "text": "Be the change that you wish to see in the world.", "author": "Mahatma Gandhi", "tags": ["life", "wisdom"]},
    {"id": 5, "text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein", "tags": ["life", "wisdom"]},
    {"id": 6, "text": "The unexamined life is not worth living.", "author": "Socrates", "tags": ["wisdom", "life"]},
    {"id": 7, "text": "I have not failed. I've just found 10,000 ways that won't work.", "author": "Thomas Edison", "tags": ["tech", "humor"]},
    {"id": 8, "text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds", "tags": ["tech"]},
    {"id": 9, "text": "Premature optimization is the root of all evil.", "author": "Donald Knuth", "tags": ["tech"]},
    {"id": 10, "text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler", "tags": ["tech"]},
    {"id": 11, "text": "First, solve the problem. Then, write the code.", "author": "John Johnson", "tags": ["tech"]},
    {"id": 12, "text": "I'm not arguing, I'm just explaining why I'm right.", "author": "Unknown", "tags": ["humor"]},
    {"id": 13, "text": "I'm on a seafood diet. I see food and I eat it.", "author": "Dolly Parton", "tags": ["humor"]},
    {"id": 14, "text": "The trouble with having an open mind is that people keep coming along and sticking things into it.", "author": "Terry Pratchett", "tags": ["humor", "wisdom"]},
    {"id": 15, "text": "Life is what happens when you're busy making other plans.", "author": "John Lennon", "tags": ["life"]},
    {"id": 16, "text": "The purpose of our lives is to be happy.", "author": "Dalai Lama", "tags": ["life", "wisdom"]},
    {"id": 17, "text": "Get busy living, or get busy dying.", "author": "Stephen King", "tags": ["life"]},
    {"id": 18, "text": "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.", "author": "Albert Einstein", "tags": ["humor", "wisdom"]},
]


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/quotes")
def list_quotes():
    return {"quotes": QUOTES, "count": len(QUOTES)}


@app.get("/quote")
def random_quote():
    return random.choice(QUOTES)


@app.get("/quote/{tag}")
def random_quote_by_tag(tag: str):
    pool = [q for q in QUOTES if tag.lower() in q["tags"]]
    if not pool:
        raise HTTPException(status_code=404, detail=f"No quotes for tag '{tag}'")
    return random.choice(pool)


INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Random Quotes</title>
<style>
  body { font-family: -apple-system, system-ui, sans-serif; max-width: 640px; margin: 4rem auto; padding: 0 1rem; color: #222; }
  .card { background: #f6f7f9; border-radius: 12px; padding: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,.08); }
  blockquote { font-size: 1.25rem; line-height: 1.5; margin: 0 0 1rem; }
  .author { color: #666; font-style: italic; }
  .tags { margin-top: .5rem; font-size: .85rem; color: #888; }
  button { margin-top: 1.5rem; padding: .6rem 1.2rem; font-size: 1rem; border: 0; border-radius: 8px; background: #0a66c2; color: white; cursor: pointer; }
  button:hover { background: #084a8e; }
</style>
</head>
<body>
  <h1>Random Quotes</h1>
  <div class="card">
    <blockquote id="text">Loading...</blockquote>
    <div class="author" id="author"></div>
    <div class="tags" id="tags"></div>
  </div>
  <button onclick="loadQuote()">New quote</button>
<script>
async function loadQuote() {
  const r = await fetch('/quote');
  const q = await r.json();
  document.getElementById('text').textContent = '"' + q.text + '"';
  document.getElementById('author').textContent = '— ' + q.author;
  document.getElementById('tags').textContent = 'tags: ' + q.tags.join(', ');
}
loadQuote();
</script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def index():
    return INDEX_HTML
