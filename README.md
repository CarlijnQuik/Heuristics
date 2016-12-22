# Heuristieken

## Run Algorithms

To run the different algorithms, open up main.py and paste the correct lines at the bottom of the script.<br />
Function arguments marked with `<>` are optional. Function arguments marked with `[]` are required. All other arguments should be left untouched.

#### Run Random Hillclimber
```python
random_hillclimber = hillclimber.random_hillclimber(schedule, courses, <desired_score>, <max_duration>)
write_csv(random_hillclimber["schedule"])
```

#### Run Guided Hillclimber
```python
guided_hillclimber = hillclimber.guided_hillclimber(schedule, courses, <desired_score>)
write_csv(guided_hillclimber["schedule"])
```

#### Run  Random Simulated Annealer
```python
random_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, [desired_score], <starting_temperature>, <max_duration>)
write_csv(random_simulated_annealer["schedule"])
```

#### Run Guided Simulated Annealer

```python
guided_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, [desired_score], <starting_temperature>, <max_duration>)
write_csv(guided_simulated_annealer["schedule"])
```

#### Write CSV
The `write_csv` function will write the entire schedule to a simple `.csv` file located in `/output_files/`

## Change Variables

#### Use Preset
To use other input files, place all your files inside `/input_files/` and open `main.py`. Set `PRESET` to `False` and run the program. The program will ask if you want to use the default values or custom files. Hit enter and you will be able to enter the names for your custom input files.

#### Overflow percentage
The overflow percentage is used to put more students in a class than allowed. This can result in fewer groups. In order to change the overflow percentage open `load.py` and look for `OVERFLOW_PERCENTAGE` and change the value (default = 10).



### Contributors:
Chris https://github.com/Chrisderijcke92<br />
Carlijn https://github.com/CarlijnQ<br />
Erik https://github.com/DevConfesss<br />