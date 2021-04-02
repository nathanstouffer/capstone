# script to generate a tikz figure of a blockchain

def rect(offset, n):
    x = offset
    ret  = "% drawing block " + n + "\n"
    ret += "\\draw [very thick] (" + str(x) + ",0) "
    ret += "rectangle (" + str(x+width) + "," + str(height) + ");\n"
    ret += "\\draw [white] (" + str(x+width/2) + "," + str(height-0.25) + ") "
    ret += "circle (0.01) node[text=black] {hash$_" + n + "$};\n"
    ret += "\\draw [thick] (" + str(x) + "," + str(height-0.475) + ") -- "
    ret += "(" + str(x+width) + "," + str(height-0.475) + ");\n"
    ret += "\\draw [white] (" + str(x+width/2) + "," + str(height-0.75) + ") "
    ret += "circle (0.01) node[text=black] {nonce$_" + n + "$};\n"
    ret += "\\draw [thick] (" + str(x) + "," + str(height-0.95) + ") -- "
    ret += "(" + str(x+width) + "," + str(height-0.95) + ");\n"
    if (n != 'n'):
        ret += "% drawing arrow\n"
        ret += "\draw [->, very thick] (" + str(x+width) + "," + str(height-0.2375) + ") "
        ret += "-- (" + str(x+width+arrow_len) + "," + str(height-0.2375) + ");\n"
    return ret

num_blocks  = 3
width       = 1.3
height      = 1.6
arrow_len   = 0.75

out = "\\begin{center}\n\\begin{tikzpicture}[scale=1]\n\n"

for i in range(num_blocks-1):
    # draw the rectangle
    out += rect(i*(width+arrow_len), str(i))
    out += "\n"

dot_spc = 0.25
dot_x = [ (num_blocks-1)*(width+arrow_len)+1*dot_spc,
          (num_blocks-1)*(width+arrow_len)+2*dot_spc,
          (num_blocks-1)*(width+arrow_len)+3*dot_spc ]
out += "% draw the dots\n"
for x in dot_x:
    out += "\\draw [fill=black] (" + str(x) + "," + str(height-0.2375) + ") circle (0.03);\n"
out += "\n"

out += rect(dot_x[2]+dot_spc, 'n')

out += "\n\\end{tikzpicture}\n\\end{center}"

fout = open("blockchain.tex", 'w')
fout.write(out)
fout.close()
