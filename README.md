# plain-korean — STE-KO로 합쳤습니다

이 저장소는 2026-08-16에 [beamonic/ste-ko](https://github.com/beamonic/ste-ko)로 합쳤습니다. 더 갱신하지 않습니다.

## 왜 합쳤나

plain-korean의 항목 12개 중 9개가 STE-KO 규칙과 같은 내용이었습니다. 같은 규칙을 두 곳에서 관리하면 한쪽이 먼저 낡습니다.

| plain-korean | STE-KO 규칙 |
|---|---|
| 결론과 현재 상태 먼저 | 6.1 |
| 한 문장 한 뜻, 능동, 주어 명시 | 4.2, 3.1 |
| 용어는 결과로 설명, 식별자 보존 | 1.7, 1.4 |
| 사실과 추론과 미확인 구분 | 6.2 |
| 실패와 부분 성공 보존 | 6.4, 9.3 |
| 질문은 하나만 | 10.3 |
| 추상 명사 겹침 대신 동사 | 2.5 |
| 주체가 흐린 피동 금지 | 3.3 |
| 법률·의료 고정 문구 보존 | 9.4 |

고유했던 셋은 STE-KO 규칙이 되었습니다.

| 옮긴 것 | 새 번호 |
|---|---|
| 답변 분량을 상황에 맞춘다 | 10.15 |
| 다음 행동으로 끝낸다 | 10.16 |
| 구조를 남용하지 않는다 | 10.17 |

Claude Code output style 파일은 `skills/ste-ko/assets/claude-output-style.md`로 옮겼습니다.

## 대신 쓰는 법

```bash
npx skills add beamonic/ste-ko
```

`대화` 표면이 이 저장소가 하던 일을 대신합니다. `/ste-ko 대화`로 지정하며, 지정하지 않으면 `대화`가 기본입니다.

## 남은 자산

같은 조직의 다른 한국어 스킬은 계속 씁니다. 역할이 겹치지 않습니다.

- **[ux-writing-ko](https://github.com/beamonic/ux-writing-ko)** — `UI` 표면 구현체. 버튼, 오류 메시지, 빈 화면 문구.
- **[no-ai-slop-ko](https://github.com/beamonic/no-ai-slop-ko)** — 표면 무관 편집 도구. 사람이 쓴 초안을 다듬을 때.

## 라이선스

MIT. Copyright (c) 2026 Beamonic.
