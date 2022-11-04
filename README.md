# Instagram Commenter Bot
## Step 1: Setup (getting the sample request from instagram)
1. Go on the instagram post you want to comment on.
2. Open up developer tools on your browser (ctrl+shift+i | or cmd+option+i on mac) and go to the network tab
3. Post a random comment on the ig post
4. In the network tab, filter with the word "add" and you should see a request.

## Step 2: Getting the python code
1. Right click the request found in Step 1 and copy the curl command (as bash)
2. Go to https://curlconverter.com/ and paste in your curl command.
3. Convert the curl command into python code, then update the "cookies" and "headers" object in `main.py` to the one you got from curlconverter

## Step 3: Run
1. to run, just run main.py
```bash
$ python3 main.py
```
