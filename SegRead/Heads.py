import numpy as np
from math import pow
import decimal
class BinHead():

    def __init__(self, list_header_bin,order):
        self.JobId = int.from_bytes(list_header_bin[0:4:], order,signed=True)
        self.LineNumber = int.from_bytes(list_header_bin[4:8:], order,signed=True)
        self.ReelNumber = int.from_bytes(list_header_bin[8:12:], order,signed=True)
        self.Traces = int.from_bytes(list_header_bin[12:14:], order,signed=True)
        self.AuxTraces = int.from_bytes(list_header_bin[14:16:], order,signed=True)
        self.Interval = int.from_bytes(list_header_bin[16:18:], order,signed=True)
        self.IntervalOriginal = int.from_bytes(list_header_bin[18:20:], order,signed=True)
        self.Samples = int.from_bytes(list_header_bin[20:22:], order)
        self.SamplesOriginal = int.from_bytes(list_header_bin[22:24:], order,signed=True)
        self.Format = int.from_bytes(list_header_bin[24:26:], order,signed=True)
        self.EnsembleFold = int.from_bytes(list_header_bin[26:28:], order,signed=True)  # ?
        self.SortingCode = int.from_bytes(list_header_bin[28:30:], order,signed=True)
        self.VerticalSum = int.from_bytes(list_header_bin[30:32:], order,signed=True)
        self.SweepFrequencyStart = int.from_bytes(list_header_bin[32:34:], order,signed=True)
        self.SweepFrequencyEnd = int.from_bytes(list_header_bin[34:36:], order,signed=True)
        self.SweepLength = int.from_bytes(list_header_bin[36:38:], order,signed=True)
        self.Sweep = int.from_bytes(list_header_bin[38:40:], order,signed=True)
        self.SweepChannel = int.from_bytes(list_header_bin[40:42:], order,signed=True)
        self.SweepTaperStart = int.from_bytes(list_header_bin[42:44:], order,signed=True)
        self.SweepTaperEnd = int.from_bytes(list_header_bin[44:46:], order,signed=True)
        self.Taper = int.from_bytes(list_header_bin[46:48:], order,signed=True)
        self.CorrelatedTraces = int.from_bytes(list_header_bin[48:50:], order,signed=True)
        self.BinaryGainRecovery = int.from_bytes(list_header_bin[50:52:], order,signed=True)
        self.AmplitudeRecovery = int.from_bytes(list_header_bin[52:54:], order,signed=True)
        self.MeasurementSystem = int.from_bytes(list_header_bin[54:56:], order,signed=True)
        self.ImpulseSignalPolarity = int.from_bytes(list_header_bin[56:58:], order,signed=True)
        self.VibratoryPolarity = int.from_bytes(list_header_bin[58:60:], order,signed=True)
        self.order =  int.from_bytes(list_header_bin[96:100:], "big",signed=True)
        self.Spare = int.from_bytes(list_header_bin[60:401:], order,signed=True)



