# Running Jupyter Notebooks

Sometimes one experiments with many notebooks (e.g. working on publication figures or data cleaning). It may be useful for them to run all the necessary notebooks generating new data using just one command, instead of opening each file individually in Jupyter Notebook.

## Usage
```bash
./execute.sh your-plan.txt
```

where `your-plan.txt` contains paths to your notebooks - each line should contain one path, without spaces.

## Example
Run
```bash
./execute.sh example/plan.txt
```
for simple data and figure generation according to the notebooks stored in `example` directory. 


## Caution
This is a simple snippet - currently it does not support paths containing spaces. Moreover, you should not have a .py file named the same as .ipynb.
