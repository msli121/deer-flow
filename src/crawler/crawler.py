# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import logging

from src.crawler.article import Article
from src.crawler.jina_client import JinaClient
from src.crawler.readability_extractor import ReadabilityExtractor

logger = logging.getLogger(__name__)


class Crawler:
    def crawl(self, url: str) -> Article:
        # To help LLMs better understand content, we extract clean
        # articles from HTML, convert them to markdown, and split
        # them into text and image blocks for one single and unified
        # LLM message.
        #
        # Jina is not the best crawler on readability, however it's
        # much easier and free to use.
        #
        # Instead of using Jina's own markdown converter, we'll use
        # our own solution to get better readability results.
        try:
            jina_client = JinaClient()
            html = jina_client.crawl(url, return_format="html")
        except Exception as e:
            logger.error(f"Failed to fetch URL {url} from Jina: {repr(e)}")
            raise
        
        try:
            extractor = ReadabilityExtractor()
            article = extractor.extract_article(html)
        except Exception as e:
            logger.error(f"Failed to extract article from {url}: {repr(e)}")
            raise
        
        article.url = url
        return article


if __name__ == '__main__':
    import os
    os.environ["JINA_API_KEY"] = "jina_03cb4a11098e439a83dc069674f173b6u4R2V5K01SB4ZdDVA2U1Zl5hkaB2"
    crawler = Crawler()
    url = 'https://www.taiwu.com/ershoufang/TWS2025062700014.html'
    article = crawler.crawl(url)
    print(article.to_markdown())
