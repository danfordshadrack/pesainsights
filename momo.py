import pandas as pd

dict = {
    'JANUARY': ['5,345,519','1,719,627','7,959,370', '756,352', '10,326,928', '395,981'],
    'FEBRUARY': ['5,549,511 ', '1,816,078', '7,954,048', '791,805 ', '10,157,671 ', '401,969'],
    'MARCH': ['5,626,586', '1,853,290', '8,330,330', '825,888', '10,102,681', '388,523']
}

df = pd.DataFrame(dict, index=['Airtel Money', 'Halopesa', 'Tigo Pesa', 'TTCL', 'M-PESA', 'Ezy Pesa'])
df.to_csv('MOMO-sub.csv')
print(df)