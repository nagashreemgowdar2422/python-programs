def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_first_n_primes(N):
    primes = []
    current_num = 2  # Starting number to check for prime
    while len(primes) < N:
        if is_prime(current_num):
            primes.append(current_num)
        current_num += 1
    return primes

if __name__ == "__main__":
    # Check if a number is prime
    n = int(input("Enter a number to check if it's prime: "))
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

    # Find first N prime numbers
    N = int(input("Enter how many prime numbers you want to find: "))
    first_n_primes = find_first_n_primes(N)
    print(f"The first {N} prime numbers are: {first_n_primes}")