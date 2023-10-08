import yaml

if __name__ == '__main__':

  stream = open("teste2.yaml", "r")
  dictionary = yaml.safe_load(stream)

  for key, value in dictionary.items():
    print(key + " : " + str(value))