# 플레인 코리안

기술 답변, 상태 보고, 원인 진단을 자연스럽고 이해하기 쉬운 한국어로 바꿉니다. 근거, 불확실성, 위험은 숨기지 않습니다.

플레인 코리안은 에이전트 스킬과 Claude Code 사용자 지정 출력 스타일로 제공됩니다. 별도 API를 호출하지 않으며 다른 모델도 필요하지 않습니다.

## 무엇이 달라지나

- 작업 과정보다 결론과 현재 상태를 먼저 말합니다.
- 한 문장에 한 가지 뜻만 담고, 꼭 필요한 기술 용어는 풀어서 설명합니다.
- 확인된 사실, 추론, 미확인을 구분합니다.
- 실패, 부분 성공, 안전 한계를 빠뜨리지 않습니다.
- 무조건 짧게 줄이지 않고 판단에 필요한 만큼 설명합니다.

## 에이전트 스킬 설치

```sh
git clone https://github.com/beamonic/plain-korean.git
cd plain-korean
mkdir -p ~/.agents/skills
cp -R skills/plain-korean ~/.agents/skills/
```

스킬이 바로 보이지 않으면 에이전트를 다시 시작하세요.

## Claude Code 출력 스타일 설치

```sh
mkdir -p ~/.claude/output-styles
cp skills/plain-korean/assets/claude-output-style.md ~/.claude/output-styles/plain-korean.md
```

Claude Code에서 `/config`를 실행하고 출력 스타일에서 `플레인 코리안`을 고르세요. 새 세션을 시작하거나 `/clear`를 실행하면 적용됩니다.

## 사용법

```text
$plain-korean 이 배포 실패를 비개발자도 다음 행동을 결정할 수 있게 설명해 줘.
```

```text
$plain-korean 아직 확인하지 못한 사실을 숨기지 말고 이 상태 보고를 쉬운 한국어로 고쳐 줘.
```

## 검증

```sh
python3 -m unittest -v tests/test_skill.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/plain-korean
```

## 관련 프로젝트

한국어 글쓰기 자산은 통제 언어 규격 [STE-KO](https://github.com/beamonic/ste-ko)를 기반으로 층을 이룹니다. 플레인 코리안은 그중 `대화` 표면 구현체입니다.

| 층 | 프로젝트 | 무엇 | 언제 |
|---|---|---|---|
| 규격 | [ste-ko](https://github.com/beamonic/ste-ko) | 규칙 70개와 표면 4개 | 무엇이 위반인지 번호로 판정할 때 |
| `대화` 표면 | [plain-korean](https://github.com/beamonic/plain-korean) | 답변 문체 | 에이전트가 답변을 쓸 때 |
| `UI` 표면 | [ux-writing-ko](https://github.com/beamonic/ux-writing-ko) | 제품 말투와 화면 문구 | 버튼, 오류, 빈 화면을 쓸 때 |
| 표면 무관 | [no-ai-slop-ko](https://github.com/beamonic/no-ai-slop-ko) | 편집 도구 | 사람이 쓴 초안을 다듬을 때 |

같은 규칙을 두 곳에서 따로 정하지 않습니다. 규칙은 STE-KO에 한 번만 쓰고, 표면 저장소는 그 규격이 비워둔 자리만 채웁니다.

## 저장소 언어 원칙

사람이 읽는 설명과 메타데이터는 한국어로 씁니다. 코드, 명령어, 고정된 기술 식별자와 법적 효력을 보존해야 하는 공식 라이선스 원문은 예외입니다.

## 라이선스

MIT. Copyright (c) 2026 Beamonic.
