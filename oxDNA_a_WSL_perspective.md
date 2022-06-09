# oxDNA: a WSL perspective
#### This document is meant for the casual Linux user that does not want to give up the dark side of Windows for all of the light that Linux could offer. 
#### In particular, it is meant to be for those planning to use oxDNA on Windows, through the installating of Linux through the Windows Sub System for Linux (WSL) feature developed by Microsoft. 

## Quick Reminders: quick cheat sheet for common commands that you will need along your journey. 
Conversion of the .dat files to .dat.mgl files for cogli2 to read : `oxDNA_cogli filename.dat`

## Installing WSL
First thing's first: installing WSL on your Windows OS. 
So installation is relatively straightforward and it is done using the Powershell in Windows but run as an administrator. 

Almost all the documentation on installing WSL can be found here, and I don't recommend consulting other sources before fully utilising this because it can lead to quite dirty installs.

In theory, they recommend to install WSL using a simple install command but it didn't work for me and I followed the steps for manual installation and that worked fine. 

Note: At the time of writing this I am using WSL1 but WSL2 is also available. But I was not able to upgrade it, in particular I had a specific error when installing the Ubuntu linux distribution so this document is mainly for WSL1 usage. Also all information on updates are found on the WSL website and once again I recommend to consult the official website before verging into other blogs. However I was not able to upgrade it probably due to a hardware limitation of my machine, in theory it should be fine and smooth (fingers) crossed to install WSL2. In the end it does not matter too much other than to get a Linux OS (or sub-OS) working on your system. 

This is the official documentation for WSL: https://docs.microsoft.com/en-us/windows/wsl/install

### Installing a Linux Distribution
Note: When choosing a Linux distribution to install, I think the most common is Ubuntu! 

But some important lessons from past experiences:
 - Perform the installation from the Powershell as indicated on the WSL documentation and do not do it from the Microsoft store. It is a much cleaner way!
 - Make sure you only have one Linux distribution installed unless you intentionally choose to have more than one otherwise, you can check this with the Powershell command: `wsl -l -v`. Make sure there are no installed distributions before installing the desired one. 
 - And for Ubuntu: ONLY USE THE LTS (long term support) versions! I once accidently, without knowing better, updated to the developer version of future versions. They are beta versions for the next LTS release. DO NOT DO THIS! It caused a lot of issues with packages and I had to uninstall Linux and perform a clean install from that. 

Here is a rough introduction to Bash functionality written by Prof. Rovigatti, howeve it is worthwhile to look up some simple Bash commands on how to work on Linux: 
https://codimd.infn.it/s/UaU9rb0PS

But I guess depending on who is reading this, it will be either too advanced or too simple a starting point for Linux so judge accordingly and don’t worry as there are plenty of resources online for getting familiar enough to start. Just don't get overwhelmed. It's a process and one that you will get familiar with in due time.

## Text Editor of Choice for WSL
So of course you will need a text editor and this is really a subjective thing. I think based on what experience you had previously and what you’re familiar with, if there is a version available that works well for WSL Linux then go for it, and don’t get lost in the videos of people telling you why a certain text editor is best. 

For me however, the last time I was in the Linux world, I was using Geany for C++ coding but it was only because it was what the Professor was using for the course (https://www.coursera.org/learn/initiation-programmation-cpp), but I didn’t much like the layout (#personal_preference) nothing wrong though. Then was using ATOM for casual text editing but to my greatest “surprise” (#sarcasm), ATOM has a known issue with running on WSL. And it’s not an issue that exists because you run a windows version and a Linux version at the same time, so forget about it and don’t waste time trying to install it, unless it is solved by the time that you're reading this. 

I think the best, if you were like me and needed to choose one to get started with, is VS Code. The advantage is that there is extensive WSL documentation and it’s made to be compatible with WSL (also developed by Micorsoft). Meaning you install it in your windows system and with a specific configuration, you can run in on Windows as well as WSL. It’s the best plug and play solution. The only disadvantage is that if your system is slow, it might eat up a lot of RAM on your machine. 
Here is the guide to installation: https://code.visualstudio.com/docs/remote/wsl
(NOTE: installation is done on the Windows side!)


note: There is a character is this story which I will anonymously call "WSL_Yoda", he is a friend that is studying data science and hoped on the WSL train a few months before I did and a lot of the recoomendations and problem fixes I owe to Master WSL_Yoda. 

### vim
BUT, that being said, still get used to VIM, as it’s very light on the system, very fast to edit, and is used by almost all Linux users at some point. Might be worth it to also look online for some plugins/themes that might suit you, but definitely worth the effort to get used to using it initially, it is not obvious how to so if you're not familiar with it, please do take the time to have a look and how to use it, at least basically. You will find yourself using it more that you anticipated.

## Installing oxDNA
Installing oxDNA is relatively straight forward. 
Before installing make sure you have all the dependencies and here you can double check them: 
https://dna.physics.ox.ac.uk/index.php/Download_and_Installation

Then installation can be done using the following instructions found here, along with a simple tutorial on how to perform a simple LJ simulation: 
https://codimd.infn.it/s/nzcFp_9o9#


## Installing Jupyter Notebook for WSL

For a lot of Windows users that code on Python, Jupyter notebook is a common choice. Although it’s not so straight forward to install for WSL especially if you want it to behave like it does for Windows. 

Here are some guidelines. 
To install it, it is best to install it using pip3. 
```
sudo apt update && upgrade 
sudo apt install python3 python3-pip ipython3
sudo apt install python3-pip
```

These commands should install python3 and pip3 which can then be used to install jupyter notebook using the following command: 

```
pip3 install jupyter
```

Then to configure it to work like in Windows, do the following as listed in this blog: skip straight to the part about “Configuring Jupyter Notebook” and ignore the part on Windows Terminal, you will not need it and it’s his personal preference. The Ubuntu Terminal will serve you just fine unless you really believe otherwise. 

https://towardsdatascience.com/running-jupyter-notebook-on-wsl-while-using-firefox-on-windows-5a47ebfae4c1

Note: but once you install Jupyter Notebook and have it working, you will soon find it more convenient to learn how to incorporate usage and use VS Code. It works relatively well and it will avoid you having to constantly run/shut down kernels form the terminal and not being able to do anything else while running it. But of course, this is more of a preference thing and something that has to be decided as you go on and get familiar with everything. And another advantage is that you can directly run a "bash Terminal" in VS Code for WSL which makes things much more convenient. 

*Advice:* As convient as Jupyter Notebook might be, you will soon realise that it slowly becomes less convient and you will slowly find that it is better to learn how to code in python and directly compile on the terminal. Depending on how and what you are using it for, there are advantages and disadvantages but my advice is get used to using both ways of coding/running/compiling python code. Both the sof- and hard- core ways have their strengths and weaknesses. 


