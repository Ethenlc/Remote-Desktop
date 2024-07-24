# Overview

{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}

This is a program that I wrote to better understand networking. It's a client/server program where the server remote controls the client's cursor. To start the server's program, you press play and it opens a GUI. You can start listening to the correct port and you can stop the server at any time. To start the client's program, you only need to run the client.exe file. It opens a command prompt where you enter the password. 

The purpose for writing this software was to practice the concept of networking. I better understand how to use a client/server program.

[Software Demo Video](https://youtu.be/jzFlQkxPSVI)

# Network Communication

This is a client/server program using TCP on port 9999. 

There are a couple of messages sent from the server to the client and back. Most of them are to communicate if everything is working properly.

# Development Environment

This program is using python language. It's high-level and it is good for this application because it's simple and readable. There are also lots of libraries that I used in this program.

* socket - This library provides low-level network interface for using sockets, which allow communcation between computers.
* pyautogui - This is an automation library for Python that allows you to control the mouse in this program. 
* cryptography - This library is used for ecryption and decryption. In this program, it's used for the password.
* tkinter - This is a standard Python library used for GUI.
* threading - This allows the creation of multiple threads of control with just a single process. It's especially useful for network operations like this one.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python Server Libraries](https://docs.python.org/3.6/library/socketserver.html)
* [Python Socket Libraries](https://docs.python.org/3.6/library/socket.html)
* [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)

# Future Work

Here are some things that I'd like to add to this program in the future.

* The ability to click on the client's computer.
* The ability to see what the client's computer is seeing so I can better control it.
* Faster connection so that the cursor isn't delayed by so much.