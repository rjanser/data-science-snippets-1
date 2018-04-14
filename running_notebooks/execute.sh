#!/bin/bash
# $1 - file with execution plan (each line should contain a path to a Notebook)


root_dir=$(pwd)

for notebook in $(<$1)
do
    echo "Executing $notebook..."
    # Go to the right directory
    pth=$(dirname ${notebook})
    cd $pth
    jup=$(basename ${notebook})

    # Remove %matplotlib inline, as it may break the nbconvert magic
    copied_jup=$jup"2"
    awk '{gsub("%matplotlib inline", "");print}' $jup > $copied_jup
    scriptname=${jup%"ipynb"}"py"
    # Convert to python and run
    jupyter-nbconvert --to script --execute ${copied_jup}
    ipython ${scriptname}

    # Remove unnecesary files
    rm $scriptname $copied_jup

    cd $root_dir
done

echo "Finished."
