---
title: Advanced Hash Functions
parent: Data Structure and Algorithm
author: Yupeng
date: 2025-05-29
layout: default
nav_order: 2.7
math: katex
emoji: jemoji
---

# Advanced Hash Functions

## 1. Hash Function vs. Encryption: When Do You Need a Secure Hash?

Hash functions and encryption are two different concepts, but in some scenarios, a hash function does need to have cryptographic or "secure" properties. Here's a detailed explanation:

### 1.1 Ordinary Hash Functions Are Not for Encryption
- In most hash table applications, the purpose of the hash function is to distribute keys uniformly across the table to minimize collisions and improve lookup/insert efficiency.
- These hash functions only need to be fast, deterministic, and well-distributed—they do **not** need to be cryptographically secure or provide encryption.
- Example: simple string or integer hash functions for hash tables.

### 1.2 When Does a Hash Function Need to Be "Secure"?
- **Preventing Attacks (Hash Flooding Attack):**
  - In web servers, databases, or any hash table exposed to untrusted input, a simple hash function can be exploited by attackers. They can craft many keys that all hash to the same slot, causing the hash table to degrade to a linked list and severely slowing down the system (a denial-of-service attack).
  - To prevent this, hash functions with randomization ("salting") or cryptographic properties are used, making it impossible for attackers to predict hash values.
  - Example: Python 3.3+ uses a randomized seed for string hashes, so the hash value changes every time the interpreter starts.
- **Cryptographic Applications:**
  - If a hash table is used to store sensitive data such as passwords, tokens, or digital signatures, a cryptographic hash function (like SHA-256 or MD5) **must** be used. This prevents attackers from reversing the hash value to obtain the original data.
  - Cryptographic hash functions provide collision resistance and preimage resistance, making it computationally infeasible to find two inputs with the same hash or to reverse the hash to the original input.

## 2. Properties of Good Hash Functions

A good hash function should have the following properties:
- **Deterministic**: Same input always produces the same output
- **Uniform Distribution**: Outputs should be evenly distributed across the range
- **Avalanche Effect**: Small changes in input should cause large changes in output
- **Efficiency**: Should be computationally efficient
- **Collision Resistance** (for cryptographic use): Hard to find two different inputs with the same output

## 3. Common Hash Functions

### 3.1 MD5 (Message-Digest Algorithm 5)
- Output length: 128 bits (16 bytes)
- Fast, but not secure for cryptographic use (collisions found)
- Use for file checksums, non-critical data validation

**Python Example:**
```python
import hashlib
print(hashlib.md5(b"Hello").hexdigest())  # 8b1a9953c4611296a827abf8c47804d7
```

### 3.2 SHA-256 (Secure Hash Algorithm 256)
- Output length: 256 bits (32 bytes)
- Strong cryptographic hash, widely used for security
- Use for password hashing, digital signatures, blockchain, file integrity

**Python Example:**
```python
import hashlib
print(hashlib.sha256(b"Hello").hexdigest())
# 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

### 3.3 MurmurHash
- Output length: 32 or 64 bits
- Very fast, non-cryptographic, good for hash tables and bloom filters

**Python Example:**
```python
import mmh3
print(mmh3.hash("Hello"))  # 316307400
```

## 4. Why Are Hash Functions Used for Password Storage?

Is it safe to store passwords using a hash function, given that different passwords could map to the same hash value?

Yes, it is standard practice to store only the hash of a password (not the plaintext) in a database. While hash functions are theoretically subject to collisions (different inputs mapping to the same output), modern cryptographic hash functions like SHA-256 have such a large output space that collisions are extremely unlikely in practice. For additional security, passwords are usually hashed with a unique salt and multiple rounds (e.g., bcrypt, PBKDF2). This makes it computationally infeasible for attackers to recover the original password, even if they obtain the hash values.

**Best practices for password storage:**
- Never store plaintext passwords.
- Use a strong cryptographic hash function (e.g., SHA-256, bcrypt, Argon2).
- Always use a unique salt for each password.
- Apply multiple rounds of hashing to slow down brute-force attacks.

This approach is widely used in the industry to protect user credentials and is considered secure when implemented correctly.

## 5. What Is Actually Stored? Plaintext vs. Hashed Passwords

In a secure system, the password stored in the database is not the user's actual password, but the result of a hash function applied to the password (e.g., `hash(password)`). This ensures that even if the database is compromised, attackers cannot easily recover the original passwords.

| Username | Plaintext Password | Hashed Password (e.g., SHA-256)           |
|----------|-------------------|--------------------------------------------|
| alice    | password123       | 008c5926ca861023c1d2a36653fd88e2...        |
| bob      | qwerty            | d8578edf8458ce06fbc5bb76a58c5ca4...        |

- **Plaintext Password**: The actual password the user enters (never store this!).
- **Hashed Password**: The result of applying a hash function to the password (this is what should be stored).

When a user logs in, the system hashes the entered password and compares it to the stored hash. If they match, access is granted.

## 6. Summary and Best Practices

- Use fast, well-distributed hash functions for general hash tables.
- Use cryptographic hash functions (with salt and multiple rounds) for password and sensitive data storage.
- Never store plaintext passwords.
- Understand the difference between hash and encryption: hash is one-way and irreversible, encryption is reversible with a key.

## Visualization: Hashing vs. Encryption

### Hashing (One-way, Irreversible)

```
[Original Text]
      |
      v
 [Hash Function]
      |
      v
[Hashed String]
```
- **One-way:** You cannot get the original text back from the hashed string.

### Encryption (Two-way, Reversible with Key)

```
[Plaintext] + [Encryption Key]
      |
      v
 [Encryption Function]
      |
      v
   [Ciphertext]
      |
      v
 [Decryption Function] + [Decryption Key]
      |
      v
[Plaintext]
```
- **Two-way:** You can recover the original text from the ciphertext if you have the correct key.

### Comparison Table

| Hashing (One-way)                | Encryption (Two-way)                |
|-----------------------------------|-------------------------------------|
| Original Text                     | Plaintext + Encryption Key          |
| ↓                                 | ↓                                   |
| Hash Function                     | Encryption Function                 |
| ↓                                 | ↓                                   |
| Hashed String (Digest)            | Ciphertext                          |
| *(Cannot reverse to original)*    | ↓                                   |
|                                   | Decryption Function + Decryption Key|
|                                   | ↓                                   |
|                                   | Plaintext (Recovered)               |

**Summary:**  
- **Hashing:** One-way, irreversible, used for integrity and password storage.  
- **Encryption:** Two-way, reversible with a key, used for confidentiality.
