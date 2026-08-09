from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "plain-korean" / "SKILL.md"
OPENAI_YAML = ROOT / "skills" / "plain-korean" / "agents" / "openai.yaml"
OUTPUT_STYLE = ROOT / "skills" / "plain-korean" / "assets" / "claude-output-style.md"
README = ROOT / "README.md"
README_KO = ROOT / "README.ko.md"
LICENSE = ROOT / "LICENSE"


class PlainKoreanSkillTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.openai_yaml = OPENAI_YAML.read_text(encoding="utf-8")

    def test_frontmatter_is_discoverable(self):
        self.assertRegex(self.skill, r"(?m)^name: plain-korean$")
        self.assertRegex(self.skill, r"(?m)^description: .+때 사용한다\.$")
        self.assertNotIn("TODO", self.skill)

    def test_clarity_contract_preserves_meaning(self):
        for phrase in (
            "결론과 현재 상태",
            "한 문장에는 한 가지 뜻",
            "꼭 필요한 기술 용어",
            "확인된 사실",
            "추론",
            "실패",
            "질문을 하나",
            "코드, 로그, 인용문은 단순화하지 않는다",
        ):
            self.assertIn(phrase, self.skill)

    def test_output_style_keeps_coding_behavior(self):
        text = OUTPUT_STYLE.read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^name: 플레인 코리안$")
        self.assertRegex(text, r"(?m)^description: .+")
        self.assertRegex(text, r"(?m)^keep-coding-instructions: true$")
        self.assertIn("한국어", text)
        self.assertIn("결론", text)
        self.assertIn("검증", text)

    def test_ui_metadata_invokes_the_skill(self):
        self.assertIn('display_name: "플레인 코리안"', self.openai_yaml)
        self.assertIn("$plain-korean", self.openai_yaml)

    def test_skill_stays_small(self):
        words = re.findall(r"\S+", self.skill)
        self.assertLessEqual(len(words), 600)


class PublicSurfaceTest(unittest.TestCase):
    def test_public_prose_uses_korean(self):
        self.assertFalse(README_KO.exists())
        self.assertIn("# 플레인 코리안", README.read_text(encoding="utf-8"))
        self.assertIn("# 플레인 코리안", SKILL.read_text(encoding="utf-8"))
        self.assertIn('display_name: "플레인 코리안"', OPENAI_YAML.read_text(encoding="utf-8"))
        self.assertRegex(
            OUTPUT_STYLE.read_text(encoding="utf-8"),
            r"(?m)^name: 플레인 코리안$",
        )

    def test_public_readmes_and_license_exist(self):
        for path in (README, LICENSE):
            self.assertTrue(path.is_file(), path)

    def test_installation_uses_beamonic_repository(self):
        text = README.read_text(encoding="utf-8")
        self.assertIn("https://github.com/beamonic/plain-korean.git", text)
        self.assertIn("claude-output-style.md", text)

    def test_public_files_do_not_leak_private_lanes(self):
        forbidden = re.compile(
            "/" + r"Users/|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            re.IGNORECASE,
        )
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or path.suffix == ".pyc":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(forbidden.search(text), path)

    def test_license_is_mit_and_beamonic_owned(self):
        text = LICENSE.read_text(encoding="utf-8")
        self.assertIn("MIT License", text)
        self.assertIn("Copyright (c) 2026 Beamonic", text)


if __name__ == "__main__":
    unittest.main()
