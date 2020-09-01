import pandas as pd
import pickle as pkl

df = pd.read_csv("../data/val_bf.csv")
#Above, filepath has been changed. Added "../" at the beginning.
df.dropna(inplace = True)

target = df["Survived"]
del(df["Survived"])
    
model_unpickle = open("../data/model.pkl", 'rb')
#Above, filepath has been changed. Added "../" at the beginning.
model = pkl.load(model_unpickle)
#model.close()
#Line above gives the following error:
#AttributeError: 'RandomForestClassifier' object has no attribute 'close'
#This line should be changed to:
model_unpickle.close()

predictions = model.predict(df)
# Reassign target (if it was present) and predictions.
df["prediction"] = predictions
df["target"] = target

ok = 0
for i in df.iterrows():
    if (i[1]["target"] == i[1]["prediction"]):
        ok = ok + 1

print("accuracy is", ok / df.shape[0])
