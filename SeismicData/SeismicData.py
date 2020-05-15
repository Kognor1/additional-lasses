import SegRead as s
import pandas as pd
import numpy as np
import copy
class SeismicData():
    def __init__(self,path=None,head_e=None,data_e=None,binHead_e=None,dt_e=1.0):
        """
            path - путь до файла .sgy/.segy
            Аргументы, если нужен класс без segy файла, нужно выставить path=None
            data_e    - Данные трасс(numpy.array)
            head_e    - Заголовок(dict{"SampleCount: 2000"...})
            binHead_e - Заголовок трасс(pandas.dataframe)
            dt_e      - шаг дескретизации
        """
        self.ss = s.Seg.SegReader()
        if(path!=None):
            self.ss.open(path)
            data,head=self.ss.get_data_and_trace_heads()
            self.data=data.T
            self.head=head
            self.binHead=self.ss.get_bin_head().__dict__
            self.dt = self.ss.get_dt()/1000
            self.Tdata =np.arange(0,np.shape(self.data)[0]*self.dt,self.dt)/1000
        else:
            self.data = data_e
            self.head=head_e
            self.binHead=binHead_e
            self.dt = dt_e
            self.Tdata =np.arange(0,np.shape(self.data)[0]*self.dt,self.dt)/1000

    def get_spchere(self,CDP_X,CDP_Y,radius):
        """
            Выделяет трассы в радиусе от заданной
            CDP_X  - Координаты по x
            CDP_Y  - Координаты по y
            radius - радиус( радиус 1 - покажет 9 значений)
            -----------------------------------------------------
            return :  .   .   .
                      . (x,y) .
                      .   .   .

        """
        idx = self.head[(self.head["CDP_X"] ==CDP_X )& (self.head["CDP_Y"] ==CDP_Y)]

        i_line=    (idx["ILINE_NO"].values[0])
        x_line = (idx["XLINE_NO"].values[0])

        i_line_filter=[i_line + i for i in range(-radius,radius+1)]
        x_line_filter=[x_line + i for i in range(-radius,radius+1)]

        res = self.head.query(" @i_line_filter in ILINE_NO and @x_line_filter in XLINE_NO")
        return res


    def get_offset(self,lasData):
        """
            Функция рассчитывает и возращает оффсет
            lasData - объект типа WellData с параметрами well_X, well_Y
            ----------------------------------------------------------
            return:
                    offset
        """
        self.offsets=np.zeros(len(self.head['CDP_X']))
        for ii in range(0, len(self.head['CDP_X'])):
            self. offsets[ii]=np.sqrt((lasData.well_X-self.head['CDP_X'][ii])*(lasData.well_X-self.head['CDP_X'][ii])+(lasData.well_Y-self.head['CDP_Y'][ii])*(lasData.well_Y-self.head['CDP_Y'][ii]))
        return self.offsets

    def get_Seism_sig(self,T_well,a):
        """
            T_well - ?
            a      ->
            Функция рассчитывает и возращает Сейсмический сигнал
            lasData - объект типа WellData с параметрами well_X, well_Y
            ----------------------------------------------------------
            return:
                    Seism_sig
        """
        self.Seism_sig=np.interp(T_well,self.Tdata,np.squeeze(self.data[:,a[0]]))
        return self.Seism_sig
    def copy(self):
        """
            Возвращает Копию текущего SeismcData, но без привзяки к файлу(.sgy)
            -------------------------------------------------------------------
            return : SeismicData(....)
        """
        return SeismicData(path=None,data_e=self.data,head_e=self.head,binHead_e=self.binHead,dt_e=self.dt)
