#!/usr/bin/env python
"""llms-full.txt 재생성 — llms.txt + index.html 본문 + 앱 전문 링크.

[2026-09-06] 왜 있나: `llms.txt` 는 요약 + 링크다. 크롤러가 링크를 안 따라가면
우리 내용이 전달되지 않는다. `llms-full.txt` 는 그걸 펼쳐 놓은 판본이다.

⚠️ **index.html 이나 llms.txt 를 고치면 이 스크립트를 다시 돌릴 것.**
   안 돌리면 llms-full.txt 가 조용히 낡는다 — 낡은 문서는 능동적 오정보다.
   (앱 쪽은 라우트로 생성해 낡을 수가 없는데, 랜딩은 정적 사이트라 이 방식이다.)

재현:  cd malbab-website && python build-llms-full.py
"""
import html
import pathlib
import re

HERE = pathlib.Path(__file__).parent


def main() -> None:
    base = (HERE / "llms.txt").read_text(encoding="utf-8").rstrip()

    raw = (HERE / "index.html").read_text(encoding="utf-8")
    raw = re.sub(r"<(script|style|noscript)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    txt = html.unescape(re.sub(r"<[^>]+>", "\n", raw))

    seen: set[str] = set()
    body: list[str] = []
    for ln in (x.strip() for x in txt.split("\n")):
        if len(ln) < 2 or ln in seen:
            continue
        seen.add(ln)
        body.append(ln)

    out = [
        base, "", "---", "",
        "# 랜딩 페이지 전문 (https://malbab.com)", "",
        "아래는 랜딩에 실제로 쓰인 문구 전부다. 인용 시 출처는 https://malbab.com 로 표기할 것.",
        "이 절은 index.html 에서 자동 추출된다 (build-llms-full.py).", "",
        *body,
        "", "---", "",
        "# 더 깊은 전문", "",
        "서비스의 FAQ 전문·용어사전 전문은 앱 쪽에 있다.", "",
        "- https://app.malbab.com/llms-full.txt  (FAQ 전문 + 용어사전 전문)",
        "- https://app.malbab.com/llms.txt        (앱 요약)",
    ]
    (HERE / "llms-full.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"llms-full.txt: {(HERE / 'llms-full.txt').stat().st_size} bytes")


if __name__ == "__main__":
    main()
