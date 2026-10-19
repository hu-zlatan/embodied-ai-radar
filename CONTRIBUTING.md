# Contributing · 参与贡献

Thanks for helping! The easiest way is to [open an issue](https://github.com/hu-zlatan/embodied-ai-radar/issues/new) with a link and one sentence on why it matters. 最简单的方式是提交 issue，附上链接和一句推荐理由。

## Add an entry

Add one item to `data/curated/<topic>.yaml` (topics are listed in `data/topics.yaml`; the file you choose is the entry's primary topic):

```yaml
- title: "OpenVLA: An Open-Source Vision-Language-Action Model"   # exact title (arXiv title for papers)
  type: paper            # paper | code | dataset | benchmark | simulator | hardware
  arxiv: "2406.09246"    # quoted; optional for non-papers
  year: 2024
  org: Stanford, UC Berkeley, TRI      # optional
  code: https://github.com/openvla/openvla   # optional: url, code, project (https only)
  topics: [manipulation] # optional: extra topics besides the file's own
  tags: [real, arm, open-weights]      # optional, free-form lowercase
  highlight: true        # optional, maintainers use this sparingly
  takeaway_en: One sentence, your own words, ≤ 220 characters.
  takeaway_zh: 一句话，用自己的话写，不超过 220 字符。
```

Rules: entries must be real and links must work (CI checks arXiv titles and URLs); write takeaways in your own words — don't paste abstracts.

## Run locally

```bash
pip install -r requirements.txt
python scripts/validate.py        # offline schema checks
python scripts/build_readme.py    # regenerate README lists
python scripts/build_site.py      # site → _site/ (open _site/index.html)
```

By contributing you agree that code is MIT and curated text/data is CC BY 4.0.
