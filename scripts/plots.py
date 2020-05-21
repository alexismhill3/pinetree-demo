import matplotlib.pyplot as plt 
import csv, sys

def read_output(tsv, index):
    """
    Retrieve protein/transcript abundances for the species 
    of interest in the simple_plamid simulation.

    index should be either 2 (for protein) or 3 (for transcript)
    """

    rnapol = []
    proteinX = []
    proteinY = []
    rnapolX = []
    time = []

    with open(tsv, newline='') as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)

        for row in reader:
            if row[1] == "rnapol":
                rnapol.append(float(row[index]))
                time.append(float(row[0]))
            elif row[1] == "proteinX":
                proteinX.append(float(row[index]))
            elif row[1] == "proteinY":
                proteinY.append(float(row[index]))
            elif row[1] == "rnapol-X":
                rnapolX.append(float(row[index]))
        
    return rnapol, proteinX, proteinY, rnapolX, time

def main():
    """
    Create time series plots for protein and transcript
    abundances from the simple_plasmid simulation.
    """

    tsv = sys.argv[1]

    w, x, y, z, t = read_output(tsv, 2)
    
    # Create the protein abundance plot
    plt.scatter(t,w, c='#ee4035', s=1, label='rnapol')
    plt.scatter(t,x, c='#f37736', s=1, label='proteinX')
    plt.scatter(t,y, c='#0392cf', s=1, label='proteinY')
    plt.scatter(t,z, c='#7bc043', s=1, label='rnapol-X')
    plt.xlabel("time")
    plt.ylabel("protein")
    plt.legend(loc='upper left')
    plt.savefig("../figures/protein_simple.png", bbox_inches="tight")
    plt.close()

    w, x, y, z, t = read_output(tsv, 3)
    
    # Create the transcript abundance plot
    plt.scatter(t,w, c='#ee4035', s=1, label='rnapol')
    plt.scatter(t,x, c='#f37736', s=1, label='proteinX')
    plt.scatter(t,y, c='#0392cf', s=1, label='proteinY')
    plt.xlabel("time")
    plt.ylabel("transcript")
    plt.legend(loc='upper left')
    plt.savefig("../figures/transcript_simple.png", bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    
    main()