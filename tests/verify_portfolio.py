from __future__ import annotations

import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = DOCS / "index.html"


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.stylesheets: list[str] = []
        self.scripts: list[str] = []
        self.script_types: list[str] = []
        self.images: list[dict[str, str]] = []
        self.role_buttons: list[dict[str, str]] = []
        self.button_names: list[str] = []
        self.projects: list[dict[str, str]] = []
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.h1_count = 0
        self._button_depth = 0
        self._button_text: list[str] = []
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"])
        if tag == "link":
            rel = values.get("rel", "").lower().split()
            if "stylesheet" in rel and values.get("href"):
                self.stylesheets.append(values["href"])
            if "canonical" in rel:
                self.canonical = values.get("href", "")
        if tag == "script":
            if values.get("src"):
                self.scripts.append(values["src"])
            if values.get("type"):
                self.script_types.append(values["type"])
        if tag == "img":
            self.images.append(values)
        if tag == "meta":
            key = values.get("name") or values.get("property")
            if key:
                self.meta[key.lower()] = values.get("content", "")
        if tag == "button":
            self._button_depth += 1
            self._button_text = []
            if values.get("data-role"):
                self.role_buttons.append(values)
        if tag == "article" and "project-card" in values.get("class", "").split():
            self.projects.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag == "button" and self._button_depth:
            name = " ".join(" ".join(self._button_text).split())
            self.button_names.append(name)
            self._button_depth -= 1
            self._button_text = []

    def handle_data(self, data: str) -> None:
        cleaned = " ".join(data.split())
        if cleaned:
            self.text.append(cleaned)
            if self._button_depth:
                self._button_text.append(cleaned)


def is_external_http(href: str) -> bool:
    return urlparse(href).scheme in {"http", "https"}


