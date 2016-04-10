# PyLogger
A free key logger made in Python.

If you care to, please donate me money for my efforts. All money donated will be used in training courses for me to learn how to give better names to my programs.

### Running the key logger

#### From source code
- Clone the repo or download the zip file through the zip file button
- Install python2.7
- Add python to your environment variables
- Open command prompt and run with `python logger.py`
- To stop logging, use ctrl-c anywhere
- The logfile will be called User_[Year][Month][Day]_[Hour][Minute][Second], and will be in the same directory as logger.py

#### From the executable
- Clone the repo / grab the logger.exe file from the bin folder
- Run it.
- To stop logging, use ctrl-c anywhere
- The logfile will be called User_[Year][Month][Day]_[Hour][Minute][Second], and will be in the same directory as the executable. It can't really get easier than this.

### Supported locales
pt_PT

### Supported operating systems
Windows

### How can I help?
Aside from suggesting features (use [this](https://github.com/sceptross/KeyLogger/issues) page for that, by clicking in "New issue") you can't. You will be able to once I have time for adjusting the code for supporting serveral locales and eventually if I feel like making a GUI, several languages, but that isn't gonna happen until I finish some university work. Every suggestion you make will really only be implementable after that.

### I modified the code and want to generate an .exe, how can I do it without getting a bunch of useless files?

- Install python2.7 (if you modified the code you probably did this already)
- Add python and the Scripts folder inside your python directory to the environment variables
- Open command prompt and run `pip install pyinstaller`.
- Run [this](http://pastebin.com/q0s7aNGh) batch file in the code directory. This expects you to only have the logger.py file. Modify it to your needs if you made any other files / directories.
- The exe file will be in the bin directory created by the bat script.

# License

This project is licensed under the BSD 3-Clause License. For more information, please read the LICENSE file.
