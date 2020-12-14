from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VYF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14 & chain A ")


cmd.select("Astrand1", "resi 48+49+50+51+52+53+54 & chain A ")


cmd.select("Astrand2", "resi 60+61+62+63+64 & chain A ")


cmd.select("Astrand3", "resi 70+71+72+73 & chain A ")


cmd.select("Astrand4", "resi 79+80+81+82+83+84+85+86+87+88 & chain A ")


cmd.select("Astrand5", "resi 91+92+93+94+95+96+97 & chain A ")


cmd.select("Astrand6", "resi 102+103+104+105+106+107+108+109+110 & chain A ")


cmd.select("Astrand7", "resi 39+40+41+42+43+44+45 & chain A ")


cmd.select("Astrand8", "resi 113+114+115+116+117+118+119+120 & chain A ")


cmd.select("Astrand9", "resi 123+124+125+126+127+128+129+130+131 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH48A", pos=[27.727032,42.032276,18.146875])
cmd.pseudoatom ("PseudoH63A", pos=[22.692318,42.383663,15.199578])
cmd.pseudoatom ("PseudoH50A", pos=[23.439571,42.23444,13.028127])
cmd.pseudoatom ("PseudoH61A", pos=[17.978455,42.707893,10.015816])
cmd.pseudoatom ("PseudoH52A", pos=[19.089308,42.483315,8.089562])
cmd.pseudoatom ("PseudoH81A", pos=[14.260184,35.447975,22.481188])
cmd.pseudoatom ("PseudoH71A", pos=[13.961425,38.227066,22.057138])
cmd.pseudoatom ("PseudoH79A", pos=[8.736896,37.298534,18.761368])
cmd.pseudoatom ("PseudoH80A", pos=[10.411522,33.741825,20.800713])
cmd.pseudoatom ("PseudoH96A", pos=[15.168943,31.477425,18.92733])
cmd.pseudoatom ("PseudoH82A", pos=[16.849487,32.822666,20.323273])
cmd.pseudoatom ("PseudoH94A", pos=[21.399866,30.991234,16.890718])
cmd.pseudoatom ("PseudoH84A", pos=[23.12568,32.12421,17.790075])
cmd.pseudoatom ("PseudoH92A", pos=[27.860226,29.782274,14.606436])
cmd.pseudoatom ("PseudoH91A", pos=[29.272814,28.739712,10.477628])
cmd.pseudoatom ("PseudoH106A", pos=[23.54411,27.255627,12.264318])
cmd.pseudoatom ("PseudoH93A", pos=[23.770124,28.181185,14.291553])
cmd.pseudoatom ("PseudoH104A", pos=[18.201735,26.562212,15.962781])
cmd.pseudoatom ("PseudoH95A", pos=[17.997383,28.265726,17.749949])
cmd.pseudoatom ("PseudoH102A", pos=[12.371502,26.679502,19.247952])
cmd.pseudoatom ("PseudoH113A", pos=[27.398746,29.583834,-1.0905117])
cmd.pseudoatom ("PseudoH128A", pos=[22.540804,27.37441,0.90281475])
cmd.pseudoatom ("PseudoH115A", pos=[23.752567,26.71976,2.9608388])
cmd.pseudoatom ("PseudoH126A", pos=[18.986326,23.574747,4.78407])
cmd.pseudoatom ("PseudoH117A", pos=[19.752611,23.858213,7.09854])
cmd.pseudoatom ("PseudoH124A", pos=[15.314282,20.329784,9.385368])
cmd.pseudoatom ("PseudoH119A", pos=[15.28558,21.488543,11.443835])
cmd.pseudoatom ("PseudoH125A", pos=[15.126588,21.269802,5.00305])
cmd.pseudoatom ("PseudoH13A", pos=[16.403313,25.624863,-0.0025401711])
cmd.pseudoatom ("PseudoH127A", pos=[18.293116,26.132988,1.2340829])
cmd.pseudoatom ("PseudoH10A", pos=[19.675999,31.85794,-1.0715687])
cmd.pseudoatom ("PseudoH129A", pos=[22.018454,31.319393,-1.1812613])
cmd.pseudoatom ("PseudoH8A", pos=[24.837229,36.2702,-0.80140895])
cmd.pseudoatom ("PseudoH131A", pos=[27.205284,35.612194,-1.3958055])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 49 & chain A & name O", "resi 64 & chain A & name N")
cmd.distance("StrongHBond", "resi 49 & chain A & name N", "resi 64 & chain A & name O")
cmd.distance("StrongHBond", "resi 51 & chain A & name O", "resi 62 & chain A & name N")
cmd.distance("StrongHBond", "resi 51 & chain A & name N", "resi 62 & chain A & name O")
cmd.distance("StrongHBond", "resi 53 & chain A & name O", "resi 60 & chain A & name N")
cmd.distance("StrongHBond", "resi 53 & chain A & name N", "resi 60 & chain A & name O")
cmd.distance("StrongHBond", "resi 70 & chain A & name O", "resi 82 & chain A & name N")
cmd.distance("StrongHBond", "resi 70 & chain A & name N", "resi 82 & chain A & name O")
cmd.distance("StrongHBond", "resi 72 & chain A & name O", "resi 80 & chain A & name N")
cmd.distance("StrongHBond", "resi 72 & chain A & name N", "resi 80 & chain A & name O")
cmd.distance("StrongHBond", "resi 81 & chain A & name O", "resi 97 & chain A & name N")
cmd.distance("StrongHBond", "resi 81 & chain A & name N", "resi 97 & chain A & name O")
cmd.distance("StrongHBond", "resi 83 & chain A & name O", "resi 95 & chain A & name N")
cmd.distance("StrongHBond", "resi 83 & chain A & name N", "resi 95 & chain A & name O")
cmd.distance("StrongHBond", "resi 85 & chain A & name O", "resi 93 & chain A & name N")
cmd.distance("StrongHBond", "resi 85 & chain A & name N", "resi 93 & chain A & name O")
cmd.distance("StrongHBond", "resi 88 & chain A & name O", "resi 91 & chain A & name N")
cmd.distance("StrongHBond", "resi 88 & chain A & name N", "resi 91 & chain A & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 107 & chain A & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 107 & chain A & name O")
cmd.distance("StrongHBond", "resi 94 & chain A & name O", "resi 105 & chain A & name N")
cmd.distance("StrongHBond", "resi 94 & chain A & name N", "resi 105 & chain A & name O")
cmd.distance("StrongHBond", "resi 96 & chain A & name O", "resi 103 & chain A & name N")
cmd.distance("StrongHBond", "resi 96 & chain A & name N", "resi 103 & chain A & name O")
cmd.distance("StrongHBond", "resi 114 & chain A & name O", "resi 129 & chain A & name N")
cmd.distance("StrongHBond", "resi 114 & chain A & name N", "resi 129 & chain A & name O")
cmd.distance("StrongHBond", "resi 116 & chain A & name O", "resi 127 & chain A & name N")
cmd.distance("StrongHBond", "resi 116 & chain A & name N", "resi 127 & chain A & name O")
cmd.distance("StrongHBond", "resi 118 & chain A & name O", "resi 125 & chain A & name N")
cmd.distance("StrongHBond", "resi 118 & chain A & name N", "resi 125 & chain A & name O")
cmd.distance("StrongHBond", "resi 120 & chain A & name O", "resi 123 & chain A & name N")
cmd.distance("StrongHBond", "resi 120 & chain A & name N", "resi 123 & chain A & name O")
cmd.distance("StrongHBond", "resi 126 & chain A & name O", "resi 14 & chain A & name N")
cmd.distance("StrongHBond", "resi 126 & chain A & name N", "resi 14 & chain A & name O")
cmd.distance("StrongHBond", "resi 128 & chain A & name O", "resi 12 & chain A & name N")
cmd.distance("StrongHBond", "resi 128 & chain A & name N", "resi 12 & chain A & name O")
cmd.distance("StrongHBond", "resi 130 & chain A & name O", "resi 9 & chain A & name N")
cmd.distance("StrongHBond", "resi 130 & chain A & name N", "resi 9 & chain A & name O")
cmd.distance("WeakHBond", "resi 64 & chain A & name O", "PseudoH48A")
cmd.distance("WeakHBond", "resi 49 & chain A & name O", "PseudoH63A")
cmd.distance("WeakHBond", "resi 62 & chain A & name O", "PseudoH50A")
cmd.distance("WeakHBond", "resi 51 & chain A & name O", "PseudoH61A")
cmd.distance("WeakHBond", "resi 60 & chain A & name O", "PseudoH52A")
cmd.distance("WeakHBond", "resi 70 & chain A & name O", "PseudoH81A")
cmd.distance("WeakHBond", "resi 80 & chain A & name O", "PseudoH71A")
cmd.distance("WeakHBond", "resi 72 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 97 & chain A & name O", "PseudoH80A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH96A")
cmd.distance("WeakHBond", "resi 95 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 83 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH84A")
cmd.distance("WeakHBond", "resi 85 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 107 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH106A")
cmd.distance("WeakHBond", "resi 105 & chain A & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 96 & chain A & name O", "PseudoH102A")
cmd.distance("WeakHBond", "resi 129 & chain A & name O", "PseudoH113A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH128A")
cmd.distance("WeakHBond", "resi 127 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH126A")
cmd.distance("WeakHBond", "resi 125 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH124A")
cmd.distance("WeakHBond", "resi 123 & chain A & name O", "PseudoH119A")
cmd.distance("WeakHBond", "resi 14 & chain A & name O", "PseudoH125A")
cmd.distance("WeakHBond", "resi 126 & chain A & name O", "PseudoH13A")
cmd.distance("WeakHBond", "resi 12 & chain A & name O", "PseudoH127A")
cmd.distance("WeakHBond", "resi 128 & chain A & name O", "PseudoH10A")
cmd.distance("WeakHBond", "resi 9 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 130 & chain A & name O", "PseudoH8A")
cmd.distance("WeakHBond", "resi 7 & chain A & name O", "PseudoH131A")
cmd.distance("NonHBond", "resi 50 & chain A & name CB", "resi 63 & chain A & name CB")
cmd.distance("NonHBond", "resi 52 & chain A & name CB", "resi 61 & chain A & name CB")
cmd.distance("NonHBond", "resi 71 & chain A & name CB", "resi 81 & chain A & name CB")
cmd.distance("NonHBond", "resi 73 & chain A & name CB", "resi 79 & chain A & name CB")
cmd.distance("NonHBond", "resi 82 & chain A & name CB", "resi 96 & chain A & name CB")
cmd.distance("NonHBond", "resi 84 & chain A & name CB", "resi 94 & chain A & name CB")
cmd.distance("NonHBond", "resi 86 & chain A & name CB", "resi 92 & chain A & name CB")
cmd.distance("NonHBond", "resi 91 & chain A & name CB", "resi 108 & chain A & name CB")
cmd.distance("NonHBond", "resi 93 & chain A & name CB", "resi 106 & chain A & name CB")
cmd.distance("NonHBond", "resi 95 & chain A & name CB", "resi 104 & chain A & name CB")
cmd.distance("NonHBond", "resi 97 & chain A & name CB", "resi 102 & chain A & name CB")
cmd.distance("NonHBond", "resi 113 & chain A & name CB", "resi 130 & chain A & name CB")
cmd.distance("NonHBond", "resi 115 & chain A & name CB", "resi 128 & chain A & name CB")
cmd.distance("NonHBond", "resi 117 & chain A & name CB", "resi 126 & chain A & name CB")
cmd.distance("NonHBond", "resi 119 & chain A & name CB", "resi 124 & chain A & name CB")
cmd.distance("NonHBond", "resi 127 & chain A & name CB", "resi 13 & chain A & name CB")
cmd.distance("NonHBond", "resi 129 & chain A & name CB", "resi 10 & chain A & name CB")
cmd.distance("NonHBond", "resi 131 & chain A & name CB", "resi 8 & chain A & name CB")
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