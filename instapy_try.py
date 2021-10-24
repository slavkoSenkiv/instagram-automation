import datetime

from instapy import InstaPy
import time

# <editor-fold desc="get credentials">
current_working_account = open('/Users/ysenkiv/Code/my projects/instagram automation/curent_working_account.txt', 'r')
account = current_working_account.read(); print(account)
path_to_credentials = f'/Users/ysenkiv/Code/access files/personal/instagram/{account}.txt'

with open(path_to_credentials) as credentials_file:
    lines = credentials_file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
# </editor-fold>

print(username, password)
start_time = time.time()
session = InstaPy(username=username, password=password)
# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.login()
session.like_by_tags(["cutedog"], amount=1)
session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=100)
# session.set_do_comment(True, percentage=100)
# session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
print('script run time', time.time() - start_time)