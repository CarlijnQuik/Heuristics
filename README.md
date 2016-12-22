# Heuristieken

## Run Algorithms

To run the different algorithms, open up main.py and paste the correct lines at the bottom of the script.<br />
Function arguments marked with `<>` are optional. Function arguments marked with `[]` are required. All other arguments should be left untouched.

### Run Random Hillclimber
```python
random_hillclimber = hillclimber.random_hillclimber(schedule, courses, <desired_score>, <max_duration>)
write_csv(random_hillclimber["schedule"])
```

### Run Guided Hillclimber
```python
guided_hillclimber = hillclimber.guided_hillclimber(schedule, courses, <desired_score>)
write_csv(guided_hillclimber["schedule"])
```

### Run  Random Simulated Annealer
```python
random_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, [desired_score], <starting_temperature>, <max_duration>)
write_csv(random_simulated_annealer["schedule"])
```

### Run Guided Simulated Annealer

```python
guided_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, [desired_score], <starting_temperature>, <max_duration>)
write_csv(guided_simulated_annealer["schedule"])
```

#### Write CSV
The `write_csv` function will write the entire schedule to a simple `.csv` file located in `/output_files/`


#### Contributors: <br />
Chris https://github.com/Chrisderijcke92<br />
Carlijn https://github.com/CarlijnQ<br />
Erik https://github.com/DevConfesss<br />