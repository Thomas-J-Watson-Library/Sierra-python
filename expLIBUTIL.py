#!python
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# file: expLIBUTIL.py
# desc: Utility function(s)

def get_target(bib):
  input_len = len(bib)

  if input_len > 10 or  input_len < 7:
      print('\n  ',bib,'is an invalid length\n')
      target = None
      exit(100)
  if input_len == 10:
      # .b1977239x
      target = bib[1:9].lower()
      # print(target)
  if input_len == 9 and bib.startswith('.'):
      # .b1977239
      target = bib[1:9].lower()
      # print(target)
  if input_len == 9 and not bib.startswith('.'):
      # b1977239x
    target = bib[0:8]
      # print(target)
  if input_len == 8 and bib.startswith('b'):
      target = bib.lower()
  if input_len == 8 and bib.startswith('B'):
      target = bib.lower()
      # print(target)
  if input_len == 8 and not bib.startswith('b'):
      # 1977239x
      target = 'b'+bib[0:7]
      # print(target)
  if input_len == 7:
      # 1977239
      target = 'b'+bib
      # print(target)
  return(target)

def API_cleanup(data):
  ''' This fixes a problem with Sierra API response that gets a MARC record.
      The API does not put quotes around the names of keys, so this does that
      step for us.
  '''
  r1 = data.replace("leader:","\"leader\" :")
  r2 = r1.replace("controlfield:","\"controlfield\":")
  r3 = r2.replace("tag :","\"tag\" :")
  r4 = r3.replace("ind :","\"ind\" :")
  r5 = r4.replace("subfield :","\"subfield\" :")
  r6 = r5.replace("]","],",1)
  r7 = r6.replace("datafield :","\"datafield\" :")
  r8 = r7.replace("{ code :","{ \"code\" :")
  rx = r8.replace(", data :",", \"data\" :")
  # rx is the last replacement. The API response is now valid JSON.
  return(rx)
