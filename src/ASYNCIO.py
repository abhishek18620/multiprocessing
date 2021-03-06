"""
Author : abhishek18620
Date : 2018-02-09
File : ASYNCIO

Topic : Asyncio
Link : http://www.aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html
"""
import asyncio

def ii():
    return int(input())

def mi():
    return map(int, input().split())

def li():
    return list(mi())

@asyncio.coroutine
def solve1():
    for i in range(10):
        print("solve 1" + repr(i))
        yield from asyncio.sleep(1)

@asyncio.coroutine
def solve2():
    for i in range(10):
        print("solve2" + repr(i))
        """
        yield (return) : hands the control
                         back to event loop
        """
        yield from asyncio.sleep(1)

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    sol1=asyncio.async(solve1())
    sol2=asyncio.async(solve2())
    loop.run_forever()
    loop.close()
    print("Finished")

