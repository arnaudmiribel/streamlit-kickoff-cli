from pathlib import Path

from ..main import _target_is_valid, parse_target


def test_target_is_valid():
    assert _target_is_valid(
        "https://github.com/streamlit/streamlit-example/blob/master/streamlit_app.py"
    )
    assert not _target_is_valid(
        "https://github.com/streamlit/streamlit-example/blob/master/streamlit_app"
    )
    assert not _target_is_valid(
        "https://github.com/streamlit/streamlit-example"
    )
    assert not _target_is_valid("https://google.com/")
    assert not _target_is_valid("foo")


def test_parse_git_url():

    (
        repository_url,
        project_path,
        streamlit_script_path,
        requirements_path,
    ) = parse_target(
        "https://github.com/streamlit/streamlit-example/blob/master/streamlit_app.py"
    )

    print(repository_url)
    print(project_path)
    print(streamlit_script_path)
    print(requirements_path)

    assert (
        project_path == Path("streamlit-example")
        and repository_url == "https://github.com/streamlit/streamlit-example"
        and streamlit_script_path == (project_path / "streamlit_app.py")
        and requirements_path == (Path(project_path) / "requirements.txt")
    )
