# Mario Royale AI
The very first Mario Royale... AI? No, it's more of an A.<br>
This [Python](https://python.org) program rolls a dice and chooses a random input once every .8 seconds.<br>
![ScreenShot](assets/bash.png)<br>
The program logs it's decisions and prints it in the console, and you get to watch it suffer.<br>
![ScreenShot](assets/goomba.png)<br>
There is absolutely zero strategy, good luck having the "AI" pass the 1-1 goomba.

## Version 1.1 Patch Notes
The software will now show a count.. up before it starts up<br>
You can now change the input interval from **configuration.cfg**, though it will subtract 0.8 from the value<br>
Added a config file in general, though not much plans to update it.<br>

## To look forward to?
Rebinding controls through the configuration<br>
Proper error handling for no configparser module (even though this should have been done already lol)

## Installation
You will need a program and pip to run the software
- Install [Python](https://python.org) from the official website
- Download/clone this repository then extract it to a folder, then cd into it
- Install the **pynput** package from pip3
- Install the **configparser** package from pip3

## Notes
The program will start 5 seconds after being started, so rush into the game before it starts screwing your desktop.<br>