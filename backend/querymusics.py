import pandas as pd

class QueryMusics:
    
    def __init__(self):
        self.table = pd.read_csv('total_cls.csv', encoding = "ISO-8859-1")

    def getName(self, path):
        filename = path.split('\\')[-1]
        name = filename[:-4]
        listName = name.split('-')
        if len(listName) == 1:
            return 'empty'
        elif len(listName) > 2:
            return 'empty'
        #    #return listName[0]
        return name

    def search(self, min, max):
        print("TABLE",self.table.shape)
        f1 = self.table[self.table['max'] <= max]
        f2 = f1[f1['min'] >= min]
        #print(f2)
        f3 = f2 #f3 = f2[f2['vocal'] == True]
        f4 = f3['filename']
        f5 = f4.apply(self.getName)

        return f5[f5 != 'empty']
    