# Heuristieken

### Run Random Hillclimber
`random_hillclimber = hillclimber.random_hillclimber(schedule, courses, <desired_score>, <max_duration>)
write_csv(random_hillclimber["schedule"])`

### Run Guided Hillclimber

`guided_hillclimber = hillclimber.guided_hillclimber(schedule, courses, <desired_score>)
write_csv(guided_hillclimber["schedule"])`

### Run Simulated Annealer
`random_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, [desired_score], <starting_temperature>, <max_duration>)
write_csv(random_simulated_annealer["schedule"])`

or

`guided_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, [desired_score], <starting_temperature>, <max_duration>)
write_csv(guided_simulated_annealer["schedule"])`

### 


#### Contributors: <br />
Chris https://github.com/Chrisderijcke92<br />
Carlijn https://github.com/Codingninja95<br />
Erik https://github.com/DevConfesss<br />