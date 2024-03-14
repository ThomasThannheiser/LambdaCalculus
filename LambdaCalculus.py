print("Hello, Lambda!")

# Identity
I = lambda x : x

# Constant
K = lambda x : lambda y : x

# Substitution
# S = lambda f : lambda g : lambda x : f (x) (g (x))
# S (K) (K) == I == S (K) (_)

N = K (I)  # N = lambda x : lambda y : y

# Numbers
zero = lambda f : lambda x : x          # zero == N
one = lambda f : lambda x : f (x)
two = lambda f : lambda x : f (f (x))
three = lambda f : lambda x : f (f (f (x)))

# Helper functions to see our decimal numbers
inc = lambda x : x + 1
toInt = lambda n : n (inc) (0)

# Successor
succ = lambda n : lambda f : lambda x : f (n (f) (x))

four = succ (three)
five = succ (four)

# Arithmetic
# Addition
add = lambda m : lambda n : m (succ) (n)

six = add (four) (two)

# Multiplication
mult = lambda m : lambda n : lambda x : m (n (x)) 
# Wow! Multiplication is Composition!!

ten = mult (two) (five)

# multByAdd = lambda m : lambda n : m ((add) (n)) (zero)
# print (toInt (multByAdd (three) (four)))

# Exponentiation
_pow = lambda m : lambda n : n (m)

eight = _pow (two) (three)

# powByMult = lambda m : lambda n : n (mult (m)) (one)
# print (toInt (powByMult (three) (three)))

# Boolean
true = K
false = N

# Helper function to see our Booleans
toBool = lambda p : p (True) (False)

_not = lambda x : x (false) (true)
_and = lambda x : lambda y : x (y) (x)
_or = lambda x : lambda y : x (x) (y)

# Conditionals
isZero = lambda n : n (false) (_not) (false)


# Pair
pair = lambda a : lambda b : lambda f : f (a) (b)
first = lambda p : p (K)
second = lambda p : p (N)


# Fibonacci
start = pair (zero) (one)
step = lambda p : pair (second (p)) (add (first (p)) (second (p)))
fib = lambda n : first (n (step) (start))

print (toInt (fib (eight)))


phi = lambda p : pair (succ (p (true))) (p (true))

# Predecessor
pred = lambda n : second (n (phi) (pair (zero) (zero)))
# pred (zero) = zero !

seven = pred (eight)
nine = pred (ten)

geq = lambda x : lambda y : isZero (x (pred) (y))
eq = lambda x : lambda y : _and (geq (x) (y)) (geq (y) (x))


# Recursion
# Y - Combinator
# Y = lambda f : (lambda x : f (x (x))) (lambda x : f (x (x))
# Y R = R (Y R)

Y = lambda f : (lambda x : f (lambda v : x (x) (v))) (lambda x : f (lambda v : x (x) (v)))

# Haskells Fixpoint Combinator 
# fix = lambda f : lambda x : f (fix (f)) (x)


# sumR = lambda r : lambda n : isZero (n) (zero) (add (n) (r (pred (n))))
sumR = lambda r : lambda n : isZero (n) (zero) (lambda v: add (n) (r (pred (n))) (v))

facR = lambda r : lambda n : isZero (n) (one) (lambda v: mult (n) (r (pred (n))) (v))

fibR = lambda r : lambda n : isZero (n) (zero) (eq (n) (one) (one) (lambda v: add (r (pred (n))) (r (pred (pred (n)))) (v)))

print (toInt (Y (facR) (six)))