class TraceBinHead():
    def __init__(self):
            self.TRACE_SEQUENCE_LINE =[0,4]
            self.TRACE_SEQUENCE_FILE=[4,4]
            self.FieldRecord=[8,4]
            self.TraceNumber=[12,4]
            self.EnergySourcePoint=[16,4]
            self.CDP=[20,4]
            self.CDP_TRACE=[24,4]

            self.TraceIdentificationCode=[28,2]
            self.NSummedTraces=[30,2]
            self.NStackedTraces=[32,2]
            self.DataUse=[34,2]

            self.offset=[36,4]
            self.ReceiverGroupElevation=[40,4]
            self.SourceSurfaceElevation=[44,4]
            self.SourceDepth=[48,4]
            self.ReceiverDatumElevation=[52,4]
            self.SourceDatumElevation =[56,4]
            self.SourceWaterDepth=[60,4]
            self.GroupWaterDepth=[64,4]

            self.ElevationScalar =[68,2]
            self.SourceGroupScalar=[70,2]
            self.SourceX=[72,4]
            self.SourceY=[76,4]
            self.GroupX=[80,4]
            self.GroupY=[84,4]

            self.CoordinateUnits=[88,2]
            self.WeatheringVelocity=[90,2]
            self.SubWeatheringVelocity=[92,2]
            self.SourceUpholeTime=[94,2]
            self.GroupUpholeTime=[96,2]
            self.SourceStaticCorrection=[98,2]

            self.GroupStaticCorrection=[100,2]
            self.TotalStaticApplied=[102,2]
            self.LagTimeA =[104,2]
            self.LagTimeB =[106,2]
            self.DelayRecordingTime=[108,2]
            self.MuteTimeStart=[110,2]

            self.MuteTimeEND=[112,2]
            self.TRACE_SAMPLE_COUNT=[114,2]
            self.TRACE_SAMPLE_INTERVAL=[116,2]
            self.GainType=[118,2]
            self.InstrumentGainConstant=[120,2]
            self.InstrumentInitialGain=[122,2]

            self.Correlated=[124,2]
            self.SweepFrequencyStart=[126,2]
            self.SweepFrequencyEnd=[128,2]
            self.SweepLength=[130,2]
            self.SweepType=[132,2]
            self.SweepTraceTaperLengthStart=[134,2]

            self.SweepTraceTaperLengthEnd =[136,2]
            self.TaperType=[138,2]
            self.AliasFilterFrequency=[140,2]
            self.AliasFilterSlope=[142,2]
            self.NotchFilterFrequency =[144,2]
            self.NotchFilterSlope =[146,2]

            self.LowCutFrequency =[148,2]
            self.HighCutFrequency =[150,2]
            self.LowCutSlope =[152,2]
            self.HighCutSlope =[154,2]
            self.YearDataRecorded =[156,2]
            self.DayOfYear =[158,2]

            self.HourOfDay=[160,2]
            self.MinuteOfHour=[162,2]
            self.SecondOfMinute =[164,2]
            self.TimeBaseCode=[166,2]
            self.TraceWeightingFactor=[168,2]
            self.GeophoneGroupNumberRoll1=[170,2]

            self.GeophoneGroupNumberFirstTraceOrigField=[172,2]
            self.GeophoneGroupNumberLastTraceOrigField=[174,2]
            self.GapSize=[176,2]
            self.OverTravel=[178,2]
            self.CDP_X=[180,4]
            self.CDP_Y=[184,4]

            self.ILINE_NO=[188,4]
            self.XLINE_NO=[192,4]
            self.ShortpointNumber=[196,4]
            self.ScalarValueForShortpointNumber=[200,2]
            self.TraceValueMeasurementUnit=[202,2]
            self.TransductionConstant=[204,6]

            self.TransductionUnits=[210,2]
            self.DeviceIdentifier=[212,2]
            self.ScalarToTimes=[214,2]
            self.SourceType=[216,2]
            self.SourceEnergyDirectionVerticalOrientation=[218,2]
            self.SourceEnergyDirectionCrossLineOrientation = [220, 2]
            self.SourceEnergyDirectionInLineOrientation = [222, 2]
            self.SourceMeasurement=[224,6]

            self.SourceMeasurementUnit=[230,2]
            self.ex1=[232,4]
            self.ex2=[236,4]


    def get_all_trace(self,list_trace_head_bin,order):
        if order == "big":
            order_ = ">"
        else:
            order_ = "<"
        keys = self.__dict__.keys()
        first_part = np.frombuffer(list_trace_head_bin,dtype=order_ + "i4",count=7,offset=0)
        second_part = np.frombuffer(list_trace_head_bin,dtype=">i2",count=4,offset=28)
        third_part = np.frombuffer(list_trace_head_bin,count=8,offset=36,dtype=order_ + "i4")
        fouth_part = np.frombuffer(list_trace_head_bin,count=2,offset=68,dtype=order_ + "i2")
        fifth_part = np.frombuffer(list_trace_head_bin,count=4,offset=72,dtype=order_ + "i4")
        six_part =   np.frombuffer(list_trace_head_bin,count=46,offset=88,dtype=order_ + "i2")
        seven_part = np.frombuffer(list_trace_head_bin,count =5,offset=180,dtype=order_ + "i4")
        eight_part = np.frombuffer(list_trace_head_bin,count =2,offset=200,dtype=order_ + "i2")
        mantisa=int.from_bytes(list_trace_head_bin[204:208],byteorder=order,signed=True)
        exponent = int.from_bytes(list_trace_head_bin[208:210],byteorder=order,signed=True)
        nine_part= [mantisa * pow(10,exponent)]

        ten_part =   np.frombuffer(list_trace_head_bin,count=4,offset=210,dtype=order_ + "i2")

        elev_part=  np.frombuffer(list_trace_head_bin,count =3,offset=218,dtype=order_ + "i2")


        twelve_part=[int.from_bytes(list_trace_head_bin[224:228],byteorder=order,signed=True)*
                    pow(10,int.from_bytes(list_trace_head_bin[228:230],byteorder=order,signed=True))]

        thirteen_part=  np.frombuffer(list_trace_head_bin,count =1,offset=230,dtype=order_ + "i2")
        fourteen_part =   np.frombuffer(list_trace_head_bin,count =2,offset=232,dtype=order_ + "i4")
        data=np.concatenate((first_part, second_part, third_part, fouth_part,
                             fifth_part, six_part, seven_part, eight_part,
                             nine_part, ten_part, elev_part, twelve_part,
                             thirteen_part, fourteen_part))
        trace=dict(zip(keys,data))
        iter=0
        return trace
    def get_specific_trace(self,f,order,cur,a:list=None):
        data={}
        fields = self.__dict__
        if(a==None or (len(a)<=0)):
            return
        else:
            for i in a:
                f.seek(cur+fields[i][0],0)
                data[i]=int.from_bytes(f.read(fields[i][1]),order,signed=True)
        return data

