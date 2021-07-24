import subprocess

subprocess.run(['docker', 'exec', '-it', 'separate_audio', 'python', 'analyze/src/separate_audio.py'])