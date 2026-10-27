import tempfile, unittest
from pathlib import Path
import app
class Tests(unittest.TestCase):
 def test_add_and_list(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'test.sqlite3'; app.add(["Ada","ada@example.com","Example Co","lead"],p); self.assertEqual(len(app.listing(p)),1)
if __name__=='__main__': unittest.main()
