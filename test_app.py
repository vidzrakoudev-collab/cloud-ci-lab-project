import subprocess

def test_app_runs():
    result = subprocess.run(
        ["python3", "app.py"],
        capture_output=True,
        text=True   
    )
    assert result.returncode == 0