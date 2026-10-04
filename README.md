# Algorithms Coursework

Computational geometry, geographic nearest-neighbor selection, dynamic programming, and educational RSA implementations.

## Original coursework

- CS 3343-004 — Design and Analysis of Algorithms, Spring 2025
- CS 2233-003 — Discrete Mathematical Structures, Spring 2024
- CS 3333-005 — Mathematical Foundations of Computer Science, Fall 2024

Originally completed at the University of Texas at San Antonio during the terms above and imported to GitHub later. This repository preserves the submitted implementation; repository documentation and import housekeeping were added separately.

**Languages and technologies:** Python, NumPy, Matplotlib, Java, C, Bash.

## Implementation

- A monotone-chain convex hull and plotting helper.
- Randomized Quickselect to find nearby stores using Haversine distance.
- Dynamic programming to split strings into a minimum number of dictionary words.
- Educational RSA calculations in Java and C.

## Concepts

- Geometry orientation tests, randomized selection, optimal substructure, modular arithmetic, and reconstruction of dynamic-programming solutions.

## Repository layout

| Directory | Contents |
|---|---|
| `convex-hull` | Hull implementation and visualizer |
| `nearest-stores` | Quickselect and geographic distance |
| `dictionary-word-segmentation` | Dictionary-based dynamic programming |
| `rsa/java` | Java RSA exercise |
| `rsa/c` | C RSA exercise |

## Running the source

Run Python programs from their own directories so relative input paths resolve. convex-hull requires NumPy/Matplotlib. nearest-stores and word segmentation use the bundled machine-readable inputs. Build the RSA exercises separately with a JDK or C compiler.

## Scope and limitations

- Includes course-supplied helpers and input datasets; this is a coursework collection.
- RSA programs are small educational demonstrations, not production cryptography.

Only source code, build configuration, and required text inputs are included. Written submissions, assignment instructions, PDFs, videos, generated outputs, binary builds, and private configuration are omitted. Anonymized contributor labels and supplied-code comments retain the distinction between submitted work and scaffolding. No license for course-provided material is inferred.
