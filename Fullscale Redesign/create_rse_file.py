#Importing stuff
import numpy as np
import pandas as pd

#Initializing variables (change these values)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
thrust = [3447.37, 3447.37, 3447.37, 3447.37, 3447.37, 3447.37, 3447.37, 3447.37, 3447.37, 3447.37, 3447.37]
manufacturer = 'APRL'
motor_name = 'Engine775lbf'

Isp = 195.96 #seconds
Itot = 39.78 #Newton-seconds
motor_diameter = 5.98 #in inches
motor_diameter = int(motor_diameter*25.4) #converts to mm which .rse needs
motor_length = 23.3 #inches
motor_length = int(motor_length*25.4) #converts to mm which .rse needs
initial_weight = 0 #grams
propellant_weight = 0 #grams
burn_time = 8 #seconds

file_name = 'Engine775lbf'
output_file_path = f'c:/Users/kchee/OneDrive/Documents/Clubs and Fun/APRL Github/Vehicle/Fullscale Redesign/{file_name}.rse'

#Writing the .rse file
with open(output_file_path, 'w') as file:
    file.write('<engine-database>\n')
    file.write('  <engine-list>\n')
    file.write(f'    <engine FDiv="10" FFix="1" FStep="-1." Isp="{Isp}" Itot="{Itot}" Type="reloadable" auto-calc-cg="0" auto-calc-mass="1"\n')
    file.write(f'    avgThrust="0." burn-time="{burn_time}." cgDiv="10" cgFix="1" cgStep="-1." code="{motor_name}" delays="0." dia="{motor_diameter}." exitDia="0." initWt="1"\n')
    file.write(f'    len="{motor_length}." mDiv="10" mFix="1" mStep="-1." massFrac="1" mfg="{manufacturer}" peakThrust="0." propWt="1" tDiv="10" tFix="1"\n')
    file.write(f'    tStep="-1." throatDia="0.">\n')
    file.write('      <data>\n')
    for i, j in zip(time, thrust):
        file.write(f'        <eng-data cg="0" f="{j}" m="0." t="{i}."/>\n')
    file.write('      </data>\n')
    file.write('    </engine>\n')
    file.write('  </engine-list>\n')
    file.write('</engine-database>\n')

print(f'File {output_file_path} has been created.')



#A few notes about the code:
'''
Apparently you don't actually need to input anything to Itot and maybe not even ISP because
OpenRocket will automatically calculate those things for you based on your thrust curve.
'''


