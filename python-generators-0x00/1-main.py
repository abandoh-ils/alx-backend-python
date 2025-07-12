
from itertools import islice
from streamer_users import stream_users
# stream_users = __import__('0-stream_users')


# iterate over the generator function and print only the first 6 rows

for user in islice(stream_users(), 6):
    print(user)