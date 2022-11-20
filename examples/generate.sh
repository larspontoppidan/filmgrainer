#!/bin/sh

echo Generating examples ...
echo

filmgrainer --gray --type 3 --power 0.8,0.2,0.1 -o bw_neg.png input.jpg
filmgrainer --type 4 --sat 0.8 --power 1,0.2,0.2 -o color_neg.png input.jpg
filmgrainer --type 1 --sat 0.6 --power 0.75,0.1,0.1 -o dias.png input.jpg
filmgrainer --type 1 --gray --power 1,0.3,0.2 --scale 3 --sharpen 1 -o trashed_bw.png input.jpg
filmgrainer --type 1 --sat 0.8 --power 1,0.3,0.2 --scale 3 --sharpen 1 -o trashed.png input.jpg

