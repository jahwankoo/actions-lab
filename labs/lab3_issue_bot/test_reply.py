import json

import reply as r


def test_keyword_rule_and_default():
    assert "need help" in r.build_reply("Help me", "octocat")
    assert "bug report" in r.build_reply("A BUG in step 2", "octocat")
    assert r.DEFAULT_RULE in r.build_reply("hello there", "octocat")


def test_haiku_is_deterministic():
    assert r.pick_haiku("same title") == r.pick_haiku("same title")
    assert r.pick_haiku("x") in r.HAIKUS


def test_untrusted_text_is_neutralized():
    nasty = "hi @everyone `$(curl evil)` \n\n [click](http://x) " + "z" * 200
    out = r.build_reply(nasty, "octocat")
    assert "@everyone" not in out and "@" + r.ZWSP + "everyone" in out
    assert "$(curl evil)" in out and "`$(curl evil)`" not in out  # backticks inside the quote are removed
    assert "..." in out and len(out) < 1200


def test_bad_login_and_empty_title():
    out = r.build_reply("", "bad login; rm -rf /")
    assert "friend" in out and "(no title)" in out and "0 words" in out
    assert "@octocat" in r.build_reply("x", "octocat")


def test_main_reads_event_file(tmp_path):
    event = tmp_path / "e.json"
    event.write_text(json.dumps({"issue": {"title": "Idea: stars", "user": {"login": "ada-l"}}}), encoding="utf-8")
    out = tmp_path / "reply.md"
    assert r.main(["--event", str(event), "--out", str(out)]) == 0
    text = out.read_text(encoding="utf-8")
    assert "@ada-l" in text and "An idea" in text


def test_main_tolerates_missing_fields(tmp_path):
    event = tmp_path / "e.json"
    event.write_text("{}", encoding="utf-8")
    out = tmp_path / "reply.md"
    assert r.main(["--event", str(event), "--out", str(out)]) == 0
