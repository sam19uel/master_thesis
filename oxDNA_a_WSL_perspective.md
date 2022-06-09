# oxDNA: a WSL perspective.
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

