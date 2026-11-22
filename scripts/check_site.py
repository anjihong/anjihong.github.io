"""Check deployable files, local links, fragments and image accessibility."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "site"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        if tag == "img":
            assert attrs.get("alt"), "Image missing descriptive alt text"
        if tag == "a" and attrs.get("target") == "_blank":
            assert "noopener" in attrs.get("rel", "").split(), "Unsafe new tab"
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


def check():
    page = SiteParser()
    text = (ROOT / "index.html").read_text(encoding="utf-8")
    page.feed(text)
    assert '<html lang="ko">' in text
    assert page.headings == 1, "Expected one main heading"
    for link in page.links:
        parts = urlsplit(link)
        if parts.scheme or parts.netloc:
            continue
        if parts.path:
            target = (ROOT / unquote(parts.path)).resolve()
            assert target.is_relative_to(ROOT), f"Path escapes site: {link}"
            assert target.is_file(), f"Missing asset: {link}"
            assert target.stat().st_size > 0, f"Empty asset: {link}"
        elif parts.fragment:
            assert unquote(parts.fragment) in page.ids, f"Broken anchor: {link}"
    for required in ("Drilling", "젤리의 마을", "문제 정의", "내 역할", "51.4%", "1.1%"):
        assert required in text, f"Missing portfolio content: {required}"
    print(f"PASS: {len(page.links)} references, {len(page.ids)} anchors, images and content")


if __name__ == "__main__":
    check()
