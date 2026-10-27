"""Offline data checks. Exit 1 on any curated-data error. Usage: python scripts/validate.py"""
import sys

from radar import entry_id, load_arxiv_feed, load_curated, load_embodiments, load_labs, load_resources, load_start, load_topics


def main() -> int:
    topics = load_topics()
    ids = [t["id"] for t in topics]
    errs = []
    if len(ids) != len(set(ids)):
        errs.append("topics.yaml: duplicate topic ids")
    for t in topics:
        for k in ("id", "en", "zh", "desc_en", "desc_zh", "keywords"):
            if not t.get(k):
                errs.append(f"topics.yaml: topic {t.get('id')} missing {k}")
    embs = load_embodiments()
    if len({e.get("id") for e in embs}) != len(embs):
        errs.append("embodiments.yaml: duplicate ids")
    for em in embs:
        for k in ("id", "en", "zh", "keywords"):
            if not em.get(k):
                errs.append(f"embodiments.yaml: {em.get('id')} missing {k}")
    try:
        labs = load_labs()
    except Exception as ex:  # bad regex in labs.yaml
        labs = []
        errs.append(f"labs.yaml: {ex}")
    if len({lab.get("id") for lab in labs}) != len(labs):
        errs.append("labs.yaml: duplicate ids")
    for lab in labs:
        for k in ("id", "en", "zh", "match"):
            if not lab.get(k):
                errs.append(f"labs.yaml: {lab.get('id')} missing {k}")
    entries, cerrs = load_curated()
    errs += cerrs
    resources, rerrs = load_resources()
    errs += rerrs
    _, serrs = load_start({entry_id(e) for e in entries})
    errs += serrs
    feed = load_arxiv_feed()
    for e in errs:
        print("ERROR:", e)
    print(f"{len(entries)} curated entries, {len(feed)} feed papers, {len(errs)} errors")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
