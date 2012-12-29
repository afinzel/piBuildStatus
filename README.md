piBuildStatus
=============

Using the Raspberry Pi to monitor tweets for build status and turn on traffic lights

Installation
------------
1. Take apart a lava traffic light http://www.amazon.com/gp/product/B001ETWW0M?tag=spiblog-20
2. Disconnect the lights
3. Connect as follows:

------------------------------------------------
<Network                     <USB power port>


          --------- amber light
          |           ---------- connect to all lights
          |           |
o o o o o x o o o o o x
o o o o x x o o o o o o
        | |
        | ------ red light
        --------- green light

-----------------------------------------------

4. Install twitter plugin for jenkins
5. Setup the plugins and get it to post to a twitter account
6. Modify the twitter_username to be your twitter account
7. Run pip install requirements.txt
8. Run sudo python main.py
