Any steps necessary to run your program on the command line, including compilation steps (if required) and the runtime versions you used

Import the following libraries:

import json
import pandas as pd
import re
from collections import deque

Written in Python: 3.7.2
Writtem by Mostofa Adib Shakib.

This script expects the cvs file and the json file to be on the same directory. 

Any interesting trade-offs or edge cases you ran into:

I used a variety of data structures which can make the program a bit slower.

One of the many edge cases I thought of was for classes where we have multiple keywords which are repeated more than one for the same genre hence I have a dictionary to keep tracker of all the entries which I latter use to take the average and multiple the average with the total activity.
I am using 

Approximately how long you spent (this is not timed, but it’s helpful for us)

I spent about 2 hours, the hardest thing for me in this project was finding the average for keywords that are repeated.



I would like to thank BookBub for allowing me to take this take. I learnt a great deal from this chanllenge and have a great experience.
