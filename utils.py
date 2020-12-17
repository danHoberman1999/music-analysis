# for clarification I wasn't able to access this utils file in my techinal_report.ipynb. I used import utils as util. Then in my functions wrote util.load, or util.clean_class, but I kept getting an error I couldn't solve. So I am showing you that I had everything set up here also.

import numpy as np
import matplotlib as plt
import pandas as pd

def load(filename):
    df = pd.read_csv(filename)
    return df

def clean_class(df):
    ser = df["mDevice"].copy()
    for i in range(0, len(ser), 1):
        curr = str(ser[i])
        curr = curr.lower()
        if "airpods" in curr or "airpod" in curr:
            ser[i] = "airpods"
        elif "speaker" in curr or "speakers" in curr:
            ser[i] = "speakers"
        else:
            print("Unrecognized status: %d, %s" % (i, ser[i]))
            ser[i] = np.NaN

    df["mDevice"] = ser
    
def write_csv(fname, df):
    out_file = open(fname, "w")
    df.to_csv(fname)
    out_file.close()
    
def weekendGroups(df):
    weekend_groups = df.groupby("DofW")
    saturday_ser = weekend_groups.get_group("S")
    sunday_ser = weekend_groups.get_group("SD")

    # getting mean volume of music on Saturday and Sunday
    saturday_mean = np.mean(saturday_ser["DB"])
    sunday_mean = np.mean(sunday_ser["DB"])

    t_computed, p_val = stats.ttest_ind(saturday_ser["DB"], sunday_ser["DB"])
    return t_computed, saturday_mean, sunday_mean

def stressGroups(df):
    stress_groups = df.groupby("Stress")
    stress_9_ser = stress_groups.get_group(9)
    stress_8_ser = stress_groups.get_group(8)
    stress_7_ser = stress_groups.get_group(7)
    stress_6_ser = stress_groups.get_group(6)
    stress_5_ser = stress_groups.get_group(5)
    stress_4_ser = stress_groups.get_group(4)
    stress_3_ser = stress_groups.get_group(3)
    stress_2_ser = stress_groups.get_group(2)
    stress_1_ser = stress_groups.get_group(1)

    # getting all stress mean music volume average
    stress_9_mean = np.mean(stress_9_ser["DB"])
    stress_8_mean = np.mean(stress_8_ser["DB"])
    stress_7_mean = np.mean(stress_7_ser["DB"])
    stress_6_mean = np.mean(stress_6_ser["DB"])
    stress_5_mean = np.mean(stress_5_ser["DB"])
    stress_4_mean = np.mean(stress_4_ser["DB"])
    stress_3_mean = np.mean(stress_3_ser["DB"])
    stress_2_mean = np.mean(stress_2_ser["DB"])
    stress_1_mean = np.mean(stress_1_ser["DB"])
    stress_mean = np.mean(df["DB"])

    t_computed, p_val = stats.ttest_ind(stress_9_ser["DB"], stress_1_ser["DB"])
    return t_computed, stress_9_mean, stress_8_mean, stress_7_mean, stress_6_mean, stress_5_mean, stress_4_mean, stress_3_mean, stress_2_mean, stress_1_mean

def musicGroups(df):
    #organizing data by music type
    mType_groups = df.groupby("mType")
    randb_ser = mType_groups.get_group("randb")
    rap_ser = mType_groups.get_group("rap")
    pop_ser = mType_groups.get_group("pop")
    classical_ser = mType_groups.get_group("classical")
    indie_ser = mType_groups.get_group("indie")

    #calculating mean values
    randb_mean = np.mean(randb_ser["DB"])
    rap_mean = np.mean(rap_ser["DB"])
    pop_mean = np.mean(pop_ser["DB"])
    classical_mean = np.mean(classical_ser["DB"])
    indie_mean = np.mean(indie_ser["DB"])

    # wanted length of data to calculate which I listen to more
    print(len(randb_ser))
    print(len(rap_ser))

    t_computed, p_val = stats.ttest_ind(randb_ser["DB"], rap_ser["DB"])
    return t_computed, randb_mean, rap_mean, pop_mean, classical_mean, indie_mean


def weekdayWeekend(df):
    # getting each individual day of the week
    week_groups = df.groupby("DofW")
    m_ser = week_groups.get_group("M")
    t_ser = week_groups.get_group("T")
    w_ser = week_groups.get_group("W")
    th_ser = week_groups.get_group("TH")
    f_ser = week_groups.get_group("F")
    s_ser = week_groups.get_group("S")
    sd_ser = week_groups.get_group("SD")

    # finding mean music volume for each day of the week
    m_mean = np.mean(m_ser["DB"])
    t_mean = np.mean(t_ser["DB"])
    w_mean = np.mean(w_ser["DB"])
    th_mean = np.mean(th_ser["DB"])
    f_mean = np.mean(f_ser["DB"])
    s_mean = np.mean(s_ser["DB"])
    sd_mean = np.mean(sd_ser["DB"])

    # creating a new dataset with the weekday average volume and other data set with weekend average volume
    weekdays = [m_mean, t_mean, w_mean, th_mean, f_mean]
    weekend = [s_mean, sd_mean]


    t_computed, p_val = stats.ttest_ind(weekend, weekdays)
    return t_computed

