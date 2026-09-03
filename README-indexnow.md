# IndexNow — 이 도메인(malbab.com) 전용 키

네이버 가이드: *"웹사이트가 여러 개의 도메인으로 이루어져 있다면, 각 도메인마다 별개의
key를 이용해야 합니다."* 앱(app.malbab.com)은 별도 키를 쓴다
(`backend/app/core/indexnow.py`, dark-horse 리포).

- 키: `db6337a5365fa26e83c2877836c28139`
- 키 파일: `https://malbab.com/db6337a5365fa26e83c2877836c28139.txt` (이 리포 루트 = Cloudflare Pages 서빙 루트)
- 제출: `POST https://searchadvisor.naver.com/indexnow`
  `{"host":"malbab.com","key":"db6337a5365fa26e83c2877836c28139","keyLocation":"https://malbab.com/db6337a5365fa26e83c2877836c28139.txt","urlList":[...]}`

키는 비밀이 아니다 — 공개 URL 로 서빙되는 것이 프로토콜의 전부다.
색인을 보장하지 않는다(네이버 FAQ). 크롤을 앞당길 뿐이다.
