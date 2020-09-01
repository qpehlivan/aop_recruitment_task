import pandas as pd
import numpy as np

def execute(input_file, output_file):
    
    data = pd.read_csv(input_file, sep = ";")
    
    del(data["Name"])
    del(data["Ticket"])
    del(data["Cabin"])
    
    data = data.dropna()
    
    #Above, the line with dropna() should NOT go
    #first. Before that, we must get rid of the
    #unwanted data.
    
    #This prevents deleting usable data.
    
    data.to_csv(output_file)
    
execute("../data/train.csv","../data/train.csv")

execute("../data/val.csv","../data/val.csv")
#Line 15 and 17 has been added with the file path
#to execute the function above.


#Now, both .csv files are fitted for the purpose.