# Diffie-Hellman Key Exchange Implementation

def diffie_hellman_key_exchange(prime, generator, private_key):
    """
    Computes public key and shared secret using Diffie-Hellman algorithm.

    Parameters:
        prime (int): A large prime number (p).
        generator (int): A generator (g) for the prime number.
        private_key (int): The private key chosen by the user.

    Returns:
        public_key (int): The computed public key.
        shared_secret (int): The shared secret key.
    """
    # Compute public key
    public_key = pow(generator, private_key, prime)
    return public_key


# Example: Alice and Bob agree on a prime number and generator
prime = 23  # A prime number
generator = 5  # A generator

# Alice selects her private key
private_key_alice = 6
public_key_alice = diffie_hellman_key_exchange(prime, generator, private_key_alice)

# Bob selects his private key
private_key_bob = 15
public_key_bob = diffie_hellman_key_exchange(prime, generator, private_key_bob)

# Exchange public keys and compute the shared secret
shared_secret_alice = pow(public_key_bob, private_key_alice, prime)
shared_secret_bob = pow(public_key_alice, private_key_bob, prime)

print("Alice's Public Key:", public_key_alice)
print("Bob's Public Key:", public_key_bob)
print("Shared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)