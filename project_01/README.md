# Les PocketBeagle

Morde detailed instructions can be found here : [https://www.hackster.io/tk52/edes-301-les-pocketbeagle-60fc74] (Les PB Hacksterpage)

Here are software instructions for EDES301 Les PB project
Unfortunately the listener script works for Mac ONLY. Please modify as you see fit for other Operating Systems.

Copy the folders Les PB and Button to your Pocket Beagle. Run the script by running the command 
`sudo ./run`

Then on your Mac run this command before plugging in your serial adapter
`cd /dev/`

And run it again after plugging in your serial adapter
`cd /dev/`

Find what the new device is by noticing what changes between the two terminal outputs, in my case it is **tty.usbserial-0001**, but for you it may be different. 
Then change line 7 appropriately, in the **listen_key.py** file


## To use/ test the system
*Run the Les PB code on the Pocket Beagle. Wait for the lights to be configured.
*Run the listen_key.py file on your laptop
*Open a TextDocument, Google Doc etc
*Press the buttons youve wired up!

If everything is set up correctly, you should see text output on your screen, varying with the length of your press!
Like I explained in the hackster, it unfortunately doesnt work due to the rules of Clone Hero , but it's a great start to a macro pad ! haha
