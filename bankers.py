def bankers_algorithm(available, max_need, allocation):
    num_processes = len(max_need)
    num_resources = len(available)
    
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []
    
    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need <= work for need, work in zip(max_need[i], work)):
                #Resource Allocator
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                
                finish[i] = True
                safe_sequence.append(i)
                found = True
        
        if not found:
            break
    
    if all(finish):
        print("Safe sequence:", safe_sequence)
    else:
        print("Unsafe state. Deadlock detected.")
    
    return all(finish)


available_resources = [2, 3, 0]                                
maximum_need = [[7, 4, 3], [0, 2, 0], [6, 0, 0], [0, 1, 1], [4, 3, 1]]  
allocation = [[0, 1, 0], [3, 0, 2], [3, 0, 2], [2, 1, 1], [0, 0, 2]]    

print("Available resources:", available_resources)
print("Maximum need:", maximum_need)
print("Allocation:", allocation)

bankers_algorithm(available_resources, maximum_need, allocation)
                                                                    