def sunSat_plot(saturday_mean, sunday_mean, df):
    plt.figure()

    # declaring values to be plotted
    xs = [1, 2]
    ys = [saturday_mean, sunday_mean]

    # setting range
    xrng = np.arange(len(xs))
    yrng = np.arange(0, max(ys)+50, 50)

    # making bar chart and alligning items properly
    plt.bar(xrng, ys, 0.45, align="center") 

    # labeling
    plt.xticks(xrng, ["Saturday", "Sunday"])
    plt.yticks(yrng)

    plt.grid(True)
    plt.show()
    
def volumeScatter(df):
    # scatter plot shows ranges of music volumes at different stress levels
    plt.figure()
    plt.scatter(df["Stress"], df["DB"])
    plt.xlabel('Stress levels')
    plt.ylabel('Music volume')
    plt.show()
    
    
def stressBar(stress1, stress2, stress3, stress4, stress5, stress6, stress7, stress8, stress9, df):
    plt.figure()

    # declaring plotting data
    xs = [1,2,3,4,5,6,7,8,9]
    ys =[stress1, stress2, stress3, stress4, stress5, stress6, stress7, stress8, stress9]

    # setting range 
    xrng = np.arange(len(xs))
    yrng = np.arange(0, max(ys)+40, 50)

    # giving plot an x and y label
    plt.xlabel('Stress level')
    plt.ylabel('Music volume')

    # setting up spacing and declaring plot
    plt.bar(xrng, ys, 0.45, align="center") 

    #labeling
    plt.xticks(xrng, ["1","2","3","4","5","6","7","8","9",])
    plt.yticks(yrng)

    plt.grid(True)
    plt.show()
    
def musicType_plot(rap, randb, classical, indie, pop, df):
    plt.figure()

    # declaring testing data
    xs = [1, 2, 3, 4, 5]
    ys = [randb, rap, classical, pop, indie]

    # setting range
    xrng = np.arange(len(xs))
    yrng = np.arange(0, max(ys)+60, 50)

    #labeling data
    plt.xlabel('Music Type')
    plt.ylabel('Music volume')

    # spacing and declare bar chart
    plt.bar(xrng, ys, 0.45, align="center") 


    # labeling
    plt.xticks(xrng, ["randb", "rap", "classical", "pop", "indie"])
    plt.yticks(yrng)

    plt.grid(True)
    plt.show()
    
def musicCategory_plt(df):
    plt.figure()

    # define x and y values
    xs = [1, 2, 3, 4, 5]
    ys = [len(randb_ser), len(rap_ser), len(classical_ser), len(pop_ser), len(indie_ser)]

    # setting range
    xrng = np.arange(len(xs))
    yrng = np.arange(0, max(ys)+60, 50)

    # labeling data
    plt.xlabel('Music Type')
    plt.ylabel('Days listened')

    # define bar chart and spacing
    plt.bar(xrng, ys, 0.45, align="center") 

    # more labeling
    plt.xticks(xrng, ["randb", "rap", "classical", "pop", "indie"])
    plt.yticks(yrng)

    plt.grid(True)
    plt.show()
    
    
def pieChart(df):
    stress_groups = df.groupby("Stress")
    one_ser = stress_groups.get_group(1)
    two_ser = stress_groups.get_group(2)
    three_ser = stress_groups.get_group(3)
    four_ser = stress_groups.get_group(4)
    five_ser = stress_groups.get_group(5)
    six_ser = stress_groups.get_group(6)
    seven_ser = stress_groups.get_group(7)
    eight_ser = stress_groups.get_group(8)
    nine_ser = stress_groups.get_group(9)
    plt.figure(figsize=(8,8))

    # define x and y values
    xs = [1, 2, 3, 4,5, 6, 7, 8, 9]
    ys = [len(one_ser),len(two_ser),len(three_ser),len(four_ser),len(five_ser),len(six_ser),len(seven_ser),len(eight_ser),len(nine_ser),]

    #giving plot a label for clarity
    plt.title('Percent of days at stress levels (1-9)')

    #creating pie chart
    plt.pie(ys, labels=xs, autopct="%1.1f%%")
    plt.show()


