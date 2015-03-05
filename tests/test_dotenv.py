from __future__ import with_statement
import os
from tempfile import mkstemp

from dotenv import set_variable, Dotenv, get_variable, get_variables

from utils import CompatibilityTestCase


class DotenvTest(CompatibilityTestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("FOO='bar'\n")
            file.write("Bar=foo'\n")
            file.write("baz=1234'\n")
            file.write("url='https://test.oi/do?it=fast'\n")
        self.dotenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

    def test_create(self):
        self.assertIsInstance(self.dotenv, Dotenv)
        self.assertIsInstance(self.dotenv, dict)

    def test_get_keys(self):
        expected = set(['FOO', 'Bar', 'baz', 'url'])

        self.assertEqual(expected, set(self.dotenv.keys()))

    def test_get_values(self):
        expected = set(['bar', 'foo', '1234', 'https://test.oi/do?it=fast'])

        self.assertEqual(expected, set(self.dotenv.values()))

    def test_set_new_key_value(self):
        self.dotenv['asd'] = 'qwe'

        newdotenv = Dotenv(self.file_path)

        self.assertIn('asd', newdotenv)
        self.assertEqual('qwe', newdotenv['asd'])

    def test_set_existing_key(self):
        self.dotenv['baz'] = 987

        newdotenv = Dotenv(self.file_path)

        self.assertEqual('987', newdotenv['baz'])
        with open(self.file_path, 'r') as file:
            self.assertEqual(4, len(file.readlines()))

    def test_del_key(self):
        del self.dotenv['baz']

        newdotenv = Dotenv(self.file_path)

        self.assertNotIn('baz', newdotenv)
        with open(self.file_path, 'r') as file:
            self.assertEqual(3, len(file.readlines()))


class FunctionalTest(CompatibilityTestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("FOO='bar'\n")
            file.write("Bar=foo'\n")
            file.write("baz=1234'\n")
        self.dotenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

    def test_set_new_variable(self):
        set_variable(self.file_path, 'asd', 'qwe')

        dotenv = Dotenv(self.file_path)
        self.assertIn('asd', dotenv)
        self.assertEqual('qwe', dotenv['asd'])

    def test_set_existing_variable(self):
        set_variable(self.file_path, 'baz', '987')

        dotenv = Dotenv(self.file_path)
        self.assertIn('baz', dotenv)
        self.assertEqual('987', dotenv['baz'])

    def test_get_variable(self):
        result = get_variable(self.file_path, 'baz')

        self.assertEqual('1234', result)

    def test_get_variables(self):
        result = get_variables(self.file_path)

        dotenv = Dotenv(self.file_path)

        self.assertEqual(result, dotenv)


class CommentTest(CompatibilityTestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("# a commented .env file, for testing\n")
            file.write("SOMEVAR='12345' # a var, with an inline comment\n")
            file.write("VAR='giggles'\n")
            file.write("####################\n")
            file.write("\n")
            file.write("# another comment, notice the blank line above\n")
            file.write("    # an indented comment\n")
            file.write("cheese='cake'\n")
            file.write("COMMENT='#comment#test' # a value containing a comment\n")
        self.dotenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

    def test_create(self):
        self.assertIsInstance(self.dotenv, Dotenv)
        self.assertIsInstance(self.dotenv, dict)

    def test_get_keys(self):
        expected = set(['SOMEVAR', 'VAR', 'cheese', 'COMMENT'])

        self.assertEqual(expected, set(self.dotenv.keys()))

    def test_get_values(self):
        expected = set(['12345', 'giggles', 'cake', '#comment#test'])

        self.assertEqual(expected, set(self.dotenv.values()))
