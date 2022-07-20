import unittest
from app import delete_doc, show_all_docs_info, add_new_doc


# Запускать методы класса под отдельности, иначе они накладываются друг на друга
class TestFunctions(unittest.TestCase):

    def test_delete_doc(self):
        '''Test delete item from document'''
        result = delete_doc('11-2')
        etalon = '11-2', True
        self.assertEqual(result, etalon)

    def test_show_all_docs_info(self):
        '''Test for show document'''
        result = show_all_docs_info()
        etalon = ['passport "2207 876234" "Василий Гупкин"',
                  'invoice "11-2" "Геннадий Покемонов"',
                  'insurance "10006" "Аристарх Павлов"']
        self.assertEqual(result, etalon)

    def test_delete_doc_and_show_all_docs_info(self):
        result = delete_doc('10006')
        etalon = '10006', True
        self.assertEqual(result, etalon)

        result_2 = show_all_docs_info()
        etalon_2 = ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"']
        self.assertEqual(result_2, etalon_2)

    def test_add_new_doc(self):
        '''Test add new doc with return shelf'''
        result = add_new_doc('3332-3', 'passport', 'Vlad Panasenko', '3')
        etalon = '3'
        self.assertEqual(result, etalon)

        result_2 = show_all_docs_info()
        etalon_2 = ['passport "2207 876234" "Василий Гупкин"',
                    'invoice "11-2" "Геннадий Покемонов"',
                    'insurance "10006" "Аристарх Павлов"',
                    'passport "3332-3" "Vlad Panasenko"']
        self.assertEqual(result_2, etalon_2)