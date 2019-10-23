# Agent-Based Modelling in Python
A project done as part of [the Data CDT](https://datacdt.org/)'s GEOG5995M/ENVS802 module: **Programming For Social Scientists**.

This project is the result of working through [the practical exercises](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/) put together by [Andy Evans](https://ajevans.github.io/) to teach core programming skills to students starting a four-year integrated PhD and MSc in Data Analytics and Society.

It is 'licensed' under the [The Unlicense](https://unlicense.org/), and available on [my Github](https://github.com/peterprescott/agent-based-modelling). 

It is intended to be [run from the command line](https://www.howtogeek.com/437682/command-lines-why-do-people-still-bother-with-them/), though the project includes the beginnings of a Tkinter GUI, as well as a proof-of-concept of a web-page GUI with code written in JavaScript instead of Python.

You need to have Git and Python installed. If you don't, use your system's recommended package manager to download them from the command line. (For Windows, use [Chocolatey](https://chocolatey.org/install).)

Then clone the Github repository, and navigate into the project folder. You can then immediately run the model:

```console
python --version
git --version
git clone https://github.com/peterprescott/agent-based-modelling
cd agent-based-modelling
pip install -r requirements.txt
python run_model.py
```

[![asciicast](https://asciinema.org/a/6ldhFPdvzJSHvyrVz0bcSQJp2.svg)](https://asciinema.org/a/6ldhFPdvzJSHvyrVz0bcSQJp2)
<script id="asciicast-6ldhFPdvzJSHvyrVz0bcSQJp2" src="https://asciinema.org/a/6ldhFPdvzJSHvyrVz0bcSQJp2.js" async></script>

If everything is working correctly, you should be told the *Initial Parameters* with which the model is running (as ```python run_model.py``` doesn't specify any, the model will use the defaults), and that the various steps of running the model have successfully taken place, including how long it took to run the model, and the details of the machine you are using to run it. The output data is saved in the ```output_files``` folder.

If you are interested in testing the speed of the model with iterations of various orders of magnitude, then you can use the ```tests.sh``` or ```tests.bat``` script to do so efficiently. 

[![asciicast](https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA.svg)](https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA)
<script id="asciicast-WO9oNzJcxv3veBcjtm7FRpjEA" src="https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA.js" async></script>

But you probably want to be able to **see** what your model is actually doing. We use [Matplotlib](https://matplotlib.org/) for the graphic visualization. You then run ```python run_model.py animate```, or just `python run_model.py a``` if you're feeling lazy. (In fact, any word beginning with 'a' should do the trick!)

```console
pip install -r graphic_requirements.txt
python run_model.py animate
```


