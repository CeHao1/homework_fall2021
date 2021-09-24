
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import os

class results_store:
    # exp1
    q1_sb_no_rtg_dsa = [29.0, 27.466667, 48.555557, 48.555557, 56.125, 41.7, 38.636364, 40.6, 36.916668, 40.1, 50.444443, 71.333336, 77.833336, 50.875, 55.5, 70.0, 41.5, 40.0, 37.272728, 35.583332, 40.9, 38.583332, 35.166668, 51.375, 51.0, 71.14286, 49.22222, 58.625, 74.166664, 63.142857, 59.285713, 51.0, 91.6, 54.5, 64.71429, 74.666664, 59.0, 57.125, 52.75, 43.0, 36.5, 34.333332, 30.642857, 26.933332, 26.0625, 30.071428, 27.066668, 26.1875, 28.266666, 26.933332, 27.266666, 27.533333, 25.75, 26.1875, 24.117647, 27.2, 27.0625, 30.76923, 33.23077, 36.545456, 33.666668, 40.7, 37.5, 45.444443, 38.0, 58.285713, 54.0, 58.142857, 37.18182, 51.25, 48.333332, 50.75, 60.142857, 90.8, 54.0, 51.5, 48.333332, 50.375, 82.8, 87.2, 88.2, 85.2, 60.142857, 59.75, 82.0, 64.57143, 59.285713, 67.666664, 88.8, 86.0, 78.333336, 101.5, 111.0, 75.333336, 72.0, 93.8, 72.166664, 91.0, 90.8, 117.0]
    q1_sb_rtg_dsa = [30.214285, 38.545456, 53.875, 44.77778, 64.71429, 58.42857, 122.0, 126.5, 142.0, 127.0, 161.33333, 200.0, 146.25, 200.0, 200.0, 174.33333, 142.33333, 200.0, 135.66667, 200.0, 103.4, 61.42857, 41.81818, 36.416668, 35.0, 57.125, 41.0, 72.833336, 86.2, 119.0, 139.66667, 161.66667, 200.0, 200.0, 200.0, 200.0, 186.33333, 179.66667, 162.33333, 153.0, 187.66667, 193.66667, 186.66667, 200.0, 153.33333, 180.33333, 200.0, 180.66667, 177.33333, 150.0, 150.66667, 160.0, 162.0, 200.0, 186.66667, 200.0, 200.0, 200.0, 181.33333, 164.66667, 178.0, 168.0, 152.33333, 149.33333, 144.66667, 139.33333, 143.66667, 145.66667, 131.0, 151.0, 151.0, 146.66667, 146.66667, 165.66667, 162.33333, 163.0, 182.33333, 190.66667, 200.0, 199.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
    q1_sb_rtg_na = [35.46154, 40.3, 53.375, 130.5, 68.71429, 73.0, 95.8, 113.4, 113.5, 195.66667, 147.0, 187.66667, 170.0, 200.0, 183.66667, 178.0, 200.0, 200.0, 146.25, 168.66667, 142.33333, 117.5, 125.0, 124.0, 116.25, 115.75, 139.33333, 176.33333, 200.0, 200.0, 200.0, 196.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 196.66667, 200.0, 164.66667, 169.66667, 145.0, 200.0, 200.0, 111.5, 200.0, 121.5, 125.25, 119.25, 113.0, 117.0, 127.25, 134.25, 140.33333, 169.33333, 177.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
    q1_lb_no_rtg_dsa = [33.54, 33.42, 45.8, 61.29, 105.0, 67.86, 57.29, 89.4, 75.0, 69.0, 43.8, 50.33, 43.3, 50.88, 55.38, 84.0, 78.5, 105.0, 72.67, 53.62, 46.0, 45.22, 45.78, 47.56, 41.9, 33.31, 30.92, 30.93, 24.59, 24.18, 25.25, 29.36, 31.46, 33.67, 41.3, 47.22, 46.67, 72.33, 67.33, 91.0, 67.17, 97.4, 91.8, 100.25, 96.6, 112.5, 100.5, 80.2, 92.2, 60.86, 71.5, 57.14, 46.44, 41.1, 37.08, 34.67, 31.46, 29.64, 32.54, 39.45, 40.9, 44.78, 55.5, 71.86, 79.33, 108.75, 117.75, 102.0, 101.25, 113.0, 139.0, 139.33, 100.0, 89.6, 112.8, 135.25, 137.67, 147.67, 168.67, 198.67, 184.67, 190.67, 200.0, 151.67, 161.0, 147.67, 146.0, 152.67, 127.75, 147.25, 117.75, 106.8, 88.8, 64.29, 72.67, 59.14, 80.17, 59.29, 72.0, 68.5]
    q1_lb_rtg_dsa = [32.62, 41.7, 57.29, 83.0, 108.5, 63.86, 84.17, 85.8, 112.25, 170.0, 148.33, 145.67, 200.0, 170.33, 200.0, 159.67, 126.5, 148.25, 136.0, 113.75, 75.67, 93.0, 62.38, 80.4, 112.5, 81.6, 110.5, 130.5, 132.5, 139.0, 170.33, 180.67, 173.0, 195.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 166.67, 200.0, 143.67, 99.6, 200.0, 143.67, 200.0, 200.0, 180.0, 196.0, 200.0, 200.0, 200.0, 155.33, 200.0, 160.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 165.67, 124.75, 102.0, 113.75, 93.2, 115.5, 106.0, 108.5, 111.25, 115.25, 118.75, 125.25, 131.5, 146.67, 147.67, 154.33, 162.0, 155.67]
    q1_lb_rtg_na = [32.62, 37.64, 53.11, 113.0, 102.5, 93.8, 117.5, 112.75, 136.33, 138.0, 200.0, 200.0, 200.0, 169.0, 178.67, 184.67, 159.67, 160.0, 186.0, 200.0, 169.0, 167.67, 185.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 195.0, 200.0, 200.0, 200.0, 139.33, 200.0, 200.0, 200.0, 200.0, 169.67, 157.0, 140.67, 122.0, 138.67, 135.67, 137.0, 171.67, 174.67, 189.67, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]

    # exp2
    q2_b70_lr007 = [15.81, 25.5, 34.46, 35.0, 36.91, 46.33, 80.67, 45.56, 53.25, 41.09, 31.92, 23.59, 21.84, 37.09, 46.33, 47.56, 51.22, 55.12, 48.67, 42.7, 68.67, 93.0, 91.6, 94.5, 57.86, 58.29, 30.77, 16.71, 24.12, 26.12, 34.67, 50.62, 58.5, 73.17, 73.0, 70.67, 67.0, 78.67, 92.2, 83.0, 62.14, 90.2, 89.0, 114.75, 139.33, 215.5, 108.0, 185.0, 161.75, 187.0, 166.0, 106.2, 111.0, 59.0, 75.33, 49.67, 44.56, 34.57, 55.88, 36.67, 30.36, 31.64, 22.05, 31.08, 21.79, 26.0, 33.15, 29.71, 42.0, 50.0, 44.7, 47.33, 47.56, 44.44, 51.62, 57.25, 77.5, 94.4, 124.25, 489.5, 278.0, 223.0, 165.67, 1000.0, 434.33, 1000.0, 1000.0, 430.0, 630.0, 310.5, 122.6, 208.5, 425.5, 590.0, 146.2, 471.0, 80.0, 167.75, 185.67, 1000.0]
    q2_b50_lr006 = [14.41, 18.73, 22.39, 27.67, 38.25, 28.57, 29.57, 29.71, 39.91, 34.08, 37.09, 28.93, 31.85, 29.36, 28.64, 22.22, 22.26, 26.31, 30.79, 31.08, 39.55, 46.33, 44.9, 59.57, 45.0, 64.75, 57.86, 75.33, 71.5, 60.86, 54.75, 31.54, 66.29, 47.89, 86.14, 80.6, 91.0, 101.25, 84.4, 207.5, 98.0, 75.33, 35.69, 31.85, 34.69, 34.25, 57.86, 52.0, 52.38, 58.86, 151.0, 81.67, 142.0, 68.17, 63.0, 56.62, 45.0, 28.93, 28.86, 22.84, 22.37, 23.0, 25.24, 26.19, 31.31, 33.5, 34.83, 44.1, 50.12, 69.83, 62.29, 97.4, 110.25, 82.0, 73.67, 48.11, 45.0, 46.11, 47.67, 40.3, 38.36, 47.22, 52.0, 48.0, 46.11, 68.17, 67.29, 136.0, 141.0, 193.75, 689.0, 291.0, 1000.0, 243.0, 184.67, 306.5, 149.67, 140.75, 67.14, 91.83]
    q2_b150_lr006 = [14.88, 19.7, 29.6, 38.08, 36.5, 44.84, 52.72, 42.06, 34.29, 42.42, 41.14, 45.93, 42.17, 67.06, 59.76, 61.79, 59.5, 83.88, 75.57, 81.96, 64.41, 66.77, 82.08, 96.52, 99.71, 91.27, 113.72, 102.0, 109.95, 97.57, 128.47, 133.53, 144.67, 146.93, 155.29, 242.3, 194.82, 189.33, 210.36, 129.12, 108.05, 113.0, 157.77, 156.0, 102.3, 68.37, 90.87, 63.72, 49.0, 32.84, 27.85, 29.09, 38.02, 50.02, 67.23, 87.87, 142.93, 208.3, 959.33, 460.17, 390.17, 1000.0, 817.0, 705.33, 720.33, 995.67, 482.0, 624.75, 268.0, 234.9, 531.6, 783.0, 1000.0, 526.25, 90.12, 28.68, 11.72, 9.28, 7.65, 14.06, 21.8, 48.67, 119.65, 222.33, 229.78, 337.33, 206.6, 162.23, 258.38, 204.7, 291.14, 408.2, 701.33, 842.0, 1000.0, 1000.0, 742.25, 235.3, 143.0, 111.11]

    # exp3
    q3 = [-184.66, -156.6, -139.16, -121.15, -112.67, -110.93, -106.4,  -83.02,  -69.85, -54.97,  -45.04,  -56.61, -123.22, -130.05, -106.87, -122.15,  -88.24,  -70.79,  -64.51,  -36.81,  7.38,   11.66,   13.31,   17.43,    8.36,   43.76,   22.8,  75.68,   75.71,   59.6,   110.61,   96.64,   82.5,   116.12,  152.24,  137.26,   139.15,   90.86,  150.42,  151.47,  142.97,  122.39,  127.63,  123.81,  106.16,  146.63,  136.6,   119.5,   132.03,  140.24,  152.25,  174.17,  147.59,  149.15,          163.14,  131.28,  152.98,  142.57,  150.51,  159.32,  163.26,  161.86,  161.19, 159.12,  151.89,  156.25,  152.13,  160.08,  158.03,  142.41,  155.89,  154.47,            174.89,  156.64,  160.53,  113.58,  169.28,  147.63,  168.94,  121.35,  185.09, 130.77,  173.75,  151.7,   178.43,  144.39,  122.59,  131.03,  172.99,  161.92,            141.11,  145.11,  139.39,  155.51,  125.93,  177.29,  144.7,   169.1,   170.0, 170.31]

    # exp4
    q4_search_b50000_lr02_rtg_nnbaseline = [-71.14,-80.07,-77.08,-80.09,-73.22,-69.02,-79.77,-50.79,-51.47,-49.21,-39.73,-32.95,-30.43,-20.73,-23.86,-20.14,0.87,1.21,9.81,14.64,20.22,23.63,31.1,23.32,43.69,55.26,23.36,13.85,30.49,58.82,59.74,55.78,74.84,64.92,73.42,49.16,58.59,83.58,95.72,92.21,80.07,107.76,99.19,89.13,109.73,102.64,122.11,135.09,122.82,146.75,128.97,137.34,83.92,120.89,149.7,129.88,150.3,136.42,123.34,134.11,130.1,132.48,126.68,119.28,115.0,130.95,120.55,147.95,139.23,136.24,135.51,120.24,133.05,141.72,147.56,130.6,145.58,138.43,175.1,161.86,120.56,164.58,145.08,132.98,119.47,50.11,128.18,107.68,104.38,112.49,168.11,154.93,138.9,159.5,176.63,146.79,155.05,156.15,147.19,156.44]
    q4_search_b30000_lr02_rtg_nnbaseline = [-91.43,-85.63,-86.12,-77.24,-63.23,-76.73,-70.56,-67.24,-63.06,-62.09,-54.74,-68.3,-43.06,-42.94,-43.67,-36.47,-37.93,-35.3,-12.95,-1.9,-13.8,-0.88,-8.97,11.19,12.61,9.73,25.06,17.65,19.03,42.26,42.06,47.97,45.04,41.94,44.09,53.66,57.43,59.49,56.88,61.69,59.21,72.21,50.1,79.3,82.78,83.4,99.98,74.05,71.54,65.42,92.39,83.46,77.82,76.69,90.44,96.84,82.04,103.57,106.87,94.84,106.65,74.05,72.83,77.81,93.13,112.88,123.45,95.16,104.24,115.57,135.74,132.96,130.52,100.42,140.51,95.28,109.37,129.57,141.06,101.02,146.19,107.02,121.23,145.8,89.53,64.12,40.42,87.05,93.97,50.44,39.61,90.16,94.42,118.62,116.62,33.46,168.41,156.51,97.61,137.96]
    q4_search_b10000_lr02_rtg_nnbaseline = [-91.99,-96.07,-92.04,-103.47,-94.9,-91.02,-86.93,-92.38,-77.0,-66.53,-78.04,-93.6,-90.01,-86.34,-78.98,-76.82,-81.03,-76.01,-74.88,-75.35,-85.82,-70.45,-67.08,-62.37,-71.89,-55.22,-48.22,-69.3,-32.22,-21.3,-15.68,-5.06,22.73,16.98,9.68,16.56,21.11,13.33,33.27,55.7,59.94,12.07,22.7,-8.36,7.71,13.64,39.88,47.48,66.33,76.49,62.59,77.86,118.41,94.4,104.86,121.72,91.06,86.76,85.44,105.41,114.64,112.84,136.05,140.13,127.63,141.14,168.23,190.69,174.08,113.81,117.83,110.3,144.5,107.51,97.51,136.29,197.41,228.34,256.95,228.09,177.81,109.72,99.77,125.13,158.91,231.47,163.19,167.76,208.35,250.57,252.1,271.47,237.3,174.28,122.42,125.74,59.16,43.73,63.21,99.47]
    q4_search_b50000_lr01_rtg_nnbaseline = [-83.15, -85.93, -69.72, -74.46, -76.49, -77.1, -74.26, -64.63, -76.7, -69.12, -59.07, -63.02, -62.41, -48.76, -53.72, -56.58, -53.98, -46.74, -36.13, -36.77, -23.46, -22.09, -19.67, -25.12, -11.0, 0.93, -10.55, -2.67, -4.6, -16.53, 2.09, 5.06, -3.53, 12.84, 19.67, 6.07, 2.98, 25.33, 18.12, 28.84, 25.46, 28.69, 24.03, 24.93, 40.48, 40.83, 56.6, 56.03, 48.11, 51.17, 31.55, 27.12, 57.2, 50.94, 63.54, 73.57, 67.61, 86.31, 69.13, 65.61, 86.84, 64.54, 80.3, 54.15, 62.04, 82.23, 77.69, 76.77, 91.42, 114.37, 77.92, 85.45, 88.5, 88.67, 96.06, 101.13, 103.52, 124.34, 136.37, 107.47, 98.29, 114.54, 92.86, 113.21, 101.3, 66.63, 110.96, 92.45, 112.09, 88.0, 117.79, 112.87, 131.93, 124.94, 153.64, 138.59, 147.4, 138.93, 144.93, 149.5]
    q4_search_b30000_lr01_rtg_nnbaseline = [-82.58, -89.62, -92.14, -85.97, -85.7, -88.1, -80.83, -73.06, -68.42, -80.35, -72.15, -67.89, -66.16, -63.88, -73.66, -51.1, -52.41, -57.2, -47.47, -41.87, -40.13, -39.61, -41.42, -26.28, -29.8, -29.09, -36.19, -15.22, -22.52, -17.2, -22.1, -13.91, -14.85, -3.55, 1.84, 9.25, 9.3, 9.24, 5.8, 6.06, 3.57, 15.78, 23.36, 21.69, 26.33, 34.1, 35.7, 27.19, 29.2, 39.54, 21.27, 40.91, 44.89, 49.31, 53.89, 29.33, 48.88, 51.01, 60.09, 56.93, 47.88, 62.76, 82.32, 70.36, 77.41, 70.29, 69.91, 80.34, 73.33, 83.23, 77.49, 94.77, 85.96, 100.23, 98.97, 103.83, 102.78, 121.88, 103.87, 100., 100.19, 127.47, 112.68, 123.54, 128.62, 121.78, 99.94, 122.12, 111.97, 101.15, 123.96, 117.05, 107.8, 106.55, 105.54, 110.49, 117.56, 99.29, 120.85, 127.97]
    q4_search_b10000_lr01_rtg_nnbaseline = [-92.25,-94.39,-83.22,-89.22,-79.25,-87.71,-86.28,-85.9,-81.19,-72.39,-64.81,-77.54,-79.41,-81.32,-81.89,-87.38,-70.28,-69.02,-51.8,-85.67,-67.22,-65.97,-72.68,-51.39,-48.39,-53.98,-57.79,-48.03,-49.87,-46.96,-47.49,-52.2,-49.8,-52.57,-47.8,-28.38,-50.74,-58.91,-49.02,-47.95,-33.18,-32.92,-32.08,-33.53,-25.35,-27.22,-38.46,-28.49,-28.86,-28.82,-14.37,-23.88,-22.72,-18.02,-0.34,-16.29,-18.54,-7.43,-12.71,-2.94,-12.18,-5.23,-0.78,-2.73,-0.81,-9.09,-2.37,-10.2,-16.3,4.47,-4.24,4.96,10.12,9.4,19.92,12.19,1.64,12.07,13.88,18.94,29.91,24.8,34.17,29.54,40.12,44.13,27.98,38.46,50.2,46.6,24.6,28.68,37.43,27.69,38.47,50.31,40.03,62.91,50.13,50.39]
    q4_search_b50000_lr005_rtg_nnbaseline = []

    q4_b50000_r02 = []
    q4_b50000_r02_rtg = []
    q4_b50000_r02_nnbaseline = []
    q4_b50000_r02_rtg_nnbaseline = [] # already has

def set_plot_env(rewards_dict, exp_name):

    plt.figure(figsize=(10,5))
    style = "whitegrid"
    sns.set_theme(style=style) # background color
    ax = plt.gca()

    # rewards_dist {'name':[], 'rewards]':[]}
    color_list = ['b', 'r', 'y', 'g', 'm', 'k']
    for idx, name in enumerate(rewards_dict['name']):
        plot_reward(ax, rewards_dict['rewards'][idx], name, color=color_list[idx])

    ax.legend(loc='center right')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Reward')
    ax.set_title('reward of ' + exp_name +' experiment')
    # ax.set_xlim([-0.5,10])
    ax.legend()

    exp_dir = 'plots/'
    if not os.path.exists(exp_dir):
        os.makedirs(exp_dir)
    plt.savefig(fname=exp_dir + 'figure-2_' + exp_name + '.png', format='png', dpi=1000)

    plt.show()


def plot_reward(ax, rewards, name, color):
    rewards = np.array(rewards)
    iterations = np.arange(rewards.shape[0])
    ax.plot(iterations, rewards, label=name)


if __name__ == '__main__':
    r = results_store()

    # exp1
    exp1_f1 = {'name':['q1_sb_no_rtg_dsa', 'q1_sb_rtg_dsa', 'q1_sb_rtg_na'], 'rewards':[r.q1_sb_no_rtg_dsa, r.q1_sb_rtg_dsa, r.q1_sb_rtg_na]}
    exp1_f2 = {'name':['q1_lb_no_rtg_dsa', 'q1_lb_rtg_dsa', 'q1_lb_rtg_na'], 'rewards':[r.q1_lb_no_rtg_dsa, r.q1_lb_rtg_dsa, r.q1_lb_rtg_na]}

    # set_plot_env(exp1_f1, 'exp1_sb')
    # set_plot_env(exp1_f2, 'exp1_lb')

    # exp2
    exp2_f1= {'name':['q2_b150_lr0.006'], 'rewards':[r.q2_b150_lr006]}
    # set_plot_env(exp2_f1, 'exp2_b150_r0.006')

    # exp3
    exp3_f1 =  {'name':['q3_b40000_lr0.005'], 'rewards':[r.q3]}
    # set_plot_env(exp3_f1, 'q3_b40000_lr0.005')

    # exp4
    exp4_f1 = {'name':[
                        'q4_search_b10000_lr0.01_rtg_nnbaseline', 'q4_search_b30000_lr0.01_rtg_nnbaseline', 'q4_search_b50000_lr0.01_rtg_nnbaseline',
                        'q4_search_b10000_lr0.02_rtg_nnbaseline', 'q4_search_b30000_lr0.02_rtg_nnbaseline', 'q4_search_b50000_lr0.02_rtg_nnbaseline'], 

            'rewards':[
                r.q4_search_b10000_lr01_rtg_nnbaseline, r.q4_search_b30000_lr01_rtg_nnbaseline, r.q4_search_b50000_lr01_rtg_nnbaseline,
                r.q4_search_b10000_lr02_rtg_nnbaseline, r.q4_search_b30000_lr02_rtg_nnbaseline, r.q4_search_b50000_lr02_rtg_nnbaseline]}
    set_plot_env(exp4_f1, 'exp4')