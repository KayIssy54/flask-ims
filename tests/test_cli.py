import unittest
from unittest.mock import patch
import cli


class CLITestCase(unittest.TestCase):

    @patch("builtins.input", side_effect=["6"])
    def test_exit(self, mock_input):

        try:
            cli.main()
        except SystemExit:
            pass

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()