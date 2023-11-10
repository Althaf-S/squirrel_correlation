import json

def load_journal_file(jfile = "/home/althaf/sqcr/squirrel_correlation/journal.json"):
   with open(jfile, 'r') as file:
      journal = json.load(file)
   return journal
    
print(load_journal_file())


