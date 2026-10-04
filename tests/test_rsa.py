import pathlib, shutil, subprocess, tempfile, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]
class RSAArithmeticTests(unittest.TestCase):
    def test_inverse_handles_negative_coefficient_and_non_coprime_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory)
            (path/'test.c').write_text('#include <assert.h>\n#define main coursework_main\n#include "rsa.c"\n#undef main\nint main(void) {\n    assert(modInverse(17, 3120) == 2753);\n    assert(modInverse(3, 11) == 4);\n    assert(modInverse(6, 12) == 0);\n    assert(modInverse(1, 0) == 0);\n    assert(decrypt(encrypt(65, 17, 3233), 2753, 3233) == 65);\n    return 0;\n}\n')
            program = path/'test.exe'
            subprocess.run([shutil.which('gcc'), '-std=c11', '-I', str(ROOT/'rsa/c'), str(path/'test.c'), '-lm', '-o', str(program)], check=True)
            subprocess.run([str(program)], check=True, timeout=5)
