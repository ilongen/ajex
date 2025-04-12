import unittest
import pandas as pd
from template.manipulationData import manipulationData 

class TestManipulationData(unittest.TestCase):
    def test_delete_cell(self):
        # 1. Criar um DataFrame com NA
        df = pd.DataFrame({
            'A': [None, 1, None],
            'B': [None, 2, None],
            'C': [None, 3, 4],
            'D': [None, 3, 4],
            'E': [None, None, None],
            'F': [None, None, None],
            'G': [None, 3, None],
            'H': [None, None, 4],

        })

        # 2. Criar o objeto e rodar os métodos
        manip = manipulationData(df.copy())
        manip.valueCell_isna()
        result = manip.deletCell()

        # 3. Verificar se a linha 0 foi deletada (tinha 100% NA)
        self.assertEqual(len(result), 2)
        self.assertNotIn(0, result.index)

if __name__ == '__main__':
    unittest.main()
