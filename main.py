# Given a list of access log records create a program showing only events for a given set of users (frank, ann etc..)
# and given set of fields (host, user, method, status, duration) .
# 127.0.0.1 frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 232

# Provide a report :
# 1) host, user, method, status, duration
# 2) count requests per user, average duration per user


logs = ['127.0.0.1 frank [10/Oct/2000:13:55:36 -0700] "GET /res1 HTTP/1.0" 200 100 ',
        '192.0.0.1 anonymous [10/Oct/2000:13:55:36 -0700] "GET /res2 HTTP/1.0" 200 5000',
        '192.0.0.1 joe [10/Oct/2000:13:55:36 -0700] "PUT /some/resource HTTP/1.0" 200 3000',
        '127.0.0.1 frank [10/Oct/2000:13:55:36 -0700] "POST /test HTTP/1.0" 200 500',
        '127.0.0.1 joe [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326',
        '10.0.0.1 anonymous [10/Oct/2000:13:55:36 -0700] "GET /res1 HTTP/1.0" 200 50',
        '192.0.0.1 joe [10/Oct/2000:13:55:36 -0700] "DELETE /some/resource HTTP/1.0" 200 150',
        '127.0.0.1 frank [10/Oct/2000:13:55:36 -0700] "POST /test HTTP/1.0" 200 500',
        '127.0.0.1 joe [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 10000',
        ]
# --------------------------------------------------
# IMPLEMENTATION
# --------------------------------------------------
dictLine = []

for i in logs:
    content = i.split()

    logLine = {  # parse logs
        'host': content[0],
        'user': content[1],
        'method': content[4],
        'status': content[7],
        'duration': content[8]
    }
    dictLine.append(logLine)

# create a report with host, user, method, status and duration
with open('report_for_1.txt', 'w', encoding='utf-8') as f:
    for i in dictLine:
        f.write(str(i) + '\n')
# ----------------------------------------------------------

# dictionary with information about number of requests and sum of requests durations per user
sumPerUser = {}

for i in dictLine:  # going through previously created list of parsed logs
    if i['user'] in sumPerUser:
        currUser = sumPerUser[f'{i["user"]}']
        currUser['duration'] += int(i['duration'])  # adding duration to already existing duration
        currUser['number'] += 1  # adding request to already existing number of requests
        currUser['average'] = round(int(currUser['duration']) / int(currUser['number']))  # calculating average duration

    else:
        sumPerUser[i['user']] = {  # adding new user information to dictionary
            'number': 1,
            'duration': int(i['duration']),
        }

# create a report with number of requests and average duration of request per user
with open('report_for_2.txt', 'w', encoding='utf-8') as f:
    for i in sumPerUser:
        f.write(str(i) + ' = ' + str(sumPerUser[i]) + '\n')
