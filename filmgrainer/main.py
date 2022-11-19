
import sys
import filmgrainer.filmgrainer as filmgrainer

class Args:
    def __init__(self):
        self.gray_scale = False
        self.grain_type = 1
        self.grain_power = 0.5
        self.shadows = 0.3
        self.highs = 0.3
        self.scale = 1.0
        self.sharpen = 0
        self.src_gamma = 1.0
        self.seed = 1
        self.file_out = None

    @staticmethod
    def parse(args):
        a = Args()
        while len(args) > 1:
            if args[0] == "--gray":
                a.gray_scale = True
            elif args[0] == "--gamma":
                args.pop(0)
                a.src_gamma = float(args[0])
            elif args[0] == "--type":
                args.pop(0)
                a.grain_type = int(args[0])
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
            elif args[0] == "-h":
                usage()
                sys.exit(-1)
            else:
                raise Exception("Unknown option: " + args[0])
            args.pop(0)
        a.file_in = args[0]
        return a

def usage():
    print("""Usage:

  filmgrainer [OPTION] [OPTION] ... <input-filename>

Options:
  --gamma <gamma>                          Gamma compensate input, default: 1.0
  --gray                                   Convert to grayscale
  --type <type>                            Specify grain type: (default: 3)
                                           1: smooth fine, 2: fine, 3: coarse, 4: coarser
  --power <overall>,<highlights>,<shadows> Grain power: overall, for highlights and for shadows
  --scale <ratio>                          Scaling, default 1.0. This will scale the image before
                                           applying grain and scale back to normal size afterwards.
  --sharpen <passes>                       Sharpen output passes, default: 0
  --seed <number>                          Seed for grain random generator
  -o <output-filename>                     Set output filename
  -h                                       Show this help

Example, for a coarse black and white look:
  filmgrainer --gray --type 3 --power 0.8,0.2,0.1 -o output.jpg input.jpg

Example, for a heavily grained color negative look:
  filmgrainer --type 3 --power 0.8,0.2,0.1 -o output.jpg input.jpg   

Example, for a finely grained color negative look:
  filmgrainer --type 3 --power 0.8,0.2,0.1 -o output.jpg input.jpg   
""")

def main():
    try:
        args = Args.parse(sys.argv[1:])
    except Exception as e:
        usage()
        sys.exit(-1)
    else:
        filmgrainer.process(args.file_in, args.scale, args.src_gamma, 
            args.grain_power, args.shadows, args.highs, args.grain_type, 
            args.gray_scale, args.sharpen, args.seed, args.file_out)

if __name__ == "__main__":
    main()

