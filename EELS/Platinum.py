import eels

e_min = 65
e_max = 80

c_pi = 286.75
e_dif = c_pi - 285
e_init = 60.75
e_init = e_init - e_dif

pt1 = eels.data_energy(r'200127\SI data (25)\Pt\Pt-1.txt', e_init, 0.25)
platinum1 = eels.trimer(pt1[0], pt1[1], e_min, e_max, e_init, 0.25)

pt2 = eels.data_energy(r'200127\SI data (25)\Pt\Pt-2.txt', e_init, 0.25)
platinum2 = eels.trimer(pt2[0], pt2[1], e_min, e_max, e_init, 0.25)

c_pi = 287.66
e_dif = c_pi - 285
e_init = 51.26
e_init = e_init - e_dif

nitro3 = eels.data_energy(r'200127\181205_si40\Graphitic-N.txt', e_init, 0.4)
nitrogen3 = eels.trimer(nitro3[0], nitro3[1], e_min, e_max, e_init, 0.4)

eels.plotter(platinum1, platinum2, nitrogen3)