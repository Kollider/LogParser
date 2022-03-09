# LogParser
# Given a list of access log records create a program showing only events for a given set of users (frank, ann etc..)
# and given set of fields (host, user, method, status, duration) .
# 127.0.0.1 frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 232

# Provide a report :
# 1) host, user, method, status, duration
# 2) count requests per user, average duration per user
