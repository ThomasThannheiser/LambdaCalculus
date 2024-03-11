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

inc = lambda x : x + 1
toInt = lambda n : n (inc) (0)
toBool = lambda p : p (True) (False)

succ = lambda n : lambda f : lambda x : f (n (f) (x))

four = succ (three)
five = succ (four)

# Arithmetic
add = lambda m : lambda n : m (succ) (n)

six = add (four) (two)

mult = lambda m : lambda n : lambda x : m (n (x)) 
# Wow! Multiplication is Composition!!

ten = mult (two) (five)

pow = lambda m : lambda n : n (m)

eight = pow (two) (three)


# Boolean
true = K
false = N

_and = lambda x : lambda y : x (y) (x)
_or = lambda x : lambda y : x (x) (y)
_not = lambda x : x (false) (true)

# Conditionals
isZero = lambda n : n (false) (_not) (false)


# Pair
pair = lambda a : lambda b : lambda f : f (a) (b)

first = lambda p : p (true)
second = lambda p : p (false)


# Fibonacci
start = pair (zero) (one)
step = lambda p : pair (second (p)) (add (first (p)) (second (p)))
fib = lambda n : first (n (step) (start))


phi = lambda p : pair (succ (p (true))) (p (true))

pred = lambda n : second (n (phi) (pair (zero) (zero)))

seven = pred (eight)
nine = pred (ten)

geq = lambda x : lambda y : isZero (x (pred) (y))
eq = lambda x : lambda y : _and (geq (x) (y)) (geq (y) (x))

# Recursion
# Y-Combinator
# Y = lambda f : (lambda x : f (x (x))) (lambda x : f (x (x))

Y = lambda f : (lambda x : f (lambda v : x (x) (v))) (lambda x : f (lambda v : x (x) (v)))

# fix = lambda f : lambda x : f (fix (f)) (x)

# sum = lambda r : lambda n : isZero (n) (zero) (add (n) (r (pred (n))))
_sum = lambda r : lambda n : isZero (n) (zero) (lambda v: add (n) (r (pred (n))) (v))

fac = lambda r : lambda n : isZero (n) (one) (lambda v: mult (n) (r (pred (n))) (v))

_fib = lambda r : lambda n : isZero (n) (zero) (eq (n) (one) (one) (lambda v: add (r (pred (n))) (r (pred (pred (n)))) (v)))
