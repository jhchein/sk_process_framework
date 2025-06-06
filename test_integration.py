import subprocess
import sys


def test_part1_runs():
    """Test that part1.py runs end-to-end without error."""
    result = subprocess.run(
        [sys.executable, "part1.py"], capture_output=True, text=True
    )
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    assert result.returncode == 0, f"part1.py failed with exit code {result.returncode}"


def test_part2_runs():
    """Test that part2.py runs end-to-end without error."""
    result = subprocess.run(
        [sys.executable, "part2.py"], capture_output=True, text=True
    )
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    assert result.returncode == 0, f"part2.py failed with exit code {result.returncode}"
