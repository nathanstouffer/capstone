import matplotlib.pyplot as plt

def process(file, axes, j):
    data = []
    fin = open(file, "r")
    fin.readline()
    for line in fin:
        line = line.rstrip()[:-1].split(":")
        for i in range(len(line)):
            splt = line[i].split(",")
            line[i] = [ int(splt[0]), int(splt[1]), float(splt[2]), int(splt[3]) ]
        data.append(line)
    fin.close()

    for line in data:
        axes[0,j].plot([x[0] for x in line], [x[2] for x in line], '-', color='black', linewidth=0.15)
        axes[1,j].plot([x[0] for x in line], [x[3] for x in line], '-', color='black', linewidth=0.15)

algorand = "../data/capstone-algorand_d-04.19.2021_t-18.33.37/agg-del-rnd-prop-info.txt"
bitcoin  = "../data/capstone-bitcoin_d-04.19.2021_t-22.34.47/agg-del-rnd-prop-info.txt"
ethereum = "../data/capstone-ethereum_d-04.20.2021_t-05.24.39/agg-del-rnd-prop-info.txt"

files = [ algorand, bitcoin, ethereum ]
fig, axes = plt.subplots(2, 3, figsize=(16,8))

j = 0
for file in files:
    process(file, axes, j)
    j += 1

# set x labels
xlabels = [ "dummy", "0", "4", "8", "12", "16", "20"]
axes[0,0].set_xticklabels(xlabels)
axes[0,1].set_xticklabels(xlabels)
axes[0,2].set_xticklabels(xlabels)
axes[1,0].set_xticklabels(xlabels)
axes[1,1].set_xticklabels(xlabels)
axes[1,2].set_xticklabels(xlabels)

# set y ranges
prop_ylim = [ -0.65, 0.65 ]
vote_ylim = [ -50, 1050 ]
axes[0,0].set_ylim(prop_ylim)
axes[0,1].set_ylim(prop_ylim)
axes[0,2].set_ylim(prop_ylim)
axes[1,0].set_ylim(vote_ylim)
axes[1,1].set_ylim(vote_ylim)
axes[1,2].set_ylim(vote_ylim)

# set title
axes[0,0].set_title("Algorand")
axes[0,1].set_title("Bitcoin")
axes[0,2].set_title("Ethereum")

# set labels
axes[0,0].set_ylabel("Proportional gain")
axes[1,0].set_ylabel("Number of valid votes")
axes[1,0].set_xlabel("Deleted vote's round")
axes[1,1].set_xlabel("Deleted vote's round")
axes[1,2].set_xlabel("Deleted vote's round")

fig.suptitle("Proportional gain and number of remaining valid votes using a deleting strategy", fontsize=14)

plt.show()
