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


## Installation

Install the dependencies.

```sh
git clone ...
python3 -m venv venv
pip install -r requirements.txt
```

## Usage
Input data: 
| Type | Description |
| ---- | ----------- |
| SWM | Swimming |
| RUN | Run |
| WLK | Sport Walking |

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

```sh
'RUN', [15000, 1, 75]
```
| # | RUN | Description | units |
| - | --- | ----------- | ----- |
| 1 | 15000 | steps | ea |
| 2 | 1 | duration | h |
| 3 | 75 | weight | kg |

```sh
'WLK', [9000, 1, 75, 180]
```
| # | RUN | Description | units |
| - | --- | ----------- | ----- |
| 1 | 15000 | steps | ea |
| 2 | 1 | duration | h |
| 3 | 75 | weight | kg |
| 4 | 180 | heigh of user | sm |


## License

MIT