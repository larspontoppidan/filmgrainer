
import sys
import filmgrainer.filmgrainer as filmgrainer

from filmgrainer import __version__
github = "https://github.com/larspontoppidan/filmgrainer"

class Arguments:
    def __init__(self):
        self.gray_scale = False
        self.grain_type = 1
        self.grain_sat = 0.5        
        self.grain_power = 0.7
        self.shadows = 0.2
        self.highs = 0.2
        self.scale = 1.0
        self.sharpen = 0
        self.src_gamma = 1.0
        self.seed = 1
        self.file_in = None
        self.file_out = None

    @staticmethod
    def parse(args):
        a = Arguments()
        while len(args) > 0:
            if len(args) == 1 and not args[0].startswith('-'):
                a.file_in = args[0]
            elif args[0] == "--gray":
                a.gray_scale = True
            elif args[0] == "--gamma":
                args.pop(0)
                a.src_gamma = float(args[0])
            elif args[0] == "--type":
                args.pop(0)
                a.grain_type = int(args[0])
            elif args[0] == "--sat":
                args.pop(0)
                a.grain_sat = float(args[0])
            elif args[0] == "-o":
                args.pop(0)
                a.file_out = args[0]
            elif args[0] == "--seed":
                args.pop(0)
                a.seed = int(args[0])
            elif args[0] == "--scale":
                args.pop(0)
                a.scale = float(args[0])
            elif args[0] == "--sharpen":
                args.pop(0)
                a.sharpen = int(args[0])
            elif args[0] == "--power":
                args.pop(0)
                sp = args[0].split(",")
                a.grain_power = float(sp[0])
                a.highs = float(sp[1])
                a.shadows = float(sp[2])
            elif args[0] == "--version":
                version()
                sys.exit()
            elif args[0] == "-h":
                usage()
                sys.exit()
            else:
                raise Exception("Unknown option: " + args[0])
            args.pop(0)
        return a

def version():
    print("filmgrainer v%s, see more: %s" % (__version__, github))

def usage():
    print("""Usage:
  filmgrainer [OPTION] [OPTION] ... INPUTFILE

Options:
--------
  --gamma <gamma>                          Gamma compensate input, default: 1.0
  --gray                                   Grayscale mode
  --type <type>                            Grain type:
                                           1: fine, 2: fine simple, 3: coarse, 4: coarser
  --sat <saturation>                       Grain color saturation, 0.0 to 1.0
  --power <overall>,<highlights>,<shadows> Grain power: overall, highlights, shadows
  --scale <ratio>                          Scaling, default 1.0. This will scale the image before
                                           applying grain and scale back to original size 
                                           afterwards for an increase in grain size.
  --sharpen <passes>                       Sharpen output, passes, default: 0
  --seed <number>                          Seed for grain random generator
  -o <output-filename>                     Set output filename
  -h                                       Show this help
  --version                                Show version

Examples:
---------
Coarse black and white look:
  filmgrainer --gray --type 3 --power 0.8,0.2,0.1 -o bw_neg.png input.jpg

Heavily grained color negative look:
  filmgrainer --type 4 --sat 0.8 --power 1,0.2,0.2 -o color_neg.png input.jpg

Gentle dias-film like grain:
  filmgrainer --type 1 --sat 0.6 --power 0.75,0.1,0.1 -o dias.png input.jpg

Totally trashing a picture with grain:
  filmgrainer --type 1 --gray --power 1,0.3,0.2 --scale 3 --sharpen 1 -o trashed_bw.png input.jpg
  filmgrainer --type 1 --sat 0.8 --power 1,0.3,0.2 --scale 3 --sharpen 1 -o trashed.png input.jpg
""")

def main():
    try:
        if len(sys.argv) == 1:
            version()
            print("")
            usage()
            return
        args = Arguments.parse(sys.argv[1:])
        if args.file_in is None:
            raise ValueError("No input file specified")
    except Exception as e:
        print("Error: %s" % str(e))
        sys.exit(-1)
    else:
        if args.file_out is None:
            args.file_out = args.file_in + "-grain.png"

        filmgrainer.process(args.file_in, args.scale, args.src_gamma, 
            args.grain_power, args.shadows, args.highs, args.grain_type, 
            args.grain_sat, args.gray_scale, args.sharpen, args.seed, args.file_out)

if __name__ == "__main__":
    main()
