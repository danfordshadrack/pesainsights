import pandas as pd

read_file = pd.read_csv(r'C:\Users\HP ELITEBOOK GAMING\Desktop\pesainsight\tigo.txt')
read_file.to_csv('tigodata', index=None)
