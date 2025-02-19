from tkinter import messagebox
import unittest


class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort_with_data(self):
        from run_normal import bubble_loop

        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_loop(data, master)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubble_sort_without_data(self):
        from run_normal import bubble_loop

        data = []
        bubble_loop(data, master)
        self.assertEqual(data, [])

    def test_bubble_sort_single_element(self):
        from run_normal import bubble_loop

        data = [1]
        bubble_loop(data, master)
        self.assertEqual(data, [1])

    def test_bubble_sort_duplicate_elements(self):
        from run_normal import bubble_loop

        data = [5] * 10
        bubble_loop(data, master)
        self.assertEqual(data, [5] * 10)

    def test_bubble_sort_with_negative_numbers(self):
        from run_normal import bubble_loop

        data = [9, -8, 7, -6, 5, -4, 3, -2, 1]
        bubble_loop(data, master)
        self.assertEqual(data, [-8, -6, -4, -2, 1, 3, 5, 7, 9])

    def test_selection_sort_with_data(self):
        from run_normal import selection_loop

        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        selection_loop(data, master)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_selection_sort_without_data(self):
        from run_normal import selection_loop

        data = []
        selection_loop(data, master)
        self.assertEqual(data, [])

    def test_selection_sort_single_element(self):
        from run_normal import selection_loop

        data = [1]
        selection_loop(data, master)
        self.assertEqual(data, [1])

    def test_selection_sort_duplicate_elements(self):
        from run_normal import selection_loop

        data = [5] * 10
        selection_loop(data, master)
        self.assertEqual(data, [5] * 10)

    def test_selection_sort_with_negative_numbers(self):
        from run_normal import selection_loop

        data = [9, -8, 7, -6, 5, -4, 3, -2, 1]
        selection_loop(data, master)
        self.assertEqual(data, [-8, -6, -4, -2, 1, 3, 5, 7, 9])

    def test_insertion_sort_with_data(self):
        from run_normal import insertion_loop

        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_loop(data, master)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_insertion_sort_without_data(self):
        from run_normal import insertion_loop

        data = []
        insertion_loop(data, master)
        self.assertEqual(data, [])

    def test_insertion_sort_single_element(self):
        from run_normal import insertion_loop

        data = [1]
        insertion_loop(data, master)
        self.assertEqual(data, [1])

    def test_insertion_sort_duplicate_elements(self):
        from run_normal import insertion_loop

        data = [5] * 10
        insertion_loop(data, master)
        self.assertEqual(data, [5] * 10)

    def test_insertion_sort_with_negative_numbers(self):
        from run_normal import insertion_loop

        data = [9, -8, 7, -6, 5, -4, 3, -2, 1]
        insertion_loop(data, master)
        self.assertEqual(data, [-8, -6, -4, -2, 1, 3, 5, 7, 9])


def run_tests(window):  # Run the unittests
    global master
    master = window
    result = unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestSortingAlgorithms)
    )
    if result.wasSuccessful():
        messagebox.showinfo(
            "Test Results", f"All tests passed!\n\nRan {result.testsRun} tests."
        )

    else:
        error_message = "Tests failed:\n\n"
        for failed_test, traceback in result.failures:
            error_message += f"FAIL: {failed_test.id()}\n\n"
            error_message += f"{traceback.split('AssertionError: ')[-1].strip()}\n\n"
        messagebox.showerror("Test Results", error_message)
