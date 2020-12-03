from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1IFC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9+10+11+12 & chain A ")


cmd.select("Astrand1", "resi 123+124+125+126+127+128+129+130 & chain A ")


cmd.select("Astrand2", "resi 34+35+36+37+38+39+40+41+42 & chain A ")


cmd.select("Astrand3", "resi 47+48+49+50+51+52 & chain A ")


cmd.select("Astrand4", "resi 57+58+59+60+61+62 & chain A ")


cmd.select("Astrand5", "resi 67+68+69+70+71 & chain A ")


cmd.select("Astrand6", "resi 76+77+78+79+80+81+82+83+84 & chain A ")


cmd.select("Astrand7", "resi 89+90+91+92+93+94 & chain A ")


cmd.select("Astrand8", "resi 100+101+102+103+104+105+106+107+108 & chain A ")


cmd.select("Astrand9", "resi 113+114+115+116+117+118 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH130A", pos=[-3.823699,4.386661,14.565383])
cmd.pseudoatom ("PseudoH6A", pos=[-1.7277236,5.3139324,13.151609])
cmd.pseudoatom ("PseudoH128A", pos=[2.583986,4.237753,16.634138])
cmd.pseudoatom ("PseudoH126A", pos=[8.559644,1.9393165,17.391811])
cmd.pseudoatom ("PseudoH11A", pos=[9.71225,2.524467,19.489094])
cmd.pseudoatom ("PseudoH124A", pos=[14.126458,-2.4959614,18.555218])
cmd.pseudoatom ("PseudoH36A", pos=[6.780695,9.533257,10.373674])
cmd.pseudoatom ("PseudoH51A", pos=[4.491339,6.8923955,5.5825])
cmd.pseudoatom ("PseudoH38A", pos=[2.2873135,5.9128304,7.095826])
cmd.pseudoatom ("PseudoH49A", pos=[0.77107376,2.6728232,3.1016073])
cmd.pseudoatom ("PseudoH40A", pos=[-1.3828387,2.0272317,4.1818757])
cmd.pseudoatom ("PseudoH47A", pos=[-1.9193797,-2.2951593,-0.18215144])
cmd.pseudoatom ("PseudoH61A", pos=[2.5551808,0.064747274,-2.4498239])
cmd.pseudoatom ("PseudoH48A", pos=[0.85136396,1.1986642,-1.0186275])
cmd.pseudoatom ("PseudoH59A", pos=[3.6844587,6.0399547,-0.3458631])
cmd.pseudoatom ("PseudoH50A", pos=[2.7416015,6.315317,1.6510072])
cmd.pseudoatom ("PseudoH57A", pos=[6.505691,11.127664,2.7939878])
cmd.pseudoatom ("PseudoH67A", pos=[9.716377,-8.819272,-3.610815])
cmd.pseudoatom ("PseudoH79A", pos=[14.142258,-5.081133,-2.123792])
cmd.pseudoatom ("PseudoH69A", pos=[13.481955,-2.978237,-3.51888])
cmd.pseudoatom ("PseudoH77A", pos=[17.470741,0.8261236,-0.3411417])
cmd.pseudoatom ("PseudoH71A", pos=[15.566056,1.6922708,0.78845596])
cmd.pseudoatom ("PseudoH78A", pos=[17.59905,-3.5904775,0.49273145])
cmd.pseudoatom ("PseudoH93A", pos=[14.205499,-8.201348,1.948457])
cmd.pseudoatom ("PseudoH91A", pos=[8.431022,-8.764696,4.4634705])
cmd.pseudoatom ("PseudoH82A", pos=[6.5616937,-8.922995,3.1868832])
cmd.pseudoatom ("PseudoH89A", pos=[2.5295908,-9.42376,6.8454366])
cmd.pseudoatom ("PseudoH105A", pos=[6.7481723,-8.096042,10.229511])
cmd.pseudoatom ("PseudoH90A", pos=[6.6485934,-9.814202,8.350479])
cmd.pseudoatom ("PseudoH103A", pos=[12.913288,-8.996559,7.867891])
cmd.pseudoatom ("PseudoH101A", pos=[18.684462,-9.697937,5.0114403])
cmd.pseudoatom ("PseudoH94A", pos=[18.610825,-8.185821,3.0855076])
cmd.pseudoatom ("PseudoH102A", pos=[16.959816,-7.393518,8.598303])
cmd.pseudoatom ("PseudoH117A", pos=[12.546064,-5.6448793,12.069518])
cmd.pseudoatom ("PseudoH104A", pos=[10.702981,-6.138658,10.442772])
cmd.pseudoatom ("PseudoH115A", pos=[6.2792144,-3.6727347,13.201305])
cmd.pseudoatom ("PseudoH106A", pos=[4.3202667,-4.89932,12.208567])
cmd.pseudoatom ("PseudoH113A", pos=[0.24703574,-2.4241447,15.191588])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR91A", pos=[9.009644,-7.4494586,5.509815])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 7 & chain A & name O", "resi 129 & chain A & name N")
cmd.distance("StrongHBond", "resi 7 & chain A & name N", "resi 129 & chain A & name O")
cmd.distance("StrongHBond", "resi 10 & chain A & name O", "resi 127 & chain A & name N")
cmd.distance("StrongHBond", "resi 10 & chain A & name N", "resi 127 & chain A & name O")
cmd.distance("StrongHBond", "resi 12 & chain A & name O", "resi 125 & chain A & name N")
cmd.distance("StrongHBond", "resi 12 & chain A & name N", "resi 125 & chain A & name O")
cmd.distance("StrongHBond", "resi 37 & chain A & name O", "resi 52 & chain A & name N")
cmd.distance("StrongHBond", "resi 37 & chain A & name N", "resi 52 & chain A & name O")
cmd.distance("StrongHBond", "resi 39 & chain A & name O", "resi 50 & chain A & name N")
cmd.distance("StrongHBond", "resi 39 & chain A & name N", "resi 50 & chain A & name O")
cmd.distance("StrongHBond", "resi 41 & chain A & name O", "resi 48 & chain A & name N")
cmd.distance("StrongHBond", "resi 41 & chain A & name N", "resi 48 & chain A & name O")
cmd.distance("StrongHBond", "resi 47 & chain A & name O", "resi 62 & chain A & name N")
cmd.distance("StrongHBond", "resi 47 & chain A & name N", "resi 62 & chain A & name O")
cmd.distance("StrongHBond", "resi 49 & chain A & name O", "resi 60 & chain A & name N")
cmd.distance("StrongHBond", "resi 49 & chain A & name N", "resi 60 & chain A & name O")
cmd.distance("StrongHBond", "resi 51 & chain A & name O", "resi 58 & chain A & name N")
cmd.distance("StrongHBond", "resi 51 & chain A & name N", "resi 58 & chain A & name O")
cmd.distance("StrongHBond", "resi 68 & chain A & name O", "resi 80 & chain A & name N")
cmd.distance("StrongHBond", "resi 68 & chain A & name N", "resi 80 & chain A & name O")
cmd.distance("StrongHBond", "resi 70 & chain A & name O", "resi 78 & chain A & name N")
cmd.distance("StrongHBond", "resi 70 & chain A & name N", "resi 78 & chain A & name O")
cmd.distance("StrongHBond", "resi 79 & chain A & name O", "resi 94 & chain A & name N")
cmd.distance("StrongHBond", "resi 79 & chain A & name N", "resi 94 & chain A & name O")
cmd.distance("StrongHBond", "resi 81 & chain A & name O", "resi 92 & chain A & name N")
cmd.distance("StrongHBond", "resi 81 & chain A & name N", "resi 92 & chain A & name O")
cmd.distance("StrongHBond", "resi 83 & chain A & name O", "resi 90 & chain A & name N")
cmd.distance("StrongHBond", "resi 83 & chain A & name N", "resi 90 & chain A & name O")
cmd.distance("StrongHBond", "resi 89 & chain A & name O", "resi 106 & chain A & name N")
cmd.distance("StrongHBond", "resi 89 & chain A & name N", "resi 106 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 104 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 104 & chain A & name O")
cmd.distance("StrongHBond", "resi 93 & chain A & name O", "resi 102 & chain A & name N")
cmd.distance("StrongHBond", "resi 93 & chain A & name N", "resi 102 & chain A & name O")
cmd.distance("StrongHBond", "resi 103 & chain A & name O", "resi 118 & chain A & name N")
cmd.distance("StrongHBond", "resi 103 & chain A & name N", "resi 118 & chain A & name O")
cmd.distance("StrongHBond", "resi 105 & chain A & name O", "resi 116 & chain A & name N")
cmd.distance("StrongHBond", "resi 105 & chain A & name N", "resi 116 & chain A & name O")
cmd.distance("StrongHBond", "resi 107 & chain A & name O", "resi 114 & chain A & name N")
cmd.distance("StrongHBond", "resi 107 & chain A & name N", "resi 114 & chain A & name O")
cmd.distance("WeakHBond", "resi 5 & chain A & name O", "PseudoH130A")
cmd.distance("WeakHBond", "resi 129 & chain A & name O", "PseudoH6A")
cmd.distance("WeakHBond", "resi 7 & chain A & name O", "PseudoH128A")
cmd.distance("WeakHBond", "resi 10 & chain A & name O", "PseudoH126A")
cmd.distance("WeakHBond", "resi 125 & chain A & name O", "PseudoH11A")
cmd.distance("WeakHBond", "resi 12 & chain A & name O", "PseudoH124A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH36A")
cmd.distance("WeakHBond", "resi 37 & chain A & name O", "PseudoH51A")
cmd.distance("WeakHBond", "resi 50 & chain A & name O", "PseudoH38A")
cmd.distance("WeakHBond", "resi 39 & chain A & name O", "PseudoH49A")
cmd.distance("WeakHBond", "resi 48 & chain A & name O", "PseudoH40A")
cmd.distance("WeakHBond", "resi 41 & chain A & name O", "PseudoH47A")
cmd.distance("WeakHBond", "resi 47 & chain A & name O", "PseudoH61A")
cmd.distance("WeakHBond", "resi 60 & chain A & name O", "PseudoH48A")
cmd.distance("WeakHBond", "resi 49 & chain A & name O", "PseudoH59A")
cmd.distance("WeakHBond", "resi 58 & chain A & name O", "PseudoH50A")
cmd.distance("WeakHBond", "resi 51 & chain A & name O", "PseudoH57A")
cmd.distance("WeakHBond", "resi 80 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 68 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH69A")
cmd.distance("WeakHBond", "resi 70 & chain A & name O", "PseudoH77A")
cmd.distance("WeakHBond", "resi 76 & chain A & name O", "PseudoH71A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 79 & chain A & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 83 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH105A")
cmd.distance("WeakHBond", "resi 104 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH103A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH101A")
cmd.distance("WeakHBond", "resi 100 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH102A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 105 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH106A")
cmd.distance("WeakHBond", "resi 107 & chain A & name O", "PseudoH113A")
cmd.distance("NonHBond", "resi 6 & chain A & name CB", "resi 130 & chain A & name CB")
cmd.distance("NonHBond", "resi 8 & chain A & name CB", "resi 128 & chain A & name CB")
cmd.distance("NonHBond", "resi 11 & chain A & name CB", "resi 126 & chain A & name CB")
cmd.distance("NonHBond", "resi 38 & chain A & name CB", "resi 51 & chain A & name CB")
cmd.distance("NonHBond", "resi 40 & chain A & name CB", "resi 49 & chain A & name CB")
cmd.distance("NonHBond", "resi 42 & chain A & name CB", "resi 47 & chain A & name CB")
cmd.distance("NonHBond", "resi 48 & chain A & name CB", "resi 61 & chain A & name CB")
cmd.distance("NonHBond", "resi 50 & chain A & name CB", "resi 59 & chain A & name CB")
cmd.distance("NonHBond", "resi 52 & chain A & name CB", "resi 57 & chain A & name CB")
cmd.distance("NonHBond", "resi 67 & chain A & name CB", "resi 81 & chain A & name CB")
cmd.distance("NonHBond", "resi 69 & chain A & name CB", "resi 79 & chain A & name CB")
cmd.distance("NonHBond", "resi 71 & chain A & name CB", "resi 77 & chain A & name CB")
cmd.distance("NonHBond", "resi 82 & chain A & name CB", "PseudoR91A")
cmd.distance("NonHBond", "resi 84 & chain A & name CB", "resi 89 & chain A & name CB")
cmd.distance("NonHBond", "resi 90 & chain A & name CB", "resi 105 & chain A & name CB")
cmd.distance("NonHBond", "resi 92 & chain A & name CB", "resi 103 & chain A & name CB")
cmd.distance("NonHBond", "resi 94 & chain A & name CB", "resi 101 & chain A & name CB")
cmd.distance("NonHBond", "resi 104 & chain A & name CB", "resi 117 & chain A & name CB")
cmd.distance("NonHBond", "resi 106 & chain A & name CB", "resi 115 & chain A & name CB")
cmd.distance("NonHBond", "resi 108 & chain A & name CB", "resi 113 & chain A & name CB")
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
