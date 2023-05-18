# Robotic Researcher
The purpose of this software robot is to find key information about important scientists
and display it to the user.

rpaframework is used to complete this task. Documentation for the provided library can be found [here](https://rpaframework.org/#)
When this robot is run, it should:

1. Introduce itself and explain the steps it's about to take.
2. Navigate to the wikipedia page of the scientists found in the list SCIENTISTS.
3. Retrieve the dates the scientists were born and died and calculate their age. Also, 
    retrieve the first paragraph of their wikipedia page.
4. Display all of this information to the user in an easily understood manner. 

## Run the project: 
```commandline
pip install -r requirements.txt 
python main.py
```

## Project structure: 

main.py runs the Robotic Researcher. <br />
robotics.py contains Robot implementation <br />
settings/static.py contains static constants  <br />
settings/types.py contains dataclass Scientist, which holds the necessary information, which should be displayed. 
