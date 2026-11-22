"""Generate the optional one-page Korean resume (PyMuPDF and Malgun Gothic)."""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
fonts = {
    "Malgun": fitz.Font(fontfile="C:/Windows/Fonts/malgun.ttf"),
    "MalgunBold": fitz.Font(fontfile="C:/Windows/Fonts/malgunbd.ttf"),
}
out = ROOT / "site/assets/ahn-jihong-resume.pdf"
doc = fitz.open()
page = doc.new_page(width=595.28, height=841.89)
for name, font in fonts.items():
    page.insert_font(fontname=name, fontbuffer=font.buffer)
doc.set_metadata({"title": "안지홍 | 게임 클라이언트 개발자", "author": "안지홍"})
left, width, y = 44, 507, 52


def rgb(color):
    return tuple(int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))


def text(value, size=9, bold=False, color="#384340", gap=5):
    global y
    font = "MalgunBold" if bold else "Malgun"
    lines, current = [], ""
    for word in value.split():
        candidate = f"{current} {word}".strip()
        if current and fonts[font].text_length(candidate, fontsize=size) > width:
            lines.append(current)
            current = word
        else:
            current = candidate
    lines.append(current)
    for line in lines:
        page.insert_text((left, y), line, fontname=font, fontsize=size, color=rgb(color))
        y += size + gap


def heading(value):
    global y
    y += 7
    page.draw_line((left, y), (left + width, y), color=rgb("#d5ded8"), width=.7)
    y += 21
    text(value, 12, True, "#244b38", 8)


text("안지홍  /  hong", 27, True, "#13231a", 8)
text("GAME CLIENT DEVELOPER", 10, True, "#49704e", 9)
text("부산대학교 정보컴퓨터공학부  |  Unity · C# · 게임 클라이언트 개발", 9, gap=8)
text("mm118524@gmail.com  |  https://github.com/anjihong", 9, gap=10)
page.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(left, y - 29, left + 120, y - 15), "uri": "mailto:mm118524@gmail.com"})
page.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(left + 127, y - 29, left + 300, y - 15), "uri": "https://github.com/anjihong"})
text("게임플레이 구현부터 출시, 라이브 운영 대응까지 경험했습니다. 사용자 피드백과 실기기 계측을 바탕으로 플레이 경험을 다듬고, 팀이 나눠 개발할 수 있는 구조를 고민합니다.", 9, gap=5)

heading("대표 프로젝트  |  Drilling")
text("2025.06 ~ 업데이트 중  ·  6인 팀  ·  PD / 기획 / 클라이언트 개발", 9, True, gap=7)
text("부담 없이 즐기는 2D 마이닝 어드벤처. 2026.11.03 Steam 정식 출시.", 9, gap=7)
text("• 일정·업무 분배와 출시 준비를 맡고, 게임 기능·에디터 툴·상점 UI·미니맵·엔딩을 구현했습니다.")
text("• 전체 타일맵 탐색을 원석 캐싱으로 전환하고, 청크 스트리밍·Sprite Atlas를 적용했습니다.")
text("• 저장 버전과 구버전 보정으로 세이브 호환을 처리하고, 플레이어를 6개 모듈로 분리했습니다.")
text("• 데모 다운로드 약 2,000명, 2025 게임핑 루키 콘테스트 2위. 축제 부스에서 300명 이상 플레이를 관찰하고 튜토리얼과 초반 난이도에 반영했습니다.")
text("기술: Unity 6, C#, URP, ScriptableObject, Timeline, Cinemachine, GitHub Actions", 8, color="#607069", gap=7)
text("게임 / 데모: https://store.steampowered.com/app/4304980/Drilling/", 8, color="#244b38")

heading("현장실습  |  (주)에버스톤 · 젤리의 마을")
text("2025.09.01 ~ 2026.01.01  ·  18주  ·  모바일 게임 클라이언트 개발", 9, True, gap=7)
text("• 미니게임 8종을 개발하고 공통 팝업·타이머 등을 추상 클래스와 공통 매니저로 정리했습니다.")
text("• Spine 코스튬의 파츠별 런타임 합성과 색상 변경을 아트 리소스 재작업 없이 구현했습니다.")
text("• ReadPixels의 GPU Stall을 확인해 RenderTexture 직접 바인딩으로 변경했습니다. 같은 조건에서 Costume.CombineLayers 함수 점유율이 51.4%에서 1.1%로 감소했습니다.")
text("• dev/test/live를 분리해 뒤끝 서버 이관을 진행하고, Firebase 지표·푸시·알림 설정을 구현했습니다. CBT 배포와 G-STAR BTB 시연 준비에도 참여했습니다.")
text("기술: Unity, C#, Spine, Addressables, Sprite Atlas, 뒤끝, Firebase, Unity Profiler, SVN", 8, color="#607069", gap=7)

heading("기술과 관심 분야")
text("개발: Unity / C#, UI·게임플레이, 데이터·세이브 호환, ScriptableObject", 9)
text("최적화·연출: Profiler, Addressables, Sprite Atlas, Shader Graph, VFX Graph, Spine", 9)
text("협업: Git / GitHub, SVN, Notion, 일정 관리, 기획 문서, 플레이 피드백", 9)
text("관심: 테크니컬 아트(TA), 렌더링, 리소스 관리와 성능 개선", 9)
assert y < 790, f"Resume overflows the page: {y}"
page.insert_text((left, 813), "2026.11  |  프로젝트 및 현장실습 기록 기반", fontname="Malgun", fontsize=7, color=rgb("#79847d"))
page.insert_text((533, 813), "1 / 1", fontname="Malgun", fontsize=7, color=rgb("#79847d"))
doc.subset_fonts()
doc.save(out, garbage=4, deflate=True)
print(f"Created {out}")
