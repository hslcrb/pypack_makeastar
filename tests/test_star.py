import unittest
import sys
import io
from star import triangle, pyramid, diamond, arrow, right_triangle, rhombus, inverted

class TestStarPatterns(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print output
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        # Reset redirection
        sys.stdout = sys.__stdout__

    def get_output(self):
        return self.capturedOutput.getvalue()

    def test_triangle_default(self):
        """Test triangle with default height (equals width)"""
        triangle(3).draw()
        expected = "*\n**\n***\n"
        self.assertEqual(self.get_output(), expected)

    def test_triangle_custom_height(self):
        """Test triangle with custom height"""
        triangle(5, 3).draw()
        expected = "*\n***\n*****\n"
        self.assertEqual(self.get_output(), expected)

    def test_pyramid(self):
        pyramid(3).draw()
        expected = "  *\n ***\n*****\n"
        self.assertEqual(self.get_output(), expected)

    def test_rhombus(self):
        rhombus(3).draw()
        expected = "  *\n ***\n*****\n ***\n  *\n"
        self.assertEqual(self.get_output(), expected)

    def test_diamond_gem(self):
        # n=3: width=5. crown range(1): i=0 -> 3 stars. mid: 5. pav range(2): 2, 1 -> 3, 1.
        # Total: 3, 5, 3, 1.
        diamond(3).draw()
        expected = " *** \n*****\n *** \n  *  \n"
        # Since rstrip is used, spaces on the right might be gone.
        # Let's check the lines.
        lines = self.get_output().splitlines()
        self.assertEqual(lines[0].strip(), "***")
        self.assertEqual(lines[1].strip(), "*****")
        self.assertEqual(lines[2].strip(), "***")
        self.assertEqual(lines[3].strip(), "*")

    def test_arrow(self):
        arrow(3).draw()
        expected = "*\n**\n***\n**\n*\n"
        self.assertEqual(self.get_output(), expected)

    def test_custom_char(self):
        triangle(2, char='#').draw()
        expected = "#\n##\n"
        self.assertEqual(self.get_output(), expected)

    def test_composition(self):
        p = triangle(2) + inverted(2)
        p.draw()
        expected = "*\n**\n**\n*\n"
        self.assertEqual(self.get_output(), expected)

if __name__ == '__main__':
    unittest.main()
