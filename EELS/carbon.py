import eels

e_min = 270
e_max = 320

c_pi = 286.5
e_dif = c_pi - 285
e_init = 60.75
e_init = e_init - e_dif

nitro1 = eels.data_energy(r'200127\SI data (25)\C at N\b_4.txt', e_init, 0.25)
nitrogen1 = eels.trimer(nitro1[0], nitro1[1], e_min, e_max, e_init, 0.25)

nitro2 = eels.data_energy(r'200127\SI data (25)\C at N\c_4.txt', e_init, 0.25)
nitrogen2 = eels.trimer(nitro2[0], nitro2[1], e_min, e_max, e_init, 0.25)

nitro3 = eels.data_energy(r'200127\SI data (25)\C at N\gra_1st_spe.txt', e_init, 0.25)
nitrogen3 = eels.trimer(nitro3[0], nitro3[1], e_min, e_max, e_init, 0.25)

eels.plotter(nitrogen1, nitrogen2, nitrogen3)