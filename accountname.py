
def get_account_name():
  """Return the account name from hotslig.properties"""
  prop_file = open('hotslig.properties', 'r')
  lines = prop_file.read().split("\n")
  dict = {}
  for line in lines:
    props = line.split('=')
    if line != '' and len(props) == 2:
      dict[props[0]] = props[1]

  account_name = dict['accountName'] if dict['accountName'] is not None else 'Funda'
  return account_name