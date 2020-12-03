from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QO4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 4+5+6+7+8+9+10+11+12 & chain A ")


cmd.select("Astrand1", "resi 46+47+48+49+50+51+52+53 & chain A ")


cmd.select("Astrand2", "resi 56+57+58+59+60+61+62+63 & chain A ")


cmd.select("Astrand3", "resi 67+68+69+70+71 & chain A ")


cmd.select("Astrand4", "resi 77+78+79+80+81+82+83+84+85 & chain A ")


cmd.select("Astrand5", "resi 88+89+90+91+92 & chain A ")


cmd.select("Astrand6", "resi 97+98+99+100+101+102+103 & chain A ")


cmd.select("Astrand7", "resi 37+38+39+40+41+42+43 & chain A ")


cmd.select("Astrand8", "resi 106+107+108+109+110+111+112+113 & chain A ")


cmd.select("Astrand9", "resi 116+117+118+119+120+121+122+123+124 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH46A", pos=[-15.894597,17.889612,-12.958038])
cmd.pseudoatom ("PseudoH61A", pos=[-9.532767,17.956593,-11.358955])
cmd.pseudoatom ("PseudoH48A", pos=[-9.588808,20.24862,-11.065541])
cmd.pseudoatom ("PseudoH59A", pos=[-3.741257,20.662964,-9.316732])
cmd.pseudoatom ("PseudoH50A", pos=[-4.0377917,22.172028,-7.849589])
cmd.pseudoatom ("PseudoH57A", pos=[1.4382929,22.952185,-5.961007])
cmd.pseudoatom ("PseudoH52A", pos=[0.81921077,24.049553,-3.9062665])
cmd.pseudoatom ("PseudoH67A", pos=[-13.019941,7.537996,-10.038902])
cmd.pseudoatom ("PseudoH79A", pos=[-7.5586095,7.283011,-7.6211386])
cmd.pseudoatom ("PseudoH69A", pos=[-6.324157,8.599982,-9.219002])
cmd.pseudoatom ("PseudoH77A", pos=[-1.3855189,9.401928,-6.779015])
cmd.pseudoatom ("PseudoH82A", pos=[-15.132093,11.166983,-4.9330297])
cmd.pseudoatom ("PseudoH89A", pos=[-17.879948,15.2796755,-2.5084705])
cmd.pseudoatom ("PseudoH84A", pos=[-20.950956,14.342733,-3.119967])
cmd.pseudoatom ("PseudoH88A", pos=[-19.338001,18.039152,0.74440104])
cmd.pseudoatom ("PseudoH99A", pos=[-14.627153,14.255551,1.7274857])
cmd.pseudoatom ("PseudoH90A", pos=[-15.733903,12.546491,0.1914056])
cmd.pseudoatom ("PseudoH97A", pos=[-10.815207,8.598519,1.9711717])
cmd.pseudoatom ("PseudoH106A", pos=[-14.245309,28.68126,4.726323])
cmd.pseudoatom ("PseudoH121A", pos=[-10.803826,23.869862,7.206702])
cmd.pseudoatom ("PseudoH108A", pos=[-12.425261,22.417479,6.2412314])
cmd.pseudoatom ("PseudoH119A", pos=[-10.164463,17.68476,9.387585])
cmd.pseudoatom ("PseudoH110A", pos=[-11.291954,15.953896,7.886988])
cmd.pseudoatom ("PseudoH117A", pos=[-9.591396,11.348953,11.06711])
cmd.pseudoatom ("PseudoH112A", pos=[-9.361877,9.916056,9.05091])
cmd.pseudoatom ("PseudoH118A", pos=[-7.461418,15.195092,11.94665])
cmd.pseudoatom ("PseudoH11A", pos=[-6.5101037,21.426096,11.144254])
cmd.pseudoatom ("PseudoH120A", pos=[-7.8374233,21.369085,9.37262])
cmd.pseudoatom ("PseudoH8A", pos=[-6.4350033,26.037497,5.6469555])
cmd.pseudoatom ("PseudoH122A", pos=[-8.323008,27.16781,5.6337585])
cmd.pseudoatom ("PseudoH6A", pos=[-8.95751,29.686693,0.60185915])
cmd.pseudoatom ("PseudoH124A", pos=[-10.879143,31.363981,0.9441954])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 47 & chain A & name O", "resi 62 & chain A & name N")
cmd.distance("StrongHBond", "resi 47 & chain A & name N", "resi 62 & chain A & name O")
cmd.distance("StrongHBond", "resi 49 & chain A & name O", "resi 60 & chain A & name N")
cmd.distance("StrongHBond", "resi 49 & chain A & name N", "resi 60 & chain A & name O")
cmd.distance("StrongHBond", "resi 51 & chain A & name O", "resi 58 & chain A & name N")
cmd.distance("StrongHBond", "resi 51 & chain A & name N", "resi 58 & chain A & name O")
cmd.distance("StrongHBond", "resi 53 & chain A & name O", "resi 56 & chain A & name N")
cmd.distance("StrongHBond", "resi 53 & chain A & name N", "resi 56 & chain A & name O")
cmd.distance("StrongHBond", "resi 68 & chain A & name O", "resi 80 & chain A & name N")
cmd.distance("StrongHBond", "resi 68 & chain A & name N", "resi 80 & chain A & name O")
cmd.distance("StrongHBond", "resi 70 & chain A & name O", "resi 78 & chain A & name N")
cmd.distance("StrongHBond", "resi 70 & chain A & name N", "resi 78 & chain A & name O")
cmd.distance("StrongHBond", "resi 83 & chain A & name O", "resi 90 & chain A & name N")
cmd.distance("StrongHBond", "resi 83 & chain A & name N", "resi 90 & chain A & name O")
cmd.distance("StrongHBond", "resi 85 & chain A & name O", "resi 88 & chain A & name N")
cmd.distance("StrongHBond", "resi 85 & chain A & name N", "resi 88 & chain A & name O")
cmd.distance("StrongHBond", "resi 89 & chain A & name O", "resi 100 & chain A & name N")
cmd.distance("StrongHBond", "resi 89 & chain A & name N", "resi 100 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 98 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 98 & chain A & name O")
cmd.distance("StrongHBond", "resi 107 & chain A & name O", "resi 122 & chain A & name N")
cmd.distance("StrongHBond", "resi 107 & chain A & name N", "resi 122 & chain A & name O")
cmd.distance("StrongHBond", "resi 109 & chain A & name O", "resi 120 & chain A & name N")
cmd.distance("StrongHBond", "resi 109 & chain A & name N", "resi 120 & chain A & name O")
cmd.distance("StrongHBond", "resi 111 & chain A & name O", "resi 118 & chain A & name N")
cmd.distance("StrongHBond", "resi 111 & chain A & name N", "resi 118 & chain A & name O")
cmd.distance("StrongHBond", "resi 113 & chain A & name O", "resi 116 & chain A & name N")
cmd.distance("StrongHBond", "resi 113 & chain A & name N", "resi 116 & chain A & name O")
cmd.distance("StrongHBond", "resi 119 & chain A & name O", "resi 12 & chain A & name N")
cmd.distance("StrongHBond", "resi 119 & chain A & name N", "resi 12 & chain A & name O")
cmd.distance("StrongHBond", "resi 121 & chain A & name O", "resi 10 & chain A & name N")
cmd.distance("StrongHBond", "resi 121 & chain A & name N", "resi 10 & chain A & name O")
cmd.distance("StrongHBond", "resi 123 & chain A & name O", "resi 7 & chain A & name N")
cmd.distance("StrongHBond", "resi 123 & chain A & name N", "resi 7 & chain A & name O")
cmd.distance("WeakHBond", "resi 62 & chain A & name O", "PseudoH46A")
cmd.distance("WeakHBond", "resi 47 & chain A & name O", "PseudoH61A")
cmd.distance("WeakHBond", "resi 60 & chain A & name O", "PseudoH48A")
cmd.distance("WeakHBond", "resi 49 & chain A & name O", "PseudoH59A")
cmd.distance("WeakHBond", "resi 58 & chain A & name O", "PseudoH50A")
cmd.distance("WeakHBond", "resi 51 & chain A & name O", "PseudoH57A")
cmd.distance("WeakHBond", "resi 56 & chain A & name O", "PseudoH52A")
cmd.distance("WeakHBond", "resi 80 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 68 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH69A")
cmd.distance("WeakHBond", "resi 70 & chain A & name O", "PseudoH77A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 83 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 88 & chain A & name O", "PseudoH84A")
cmd.distance("WeakHBond", "resi 100 & chain A & name O", "PseudoH88A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH99A")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 122 & chain A & name O", "PseudoH106A")
cmd.distance("WeakHBond", "resi 107 & chain A & name O", "PseudoH121A")
cmd.distance("WeakHBond", "resi 120 & chain A & name O", "PseudoH108A")
cmd.distance("WeakHBond", "resi 109 & chain A & name O", "PseudoH119A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH110A")
cmd.distance("WeakHBond", "resi 111 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH112A")
cmd.distance("WeakHBond", "resi 12 & chain A & name O", "PseudoH118A")
cmd.distance("WeakHBond", "resi 119 & chain A & name O", "PseudoH11A")
cmd.distance("WeakHBond", "resi 10 & chain A & name O", "PseudoH120A")
cmd.distance("WeakHBond", "resi 121 & chain A & name O", "PseudoH8A")
cmd.distance("WeakHBond", "resi 7 & chain A & name O", "PseudoH122A")
cmd.distance("WeakHBond", "resi 123 & chain A & name O", "PseudoH6A")
cmd.distance("WeakHBond", "resi 5 & chain A & name O", "PseudoH124A")
cmd.distance("NonHBond", "resi 46 & chain A & name CB", "resi 63 & chain A & name CB")
cmd.distance("NonHBond", "resi 48 & chain A & name CB", "resi 61 & chain A & name CB")
cmd.distance("NonHBond", "resi 50 & chain A & name CB", "resi 59 & chain A & name CB")
cmd.distance("NonHBond", "resi 52 & chain A & name CB", "resi 57 & chain A & name CB")
cmd.distance("NonHBond", "resi 67 & chain A & name CB", "resi 81 & chain A & name CB")
cmd.distance("NonHBond", "resi 69 & chain A & name CB", "resi 79 & chain A & name CB")
cmd.distance("NonHBond", "resi 71 & chain A & name CB", "resi 77 & chain A & name CB")
cmd.distance("NonHBond", "resi 82 & chain A & name CB", "resi 91 & chain A & name CB")
cmd.distance("NonHBond", "resi 88 & chain A & name CB", "resi 101 & chain A & name CB")
cmd.distance("NonHBond", "resi 90 & chain A & name CB", "resi 99 & chain A & name CB")
cmd.distance("NonHBond", "resi 92 & chain A & name CB", "resi 97 & chain A & name CB")
cmd.distance("NonHBond", "resi 108 & chain A & name CB", "resi 121 & chain A & name CB")
cmd.distance("NonHBond", "resi 110 & chain A & name CB", "resi 119 & chain A & name CB")
cmd.distance("NonHBond", "resi 112 & chain A & name CB", "resi 117 & chain A & name CB")
cmd.distance("NonHBond", "resi 120 & chain A & name CB", "resi 11 & chain A & name CB")
cmd.distance("NonHBond", "resi 122 & chain A & name CB", "resi 8 & chain A & name CB")
cmd.distance("NonHBond", "resi 124 & chain A & name CB", "resi 6 & chain A & name CB")
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
