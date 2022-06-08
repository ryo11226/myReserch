import eels
import csv

e_min = 350
e_max = 470

c_pi = 286.75
e_dif = c_pi - 285
e_init = 60.75
e_init = e_init - e_dif

nitro1 = eels.data_energy(r'200127\SI data (25)\N_spe\b_raw.txt', e_init, 0.25)
nitrogen1 = eels.trimer(nitro1[0], nitro1[1], e_min, e_max, e_init, 0.25)
with open(r'python_code\EELS\nitrogen.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(nitrogen1[1])


nitro2 = eels.data_energy(r'200127\SI data (25)\N_spe\c_raw.txt', e_init, 0.25)
nitrogen2 = eels.trimer(nitro2[0], nitro2[1], e_min, e_max, e_init, 0.25)

c_pi = 287.66
e_dif = c_pi - 285
e_init = 51.26
e_init = e_init - e_dif

nitro3 = eels.data_energy(r'200127\181205_si40\Graphitic-N.txt', e_init, 0.4)
nitrogen3 = eels.trimer(nitro3[0], nitro3[1], e_min, e_max, e_init, 0.4)

eels.plotter(nitrogen1, nitrogen2, nitrogen3)