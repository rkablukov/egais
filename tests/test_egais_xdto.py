import unittest

import sys
from io import StringIO
import egais


class TestEgaisXdto(unittest.TestCase):

    def setUp(self):
        self.data_dir = "./tests/data"

    def test_parse_WayBill_v3(self):        
        wb = egais.parse('%s/WayBill_v3.xml' % self.data_dir)
        
        self.assertEqual(wb.Owner.FSRAR_ID, '010000000435')
        self.assertEqual(wb.Document.WayBill_v3.Header.Type, 'WBInvoiceFromMe')
    
    def test_export_QueryFormF2(self):
        doc = egais.Documents()
        doc.Owner = egais.SenderInfo(FSRAR_ID='123456789012')
        doc.Document = egais.DocBody()

        queryFormF2 = egais.QueryFormF1F2(FormRegId='FB-000000005664278')
        doc.Document.QueryFormF2 = queryFormF2

        with StringIO() as sf:
            doc.export(sf, 0)
            result = sf.getvalue()
        
        self.assertIn('123456789012', result)
        self.assertIn('FB-000000005664278', result)


if __name__ == '__main__':
    unittest.main()