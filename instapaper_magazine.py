
import pandas as pd
from time import sleep
import markdown2
import pdfkit
import os
import requests
from bs4 import BeautifulSoup
import re

# Load Instapaper CSV
csv_path = "Instapaper-Export.csv"  # Update if needed
df = pd.read_csv(csv_path)

# Get top N articles
top_n = 5
articles = df.head(top_n)

# Begin Markdown content
md_content = "# Instapaper Magazine\n"

for idx, row in articles.iterrows():
    url = row["URL"]
    title = row["Title"]
    md_content += f"\n\n---\n\n## {title}\n"
    md_content += f"*Original URL: [{url}]({url})*\n\n"

    try:
        # Fetch and parse HTML
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.encoding = response.apparent_encoding  # Use best-guess encoding
        soup = BeautifulSoup(response.text, "html.parser")

        # Heuristics to find the main content area
        article_html = ""
        for tag in ['article', 'main', 'section', 'div']:
            candidate = soup.find(tag)
            if candidate and len(candidate.get_text()) > 500:
                article_html = candidate
                break

        if not article_html:
            raise ValueError("Could not find main content")

        # Remove scripts, styles, figcaptions, and noscript
        for tag in article_html(["script", "style", "noscript", "figcaption"]):
            tag.decompose()

        # Remove image captions and surrounding <figure> wrappers
        for figure in article_html.find_all("figure"):
            if figure.img:
                img_tag = figure.img
                figure.replace_with(img_tag)
            else:
                figure.decompose()

        # Convert relative image URLs to absolute
        for img in article_html.find_all("img"):
            src = img.get("src")
            if src and src.startswith("/"):
                img["src"] = requests.compat.urljoin(url, src)

        # Extract cleaned HTML content
        html_str = str(article_html)

        # Convert HTML to markdown
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0
        markdown_article = h.handle(html_str)

        # Clean up encoding artifacts manually
        replacements = {
            "â€”": "—", "â€“": "–",
            "â€˜": "'", "â€™": "'",
            "â€œ": '"', "â€": '"',
            "â€¦": "...", "Â": "",
            "\u2014": "—", "\u2013": "–",
            "\u2018": "'", "\u2019": "'",
            "\u201c": '"', "\u201d": '"',
            "\xa0": " "
        }
        for bad, good in replacements.items():
            markdown_article = markdown_article.replace(bad, good)

        # Remove lines that are just "IMAGE" or similar
        markdown_article = re.sub(r'^\s*!\[.*?\]\(.*?\)\s*\n?\*?IMAGE\*?.*?\n?', '', markdown_article, flags=re.MULTILINE | re.IGNORECASE)

        md_content += markdown_article + "\n"

    except Exception as e:
        md_content += f"Error extracting article content: {e}\n"

    sleep(2)

# Convert to HTML with styling
html_style = """
<style>
  body {
    font-family: Georgia, serif;
    font-size: 16pt;
    line-height: 1.6;
    max-width: 700px;
    margin: auto;
    padding: 2em;
  }
  h1, h2, h3 {
    margin-top: 2em;
  }
  img {
    max-width: 100%;
    height: auto;
    margin: 1em 0;
  }
</style>
"""

html_content = html_style + markdown2.markdown(md_content)

# Save to HTML
with open("instapaper_magazine_temp.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Convert to PDF
pdfkit.from_file("instapaper_magazine_temp.html", "Instapaper_Magazine_Inline_Images.pdf")

# Cleanup
os.remove("instapaper_magazine_temp.html")

print("PDF created: Instapaper_Magazine_Inline_Images.pdf")
