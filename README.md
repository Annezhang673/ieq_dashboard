# Read me for IEQ interface

## Backend Setup

Backend part of this system is a python program that provides real-time data (json file) of Linklab to frontend interface every 5 minutes.

Operating environment:

1. OS: Windows10
2. python 3.8.13
3. go to ./backend/ and run following command

```shell
$ pip install -r requirements.txt
```

4. In order to run the backend program, you need to setup the env file in ./backend/, however, I will not provide this on github since it is key to Linklab IEQ server. If you are a student or faculty in this class, you should know where it is. So, download the env file and put it in ./backend/, then, run following command

```shell
$ mv env .env
```

5. Now you can run ./backend/real_time_IEQ.py and this program will automatically generate Linklab data to frontend interface



## Frontend Setup

After activating the backend part, we can setup the front end interface now.

1. run following command at root (./) to install node.js

```shell
npm install -g npm
```

2. Then, run following command to activate the interface on localhost:3000

```shell
npm start
```

now, you can see the front-end interface, this interface will update automatically every 5 minutes if you have activated the backend program.

## Group members
Blake Wang, Xinyue Fan, Anne Zhang, Francis Becker
