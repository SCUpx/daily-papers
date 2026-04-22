import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from typing import List, Optional

import feedparser

from src.logger import logger
from src.models import Paper

ARXIV_REQUEST_TIMEOUT_SEC = 60


class ArxivClient:
    """ArXiv API client"""

    def __init__(
        self,
        max_results: int = 500,
        base_url: str = "http://export.arxiv.org/api/query",
        categories: Optional[List[str]] = None,
        search_keywords: Optional[List[str]] = None,
    ):
        self.max_results = max_results
        self.base_url = base_url
        self.categories = categories or ["cs.CV", "cs.CL", "cs.AI", "cs.LG", "cs.MM"]
        self.search_keywords = search_keywords or []

    def _build_query(self) -> str:
        """Build ArXiv search query.

        If search_keywords is configured, use keyword search (ti: + abs:) across
        all specified categories, which gives far more relevant results than
        browsing by category alone.

        Otherwise fall back to category-only browsing.
        """
        if self.search_keywords:
            # Build per-keyword sub-queries: match title OR abstract
            kw_parts = []
            for kw in self.search_keywords:
                escaped = urllib.parse.quote(f'"{kw}"', safe="")
                # Use raw string for query building (will be URL-encoded later)
                kw_parts.append(f'(ti:"{kw}" OR abs:"{kw}")')
            keyword_query = " OR ".join(kw_parts)

            if self.categories:
                cat_query = " OR ".join([f"cat:{cat}" for cat in self.categories])
                return f"({keyword_query}) AND ({cat_query})"
            return keyword_query

        # Fallback: category-only
        return " OR ".join([f"cat:{cat}" for cat in self.categories])

    def fetch_papers(self) -> List[Paper]:
        """Fetch latest papers"""
        query = self._build_query()
        params = {
            "search_query": query,
            "max_results": self.max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = self.base_url + "?" + urllib.parse.urlencode(params)

        if self.search_keywords:
            logger.info(
                f"Fetching latest {self.max_results} papers via keyword search: "
                f"{self.search_keywords}"
            )
        else:
            logger.info(
                f"Fetching latest {self.max_results} papers from categories: "
                f"{self.categories}"
            )

        try:
            with urllib.request.urlopen(url, timeout=ARXIV_REQUEST_TIMEOUT_SEC) as resp:
                body = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            logger.error(f"ArXiv HTTP error: {e.code} {e.reason}")
            raise
        except urllib.error.URLError as e:
            logger.error(f"ArXiv network error: {e.reason}")
            raise

        feed = feedparser.parse(body)
        if getattr(feed, "bozo", False) and feed.bozo_exception:
            logger.warning(f"ArXiv feed parse warning: {feed.bozo_exception}")

        papers: List[Paper] = []
        for entry in feed.entries:
            paper = self._parse_entry(entry)
            papers.append(paper)

        logger.info(f"Fetched {len(papers)} papers")
        return papers

    def _parse_entry(self, entry: dict) -> Paper:
        """Parse paper entry"""
        return Paper(
            title=self._clean_text(entry.get("title", "")),
            authors=[self._clean_text(a.get("name", "")) for a in entry.get("authors", [])],
            abstract=self._clean_text(entry.get("summary", "")),
            link=self._clean_text(entry.get("link", "")),
            tags=[t.get("term", "") for t in entry.get("tags", [])],
            comment=self._clean_text(entry.get("arxiv_comment", "")),
            date=self._parse_date(entry.get("published", "")),
        )

    @staticmethod
    def _clean_text(text: str) -> str:
        return " ".join(text.replace("\n", " ").split())

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        try:
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except (ValueError, TypeError, OSError) as e:
            logger.warning(f"Failed to parse date {date_str!r}: {e}")
            return datetime.now()
