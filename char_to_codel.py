# char_to_codel.py

try:
    from PIL import Image
except:
    import pip
    pip.main(['install','pillow'])

import sys

def interpret(v):
    #codel_size = v[0]
    #filename = v[1]
    #image_path = v[2] or "[read_from]_[codel_size].png"

    codel_size = int(v[1])
    filename = v[2]
    try:
        image_path = v[3]
    except:
        image_path = "{}_{}.png".format(filename.split(".")[0], codel_size)

    with open(filename) as code_file:
        lines = code_file.read().splitlines()

    width = len(max(lines, key=len)) * codel_size
    height = len(lines) * codel_size
    im = Image.new('RGB', (width, height))

    color_dict = {'k':(0,0,0),'w':(255,255,255),
                  'q':(255,192,192),'r':(255,0,0),'s':(192,0,0),
                  'x':(255,255,192),'y':(255,255,0),'z':(192,192,0),
                  'f':(192,255,192),'g':(0,255,0),'h':(0,192,0),
                  'a':(192,255,255),'c':(0,255,255),'e':(0,192,192),
                  'p':(192,192,255),'b':(0,0,255),'d':(0,0,192),
                  'l':(255,192,255),'m':(255,0,255),'n':(192,0,192)}
    pixel_data = []

    for item in lines:
        for i in range(codel_size):
            for char in item:
                for j in range(codel_size):
                    try:
                        pixel_data.append(color_dict[char])
                    except:
                        pixel_data.append(color_dict['w'])

    im.putdata(pixel_data)
    im.save(image_path)

if __name__ == "__main__":
    v = sys.argv
    interpret(v)
