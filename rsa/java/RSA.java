// RSA HW Project

import java.math.BigInteger;

public class RSA {

    // recursive!!! greatest common denominator
    public static BigInteger gcd(BigInteger a, BigInteger b) {
                if (b.equals(BigInteger.ZERO)) {
            return a;
        } else {
             return gcd(b, a.mod(b));}
    }
    // works with the guidelines, makes the rsa stuff
    public static BigInteger inverseMod(BigInteger e, BigInteger phi) {
        BigInteger m0 = phi, x0 = BigInteger.ZERO, x1 = BigInteger.ONE;
        while (e.compareTo(BigInteger.ONE) > 0) {
            // dividing e by phi
            BigInteger q = e.divide(phi);
            BigInteger temp = phi;
            // creates phi and e
            phi = e.mod(phi);
            e = temp;
            // creates x0 and x1
            temp = x0;
            x0 = x1.subtract(q.multiply(x0));
            x1 = temp;
        }

        // makes x1 positive
        if (x1.compareTo(BigInteger.ZERO) < 0) {
            x1 = x1.add(m0);
        }
        return x1;
    }

    // generates rsa public and private keys
    public static BigInteger[] generateKeys(BigInteger p, BigInteger q, BigInteger e) {
         BigInteger n=p.multiply(q);
         BigInteger phiN=(p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

        if (!gcd(e, phiN).equals(BigInteger.ONE)) {
            throw new IllegalArgumentException("e is not coprime with phi(n)");
        }
//the guidelines doesnt say it needs user interaction, so its just hard set. hope that doesnt ruin anything
        BigInteger d=inverseMod(e, phiN);
        return new BigInteger[]{e, n, d, n}; // uses the keys said in the guidelines
    }

    // the encrypt part of rsa
    public static BigInteger encrypt(BigInteger message, BigInteger[] publicKey) {
        BigInteger e = publicKey[0];
        BigInteger n = publicKey[1];
        return message.modPow(e, n);
    }

    // uses the rsa stuff for decrytpt
    public static BigInteger decrypt(BigInteger ciphertext, BigInteger[] privateKey) {
        BigInteger d = privateKey[0];
        BigInteger n = privateKey[1];
        return ciphertext.modPow(d, n);
    }

    public static void main(String[] args) {
        BigInteger p =BigInteger.valueOf(3);
        BigInteger q =BigInteger.valueOf(11);
        BigInteger e =BigInteger.valueOf(7);

        // makes the keys for it
          BigInteger[] keys = generateKeys(p, q, e);
            BigInteger[] publicKey = {keys[0], keys[1]};
         BigInteger[] privateKey = {keys[2], keys[3]};

        // jus an example
            BigInteger m = BigInteger.valueOf(2);

        // encrypts
          BigInteger ciphertext = encrypt(m, publicKey);

        // decrypts
          BigInteger decryptedMessage = decrypt(ciphertext, privateKey);

        // output the results
        System.out.println("Public Key (e, n): " + publicKey[0] + ", " + publicKey[1]);
        System.out.println("Private Key (d, n): " + privateKey[0] + ", " + privateKey[1]);
        System.out.println("Original Message: " + m);
        System.out.println("Encrypted Message: " + ciphertext);
        System.out.println("Decrypted Message: " + decryptedMessage);
        //I REALLY HOPE THESE OUTPUTS ARE CORRECT, NO WHERE IN THE INSTRUCTIONS DOES IT SAY WHAT I AM SUPPOSED TO BE GETTING HERE.
    }
}
