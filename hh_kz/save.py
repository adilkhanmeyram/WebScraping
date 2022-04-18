import csv

def save_to_csv(jobs):
  file = open('test.csv', mode='w' , newline = '')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link' , 'zp'])
  for job in jobs:
    try:
      writer.writerow([job['title'],job['company'],job['location'] , job['link'] , job['zp']])
    except UnicodeError:
        writer.writerow(["NAN" , "NAN","NAN" , "NAN"])
  return