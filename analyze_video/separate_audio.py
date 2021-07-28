import subprocess

print('work?')
subprocess.run(['docker', 'exec', '-it', 'separate_audio', 'python', 'analyze/src/separate_audio.py'])
subprocess.run(['docker', 'exec', '-it', 'transcript_audio', 'python', 'analyze/src/transcript.py'])