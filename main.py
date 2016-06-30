import os
import time

time.sleep(120)
print "Code release 1.2"
print "Downloading new source..."
process = Popen(["sh", "swupgrade.sh"], stdout=PIPE)
(output, err) = process.communicate()
print output
exit_code = process.wait()
if not exit_code:
    print "New source downloaded. Restarting Client.py"
    os.execl(sys.executable, *([sys.executable]+sys.argv))