def resolve_local(href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme or href.startswith(("#", "mailto:", "tel:")):
        return None
    clean = parsed.path.lstrip("/")
    return DOCS / clean


def main() -> int:
    failures: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    require(INDEX.is_file(), "missing docs/index.html")
    if not INDEX.is_file():
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    html = INDEX.read_text(encoding="utf-8")
    parser = PortfolioParser()
    parser.feed(html)

    required_ids = {
        "overview",
        "snapshot",
        "experience",
        "projects",
        "skills",
        "credentials",
        "resumes",
        "contact",
        "role-title",
        "role-summary",
        "role-resume",
        "role-tools",
        "role-proof",
        "copy-email",
        "copy-status",
    }
    missing_ids = sorted(required_ids.difference(parser.ids))
    require(not missing_ids, f"missing required ids: {', '.join(missing_ids)}")

    duplicate_ids = sorted(key for key, count in Counter(parser.ids).items() if count > 1)
    require(not duplicate_ids, f"duplicate ids: {', '.join(duplicate_ids)}")
    require(parser.h1_count == 1, f"expected exactly one h1, found {parser.h1_count}")

    required_nav = {
        "#overview",
        "#experience",
        "#projects",
        "#skills",
        "#credentials",
        "#resumes",
        "#contact",
    }
    missing_nav = sorted(required_nav.difference(parser.hrefs))
    require(not missing_nav, f"missing navigation targets: {', '.join(missing_nav)}")

    role_values = {button.get("data-role", "") for button in parser.role_buttons}
    require(role_values == {"it", "soc", "grc"}, f"role values must be it/soc/grc, found {sorted(role_values)}")
    require(len(parser.role_buttons) == 3, f"expected 3 role buttons, found {len(parser.role_buttons)}")
    require(
        sum(button.get("aria-pressed") == "true" for button in parser.role_buttons) == 1,
        "exactly one role button must start pressed",
    )
    require(all(parser.button_names), "every button must have a visible accessible name")

    require(len(parser.projects) == 6, f"expected 6 project cards, found {len(parser.projects)}")
    required_project_attrs = {
        "data-project",
        "data-roles",
        "data-rank-it",
        "data-rank-soc",
        "data-rank-grc",
    }
    for index, project in enumerate(parser.projects, start=1):
        missing = sorted(required_project_attrs.difference(project))
        require(not missing, f"project {index} missing attributes: {', '.join(missing)}")

    required_repo_urls = {
        "https://github.com/BrianSantiago-GRC/entra-identity-security-review",
        "https://github.com/BrianSantiago-GRC/Microsoft-Sentinel-SIEM",
        "https://github.com/BrianSantiago-GRC/microsoft-defender-endpoint-investigation",
        "https://github.com/BrianSantiago-GRC/grc-access-review-audit-evidence-pack",
        "https://github.com/BrianSantiago-GRC/iam-jml-access-workflow-pack",
        "https://github.com/BrianSantiago-GRC/grc-portfolio",
    }
    missing_repos = sorted(required_repo_urls.difference(parser.hrefs))
    require(not missing_repos, f"missing repository links: {', '.join(missing_repos)}")

    required_resumes = {
        "assets/resumes/Brian_Santiago_IT.pdf",
        "assets/resumes/Brian_Santiago_SOC.pdf",
        "assets/resumes/Brian_Santiago_GRC.pdf",
    }
    missing_resumes = sorted(required_resumes.difference(parser.hrefs))
    require(not missing_resumes, f"missing resume links: {', '.join(missing_resumes)}")

    for href in parser.hrefs + parser.stylesheets + parser.scripts:
        local = resolve_local(href)
        if local is not None:
            require(local.is_file() or local.is_dir(), f"missing local target: {href}")
        if is_external_http(href):
            require(urlparse(href).scheme == "https", f"external link must use HTTPS: {href}")

    for resume in required_resumes:
        path = DOCS / resume
        require(path.is_file(), f"missing resume file: {resume}")
        if path.is_file():
            require(path.read_bytes().startswith(b"%PDF"), f"invalid PDF signature: {resume}")

    require("assets/site.css" in parser.stylesheets, "missing assets/site.css reference")
    require("assets/site.js" in parser.scripts, "missing assets/site.js reference")
    require("application/ld+json" in parser.script_types, "missing Person JSON-LD")
    require(parser.canonical == "https://briansantiago-grc.github.io/BrianSantiago-GRC/", "canonical URL is incorrect")
    require(bool(parser.meta.get("description")), "missing meta description")
    require(parser.meta.get("viewport") == "width=device-width, initial-scale=1", "viewport metadata is incorrect")
    require(
        any(image.get("src") == "recruiter_portfolio_hero_visual.png" and image.get("alt") for image in parser.images),
        "hero visual must be present with useful alt text",
    )

    visible_text = " ".join(parser.text).lower()
    for label in ("problem", "action", "tools", "result", "scope"):
        require(label in visible_text, f"missing project evidence label: {label}")
    for required_copy in (
        "professional experience",
        "hands-on lab",
        "synthetic",
        "ocala, florida",
        "400+",
        "99%",
        "500+",
        "200+",
        "in progress - target q4 2026",
    ):
        require(required_copy in visible_text, f"missing recruiter copy: {required_copy}")

    forbidden_copy = {
        "contained endpoint alert",
        "8 kql detection rules",
        "false-positive reduction around 35%",
        "route plan",
        "event log",
    }
    for phrase in forbidden_copy:
        require(phrase not in visible_text, f"forbidden or unsupported copy remains: {phrase}")

    script_text = (DOCS / "assets" / "site.js")
    if script_text.is_file():
        javascript = script_text.read_text(encoding="utf-8")
        for token in ("applyRole", "history.replaceState", "URLSearchParams", "aria-pressed", "popstate"):
            require(token in javascript, f"site.js missing role behavior token: {token}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"PORTFOLIO_VERIFY_FAILED ({len(failures)} failures)")
        return 1

    print("PORTFOLIO_VERIFY_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
