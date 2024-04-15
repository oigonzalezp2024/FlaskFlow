import json
from flask import Flask, render_template

class FlaskFlow(Flask):
    
    def renderJson(self, name:str='', page:str='', getData:str='./data/data.json')->object:
        obj = self.readJsonFile(getData)
        keys = self.getKeys(obj[0])
        data = self.getData(obj)
        render = self.renderTable(page, name, keys, data)
        return render
    
    def readJsonFile(self, file:str='./data/data.json')->object:
        fileData = open(file=file, mode='r', encoding='utf-8')
        data = fileData.read()
        fileData.close()
        objs = json.loads(data)
        return objs

    def getKeys(self, reg:object)->list:
        keys = []
        for key in reg.keys():
            keys.append(key)
        return keys 
    
    def getData(self, objs:object)->list:
        data = []
        for obj in objs:
            values = []
            for key in obj.values():
                values.append(key)
            data.append(values)
        return data
    
    def renderTable(self, page:str, name:str, keys:list, data:list)->object:
        render = render_template(
        page,
        name=name,
        keys=keys,
        data=data
        )
        return render
