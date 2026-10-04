//  CS-3333-005 RSA Project
#include <stdio.h>
#include <stdlib.h>
#include <math.h>



// gcd part here
unsigned long gcd(unsigned long a, unsigned long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}



// modulo inverse algorithm stuff

unsigned long modInverse(unsigned long a, unsigned long m)
{
    unsigned long m0 = m, t, q;

     unsigned long x0 = 0, x1 = 1;

    if (m == 1)
        return 0;

    while (a > 1)
    {
         q = a / m;
         t = m;
         m = a % m;
         a = t;
         t = x0;
         x0 = x1 - q * x0;
          x1 = t;
    }

    if (x1 < 0)
        x1 += m0;

    return x1;
}



// Function to generate keys for RSA encryption
void generateKeys(unsigned long p, unsigned long q, unsigned long *n, unsigned long *e, unsigned long *d)
{

    *n = p * q; // Calculates n here
    unsigned long phi = (p - 1) * (q - 1); // does math

    // for e
    *e = 2;
    while (*e < phi && gcd(*e, phi) != 1) {
        (*e)++;
    }

    // for d
    *d = modInverse(*e, phi);
}



// rsa encription
unsigned long encrypt(unsigned long plaintext, unsigned long e, unsigned long n)
{
    unsigned long ciphertext = 1;
    for (unsigned long i = 0; i < e; i++) {
        ciphertext = (ciphertext * plaintext) % n;
    }
    return ciphertext;
}



// decrypts
unsigned long decrypt(unsigned long ciphertext, unsigned long d, unsigned long n) {
    unsigned long plaintext = 1;
    for (unsigned long i = 0; i < d; i++) {
        plaintext = (plaintext * ciphertext) % n;
    }
    return plaintext;
}




    int main()
{
     unsigned long p, q;  // prime numbers
     unsigned long n, e, d;

    printf("Enter p and q (prime numbers, ex: '3 11'): ");
     scanf("%lu %lu", &p, &q);

     // generates rsa keys
    generateKeys(p, q, &n, &e, &d);

    printf("Public key (e, n): (%lu, %lu)\n", e, n);
    printf("Private key (d, n): (%lu, %lu)\n\n", d, n);

     // plaintext printing
    unsigned long plaintext;
    printf("Enter an integer between 0 and n-1 as plain text to be encrypted: ");
    scanf("%lu", &plaintext);


    printf("Original plaintext: %lu\n", plaintext);
    unsigned long ciphertext = encrypt(plaintext, e, n);
    printf("Encrypted ciphertext: %lu\n", ciphertext);
     unsigned long decrypted = decrypt(ciphertext, d, n);
     printf("Decrypted plaintext: %lu\n", decrypted);

        return 0;
     }
