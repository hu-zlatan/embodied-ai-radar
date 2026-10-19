"""Offline data checks. Exit 1 on any curated-data error. Usage: python scripts/validate.py"""
import sys

from radar import load_arxiv_feed, load_curated, load_topics


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
    entries, cerrs = load_curated()
    errs += cerrs
    feed = load_arxiv_feed()
    for e in errs:
        print("ERROR:", e)
    print(f"{len(entries)} curated entries, {len(feed)} feed papers, {len(errs)} errors")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
