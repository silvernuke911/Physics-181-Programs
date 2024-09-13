import matplotlib as mpl
import matplotlib.font_manager as font_manager

mpl.rcParams['font.family']='serif'
cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + '/fonts/ttf/cmr10.ttf')
mpl.rcParams['font.serif']=cmfont.get_name()
mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['axes.unicode_minus']=False
mpl.rcParams['axes.formatter.use_mathtext']=True
mpl.rcParams.update({'font.size': 15})

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# plt.rcParams['text.usetex'] = True

def plot():
    plt.grid()
    # plt.xlim([np.min(x),np.max(x)])
    # plt.xticks(np.arange(round(np.min(x),6),round(np.max(x),6),2.5e-7),fontsize=12)
    plt.xlim([-0.02,0.02])
    plt.xticks(np.arange(-0.02,0.03,0.01),fontsize=12)
    plt.yticks(fontsize=12)

    # plt.title()
    plt.minorticks_on()
    plt.tick_params(axis="x", which="both", direction="in",top=True)
    plt.tick_params(axis="y", which="both", direction="in",right=True)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.plot(x,y1,marker='.',markerfacecolor='red',markersize=10,color='black',linestyle='solid',label='Input Waveform')
    plt.plot(x,y2,marker='.',markerfacecolor='blue',markersize=10,color='black',linestyle='solid',label='Output Waveform')
    plt.legend(loc="upper left",fontsize=10)
    plt.savefig(f'{root}\photos\{name}.png')
    print(f'{name} image generated and saved')
    #plt.show
    plt.clf()

def plot_phase():
    plt.scatter(x,y,zorder=1,marker='o',color='red',edgecolors= "black")
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.set_axisbelow(True)
    plt.xlabel('Input Voltage (V)')
    plt.ylabel('Output Voltage (V)')
    plt.tick_params(axis="x", which="both", direction="in",top=True)
    plt.tick_params(axis="y", which="both", direction="in",right=True)
    plt.grid()
    savefig()

def savefig():
    plt.savefig(f'{root}\photos\{name}_equal.png')
    print(f'{name} image generated and saved')
    plt.clf()

path = r'C:\Users\verci\Documents\Python Code\python181\e7-e8\phase_angles'
avoid_dir=r'photos'
for root, dirs, files in os.walk(path, topdown=False):
    if avoid_dir not in root:
        for name in files:
            filepath=os.path.join(root, name)
            print(filepath)
            data = pd.read_csv(filepath)
            # print(data)
            # x=data.t
            # y1=data.ch1
            # y2=data.ch2
            x=data.ch1
            y=data.ch2
            plot_phase()

def single_file():
    path = r'C:\Users\verci\Documents\Python Code\python181\e7-e8\e8\0.02'
    avoid_dir=r'photos'
    filename='8c2si___.csv'
    for root, dirs, files in os.walk(path, topdown=False):
        if avoid_dir not in root:
            for name in files:
                if name==filename:
                    filepath=os.path.join(root, name)
                    print(filepath)
                    data = pd.read_csv(filepath)
                    # print(data)
                    x=data.t
                    y1=data.ch1
                    y2=data.ch2
                    plot()

def search_and_replace():
    path = r'C:\Users\verci\Documents\Python Code\python181'
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in files:
            with open(os.path.join(root, name), 'r') as file:
                data = file.read() 
                data = data.replace('Time', 't')
                data = data.replace('X(CH1)', 'ch1')
                data = data.replace('X(CH2)', 'ch2')
                data = data.replace('Second', '')
                data = data.replace('Volt', '')
            with open(os.path.join(root, name), 'w') as file:
                file.write(data)
            print(f'Data in {name} replaced') 
