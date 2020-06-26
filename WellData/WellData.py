
from LAS import Converter
import pandas as pd
import numpy as np
import re
class WellData():
    def __init__(self,path,data=None,params=None,del_invalid=False):
        """
            Конструктор:
                path - путь до файла .las
                data   - данные, что нужно достать из файла {"Название параметра в файле": "Новое его название для dataframe"}
                params - параметры, что нужно достать из файла {"Название параметра в файле": "Новое его название для dataframe"}
                del_invalid -Удалять ли невалидные значения 
                
        """
        c= Converter()
        self.log = c.set_file(path)
        self.well = self.log.well
        params_l=self.log.parameter
        try:
            
            loc = self.log.well["LOC"]["value"]
            self.well_X,self.well_Y=re.findall(r'\d+\.\d+',loc)
        except Exception as e:
            print('Скорее всего отсутсвует поле loc, либо его формат неверен. Посмотрите stackTrace выше')
        if(params!=None):
            self.heads={}
            for key,value in params.items():
                self.__dict__[value] =params_l[key]['value']
                self.heads[value]= self.__dict__[value]
          
            self.heads=pd.DataFrame(self.heads,index=[0])
        
        if(data!=None):
            self.data={}
            for key,value in data.items():
                self.__dict__[value] =self.log.data[key]
                self.data[value]=self.__dict__[value]     
            self.data=pd.DataFrame(self.data)
            
            if(del_invalid):
                self.data=self.data.dropna()
        else:
            self.data = {}
            for key, value in self.log.data.items():
                self.__dict__[key] = self.log.data[key]
                self.data[key] = self.__dict__[key]
            self.data = pd.DataFrame(self.data)
            if (del_invalid):
                self.data = self.data.dropna()

    def convert_to_df_head(self):
        """
            func:
             Вовзращает dataframe из данных head(params)
            -----------------------------------------------
            return :
                        head
        """
        return self.heads
    def convert_to_df_data(self):
           """
            func:
             Вовзращает dataframe из данных data
            -----------------------------------------------
            return :
                        data
           """
           return self.data
    
    
    def convert_to_df(self,including=None,excluding=None):
        """
            including  - какие колонки включать
            excluding  - какие колонки исключать 
            func:
                 Более глубокая настройка конвертации указываем какие колонки нужны или какие не нужны
        """
        if(including):
                newdict={}
                for i in including:
                    newdict[i]=self.__dict__[i]
                return  pd.DataFrame(newdict)
        temp = self.__dict__.copy()
        try:
            temp["heads"]=None
            del temp["heads"]
            temp["data"] = None
            del temp["data"]
            del temp["log"]
            del temp["well"]
        except Exception as e:
            print(e)

        if(excluding):
                newdict={}
                for key,value in temp.items() :
                    if(key in excluding):
                        continue
                    else:
                        newdict[key]=value
                return  pd.DataFrame(newdict)
            
            
        return pd.DataFrame(temp)
    
    def merge(self,well,left_on,right_on):
        """
            well - data другого .las файла( pandas.dataframe)
            left_on - ключи из левого frame, по которому будет производиться слияние
            right_on - ключи из правого frame, по которому будет производиться слияние
            func:
                Слияние двух data .las файлов
            ----------------------------------
            return: 
                    новый dataframe после merger
        """
        well_res=self.data.merge(well,left_on=left_on, right_on=right_on)
        self.data=well_res
        return self.data
    
    def set_reflectivity(self,params):
        """
            params - Параметры для расчёта(?)
            func:
                Функция для расчёта и добавления столбца 'Reflectivity'
            ----------------------------------------------------------
            return : 
                    None
        """
        self.data['Reflectivity']=0.0
        for ii in range(0,len(self.data['Time'])-1):
            self.data['Reflectivity'][ii]=((1/self.data[params[0]][ii])*self.data[params[1]][ii]-(1/self.data[params[0]][ii+1])*self.data[params[1]][ii+1])/((1/self.data[params[0]][ii])*self.data[params[1]][ii]+(1/self.data[params[0]][ii+1])*self.data[params[1]][ii+1])
            
            
    
    def get_Refl_int(self,T_well):
        """
            T_well - данные для интерполирования
            func:
                Интерполируем T_well по параметрам "Time" и "Reflectivity"
            ---------------------------------------------------------------
            return :
                    Refl_int
        """
        self.Refl_int=np.interp(T_well,self.data['Time'],self.data['Reflectivity'])
        return self.Refl_int