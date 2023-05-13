# Module of Fitness-tracker
Script receive information about training type and raw data.
As result it output information about:

- Training type
- Duration
- Distance
- Average speed
- Spent calories

## Features

- Realized calculation logic for calories of Training Swimming, Run, Sport Walking.


#### Tested Python version
3.7-3.9

## Installation (windows)

Clone repository

```sh
git clone git@github.com:KuzenkovAG/module-fitness-tracker.git
```
Install environment
```sh
cd module-fitness-tracker/
```
```sh
python -m venv venv
```
Activate environment
```sh
source venv/Scripts/activate
```
Install requirements
```sh
pip install -r requirements.txt
```
Run script
```sh
python fitness_tracker.py
```

## Usage
#### Input data
```sh
'SWM', [720, 1, 80, 25, 40]
```
| # | SWM | Description | units |
| - | --- | ----------- | ----- |
| 1 | 720 | numbers of strokes in swimming | ea |
| 2 | 1 | duration | h |
| 3 | 80 | weight | kg |
| 4 | 25 | pool leight | m |
| 5 | 40 | counts pool during training | ea |

#### Output data
```sh
Training type: Swimming; Duration: 1.000 h.; Distance: 0.994 km; Avg. speed: 1.000 km/h; Spent kcal: 336.000.
```

#### Input data
```sh
'RUN', [15000, 1, 75]
```
| # | RUN | Description | units |
| - | --- | ----------- | ----- |
| 1 | 15000 | steps | ea |
| 2 | 1 | duration | h |
| 3 | 75 | weight | kg |

#### Output data
```sh
Training type: Running; Duration: 1.000 h.; Distance: 9.750 km; Avg. speed: 9.750 km/h; Spent kcal: 797.805.
```

#### Input data
```sh
'WLK', [9000, 1, 75, 180]
```
| # | WLK | Description | units |
| - | --- | ----------- | ----- |
| 1 | 9000 | steps | ea |
| 2 | 1 | duration | h |
| 3 | 75 | weight | kg |
| 4 | 180 | heigh of user | sm |

#### Output data
```sh
Training type: SportsWalking; Duration: 1.000 h.; Distance: 5.850 km; Avg. speed: 5.850 km/h; Spent kcal: 349.252.
```

## Author

[Alexey Kuzenkov]


## License

MIT

   [Alexey Kuzenkov]: <https://github.com/KuzenkovAG>
