import numpy as np

def gradient_descent(start, gradient, learn_rate, max_iter, tol=0.01):
  steps = [start] # history tracking
  x = start

  for _ in range(max_iter):
    diff = learn_rate*gradient(x)
    if np.abs(diff)<tol:
      break    
    x = x - diff
    steps.append(x) # history tracing

  return steps, x




def func1(x):
  return x**2-4*x+1

def gradient_func1(x):
  return 2*x - 4

if __name__ == '__main__':
  history, result = gradient_descent(9, gradient_func1, 0.1, 100)
