import os
import unittest

from app import obtener_puerto

class TestApp(unittest.TestCase):
    def test_obtener_puerto_default(self):
        if 'PORT' in os.environ:
            del os.environ['PORT']
        self.assertEqual(obtener_puerto(), 8501)

    def test_obtener_puerto_env(self):
        os.environ['PORT'] = '1234'
        self.assertEqual(obtener_puerto(), 1234)
        del os.environ['PORT']

if __name__ == '__main__':
    unittest.main()
