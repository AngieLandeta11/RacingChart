# pip install sjvisualizer-0.0.7-py2.py3-none-any.whl
from sjvisualizer import DataHandler,Canvas,BarRace, StaticImage

import json


EXCEL_FILE="data/GDP.xlsx";
FPS=60;
DURATION=0.5;
with open("colors.json") as f:
    colors=json.load(f)

df=DataHandler.DataHandler(excel_file=EXCEL_FILE,number_of_frames=FPS*DURATION*60).df

canvas=Canvas.canvas()
bar_chart=BarRace.bar_race(df=df,canvas=canvas.canvas,colors=colors)
canvas.add_sub_plot(bar_chart)


canvas.add_title("Economías más grandes por PIB",color=(0,0,0))
canvas.add_sub_title("De 1960-2021",color=(50,50,50))
canvas.add_time(df=df,time_indicator="year")

ex=StaticImage.static_image(canvas=canvas.canvas,file="analitica.png",x_pos=420,y_pos=25,width=120,height=120)
canvas.add_sub_plot(ex)

canvas.play(fps=FPS)
