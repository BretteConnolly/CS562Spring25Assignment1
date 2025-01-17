import MonteCarlo
import ZeroR
import perceptron

print("testing Monte Carlo")
MonteCarlo.monte_carlo_approach(10)

print("testing ZeroR")
fname = "tennis.csv"
with open(fname) as f :
    data = f.readlines()
    print(ZeroR.zeroR(data))
print("You can test the command line arguments from the command line.")

print("Testing wc")
print("You can run wc from the command line, like so")
print("wc --strip ~/Documents   or")
print("wc --strip --pfile=works.pkl ~/Documents")

print("testing perceptron")
perceptron.perceptron_training()

print("")