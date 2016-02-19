import praw, sys, os
from collections import deque
from time import sleep
from subprocess import Popen, STDOUT

r = praw.Reddit(user_agent='client:v1.0 /u/testapipraw')
done = deque(maxlen=300)
while True:
	submissions = r.get_subreddit(sys.argv[1]).get_new(limit=10)
	if not submissions:
		sleep(10)
		continue
	for sub in submissions:
		if sub.id not in done :#and sys.argv[2].lower() in sub.title.lower() :
			tags = sys.argv[2].lower().split(',')
			if any(x in sub.title.lower() for x in tags):
				done.append(sub.id)
				os.system('cvlc --play-and-exit ~/beep.mp3')
				Popen(['google-chrome', sub.permalink], stdout=os.open(os.devnull, os.O_RDWR), stderr=STDOUT)
	sleep(10)