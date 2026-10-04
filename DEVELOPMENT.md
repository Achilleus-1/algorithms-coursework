# Development

Create a Python 3.12 virtual environment, then run `python -m pip install -r
requirements.txt`. With a JDK and GCC available, run `python tools/check_repository.py`.
This compiles both RSA exercises and tests dynamic-programming segmentation.
RSA is an educational demonstration and must not protect real information.

Run each Python program from its own directory so the supplied input paths
resolve. Plotting needs a display; use `MPLBACKEND=Agg` for headless checks.
The nearest-store Queries.csv now uses approximate public city centers.
See DATASETS.md for the distinction between these new examples and original
course-supplied business/algorithm datasets with unverified reuse terms.
