# unit_converter
Simple application to make unit conversion (Length, Data)
```
input is provided by 3 space separated arguments:
    - amount to convert
    - unit with prefix to convert from
    - unit with prefix to convert to
    
inputs are case-sensitive
prefix and unit must be one word!
```
## Supported units

SI prefixes are supported, full list [here](https://en.wikipedia.org/wiki/Metric_prefix#List_of_SI_prefixes)

short as well long form are supported, e.g "meter" and "m", "kilo" and "k"


## CLI

```
python3 converter.py 1 meter in
```

## Setup
``` 
git clone https://github.com/zubrik13/unit_converter.git
cd unit_converter
pip install -r requirements.txt
python3 run.py
```
## Docker
```
docker pull zubrik/unit_converter:latest
docker run -ti -p 5000:5000 zubrik/unit_converter:latest
```

