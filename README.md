# Python - async and multi-process

This is a sample project created to demonstrate methods for improving performance of CPU
intensive(ish) code. It solves the problem of generating prime factors of given numbers using.

* Traditional synchronous code
* Asynchronous code
* Simple multi-processing

This was tested on my home laptop (Intel Core i7 @ 1.9Ghz with 8 cores) with the following
results.

_N.B._ At the time of running the laptop was in power-saving mode

Attempt # | Sync  | Async | Multi-Process
--------- | ----- | ----- | -------------
1         | 20.66 | 17.42 | 13.72
2         | 20.14 | 16.18 | 12.93
3         | 19.55 | 18.55 | 12.8

As expected the multi-process solution performed better given the type of work being
performed, with some slight improvements found by using async.