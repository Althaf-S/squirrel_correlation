import json
import math

def load_journal(j_file = 'journal.json'):
   with open(j_file, 'r') as journal:
      journal_data = json.load(journal)
   return journal_data

def compute_phi():
    data = list(load_journal())
    #print(data)
    events_done = []
    n00,n01,n10,n11 = 0,0,0,0
    n1a,n0a,na1,na0 = 0,0,0,0
    for i in data:
      for event in i['events']:
        events_done.append(event)
      is_event = i['events']
      is_squirrel = i['squirrel']
      for j in events_done:
         if j in is_event and is_squirrel:
            n11 += 1
         elif j in is_event and not is_squirrel:
            n10 += 1
         elif j not in is_event and is_squirrel:
            n01 += 1
         elif j not in is_event and not is_squirrel:
            n00 =+ 1
         

#print(load_journal(),)
compute_phi()
    
    
    
       
