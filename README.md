# human-benchmarker
This is a small program that I made using Python and some Windows tools to get sub 30 millisecond scores on humanbenchmark.com's Reaction Time test.

This is actually just a really simple Python program. It works simply just by checking if the colour of the pixel that the mouse cursor is hovering on is #4bdb6a hex (or rgb(75, 219, 106)). Then, whenever it detects that the cursor is hovering over this specific colour, it just clicks.

I first implemented this behaviour with PyAutoGui, but that would get results similar to 70-80ms FOR ME. After I switched over to using the ctypes library, it dropped down quite significantly to 30-40ms per click (FOR ME). I'm not sure of a way to make this any faster, as it is already quite dependent on your internet speed and other such limiting factors, and not the just program itself. If you have any suggestions on how to make the program even faster, just let me know in an Issue.

HOW TO USE

By default when you run the .exe it will just open up a command prompt with a blank screen. You are pretty safe to move your cursor around as it will only click if it sees the specific shade of green (#4bdb6a). You can go over to the website and click on the Reaction Time Test : https://humanbenchmark.com/tests/reactiontime

Click anywhere on the blue box to start, and the box will turn red. IMPORTANT : Keep your cursor over a red pixel for the program to work. After a random delay, the box will suddenly turn green. The program will then detect that it has turned green and click, and the box will become blue again and show you how fast you clicked. The program runs indefinitely, so you can just click on the blue box again to continue. The process will happens 3 more times, and at the end it will show you "your" average reaction time.
