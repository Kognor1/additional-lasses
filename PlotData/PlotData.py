import pandas as pd
import numpy as np
import pylab as plt
class PlotData():#Класс для хранения данных (новое название)
    def __init__(self,x,y,color=None,linestyle=None,linewidth=2,label=None):
        """
            Конструктор:
             x,y - данные
             color - цвет
             label - метка
             linestyle - тип линий{'-', '--', '-.', ':', '', } 
             linewidth - ширина линии
            #Те же данные, что передаются в plot(x,y,color,lineidth,label)
        """
        self.x=x
        self.y=y
        self.color=color
        self.linewidth = linewidth
        self.label=label
        self.linestyle=linestyle
        
    def get_x(self):
        """Getter :
               return x
        """
        return self.x
    
    def get_y(self):
        """Getter :
               return y
        """
        return self.y
    def get_color(self):
        """Getter :
               return color
        """
        return self.color
    
    def get_linewidth(self):
        """Getter :
               return linewidth
        """
        return self.linewidth
    
    def get_label(self):
        """Getter :
               return label
        """
        return self.label
    def get_linestyle(self):
        """Getter :
               return linestyle
        """
        return self.linestyle

class SubFig():
    """Класс отвечающий за один график на канвасе аналог axs[i]"""
    def __init__(self,plots_data=[],
                 x_lim=[],
                 y_lim=[],
                 x_label="X",
                 y_label="Y",
                 title="title",
                 fontsize=14,
                 linestyle="-"):
        
        """
            Constructor : 
                plots_data - Список классов для даты[plot_data_1(),plot_data_2()...]
                x_lim      - [min,max] по x
                y_lim      - [min,max] по y
                x_label    - меткa по x
                y_label    - меткa по y
                title      - название
                fontsize   - размер шрифта
                linestyle  - тип линий{'-', '--', '-.', ':', '', } 
                
        """
        self.plot_data=plots_data
        self.x_label=x_label
        self.y_label=y_label
        self.title=title
        self.fontsize=14
        self.x_lim=x_lim
        self.y_lim=y_lim
        self.linestyle=linestyle
        
    def get_title(self):
        """Getter :
               return title
        """
        return self.title
           
    def get_fontsize(self):
        """Getter :
               return fontsize
        """
        return self.fontsize
           
    def get_plot_data(self):
        """Getter :
               return plot_data
        """
        return self.plot_data
           
    def get_y_label(self):
        """Getter :
               return y_label
        """
        return  self.y_label
           
    def get_x_label(self):
        """Getter :
               return x_label
        """
        return   self.x_label
    
    def get_y_lim(self):
        """Getter :
               return y_lim
        """
        return  self.y_lim
           
    def get_x_lim(self):
        """Getter :
               return x_lim
        """
        return   self.x_lim
    def get_linestyle(self):
        """Getter :
               return linestyle
        """
        return self.linestyle
    

def imshow(data,extent=None,aspect="auto",cmap=None):
    """Обрезанный аналог plt.imshow"""
    plt.imshow(data,aspect=aspect,extent=extent,cmap = cmap)
    
    
def paint_subplots(nrows=None,ncols=None,figsize=None,layers=[],wspace=0.7,hspace=0.7):
    """
        nrows - количетсво фигур в строке
        ncols - количетсво фигур в столбце
        Если nrows и ncols не заданы, или равны 1, то фигура одна
        figsize(x,y) - размер фигуры
        layers[SubFig,SubFig,...] - массив с фигурой(один элемент в массиве - одна фигура)
        wspace - размер расстояния между фигурами по гоирзонтали A <--wspace-> A
        hspace - размер расстояния между фигурами по вертикали . (A <--hspace-> A).T
    """
    if(not nrows or not ncols or (nrows==1 and ncols==1)):
        fig,axs = plt.subplots(figsize=figsize,constrained_layout=True)
        for j in range(len(layers[0].get_plot_data())):
                if(len(layers[0].get_y_lim())>0):
                    axs.set_ylim(layers[0].get_y_lim()[0],layers[0].get_y_lim()[1])
                if(len(layers[0].get_x_lim())>0):
                    axs.set_xlim(layers[0].get_x_lim()[0],layers[0].get_x_lim()[1])
                axs.set_ylabel(layers[0].get_y_label())
                axs.set_xlabel(layers[0].get_x_label());
                axs.set_title(layers[0].get_title())
                axs.plot(layers[0].get_plot_data()[j].get_x(),layers[0].get_plot_data()[j].get_y(),color=layers[0].get_plot_data()[j].get_color(),
                        linewidth=layers[0].get_plot_data()[j].get_linewidth(),label=layers[0].get_plot_data()[j].get_label(),linestyle=layers[0].get_plot_data()[j].get_linestyle())
        return
        
        
    fig,axs = plt.subplots(nrows,ncols,figsize=figsize,constrained_layout=True)
    for i in range(len(layers)):
        for j in range(len(layers[i].get_plot_data())):
            if(len(layers[i].get_y_lim())>0):
                axs[i].set_ylim(layers[i].get_y_lim()[0],layers[i].get_y_lim()[1])
            if(len(layers[i].get_x_lim())>0):
                axs[i].set_xlim(layers[i].get_x_lim()[0],layers[i].get_x_lim()[1])

            axs[i].set_ylabel(layers[i].get_y_label())
            axs[i].set_xlabel(layers[i].get_x_label());
            axs[i].plot(layers[i].get_plot_data()[j].get_x(),layers[i].get_plot_data()[j].get_y(),color=layers[i].get_plot_data()[j].get_color(),
                        linewidth=layers[i].get_plot_data()[j].get_linewidth(),label=layers[i].get_plot_data()[j].get_label(),
                        linestyle=layers[i].get_plot_data()[j].get_linestyle())

  
        axs[i].set_title(layers[i].get_title())
        plt.subplots_adjust(wspace=wspace,hspace=hspace)