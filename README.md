# 안지홍 포트폴리오

Drilling과 에버스톤 현장실습을 소개하는 한국어 정적 웹사이트. 별도 설치나 빌드 없이 GitHub Pages에서 서비스합니다.

## 파일

- `site/index.html`: 소개, 프로젝트 사례, 기술, 연락처
- `site/styles.css`: 반응형 화면 및 접근성 스타일
- `site/assets/`: 게임 화면, 프로파일러 근거, 다운로드 가능한 이력서 PDF
- `.github/workflows/pages.yml`: main 브랜치 변경 시 검증 후 GitHub Pages 배포
- `scripts/check_site.py`: 내부 링크·파일·ID·이미지 대체 텍스트 검증
- `scripts/build_resume.py`: 이력서 PDF 재생성(Windows Malgun Gothic, Python PyMuPDF 필요)

## 로컬 미리보기

저장소 루트에서 실행합니다.

```powershell
python scripts/check_site.py
python -m http.server 8765 --bind 127.0.0.1 --directory site
```

브라우저에서 http://127.0.0.1:8765 를 엽니다. `site/index.html`을 직접 열어도 주요 기능은 동작합니다.

## GitHub Pages 배포

1. `anjihong/anjihong.github.io` 공개 저장소에 이 폴더의 파일을 올립니다. `site` 폴더가 저장소 루트에 포함되어야 합니다.
2. 저장소의 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 설정합니다.
3. `main`에 push하거나 **Actions → Deploy portfolio to GitHub Pages → Run workflow**를 실행합니다.
4. 성공 후 https://anjihong.github.io/ 에서 페이지와 PDF 다운로드를 확인합니다.

다른 이름의 저장소를 사용해도 상대 경로로 작동합니다. 이 경우 배포 주소는 `https://anjihong.github.io/저장소이름/`입니다.

## 과제 제출

배포 성공을 확인한 후 `안지홍-공작과제-06.txt` 파일에 실제 배포 URL만 한 줄로 넣어 제출합니다. 아직 배포하지 않은 주소를 제출하지 마세요.

## 내용과 출처

- [원본 Notion 포트폴리오](https://app.notion.com/p/2026-3cf6a6a2944e81d7ad91f8b2c2158406)
- [Drilling 상세](https://app.notion.com/p/Drilling-3cf6a6a2944e81c089eae291caefbfc4)
- [현장실습 상세](https://app.notion.com/p/3cf6a6a2944e81259cc7d890c2de2a16)
- [Drilling Steam 상점](https://store.steampowered.com/app/4304980/Drilling/?l=koreana)
- [GitHub Pages 공식 배포 안내](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

Notion 링크는 방문자의 로그인이나 페이지 접근 권한에 따라 열리지 않을 수 있습니다. 필수 설명과 이미지는 사이트 안에 포함했습니다. 원본의 생년월일·전화번호·학번은 공개 페이지에 포함하지 않았습니다. 프로젝트별 소스 저장소 주소는 제공되지 않아 임의로 추가하지 않았습니다.

현장실습의 51.4%와 1.1%는 동일 조건의 Profiler에서 측정한 `Costume.CombineLayers` 함수 점유율입니다. 전체 FPS 개선 수치로 해석하지 않습니다. Drilling의 탐색·청크 개선에는 전후 수치가 없어 정량 성능 향상률을 적지 않았습니다.

게임 화면과 아트는 포트폴리오 설명 목적으로 사용하며 각 프로젝트 권리자의 권리를 유지합니다.
