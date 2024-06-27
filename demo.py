from dwave.system import EmbeddingComposite, DWaveSampler

# Define the problem as a Python dictionary
Q = {('B', 'B'): 1,
     ('C', 'C'): 1,
     ('A', 'D'): 2,
     ('A', 'C'): -2,
     ('B', 'D'): -2}

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_qubo(Q, num_reads = 10, label='Example')
print(sampleset)