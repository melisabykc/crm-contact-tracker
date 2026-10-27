import argparse, json, sqlite3
from pathlib import Path
DB=Path(__file__).with_name('data.sqlite3')
TABLE='contacts'
def connect(path=DB):
 c=sqlite3.connect(str(path)); c.row_factory=sqlite3.Row; c.execute("CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, company TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'lead')"); return c
def add(values,path=DB):
 with connect(path) as c:
  cur=c.execute("INSERT INTO contacts(name,email,company,status) VALUES(?,?,?,?)",values); return cur.lastrowid
def listing(path=DB):
 with connect(path) as c:return [dict(r) for r in c.execute('SELECT * FROM contacts ORDER BY id DESC')]
def main():
 p=argparse.ArgumentParser(description='Track customer contacts and relationship status.'); s=p.add_subparsers(dest='cmd',required=True); a=s.add_parser('add');
 a.add_argument('--name',required=True); a.add_argument('--email',required=True); a.add_argument('--company',required=True); a.add_argument('--status',required=True)
 s.add_parser('list'); x=p.parse_args()
 if x.cmd=='add': print(json.dumps({'id':add([x.name, x.email, x.company, x.status])}))
 else: print(json.dumps(listing(),indent=2))
if __name__=='__main__': main()
