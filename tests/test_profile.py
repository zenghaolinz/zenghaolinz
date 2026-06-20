from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET


class ProfileReadmeTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def readme(self):
        return (self.ROOT / "README.md").read_text(encoding="utf-8")

    def test_required_profile_files_exist(self):
        self.assertTrue((self.ROOT / "README.md").is_file())
        self.assertTrue((self.ROOT / "assets/profile-hero.svg").is_file())

    def test_profile_contains_bilingual_sections(self):
        readme = self.readme()
        for heading in (
            "Selected Works / 代表项目",
            "About Me / 关于我",
            "Toolbox / 技术栈",
        ):
            self.assertIn(heading, readme)
        self.assertIn("Hi, I’m nlin", readme)
        self.assertIn("一名生物专业的学生", readme)
        self.assertIn("AI Agent、本地模型和多模态 AI", readme)
        self.assertNotIn("理解复杂系统的不同入口", readme)
        self.assertNotIn("models become tools", readme)

    def test_featured_projects_link_to_real_repositories(self):
        readme = self.readme()
        for repository in (
            "ultra-studio",
            "quiz-studio",
            "Minecraft-mod-speedforce",
            "CanvasDesignStudio",
        ):
            self.assertIn(
                f"https://github.com/zenghaolinz/{repository}", readme
            )

    def test_profile_uses_only_local_visual_assets(self):
        readme = self.readme()
        self.assertIn("./assets/profile-hero.svg", readme)
        forbidden_hosts = (
            "shields.io",
            "github-readme-stats",
            "streak-stats",
            "komarev.com",
            "readme-typing-svg",
        )
        for host in forbidden_hosts:
            self.assertNotIn(host, readme)
        remote_images = re.findall(r"!\[[^]]*\]\((https?://[^)]+)\)", readme)
        self.assertEqual([], remote_images)

    def test_hero_svg_is_accessible_and_contains_approved_direction(self):
        path = self.ROOT / "assets/profile-hero.svg"
        root = ET.parse(path).getroot()
        namespace = {"svg": "http://www.w3.org/2000/svg"}
        title = root.find("svg:title", namespace)
        description = root.find("svg:desc", namespace)
        self.assertIsNotNone(title)
        self.assertIsNotNone(description)
        self.assertTrue((title.text or "").strip())
        self.assertTrue((description.text or "").strip())
        svg_text = path.read_text(encoding="utf-8")
        for phrase in (
            "FIELD NOTES",
            "Biology student,",
            "building with AI.",
            "AI AGENTS",
            "MINECRAFT MODDING",
        ):
            self.assertIn(phrase, svg_text)


if __name__ == "__main__":
    unittest.main()
