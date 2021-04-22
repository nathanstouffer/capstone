import matplotlib.pyplot as plt

def process(file, axes, j):
    data = []
    fin = open(file, "r")
    fin.readline()
    for line in fin:
        line = line.rstrip()[:-1].split(":")
        for i in range(len(line)):
            splt = line[i].split(",")
            line[i] = [ int(splt[0]), float(splt[1]), int(splt[2]) ]
        data.append(line)
    fin.close()

    for line in data:
        axes[0,j].plot([x[0] for x in line], [x[1] for x in line], '-', color='black', linewidth=0.15)
        axes[1,j].plot([x[0] for x in line], [x[2] for x in line], '-', color='black', linewidth=0.15)

algorand = "../data/capstone-algorand_d-04.19.2021_t-18.33.37/agg-rej-rnd-prop-info.txt"
bitcoin  = "../data/capstone-bitcoin_d-04.19.2021_t-22.34.47/agg-rej-rnd-prop-info.txt"
ethereum = "../data/capstone-ethereum_d-04.20.2021_t-05.24.39/agg-rej-rnd-prop-info.txt"

files = [ algorand, bitcoin, ethereum ]
fig, axes = plt.subplots(2, 3, figsize=(16,8))

j = 0
for file in files:
    process(file, axes, j)
    j += 1

# set title
axes[0,0].set_title("Algorand")
axes[0,1].set_title("Bitcoin")
axes[0,2].set_title("Ethereum")

# set y ranges
prop_ylim = [ -0.02, 0.32 ]
vote_ylim = [ -50, 1050 ]
axes[0,0].set_ylim(prop_ylim)
axes[0,1].set_ylim(prop_ylim)
axes[0,2].set_ylim(prop_ylim)
axes[1,0].set_ylim(vote_ylim)
axes[1,1].set_ylim(vote_ylim)
axes[1,2].set_ylim(vote_ylim)

# set labels
axes[0,0].set_ylabel("Proportional gain")
axes[1,0].set_ylabel("Number of valid votes")
axes[1,0].set_xlabel("Number of dishonest managers")
axes[1,1].set_xlabel("Number of dishonest managers")
axes[1,2].set_xlabel("Number of dishonest managers")

fig.suptitle("Proportional gain and number of remaining valid votes using a rejecting strategy", fontsize=14)

plt.show()
