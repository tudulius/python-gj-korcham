# 패키지 설치
# pip install trafilatura

import trafilatura

# 크롤링할 URL 설정
url = "https://m.sports.naver.com/esports/article/015/0005057943?sid3=79b"

# 웹 페이지 다운로드
downloaded = trafilatura.fetch_url(url)

# 본문 및 메타데이터 추출
result = trafilatura.extract(downloaded, output_format="json", include_comments=False, include_links=False, with_metadata=True)

# JSON 문자열을 파이썬 딕셔너리로 변환
import json
parsed_result = json.loads(result)

# 제목 출력
print("제목:", parsed_result['title'])

# 본문 출력
print("\n본문:")
print(parsed_result['text'])