
# filmgrainer

*Adding realistic film grain to pictures*

by Lars Ole Pontoppidan

## Installation

filmgrainer can be installed directly from the github repo:

```text
pip install git+https://github.com/larspontoppidan/filmgrainer
```

The package requires numpy and pillow. Consider installing in a virtual environment.

## Examples

#### Input image:  
![Input image](examples/input.jpg)

#### Coarse black and white look:  
`filmgrainer --gray --type 3 --power 0.8,0.2,0.1 -o bw_neg.png input.jpg`

![Coarse black and white look](examples/bw_neg.png)

#### Grained color negative look:  
`filmgrainer --type 4 --sat 0.8 --power 1,0.2,0.2 -o color_neg.png input.jpg`

![Grained color negative look](examples/color_neg.png)

#### Gentle dias-film like grain:  
`filmgrainer --type 1 --sat 0.6 --power 0.75,0.1,0.1 -o dias.png input.jpg`

![Gentle dias-film like grain](examples/dias.png)

#### Totally trashed by grain:  
`filmgrainer --type 1 --gray --power 1,0.3,0.2 --scale 3 --sharpen 1 -o trashed_bw.png input.jpg`

![Totally trashed by grain, black and white](examples/trashed_bw.png)

`filmgrainer --type 1 --sat 0.8 --power 1,0.3,0.2 --scale 3 --sharpen 1 -o trashed.png input.jpg`

![Totally trashed by grain](examples/trashed.png)
