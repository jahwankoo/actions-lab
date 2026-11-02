import io

import pytest
from PIL import Image

import make_card as mc


def test_same_date_same_card_different_date_different_card():
    assert mc.render("2026-11-10") == mc.render("2026-11-10")
    assert mc.render("2026-11-10") != mc.render("2026-11-11")


def test_size_and_format():
    img = Image.open(io.BytesIO(mc.render("2026-11-10")))
    assert img.size == (mc.WIDTH, mc.HEIGHT) and img.format == "PNG"


def test_bad_date_rejected():
    for bad in ("tomorrow", "2026-1-1", "", "2026-11-10; rm -rf"):
        with pytest.raises(ValueError):
            mc.render(bad)


def test_readme_update_is_idempotent_and_keeps_other_text(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(f"# Title\n\n{mc.START}\nold\n{mc.END}\n\nFooter\n", encoding="utf-8")
    assert mc.update_readme(readme, "2026-11-10", "cards/latest.png") is True
    text = readme.read_text(encoding="utf-8")
    assert "2026-11-10" in text and text.startswith("# Title") and text.rstrip().endswith("Footer")
    assert mc.update_readme(readme, "2026-11-10", "cards/latest.png") is False  # nothing new to write
    assert mc.update_readme(readme, "2026-11-11", "cards/latest.png") is True


def test_missing_markers_or_file_is_not_an_error(tmp_path):
    plain = tmp_path / "README.md"
    plain.write_text("no markers", encoding="utf-8")
    assert mc.update_readme(plain, "2026-11-10", "cards/latest.png") is False
    assert mc.update_readme(tmp_path / "nope.md", "2026-11-10", "x") is False


def test_main_writes_files(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(f"{mc.START}\n{mc.END}\n", encoding="utf-8")
    assert mc.main(["--date", "2026-11-10", "--out", str(tmp_path / "cards"), "--readme", str(readme)]) == 0
    assert (tmp_path / "cards" / "latest.png").exists() and (tmp_path / "cards" / "2026-11-10.png").exists()
