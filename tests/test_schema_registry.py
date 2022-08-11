import unittest
from pathlib import Path

from sql_schema_registry.files import SchemaRegistryFiles


class TestSchemaRegistryFiles(unittest.TestCase):

    def test_get_file_list_ordered(self):
        sf = SchemaRegistryFiles(schema_name='files')
        sf.get_file_list_ordered(sql_path='.')
        self.assertEqual(sorted([p for p in Path('./files/').iterdir() if p.is_file()]),
                         sf.get_file_list_ordered(sql_path='./'))

    def test__read_file(self):
        sf = SchemaRegistryFiles(schema_name='files')
        self.assertEqual(sf._read_file(filepath='./files/3-CREATE_TABLE_d_example.sql'), 'SELECT 1;')

    def test_parse_sql_file(self):
        sf = SchemaRegistryFiles(schema_name='files')
        ddl, object_name = sf.parse_sql_file(sql_file='1-CREATE_TABLE_d_user.sql')
        self.assertEqual(ddl, 'CREATE TABLE')
        self.assertEqual(object_name, 'd_user')

    def test_check_qa_sql_file(self):
        code_formatted = "CREATE TABLE d_user_2;"
        sf = SchemaRegistryFiles(schema_name='files')
        code = sf.check_qa_sql_file(sql_file='./files/2-CREATE_TABLE_d_user_2.sql', rewrite=False)
        self.assertEqual(code, code_formatted)


if __name__ == '__main__':
    unittest.main()
