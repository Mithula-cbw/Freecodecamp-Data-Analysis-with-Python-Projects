import numpy as np

def calculate(list):  # use 'lst' consistently
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        return list
    
    matrix = np.array(list).reshape(3, 3)

    calculations = {}

    calculations["mean"] = [
        matrix.mean(axis=0).tolist(),  
        matrix.mean(axis=1).tolist(), 
        matrix.mean().item()          
    ]

    calculations["variance"] = [
        matrix.var(axis=0).tolist(),  
        matrix.var(axis=1).tolist(),  
        matrix.var().item()          
    ]

    calculations["standard deviation"] = [
        matrix.std(axis=0).tolist(),  
        matrix.std(axis=1).tolist(),  
        matrix.std().item()           
    ]

    calculations['max'] = [
        matrix.max(axis=0).tolist(),
        matrix.max(axis=1).tolist(),
        matrix.max().item()
    ]

    calculations['min'] = [
        matrix.min(axis=0).tolist(),
        matrix.min(axis=1).tolist(),
        matrix.min().item()
    ]

    calculations['sum'] = [
        matrix.sum(axis=0).tolist(),
        matrix.sum(axis=1).tolist(),
        matrix.sum().item()
    ]

    return calculations
