#!/usr/bin/env pyh
import Data_CSV
import csv



if __name__ == "__main__":

    data = ["first_name,last_name,city".split(","),

            "Tyrese,Hirthe,Strackeport".split(","),

            "Jules,Dicki,Lake Nickolasville".split(","),

            "Dedric,Medhurst,Stiedemannberg".split(",")]
    data2 =["Aaron,Sibaja, Villalobos".split(",")]
    fist="Lala"
    last="pitufa"
    city=24
    all=fist+","+last+","+str(city)
    data3=[all.split(",")]
    path = "output.csv"
    CS= Data_CSV.CSV_Manager(path)
    CS.csv_writer(data)
    CS.csv_append(data2)
    CS.csv_append(data3)
    print(len(data2[0]))
