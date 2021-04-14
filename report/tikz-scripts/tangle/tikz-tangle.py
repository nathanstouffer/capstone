from sys import argv
import math

# FUNCTIONS -----------------------------------------------------------------------------------------

# method to add two vectors
def add(v1, v2):
    sum = []
    for v in range(0, len(v1)):
        sum.append(v1[v]+v2[v])
    return sum

# method to compute the magnitude of a vector
def magnitude(vec):
    dot = 0.0
    for val in vec:
        dot += val*val
    return math.sqrt(dot)

# method to scale a vector
def scale(scalar, vector):
    vec = []
    for val in vector:
        vec.append(scalar*val)
    return vec

# method to compute return a normalized vector
def normalize(vec):
    return scale(1.0/magnitude(vec), vec)

# method to compute a vector from to points
def vector(q, p):
    vec = []
    for i in range(0, len(p)):
        vec.append(q[i]-p[i])
    return vec

# method to round a float and convert to string (for x variables)
def outx(val):
    return str(round(val, 3))

# method to round a float and convert to string (for y variables)
def outy(val):
    return str(round(val, 3))

# SCRIPT --------------------------------------------------------------------------------------------

# file name should be a relative file path to the input file
script, file_name = argv                                        # read in command line arguments

tikz_scale   = 2.5                                              # scale value for the tikz picture
radius       = 0.025                                            # radius
label_offset = 0.15                                             # label label_offset for each vertex
epsilon      = 0.1                                              # dist added so edge has space between a node
tri_height   = 0.075                                            # side length of a triangle

out_str  = "\\begin{tikzpicture}[scale="                    # initialize output string
out_str += str(tikz_scale) + ",rotate=270]"
out_str += "\n    %% vertices"
verts = {}                                                  # store the vertices

fin = open(file_name, 'r')                                  # open the input file

# VERTICES ------------------------------------------------------------------------------------------

line = fin.readline()                                       # skip dummy line
line = fin.readline()
while (line.rstrip() != "E"):                               # read in each vertex
    vert = line.rstrip().split(" ")                         # get the (x, y) positions of the vertices in the tangle
    key = vert[0]
    pos_x = float(vert[1])
    pos_y = float(vert[2])

    out_str += "\n    \\draw [fill=black]"                  # add tikz to draw vertex
    out_str += "{0:14}".format(" (" + outx(pos_x) + "," + outy(pos_y) + ")")
    out_str += " circle (" + str(radius) + ");"

    verts.update({ key : [pos_x, pos_y] })                  # update the vertex table
    line = fin.readline()                                   # read in new line

# LABELS ------------------------------------------------------------------------------------------

# write labels to the output string
out_str += "\n    %% labels"
for key in verts:
    pos_x = verts.get(key)[0]                               # get positions from the key
    pos_y = verts.get(key)[1]

    out_str += "\n    \\node at ("
    if (pos_x == 0.0 and pos_y == 0.0):
        out_str += outx(pos_x) + ","
        out_str += outy(pos_y - label_offset) + ")"
    elif (pos_x > 0.0):
        out_str += outx(pos_x + label_offset) + ","
        out_str += outy(pos_y) + ")"
    elif (pos_x < 0.0):
        out_str += outx(pos_x - label_offset) + ","
        out_str += outy(pos_y) + ")"
    out_str += " {" + key + "};"

# EDGES ------------------------------------------------------------------------------------------

edges = []
# get the edges from the file
out_str += "\n    %% edges"
for line in fin:                                            # start reading in edges
    edge = line.rstrip().split(" ")                         # get the edges in the form of a list
    edges.append(edge)                                      # add edge to edges list
    src  = edge[0]
    tar  = edge[1]

    p = verts.get(src)                                      # get the points of the vertices
    q = verts.get(tar)
    unit_vec = normalize(vector(q, p))                      # compute unit direction vector

    first  = add(p, scale( (radius+epsilon), unit_vec))
    second = add(q, scale(-(radius+epsilon), unit_vec))

    out_str += "\n    \\draw [thick] ("
    out_str += outx(first[0])  + "," + outy(first[1])  + ") -- ("
    out_str += outx(second[0]) + "," + outy(second[1]) + ");"

fin.close()                                                 # close file

# ARROWS ---------------------------------------------------------------------------------------

out_str += "\n    %% arrows"
for edge in edges:
    src = edge[0]
    tar = edge[1]

    p = verts.get(src)                                              # get the points of the vertices
    q = verts.get(tar)
    unit_vec = normalize(vector(q, p))                              # compute unit direction vector
    perp_vec = [ unit_vec[1], -unit_vec[0] ]
    tip = add(q, scale(-(radius+epsilon-0.05), unit_vec))           # compute the tip of the triangle

    base = add(tip,  scale(  -tri_height, unit_vec))                # midpoint of the base
    a    = add(base, scale( tri_height/2, perp_vec))
    b    = add(base, scale(-tri_height/2, perp_vec))

    out_str += "\n    \\fill [black] ("
    out_str += outx(tip[0]) + "," + outy(tip[1]) + ") -- ("
    out_str += outx(a[0])   + "," + outy(a[1])   + ") -- ("
    out_str += outx(b[0])   + "," + outy(b[1])   + ");"

out_str += "\n\\end{tikzpicture}"

# OUTPUT ---------------------------------------------------------------------------------------

out_file_name = file_name.split("/")[-1][:-3] + ".tex"      # create output file name
fout = open("out/" + out_file_name, 'w')                 # open output file
fout.write(out_str)                                         # write the output
fout.close()                                                # close the output file
