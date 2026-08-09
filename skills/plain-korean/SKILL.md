---
name: plain-korean
description: Use when Korean explanations, status reports, reviews, or technical answers feel hard to understand, jargon-heavy, translated, abstract, repetitive, or longer than the decision requires.
---

# Plain Korean

## Core principle

Make the user's next decision obvious in natural Korean. Simplicity means reducing interpretation cost, not deleting evidence, uncertainty, or risk.

## Workflow

1. Lead with the answer in one or two sentences. State the current result before history or method.
2. Keep one idea per sentence. Use a concrete subject and an active verb when possible.
3. Define necessary technical terms at first use with their practical meaning. Keep stable tokens such as function names, commands, and error classes unchanged.
4. Separate verified facts, inference, and unknowns. Never turn an assumption into a confirmed result.
5. Preserve failures, partial success, risk, and the safe next action. Short wording must not make an incomplete state sound complete.
6. Add structure only when it improves scanning. Prefer `결론 / 근거 / 다음 행동` for a diagnosis and a short mapping list for several exact states.
7. End with the recommended next action. Ask at most one question, and only when the answer changes the result or authorization.

## Response scale

| Situation | Default shape |
|---|---|
| Simple fact or status | 1-3 sentences |
| Explanation or recommendation | Conclusion plus 2-4 supporting points |
| Diagnosis or consequential decision | Conclusion, evidence, impact, safe next action |
| User requests depth | Expand progressively without repeating the conclusion |

## Translation rules

- Prefer familiar Korean verbs over stacked abstract nouns.
- Replace vague phrases such as “처리되었습니다” with the exact actor, action, and state.
- Explain a technical term by consequence: `idempotent` becomes “다시 실행해도 결과가 하나만 남는 성질.”
- Do not mechanically copy ASD-STE100 or English sentence patterns into Korean. Write native Korean with the same goal: one meaning, low ambiguity.
- Do not simplify code, logs, or quotations. Quote only the useful excerpt, then explain it in Korean.
- Do not alter fixed legal, medical, financial, or security wording. Add a plain-language explanation beside it when needed.

## Example

Before:

> The idempotency boundary is not guaranteed, so rerunning the batch may amplify duplicate side effects. Inspect transactional scope and checkpoint semantics first.

After:

> 지금은 배치를 다시 실행하면 안 됩니다. 같은 작업이 두 번 반영될 수 있습니다. 먼저 어디까지 저장됐는지 확인하고, 다시 실행해도 결과가 하나만 남도록 고친 뒤 재시도하세요.

## Common mistakes

- Making every answer tiny even when evidence or safety needs detail.
- Replacing precise technical terms with vague Korean.
- Adding headings to a two-sentence answer.
- Repeating the same conclusion in summary, body, and closing.
- Hiding uncertainty to sound confident.

## Final check

Confirm that the answer starts with the result, every sentence earns its place, necessary terms are explained, verified state is distinct from inference, failures remain visible, and the user knows the next action without rereading.
