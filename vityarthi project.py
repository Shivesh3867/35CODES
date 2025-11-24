import time
from plyer import notification

print("reminder app started")
print("press ctrl c to stop")

r = 1

while True:

    if r == 1:
        notification.notify(title="Water", message="drink water now", timeout=7)
        print("water reminder done")
        time.sleep(2 * 60)
        r = 2

    elif r == 2:
        notification.notify(title="Eye rest", message="rest your eyes for some time", timeout=6)
        print("eye reminder done")
        time.sleep(3 * 60)
        r = 3

    elif r == 3:
        notification.notify(title="Posture", message="sit straight relax back", timeout=7)
        print("posture check done")
        time.sleep(4 * 60)
        r = 4

    elif r == 4:
        notification.notify(title="Medicine", message="take your medicine on time", timeout=6)
        print("medicine reminder done")
        time.sleep(5 * 60)
        r = 5

    elif r == 5:
        notification.notify(title="Breathing", message="take deep breaths slowly", timeout=6)
        print("breathing reminder done")
        time.sleep(2 * 60)
        r = 6

    elif r == 6:
        notification.notify(title="Walk break", message="take a walk move your legs", timeout=7)
        print("walk reminder done")
        time.sleep(3 * 60)
        r = 7

    else:
        notification.notify(title="Rest", message="close eyes relax for few secs", timeout=8)
        print("rest done cycle restart")
        time.sleep(2 * 60)
        r = 1
