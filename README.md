
# filmgrainer

Adding realistic film grain to pictures

by Lars Ole Pontoppidan

## Installation

```text
pip install git+https://github.com/larspontoppidan/filmgrainer
```

## Usage examples

Coarse black and white look:

`filmgrainer --gray --type 3 --power 0.8,0.2,0.1 -o bw_neg.png input.jpg`

Heavily grained color negative look:
`filmgrainer --type 4 --sat 1 --power 1,0.2,0.2 -o color_neg.png input.jpg`

Finely grained color negative look:
`filmgrainer --type 3 --sat 1 --power 0.7,0.2,0.2 -o color_neg_fine.png input.jpg`

Very gentle dias-film grain:
`filmgrainer --type 1 --sat 0.5 --power 0.5,0.1,0.1 -o dias.png input.jpg`

Totally trashing a picture with grain:
`filmgrainer --type 1 --gray --power 1,0.4,0.2 --scale 3 --sharpen 1 -o trashed_bw.png input.jpg`  
`filmgrainer --type 1 --sat 0.7 --power 1,0.4,0.2 --scale 3 --sharpen 1 -o trashed.png input.jpg`

