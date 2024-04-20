## Hello, stranger
This is a simple tool allowing you to automate some actions on a website, leading to a target page, 
where there is (or there is no) target element.  
For example, each time you want to catch a termin on some website, there is a note "No termins" (usual situation).
What you are expecting is that this note is missing (unusual situation) - then likely finally there are some termins!
In case of the unusual situation you will be notified with a voice message directly from your computer 
(i.e. in the middle of the night).

## How to install
1. Install [pyenv](https://github.com/pyenv/pyenv).
2. Using pyenv, install a Python version higher than the one stated in [pyproject.toml](pyproject.toml).
3. Find a path to the Python interpreter you've just installed using `pyenv which python`.
4. Install [poetry](https://python-poetry.org/docs/)
(e.g. [using `brew`](https://formulae.brew.sh/formula/poetry) on macOS).
5. Set up this project as a poetry project. Set Python interpreter in your IDE for this project.
6. Run `poetry install` to install dependencies.
7. Install browsers and drivers by executing `playwright install`.
Sometimes you have to reopen the IDE beforehand for some reason.

## How to use
### From IDE
You should have a green arrow next to the [`test_catch_termin()`](bot/test_termin_catcher.py) test method, which starts the script.
### By schedule
`!` **Important** `!` Do not set too tight schedule for the script.
You can either DOS the website or get a ban from it. 
Two-three times per night is enough.

Add the script run to your [cron schedule](https://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job) 
with `crontab -e` command. 
Use [this website](https://crontab.guru/) to set the schedule format correctly.
Use the following template:
```
<cron_expression> <path_to_pytest> -s <path_to_bot> >> <log_file> 2>&1
```
Example:
```
05 0 * * 7 /Users/vmoloko/Library/Caches/pypoetry/virtualenvs/termin-catcher-gxpHoPb2-py3.12/bin/python -s /Users/vmoloko/Projects/termin-catcher/bot/test_termin_catcher.py >> /Users/vmoloko/Desktop/termin-catcher-data/log.txt 2>&1
```
### Some schedule mode peculiarities
On macOS, for example, cron doesn't work either when the lid is closed, or with an open lid but a locked screen.
For me, even when only the screensaver is on.  
So if you want the script to run:
* disable all the automatic sleeps and locks,
* do not close the lid,
* adjust the brightness to minimum,
* adjust the sound so you are not too frightened at night (you will be anyway),

and then it will work out. 

## How to customize
Just replace the code in [target_page.py](bot/target_page.py) with your own to catch a termin on another website.