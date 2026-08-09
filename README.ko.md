# Plain Korean

기술 설명, 상태 보고, 장애 진단을 자연스럽고 이해하기 쉬운 한국어로 바꿉니다. 짧게 쓰더라도 근거, 불확실성, 위험은 숨기지 않습니다.

Plain Korean은 에이전트 스킬과 Claude Code 커스텀 Output Style을 함께 제공합니다. 별도 API나 모델은 필요 없습니다.

[English](README.md) | 한국어

## 무엇이 달라지나

- 작업 과정보다 결과와 현재 상태를 먼저 말합니다.
- 한 문장에 한 가지 뜻만 담고, 필요한 기술 용어는 바로 풀어 씁니다.
- 검증된 사실, 추론, 미확인을 분리합니다.
- 실패, 부분 성공, 안전 제한을 생략하지 않습니다.
- 모든 답을 억지로 줄이지 않고 결정에 필요한 만큼만 씁니다.

## 에이전트 스킬 설치

```sh
git clone https://github.com/beamonic/plain-korean.git
cd plain-korean
mkdir -p ~/.agents/skills
cp -R skills/plain-korean ~/.agents/skills/
```

스킬이 바로 나타나지 않으면 에이전트를 다시 시작하세요.

## Claude Code Output Style 설치

```sh
mkdir -p ~/.claude/output-styles
cp skills/plain-korean/assets/claude-output-style.md ~/.claude/output-styles/plain-korean.md
```

Claude Code에서 `/config`를 실행하고 **Output style → Plain Korean**을 선택하세요. 새 세션을 시작하거나 `/clear`를 실행하면 적용됩니다.

## 사용

```text
$plain-korean 이 배포 실패를 비개발자가 다음 행동을 결정할 수 있게 설명해줘.
```

```text
$plain-korean 아직 검증하지 못한 내용을 숨기지 말고 이 상태 보고를 쉬운 한국어로 고쳐줘.
```

## 검증

```sh
python3 -m unittest -v tests/test_skill.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/plain-korean
```

## 라이선스

MIT. Copyright (c) 2026 Beamonic.
