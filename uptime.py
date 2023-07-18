#!/usr/bin/env python3

import httpx
import os
import sys

URLS = os.getenv("URLS", "").split("|")
failed_urls = []


def check_url(url):
    try:
        r = httpx.get(url)
        if r.is_error:
            print(url, r.status_code)
            failed_urls.append(url)
    except Exception as e:
        print(url, e)
        failed_urls.append(url)


for url in URLS:
    if not url:
        continue
    check_url(url)

if failed_urls:
    sys.exit(", ".join(failed_urls))

print("All URLs are up")
