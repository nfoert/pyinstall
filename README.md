# Auto Pyinstaller
A cross-platform quick pyinstaller

**THIS ISN'T PYINSTALLER, NOR DID I MAKE PYINSTALLER, THIS IS JUST A UTILITY THAT I MADE THAT *USES* PYINSTALLER**

Tired of typing `pyinstaller <spec file>.spec` all the time? Me too. So I made this script. It's deisgned to live in your project directory and used with Visual Studio Code. You can quickly create an executable by using `F5 + b` (F5 Because F5 is used in IDLE for running code)

## Setup
Download the `pyinstall.py` file and drop it into your project directory. Make sure `colorama` and `pyinstaller` are installed.

Next, open the command palatte by using `Control + Shift + P` and type `Keyboard` or something until you see `Prefrences: Open Keyboard Shortcuts`. Select it.

Now, press the little button on the right side. It looks like a piece of paper and an arrow.

![Piece of paper and an arrow](images/button.png)

That will open your custom keybindings file (`keybindings.json`)

In this file make it have the following:
```
// Place your key bindings in this file to override the defaultsauto[]
[
    {
        "key": "f5 b",
        "command": "workbench.action.terminal.sendSequence",
        "args": {
          "text": "python pyinstall.py\u000D"
        }
     },
]
```

If you already have keybindings in this file just add this instead:
```
{
        "key": "f5 b",
        "command": "workbench.action.terminal.sendSequence",
        "args": {
          "text": "python pyinstall.py\u000D"
        }
     },
```

Save the file. Next, open `pyinstall.py` and modify this section at the top. Replace example.py with the name of your `.spec` file or your `.py` file.
```
# Enter the name of your .spec or .py file here:

specfile_windows = "example.py"
specfile_mac = "example.py"

# -------------------------------------
```

Done! Give it a try by typing `F5 + b` You should see something like this: (Do note that you have to have an existing terminal open)
```
--------------------------------------------------------------------------
                _          _____       _           _        _ _
     /\        | |        |  __ \     (_)         | |      | | |
    /  \  _   _| |_ ___   | |__) |   _ _ _ __  ___| |_ __ _| | | ___ _ __  
   / /\ \| | | | __/ _ \  |  ___/ | | | | '_ \/ __| __/ _` | | |/ _ \ '__| 
  / ____ \ |_| | || (_) | | |   | |_| | | | | \__ \ || (_| | | |  __/ |    
 /_/    \_\__,_|\__\___/  |_|    \__, |_|_| |_|___/\__\__,_|_|_|\___|_|    
                                  __/ |
                                |___/
    Cross-Platform Pretty Pyinstaller by nfoert
--------------------------------------------------------------------------
Selected OS: Windows
PREPARE FOR PYINSTALLING
--------------------------------------------------------------------------
Starting in 1
```

I hope this little utility saves you some time. It certainly has saved some of mine.
