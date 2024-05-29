# Performance testing

To measure performance, we used a variant of Dhrystone 2 Test originally taken from this [page](http://www.roylongbottom.org.uk/dhrystone%20results.htm). 
The Original version used `clock()` to calculate delta time. Which is good for a real pc, but is not very accurate for a 
dosbox emulator. When the `clock()` call happened, a modified version sends `~>dtime` marker to stdout which is intercepted
by the test page and used to calculate delta time with `performance.now()` from the browser. Source code of the modified test is [here](https://github.com/js-dos/programs).

Basically, this test produces a lot of int operations and measures the amount of operations (Dhrystones) produced per second. 
Output is a `VAX MIPS RATING` which is Drhystones per second divided by 1757 (is as DEC VAX 11/780 result).

## Running the test


To run the test visit [Test](https://dos.zone/dhrystone-2-test-jul-2020/) page. You can choose any backend you want.

![dhry2.png](dhry2.png)




