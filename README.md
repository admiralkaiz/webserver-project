# Computer Networks (CII2J4) Final Project: Simple Web Server

Group members:

- Kaisar Kertarajasa

- Satya Rayyis Baruna

- Nadim Rafli Hamzah

## Introduction

In this project, we are making a simple web server written in Python, running on a FreeBSD virtual machine. Here, we are going to demonstrate a network communication between two hosts (Linux desktop and a FreeBSD guest VM) using TCP connection. The Linux desktop acts as a client while the FreeBSD guest VM acts as the server to handle client's request.

## Typographical Conventions

`monospaced` fonts indicate **terminal commands**, **file names**, **paths**, **package names**, **modules**, **source code**, and **URLs**.  

## Why FreeBSD?

There are several reason why do we choose FreeBSD as our server operating system:

- FreeBSD is a **free and open source** operating system, which complies to our project requirement that insist for the usage of free and open-source software.

- FreeBSD is a **lightweight** operating system so that it does not utilize too much system resources so it can run smoothly in our virtual machine without giving excessive load to the host system.

- FreeBSD is a **stable, mature, and robust** operating system which makes it suitable for a server operating system with good **performance** and **security**.

- FreeBSD is **well documented**. The documentation can be read on the <a href='https://docs.freebsd.org/en/books/handbook/'>FreeBSD handbook</a>.

For more information about FreeBSD, please refer to <a href='https://www.freebsd.org/'>its official website</a>. 

## Python for Server Programming

<a href='https://www.python.org/'>Python</a> is used to program the server as its ease of learning and compatible on multiple platforms. Python exhibits a plethora of **library** and **frameworks**, including a `socket` library to make TCP connection between client and server possible. Using Python, a **consise, lightweight, simple** web server program can be made.

## Preparation

1. First, we have to install FreeBSD in a virtual machine. This time, we are using VirtualBox to do this task.

2. Install the operating system. In this `README.md`, we are not going to discuss FreeBSD installation in depth. Make sure to follow every step of installation. If you are on doubt, you may choose the default option, or please refer to the <a href='https://docs.freebsd.org/en/books/handbook/bsdinstall/'>installation guide</a>. 
    
    Note: make sure IPv4 and DHCP configuration is enabled for the chosen network interface.

3. In the FreeBSD guest VM, make sure Python is installed. You can decide to use either `pkg` or ports to install `python`. A text editor such as `vim` is needed as well to write the server.

    Note: when logging in as a non-root user, make sure to utilize `doas` or `sudo` before proceed on using `pkg` or ports to install any package. 

## Running the Server

1. Copy the server source code into the FreeBSD guest VM. Preferrably to the home directory of a non-root user.

2. Place the HTML files in the same directory of the server.

3. To establish connection between host machine to the guest VM, in the network settings of the VM, please change Adapter 1 option to Host-Only Adapter. If you don't have any adapter yet, you may create a new adapter in Host Network Manager, and make sure the DHCP Server option is checked. For other options, please keep them in default setting.

4. Run the server with `python` command.

5. In the host machine, open a web browser, and type `http://<your-server-ip-address>:<port-number>/<path-to-file>`. For example: `http://192.168.###.###:8080/index.html` 

6. Check out the result and... _Voila!_ 