four_bytes={"JobId","LineNumber","ReelNumber","order",
            "TRACE_SEQUENCE_LINE","TRACE_SEQUENCE_FILE","FieldRecord","TraceNumber",
            "EnergySourcePoint","CDP","CDP_TRACE","offset",
            "ReceiverGroupElevation","SourceSurfaceElevation","SourceDepth","ReceiverDatumElevation",
            "SourceDatumElevation","SourceWaterDepth","GroupWaterDepth",
            "SourceX","SourceY","GroupX","GroupY"}

def writeBinHead(f,Headers,order):
    bytes=0
    for i,k in Headers.__dict__.items():
        if (i == "order"):
            continue
        if(i=="Spare"):
            f.write(k.to_bytes(340,order))
            bytes+=340
            continue
        if(i in four_bytes):
            f.write(k.to_bytes(4,order))
            bytes+=4
        else:
            f.write(k.to_bytes(2,order))
            bytes+=2
def writeTraceHeadEmpty(f,Headers,order):
    a = bytearray(240)
    print(type(Headers))
    for i,k in Headers.__dict__.items():

        if(i=="spare"):
            a.extend(int(k).to_bytes(60, order, signed=True))
            continue
        if(i in four_bytes):
            a.extend(int(k).to_bytes(4, order, signed=True))
        else:
            a.extend(int(k).to_bytes(2, order, signed=True))

    return  a
def writeTraceHead(f,Headers,order):
    order_ = ">"
    a=bytes()
    if order=="big":
        order_=">"
    else:
        order_="<"
    data = list(Headers.values)
    first_part = np.array(data[0:7], dtype=order_ + "i4").tobytes()
    second_part = np.array(data[7:11], dtype=">i2").tobytes()
    third_part = np.array(data[11:19], dtype=order_ + "i4").tobytes()

    fouth_part = np.array(data[19:21], dtype=order_ + "i2").tobytes()
    fifth_part = np.array(data[21:25],  dtype=order_ + "i4").tobytes()

    six_part = np.array(data[25:71], dtype=order_ + "i2").tobytes()
    seven_part = np.array(data[71:76],  dtype=order_ + "i4").tobytes()
    eight_part = np.array(data[76:78],  dtype=order_ + "i2").tobytes()

    num = format(decimal.Decimal(int(data[78])))
    if num!="0":
        mantisa=int(float(num[0:num.find("e")])).to_bytes(4,order, signed=True)
        power = int(float(num[num.find("e") + 2:])).to_bytes(2, order, signed=True)
    else:
        mantisa = int(0).to_bytes(4,order, signed=True)
        power =   int(0).to_bytes(2, order, signed=True)


    nine_part=mantisa+power
    ten_part = np.array(data[79:83],  dtype=order_ + "i2").tobytes()

    elev_part = np.array(data[83:86],  dtype=order_ + "i2").tobytes()

    num = format(decimal.Decimal(int(data[86])))
    if num!="0":
        mantisa=int(float(num[0:num.find("e")])).to_bytes(4,order, signed=True)
        power = int(float(num[num.find("e") + 2:])).to_bytes(2, order, signed=True)
    else:
        mantisa = int(0).to_bytes(4,order, signed=True)
        power =   int(0).to_bytes(2, order, signed=True)

    twelve_part =  mantisa+power

    thirteen_part = np.array(data[87], dtype=order_ + "i2").tobytes()
    fourteen_part = np.array(data[88:], dtype=order_ + "i4").tobytes()
    a=first_part+second_part+third_part+fouth_part+fifth_part+six_part
    a+=seven_part+eight_part+nine_part+ten_part+elev_part+twelve_part+thirteen_part+fourteen_part
    return  a

def writeData(f,Data,coef,order):
    res =None
    if ("int" in str(type(Data[0]))):
       return(Data.astype(int).tobytes())
    elif ("float" in str(type(Data[0]))):
        if(order=="big"):
            res= Data.astype(">f").tobytes()
        else:
            res = Data.astype("<f").tobytes()
    return res
