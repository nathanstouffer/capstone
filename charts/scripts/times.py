import glob

def process_dir(dir):
    sub_dirs = glob.glob(dir + "/*/")
    avg = 0.0
    max = -10000000.0
    min = -max
    for sub_dir in sub_dirs:
        fin = open(sub_dir + "/sim-time-info", 'r')
        time = fin.readlines()[-1].rstrip()
        time = time.split(": ")[-1]
        time = float(time)
        avg += time
        if (time > max):
            max = time
        if (time < min):
            min = time
    avg /= len(sub_dirs)
    return max, min, avg

alg = "../data/capstone-algorand_d-04.19.2021_t-18.33.37/"
btc = "../data/capstone-bitcoin_d-04.19.2021_t-22.34.47/"
eth = "../data/capstone-ethereum_d-04.20.2021_t-05.24.39/"

max, min, avg = process_dir(alg)
print("algorand times ---  max: " + str(int(max)) + " s    min: " + str(int(min)) + " s    avg: " + str(int(avg)) + " s")
max, min, avg = process_dir(btc)
print("bitcoin times  ---  max: " + str(int(max)) + " s    min: " + str(int(min)) + " s    avg: " + str(int(avg)) + " s")
max, min, avg = process_dir(eth)
print("ethereum times ---  max: " + str(int(max)) + " s    min: " + str(int(min)) + " s    avg: " + str(int(avg)) + " s")
