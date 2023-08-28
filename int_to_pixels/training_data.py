import numpy as np

class TrainingData:
    
    training_data = {
        0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        1: [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        2: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        3: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        4: [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        5: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        6: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        7: [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
    }

    def __init__(self):
        # X = [0 1 2 3 4 5 6 7 8 9]
        self.X = np.array(list(self.training_data.keys()))
        
        # Y = [[1 1 1 1 0 1 1 0 1 1 0 1 1 1 1],
        #      [0 0 1 0 0 1 0 0 1 0 0 1 0 0 1],
        #      ... ]
        self.Y = np.array([np.array(self.training_data[key]).flatten() for key in self.training_data.keys()])
    
    def get_training_inputs_outputs(self):
        return self.X, self.Y
    
    def get_training_data(self):
        return self.training_data
    