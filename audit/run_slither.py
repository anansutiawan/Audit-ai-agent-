import subprocess

def run_slither_audit(filename):
    try:
        result = subprocess.run(
            ["slither", filename],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Slither error: {e}"
