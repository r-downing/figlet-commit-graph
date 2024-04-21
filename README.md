# figlet-commit-graph

Inspired by https://github.com/codypotter/ascii-commit and a meme on linkedin:

> dOnt EvEn BoThEr ApplYinG tO ThIs jOb iF yoUr ComMit GraPh doEsN't LoOk LiKe tHiS.

## Setup

```bash
pip install poetry
poetry install
```

## Run

```bash
poetry shell
python main.py "Some text"
git push origin gh-pages:gh-pages
```

Wish I could automate this with github actions to keep my graph up to date, but it seems that deleting commits and force-pushing isn't enough to get them to disappear from the graph, at least not instantly.
