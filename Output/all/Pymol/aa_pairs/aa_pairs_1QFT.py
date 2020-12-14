from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QFT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 30+31+32+33+34 & chain A ")


cmd.select("Astrand1", "resi 50+51+52+53+54 & chain A ")


cmd.select("Astrand2", "resi 62+63+64+65+66+67+68+69 & chain A ")


cmd.select("Astrand3", "resi 78+79+80+81+82+83+84+85+86+87 & chain A ")


cmd.select("Astrand4", "resi 97+98+99+100+101+102 & chain A ")


cmd.select("Astrand5", "resi 107+108+109+110+111+112+113+114+115+116 & chain A ")


cmd.select("Astrand6", "resi 119+120+121+122+123+124 & chain A ")


cmd.select("Astrand7", "resi 133+134+135+136+137+138 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH67A", pos=[75.423325,41.704445,15.677717])
cmd.pseudoatom ("PseudoH51A", pos=[73.47382,42.188538,14.537705])
cmd.pseudoatom ("PseudoH65A", pos=[71.10451,36.93384,15.857202])
cmd.pseudoatom ("PseudoH53A", pos=[70.198944,36.639393,13.824343])
cmd.pseudoatom ("PseudoH63A", pos=[66.3591,32.894054,17.165983])
cmd.pseudoatom ("PseudoH62A", pos=[64.10863,34.058613,21.040653])
cmd.pseudoatom ("PseudoH83A", pos=[70.46569,33.987637,20.945026])
cmd.pseudoatom ("PseudoH64A", pos=[70.63158,33.599205,18.44764])
cmd.pseudoatom ("PseudoH81A", pos=[76.087326,36.338634,18.11123])
cmd.pseudoatom ("PseudoH66A", pos=[75.60684,37.37869,15.89684])
cmd.pseudoatom ("PseudoH79A", pos=[80.74075,40.859554,15.966015])
cmd.pseudoatom ("PseudoH68A", pos=[79.860306,42.909363,15.114141])
cmd.pseudoatom ("PseudoH82A", pos=[74.59745,35.093483,22.12852])
cmd.pseudoatom ("PseudoH100A", pos=[69.7796,37.933243,24.646683])
cmd.pseudoatom ("PseudoH84A", pos=[68.1014,36.991226,23.282011])
cmd.pseudoatom ("PseudoH98A", pos=[64.09895,40.390305,24.429554])
cmd.pseudoatom ("PseudoH86A", pos=[61.675774,38.83663,23.910028])
cmd.pseudoatom ("PseudoH97A", pos=[61.697166,43.90971,25.973896])
cmd.pseudoatom ("PseudoH109A", pos=[66.9135,41.68613,28.785666])
cmd.pseudoatom ("PseudoH99A", pos=[66.966705,39.5108,27.733236])
cmd.pseudoatom ("PseudoH107A", pos=[72.04985,37.546364,29.59884])
cmd.pseudoatom ("PseudoH110A", pos=[66.32166,46.101284,28.590412])
cmd.pseudoatom ("PseudoH122A", pos=[63.92153,49.773617,23.59562])
cmd.pseudoatom ("PseudoH112A", pos=[61.814053,48.292477,23.435158])
cmd.pseudoatom ("PseudoH120A", pos=[61.880833,50.18565,17.773415])
cmd.pseudoatom ("PseudoH115A", pos=[59.65374,50.206192,17.622654])
cmd.pseudoatom ("PseudoH119A", pos=[63.857994,50.39285,13.764949])
cmd.pseudoatom ("PseudoH136A", pos=[66.50608,53.258,18.879427])
cmd.pseudoatom ("PseudoH121A", pos=[64.43296,52.74315,20.57381])
cmd.pseudoatom ("PseudoH134A", pos=[67.47705,53.39251,25.892471])
cmd.pseudoatom ("PseudoH123A", pos=[65.80005,51.93,26.991539])
cmd.pseudoatom ("PseudoH34A", pos=[71.10641,55.414207,22.37829])
cmd.pseudoatom ("PseudoH135A", pos=[69.80823,53.595078,21.989458])
cmd.pseudoatom ("PseudoH31A", pos=[70.77369,51.056328,16.661217])
cmd.pseudoatom ("PseudoH137A", pos=[68.79104,51.000027,15.854803])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR50A", pos=[74.825,46.085854,13.055096])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 50 & chain A & name O", "resi 68 & chain A & name N")
cmd.distance("StrongHBond", "resi 50 & chain A & name N", "resi 68 & chain A & name O")
cmd.distance("StrongHBond", "resi 52 & chain A & name O", "resi 66 & chain A & name N")
cmd.distance("StrongHBond", "resi 52 & chain A & name N", "resi 66 & chain A & name O")
cmd.distance("StrongHBond", "resi 54 & chain A & name O", "resi 64 & chain A & name N")
cmd.distance("StrongHBond", "resi 54 & chain A & name N", "resi 64 & chain A & name O")
cmd.distance("StrongHBond", "resi 63 & chain A & name O", "resi 84 & chain A & name N")
cmd.distance("StrongHBond", "resi 63 & chain A & name N", "resi 84 & chain A & name O")
cmd.distance("StrongHBond", "resi 65 & chain A & name O", "resi 82 & chain A & name N")
cmd.distance("StrongHBond", "resi 65 & chain A & name N", "resi 82 & chain A & name O")
cmd.distance("StrongHBond", "resi 67 & chain A & name O", "resi 80 & chain A & name N")
cmd.distance("StrongHBond", "resi 67 & chain A & name N", "resi 80 & chain A & name O")
cmd.distance("StrongHBond", "resi 69 & chain A & name O", "resi 78 & chain A & name N")
cmd.distance("StrongHBond", "resi 69 & chain A & name N", "resi 78 & chain A & name O")
cmd.distance("StrongHBond", "resi 83 & chain A & name O", "resi 101 & chain A & name N")
cmd.distance("StrongHBond", "resi 83 & chain A & name N", "resi 101 & chain A & name O")
cmd.distance("StrongHBond", "resi 85 & chain A & name O", "resi 99 & chain A & name N")
cmd.distance("StrongHBond", "resi 85 & chain A & name N", "resi 99 & chain A & name O")
cmd.distance("StrongHBond", "resi 87 & chain A & name O", "resi 97 & chain A & name N")
cmd.distance("StrongHBond", "resi 87 & chain A & name N", "resi 97 & chain A & name O")
cmd.distance("StrongHBond", "resi 98 & chain A & name O", "resi 110 & chain A & name N")
cmd.distance("StrongHBond", "resi 98 & chain A & name N", "resi 110 & chain A & name O")
cmd.distance("StrongHBond", "resi 100 & chain A & name O", "resi 108 & chain A & name N")
cmd.distance("StrongHBond", "resi 100 & chain A & name N", "resi 108 & chain A & name O")
cmd.distance("StrongHBond", "resi 111 & chain A & name O", "resi 123 & chain A & name N")
cmd.distance("StrongHBond", "resi 111 & chain A & name N", "resi 123 & chain A & name O")
cmd.distance("StrongHBond", "resi 114 & chain A & name O", "resi 121 & chain A & name N")
cmd.distance("StrongHBond", "resi 114 & chain A & name N", "resi 121 & chain A & name O")
cmd.distance("StrongHBond", "resi 116 & chain A & name O", "resi 119 & chain A & name N")
cmd.distance("StrongHBond", "resi 116 & chain A & name N", "resi 119 & chain A & name O")
cmd.distance("StrongHBond", "resi 120 & chain A & name O", "resi 137 & chain A & name N")
cmd.distance("StrongHBond", "resi 120 & chain A & name N", "resi 137 & chain A & name O")
cmd.distance("StrongHBond", "resi 122 & chain A & name O", "resi 135 & chain A & name N")
cmd.distance("StrongHBond", "resi 122 & chain A & name N", "resi 135 & chain A & name O")
cmd.distance("StrongHBond", "resi 124 & chain A & name O", "resi 133 & chain A & name N")
cmd.distance("StrongHBond", "resi 124 & chain A & name N", "resi 133 & chain A & name O")
cmd.distance("StrongHBond", "resi 136 & chain A & name O", "resi 33 & chain A & name N")
cmd.distance("StrongHBond", "resi 136 & chain A & name N", "resi 33 & chain A & name O")
cmd.distance("StrongHBond", "resi 138 & chain A & name O", "resi 30 & chain A & name N")
cmd.distance("StrongHBond", "resi 138 & chain A & name N", "resi 30 & chain A & name O")
cmd.distance("WeakHBond", "resi 50 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 66 & chain A & name O", "PseudoH51A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH65A")
cmd.distance("WeakHBond", "resi 64 & chain A & name O", "PseudoH53A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH63A")
cmd.distance("WeakHBond", "resi 84 & chain A & name O", "PseudoH62A")
cmd.distance("WeakHBond", "resi 63 & chain A & name O", "PseudoH83A")
cmd.distance("WeakHBond", "resi 82 & chain A & name O", "PseudoH64A")
cmd.distance("WeakHBond", "resi 65 & chain A & name O", "PseudoH81A")
cmd.distance("WeakHBond", "resi 80 & chain A & name O", "PseudoH66A")
cmd.distance("WeakHBond", "resi 67 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH68A")
cmd.distance("WeakHBond", "resi 101 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 83 & chain A & name O", "PseudoH100A")
cmd.distance("WeakHBond", "resi 99 & chain A & name O", "PseudoH84A")
cmd.distance("WeakHBond", "resi 85 & chain A & name O", "PseudoH98A")
cmd.distance("WeakHBond", "resi 97 & chain A & name O", "PseudoH86A")
cmd.distance("WeakHBond", "resi 110 & chain A & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH109A")
cmd.distance("WeakHBond", "resi 108 & chain A & name O", "PseudoH99A")
cmd.distance("WeakHBond", "resi 100 & chain A & name O", "PseudoH107A")
cmd.distance("WeakHBond", "resi 123 & chain A & name O", "PseudoH110A")
cmd.distance("WeakHBond", "resi 111 & chain A & name O", "PseudoH122A")
cmd.distance("WeakHBond", "resi 121 & chain A & name O", "PseudoH112A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH120A")
cmd.distance("WeakHBond", "resi 119 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 137 & chain A & name O", "PseudoH119A")
cmd.distance("WeakHBond", "resi 120 & chain A & name O", "PseudoH136A")
cmd.distance("WeakHBond", "resi 135 & chain A & name O", "PseudoH121A")
cmd.distance("WeakHBond", "resi 122 & chain A & name O", "PseudoH134A")
cmd.distance("WeakHBond", "resi 133 & chain A & name O", "PseudoH123A")
cmd.distance("WeakHBond", "resi 134 & chain A & name O", "PseudoH34A")
cmd.distance("WeakHBond", "resi 33 & chain A & name O", "PseudoH135A")
cmd.distance("WeakHBond", "resi 136 & chain A & name O", "PseudoH31A")
cmd.distance("WeakHBond", "resi 30 & chain A & name O", "PseudoH137A")
cmd.distance("NonHBond", "resi 30 & chain A & name CB", "PseudoR50A")
cmd.distance("NonHBond", "resi 51 & chain A & name CB", "resi 67 & chain A & name CB")
cmd.distance("NonHBond", "resi 53 & chain A & name CB", "resi 65 & chain A & name CB")
cmd.distance("NonHBond", "resi 62 & chain A & name CB", "resi 85 & chain A & name CB")
cmd.distance("NonHBond", "resi 64 & chain A & name CB", "resi 83 & chain A & name CB")
cmd.distance("NonHBond", "resi 66 & chain A & name CB", "resi 81 & chain A & name CB")
cmd.distance("NonHBond", "resi 68 & chain A & name CB", "resi 79 & chain A & name CB")
cmd.distance("NonHBond", "resi 82 & chain A & name CB", "resi 102 & chain A & name CB")
cmd.distance("NonHBond", "resi 84 & chain A & name CB", "resi 100 & chain A & name CB")
cmd.distance("NonHBond", "resi 86 & chain A & name CB", "resi 98 & chain A & name CB")
cmd.distance("NonHBond", "resi 97 & chain A & name CB", "resi 111 & chain A & name CB")
cmd.distance("NonHBond", "resi 99 & chain A & name CB", "resi 109 & chain A & name CB")
cmd.distance("NonHBond", "resi 101 & chain A & name CB", "resi 107 & chain A & name CB")
cmd.distance("NonHBond", "resi 110 & chain A & name CB", "resi 124 & chain A & name CB")
cmd.distance("NonHBond", "resi 112 & chain A & name CB", "resi 122 & chain A & name CB")
cmd.distance("NonHBond", "resi 115 & chain A & name CB", "resi 120 & chain A & name CB")
cmd.distance("NonHBond", "resi 119 & chain A & name CB", "resi 138 & chain A & name CB")
cmd.distance("NonHBond", "resi 121 & chain A & name CB", "resi 136 & chain A & name CB")
cmd.distance("NonHBond", "resi 123 & chain A & name CB", "resi 134 & chain A & name CB")
cmd.distance("NonHBond", "resi 135 & chain A & name CB", "resi 34 & chain A & name CB")
cmd.distance("NonHBond", "resi 137 & chain A & name CB", "resi 31 & chain A & name CB")
cmd.show("stick", "barrel")
cmd.color("red","StrongHBond")
cmd.color("green","WeakHBond")
cmd.color("purpleblue","NonHBond")
cmd.color("magenta","PseudoR*")
cmd.color("green","name CA & barrel")
cmd.color("red","name O & barrel")
cmd.color("blue","name N & barrel")
cmd.hide("labels")
cmd.zoom("barrel")