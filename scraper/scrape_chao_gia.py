"""
Scraper: Thong bao chao gia - BV Nhi Dong Thanh Pho
URL: https://bvndtp.org.vn/chuyen-muc/thong-bao-chao-gia/
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from datetime import datetime

BASE_URL = "https://bvndtp.org.vn/chuyen-muc/thong-bao-chao-gia/page/{}/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
DELAY = 1.0  # seconds between requests


def get_total_pages(soup: BeautifulSoup) -> int:
    """Detect total number of pages from pagination."""
    # WordPress typically renders page numbers as <a> inside .page-numbers
    page_nums = soup.select("a.page-numbers, .pagination a, .nav-links a")
    numbers = []
    for a in page_nums:
        text = a.get_text(strip=True)
        if text.isdigit():
            numbers.append(int(text))
    if numbers:
        return max(numbers)

    # Fallback: look for last numeric page link in any pagination block
    all_links = soup.find_all("a", href=re.compile(r"/page/(\d+)/"))
    for link in all_links:
        m = re.search(r"/page/(\d+)/", link["href"])
        if m:
            numbers.append(int(m.group(1)))
    return max(numbers) if numbers else 1


def extract_articles(soup: BeautifulSoup) -> list[dict]:
    """Extract article title, URL, and date (if available) from a listing page."""
    articles = []

    # Try common WordPress/theme selectors in priority order
    selectors = [
        "article h2 a",
        "article h3 a",
        ".post-title a",
        ".entry-title a",
        "h2.title a",
        "h3.title a",
        ".item-title a",
        ".article-item h3 a",
        ".blog-item h3 a",
        # broad fallback: any <h2>/<h3> inside a container with an <a>
    ]

    items = []
    for sel in selectors:
        items = soup.select(sel)
        if items:
            break

    # Absolute fallback: collect all <h2>/<h3> anchors on the page
    if not items:
        items = soup.select("h2 a[href*='bvndtp.org.vn'], h3 a[href*='bvndtp.org.vn']")

    # Attempt to pair each title link with a nearby date
    for a in items:
        title = a.get_text(strip=True)
        href = a.get("href", "").strip()

        # Skip empty, navigation, or menu links
        if not title or not href or "chuyen-muc" in href or href == "#":
            continue
        if not href.startswith("http"):
            href = "https://bvndtp.org.vn" + href

        # Look for a date in the closest parent containers
        date_str = ""
        parent = a.parent
        for _ in range(6):
            if parent is None:
                break
            # Common date selectors
            date_tag = parent.select_one(
                "time, .entry-date, .post-date, .date, .published, "
                "[class*='date'], [class*='time']"
            )
            if date_tag:
                date_str = date_tag.get("datetime") or date_tag.get_text(strip=True)
                break
            parent = parent.parent

        articles.append({"Tiêu đề": title, "Ngày đăng": date_str, "Đường dẫn": href})

    return articles


def scrape_all() -> pd.DataFrame:
    all_rows: list[dict] = []

    # --- Page 1: detect total pages ---
    print("Đang tải trang 1 để xác định tổng số trang...")
    resp = requests.get(BASE_URL.format(1), headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    total_pages = get_total_pages(soup)
    print(f"Tổng số trang: {total_pages}")

    rows = extract_articles(soup)
    all_rows.extend(rows)
    print(f"  Trang 1: {len(rows)} bài")

    # --- Pages 2..total ---
    for page in range(2, total_pages + 1):
        url = BASE_URL.format(page)
        try:
            time.sleep(DELAY)
            resp = requests.get(url, headers=HEADERS, timeout=15)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            rows = extract_articles(soup)
            all_rows.extend(rows)
            print(f"  Trang {page}/{total_pages}: {len(rows)} bài")
        except Exception as e:
            print(f"  [LỖI] Trang {page}: {e}")

    df = pd.DataFrame(all_rows, columns=["Tiêu đề", "Ngày đăng", "Đường dẫn"])
    df.index = range(1, len(df) + 1)
    df.index.name = "STT"
    return df


def save_excel(df: pd.DataFrame, path: str) -> None:
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Thông báo chào giá")
        ws = writer.sheets["Thông báo chào giá"]

        # Auto-fit column widths (capped at 80)
        for col_cells in ws.columns:
            max_len = max(
                (len(str(c.value)) if c.value else 0) for c in col_cells
            )
            ws.column_dimensions[col_cells[0].column_letter].width = min(max_len + 2, 80)


if __name__ == "__main__":
    df = scrape_all()
    print(f"\nTổng cộng: {len(df)} thông báo")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = f"thong_bao_chao_gia_{timestamp}.xlsx"
    save_excel(df, out_path)
    print(f"Đã lưu: {out_path}")
