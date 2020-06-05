🚧 *Note: Work in progress* 🚧

# Numerical Methods 

Solve Numerical Methods on a computer like you do on pen-and-paper!

### Motivation

My college teaches us concepts of Numerical Methods using [this book](https://khannapublishers.in/index.php?route=product/product&manufacturer_id=90&product_id=244). Turns out it has a lot of printing mistakes, especially in the answers to the exercises in the book. Solving questions in this book was very stressful as there was no way to determine if my solutions were correct or not! There are software packages that let you calculate and verify your answers using Numerical Methods but they do it in "the most efficient way possible for a computer" rather than how one would do them on pen-and-paper.

Hence, I have created this small project that works as an answer verifier for the questions from that book.

### Features

1. Intuitive and uniform interface across the board:

```python
# Prototypes of various methods are very similar
euler(function, intial-x, initial-y, h, steps)
runge_kutta(function, initial-x, initial-y, h, steps)
...
```

2. Treats python functions as actual mathematical functions:

```python
# First-class python functions
def f(x, y):
	return x + y

modified_euler(f, 0, 1, 0.1, 3)
```

3. Lets you decide the accuracy of answers:

```python
>>> milne(f, X, Y, 0.1, ACCURACY = 5)
...
0.13174
...
>>> milne(f, X, Y, 0.1, ACCURACY = 3)  # change accuracy on the fly
...
0.132
...
```

4. Gives you intermediate steps as well:

```python
>>> euler(f, X, Y, 0.1, 10)
   X       Y    dy/dx    New-y = y+h*dy/dx
0.0000  1.0000  1.0000           1.1000
0.1000  1.1000  1.2000           1.2200
  ...     ...     ...             ...
0.9000  2.8158  3.7158           3.1874
1.0000  3.1874  0.0000           0.0000
```

5. Don't like the printed outputs? Get outputs in the form of python lists/objects/tuples instead:

```python
>>> result = euler(f, X, Y, 0.1, 10, api = True)		# 'api = True' works on all methods!
>>> result
[(0, 1, 1, 1.1), (0.1, 1.1, 1.2, 1.22) ... (0.9, 2.8158, 3.7158, 3.1874), (1.0, 3.1874, 0, 0)]
```

### How to use

**Requires Python 3**

- Download this repository ... the whole thing.
- Open and run `ode.py` using Python IDLE **OR** Open a terminal and run `python -i ode.py` **OR** `from ode import *` into your own python script.
- Head over to the [wiki](https://github.com/utk-dev/ode/wiki) of this repository for learning 'how-to' of various methods.

------

#### Disclaimer

These implementations are not how Numerical Methods should be implemented in code. These methods mimic how one would typically do calculations using a non-programmable calculator, pen and paper. 