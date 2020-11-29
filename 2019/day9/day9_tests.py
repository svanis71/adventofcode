import unittest
from . import run_intcode, unpack_instruction


class TestIntCode(unittest.TestCase):
    def test_unpack_109(self):
        self.assertEqual((9, 1, 0, 0), unpack_instruction(109))

    def test_unpack_1109(self):
        self.assertEqual((9, 1, 1, 0), unpack_instruction(1109))

    def test_unpack_1009(self):
        self.assertEqual((9, 0, 1, 0), unpack_instruction(1009))

    def test_unpack_204(self):
        self.assertEqual((4, 2, 0, 0), unpack_instruction(204))

    def test_plus_position_mode(self):
        program = [1, 2, 3, 0, 4, 0, 99]
        self.assertEqual(3, run_intcode(program, 1).pop(0))

    def test_multipy_position_mode(self):
        program = [1002, 6, 3, 6, 4, 6, 33]
        self.assertEqual(99, run_intcode(program, 1).pop(0))

    def test_print(self):
        program = [4, 3, 99, 42]
        self.assertEqual(42, run_intcode(program, 1).pop(0))

    def test_input_position_mode(self):
        program = [3, 0, 4, 0, 99]
        self.assertEqual(1, run_intcode(program, 1).pop(0))

    def test_opcode_7_lessthan_or_equal(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(1, run_intcode(program, 1).pop(0))

    def test_opcode_7_not_lessthan_or_equal(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(0, run_intcode(program, 9).pop(0))

    def test_opcode_8_isequal(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(1, run_intcode(program, 8).pop(0))

    def test_opcode_8_notequal(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(0, run_intcode(program, 9).pop(0))

    def test_opcode_8_immediate_mode_isequal(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(1, run_intcode(program, 8).pop(0))

    def test_opcode_8_immediate_mode_notequal(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(0, run_intcode(program, 9).pop(0))

    def test_opcode_9(self):
        program = [109, 2, 204, 2, 99]
        self.assertEqual(99, run_intcode(program, 1).pop(0))

    def test_should_return_999(self):
        program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(999, run_intcode(program, 7).pop(0))

    def test_should_return_1000(self):
        program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(1000, run_intcode(program, 8).pop(0))

    def test_should_return_1001(self):
        program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(1001, run_intcode(program, 9).pop(0))

    def test_1102(self):
        program = [1102, 2, 3, 0, 4, 0, 99]
        self.assertEqual(6, run_intcode(program, 9).pop(0))

    def test_ll(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        self.assertEqual(program, run_intcode(program, 1))

    def test_big_number(self):
        program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        self.assertEqual(1219070632396864, run_intcode(program, 0).pop(0))

    def test_big_number(self):
        program = [104, 1125899906842624, 99]
        self.assertEqual(1125899906842624, run_intcode(program, 0).pop(0))


if __name__ == '__main__':
    unittest.main()
