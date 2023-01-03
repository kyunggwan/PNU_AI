
class Setup:
    def __init__(self):
        self._delta = 0.01     # Step size for axis-parallel mutation
        self._alpha = 0.01     # Update rate for gradient descent
        self._dx = 10 ** (-4)  # Increment for calculating derivative
