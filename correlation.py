import json


def load_journal(j_file = 'journal.json'):
   with open(j_file, 'r') as journal:
      journal_data = json.load(journal)
   return list(journal_data)
   j_file.close()

def compute_phi(data,event):
    n11 = 0
    n00 = 0
    n10 = 0
    n01 = 0
    for i in data:
        is_squirrel = i['squirrel']
        is_event = event in i['events']
        if is_squirrel and is_event:
            n11 += 1
        elif not is_squirrel and not is_event:
            n00 += 1
        elif not is_squirrel and is_event:
            n10 += 1
        elif is_squirrel and not is_event:
            n01 += 1

    phi = (n11 * n00 - n10 * n01) / ((n11 + n10) * (n01 + n00) * (n11 + n01) * (n10 + n00)) ** 0.5
    return phi
    
    
def main():
  data = load_journal()
  events_done = []
  for i in data:
    for j in i['events']:
      events_done.append(j)
  correlation = {}
  for i in events_done:
    result = compute_phi(data,i)
    correlation[i]=result
    print(correlation)
  print("most_correlated_event =   "+max(correlation,key=correlation.get))

  print("min_correlated_event  =   "+min(correlation,key=correlation.get))

if __name__ == "__main__":
  main()


