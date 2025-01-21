

# Fun Simple33:
def RadToDeg(R):
    return R * (180 / math.pi)

def convert_radians_to_degrees(radians):
    return [RadToDeg(r) for r in radians]

# Fun Simple34: 
def Fact(N):
    if N == 0 or N == 1:
        return 1
    result = 1
    for i in range(2, N + 1):
        result *= i
    return result

def calculate_factorials(numbers):
    return [Fact(n) for n in numbers]

# Fun Simple35: 
def Fact2(N):
    result = 1
    for i in range(N, 0, -2):
        result *= i
    return result

def calculate_double_factorials(numbers):
    return [Fact2(n) for n in numbers]

# Fun Simple36: 
def Fib(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, N + 1):
        a, b = b, a + b
    return b

def calculate_fibonacci_numbers(numbers):
    return [Fib(n) for n in numbers]

# Fun Simple37:
def Power1(A, B):
    return A ** B

def calculate_powers(numbers, B):
    return [Power1(A, B) for A in numbers]

# Fun Simple38:
def Power2(A, N):
    if N == 0:
        return 1
    elif N > 0:
        result = 1
        for _ in range(N):
            result *= A
        return result
    else:
        return 1 / Power2(A, -N)

def calculate_powers_with_exponents(A, exponents):
    return [Power2(A, N) for N in exponents]

# Fun Simple39: 
def Power3(A, N):
    if N % 1 != 0:
        return Power2(A, int(N))
    else:
        return Power1(A, N)

def calculate_powers_with_fractional_exponents(A, exponents):
    return [Power3(A, N) for N in exponents]

# Fun Simple40: 
def Exp1(x, ε):
    result = 1.0
    term = 1.0
    n = 1
    while True:
        term *= x / n
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

def calculate_exponentials(x_values, ε_values):
    return [Exp1(x, ε) for x, ε in zip(x_values, ε_values)]


import math

# FunSimple41: sin(x) ni hisoblash
def sin1(x, ε):
    result = 0.0
    n = 0
    while True:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple42: cos(x) ni hisoblash
def cos1(x, ε):
    result = 0.0
    n = 0
    while True:
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple43: ln(1 + x) ni hisoblash
def Ln1(x, ε):
    if abs(x) >= 1:
        raise ValueError("|x| < 1 shartini qanoatlantirishi kerak")
    result = 0.0
    n = 1
    while True:
        term = ((-1) ** (n + 1)) * (x ** n) / n
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple44: arctg(x) ni hisoblash
def Arctg1(x, ε):
    if abs(x) >= 1:
        raise ValueError("|x| < 1 shartini qanoatlantirishi kerak")
    result = 0.0
    n = 0
    while True:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple45: (1 + x)^a ni hisoblash
def Power4(x, a, ε):
    if abs(x) >= 1:
        raise ValueError("|x| < 1 shartini qanoatlantirishi kerak")
    result = 1.0
    n = 1
    while True:
        term = (a * (a - 1) * ... * (a - n + 1)) * (x ** n) / math.factorial(n)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple46: 
def EKUB(A, B):
    while B:
        A, B = B, A % B
    return A

# FunSimple47: 
def Frac1(a, b, p, q):
    gcd = EKUB(a, b)
    p = a // gcd
    q = b // gcd
    return p, q

# FunSimple48:
def EKUK(A, B):
    return A * B // EKUB(A, B)

# FunSimple49: 
def EKUB3(A, B, C):
    return EKUB(EKUB(A, B), C)

import math

# FunSimple50: 
def TimeToHMS(T):
    H = T // 3600
    T %= 3600
    M = T // 60
    S = T % 60
    return H, M, S

def convert_seconds_to_hms(seconds_list):
    return [TimeToHMS(T) for T in seconds_list]



# FunSimple51:
def IncTime(H, M, S, T):
    total_seconds = H * 3600 + M * 60 + S + T
    return TimeToHMS(total_seconds)

def increment_times(times, T):
    return [IncTime(H, M, S, T) for H, M, S in times]

# FunSimple52: 
def isLeapYear(Y):
    return Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0)

def check_leap_years(years):
    return [isLeapYear(Y) for Y in years]

# FunSimple53:
def MonthDays(M, Y):
    if M == 2:
        return 29 if isLeapYear(Y) else 28
    elif M in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def get_month_days(months, Y):
    return [MonthDays(M, Y) for M in months]

# FunSimple54: 
def PrevDate(D, M, Y):
    if D > 1:
        return D - 1, M, Y
    elif M > 1:
        return MonthDays(M - 1, Y), M - 1, Y
    else:
        return 31, 12, Y - 1

def get_previous_dates(dates):
    return [PrevDate(D, M, Y) for D, M, Y in dates]

# FunSimple55: 
def NextDate(D, M, Y):
    days_in_month = MonthDays(M, Y)
    if D < days_in_month:
        return D + 1, M, Y
    elif M < 12:
        return 1, M + 1, Y
    else:
        return 1, 1, Y + 1

def get_next_dates(dates):
    return [NextDate(D, M, Y) for D, M, Y in dates]

# FunSimple56: 
def Leng(X1, Y1, X2, Y2):
    return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

def calculate_distances(points, A):
    return [Leng(A[0], A[1], X, Y) for X, Y in points]

# FunSimple57: 
def Perim(XA, YA, XB, YB, XC, YC):
    AB = Leng(XA, YA, XB, YB)
    BC = Leng(XB, YB, XC, YC)
    CA = Leng(XC, YC, XA, YA)
    return AB + BC + CA

def calculate_perimeters(triangles):
    return [Perim(*triangle) for triangle in triangles]

# FunSimple58:
def Area(XA, YA, XB, YB, XC, YC):
    AB = Leng(XA, YA, XB, YB)
    BC = Leng(XB, YB, XC, YC)
    CA = Leng(XC, YC, XA, YA)
    s = (AB + BC + CA) / 2
    return math.sqrt(s * (s - AB) * (s - BC) * (s - CA))

def calculate_areas(triangles):
    return [Area(*triangle) for triangle in triangles]

# FunSimple59:
def Dist(XA, YA, XB, YB, XP, YP):
    AB = Leng(XA, YA, XB, YB)
    area = Area(XA, YA, XB, YB, XP, YP)
    return (2 * area) / AB

def calculate_heights(points, A, B):
    return [Dist(A[0], A[1], B[0], B[1], X, Y) for X, Y in points]


import math

# FunSimple60: 
def Heights(XA, YA, XB, YB, XC, YC):
    hA = Dist(XB, YB, XC, YC, XA, YA)
    hB = Dist(XA, YA, XC, YC, XB, YB)
    hC = Dist(XA, YA, XB, YB, XC, YC)
    return hA, hB, hC
