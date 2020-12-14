from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1ZXU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 38+39+40+41+42+43 & chain A ")


cmd.select("Astrand1", "resi 54+55+56+57+58 & chain A ")


cmd.select("Astrand2", "resi 63+64+65+66+67+68 & chain A ")


cmd.select("Astrand3", "resi 77+78+79+80+81 & chain A ")


cmd.select("Astrand4", "resi 87+88+89+90+91+92 & chain A ")


cmd.select("Astrand5", "resi 101+102+103+104+105+106 & chain A ")


cmd.select("Astrand6", "resi 115+116+117+118+119+120 & chain A ")


cmd.select("Astrand7", "resi 131+132+133+134+135 & chain A ")


cmd.select("Astrand8", "resi 146+147+148+149 & chain A ")


cmd.select("Astrand9", "resi 158+159+160+161 & chain A ")


cmd.select("Astrand10", "resi 167+168+169+170+171+172+173 & chain A ")


cmd.select("Astrand11", "resi 187+188+189+190+191 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH58A", pos=[18.027496,10.410364,3.676235])
cmd.pseudoatom ("PseudoH40A", pos=[15.6720705,9.647812,4.138073])
cmd.pseudoatom ("PseudoH56A", pos=[13.520516,9.07344,-1.2578318])
cmd.pseudoatom ("PseudoH42A", pos=[11.298701,10.459684,-1.3564498])
cmd.pseudoatom ("PseudoH66A", pos=[14.838188,6.1084723,-6.8098207])
cmd.pseudoatom ("PseudoH55A", pos=[13.753858,7.844947,-5.618517])
cmd.pseudoatom ("PseudoH65A", pos=[17.703438,3.8001177,-4.1918316])
cmd.pseudoatom ("PseudoH80A", pos=[13.693948,0.92390937,-5.8736806])
cmd.pseudoatom ("PseudoH67A", pos=[12.0539875,2.8070803,-6.9627104])
cmd.pseudoatom ("PseudoH78A", pos=[7.9625373,-1.0298321,-9.413838])
cmd.pseudoatom ("PseudoH77A", pos=[5.333076,-4.5853424,-8.86244])
cmd.pseudoatom ("PseudoH90A", pos=[10.975543,-4.8903384,-6.674358])
cmd.pseudoatom ("PseudoH79A", pos=[11.431552,-2.768294,-7.4006386])
cmd.pseudoatom ("PseudoH87A", pos=[17.211697,-2.7909803,-8.074076])
cmd.pseudoatom ("PseudoH89A", pos=[14.411782,-6.427808,-4.078131])
cmd.pseudoatom ("PseudoH104A", pos=[8.713435,-7.797568,-2.7999074])
cmd.pseudoatom ("PseudoH91A", pos=[7.496197,-6.1595407,-4.14271])
cmd.pseudoatom ("PseudoH102A", pos=[2.0360787,-7.3529935,-2.7106757])
cmd.pseudoatom ("PseudoH101A", pos=[-1.0701901,-7.6873717,0.5936253])
cmd.pseudoatom ("PseudoH118A", pos=[4.66643,-9.958629,1.411329])
cmd.pseudoatom ("PseudoH103A", pos=[5.2054114,-9.738217,-0.77133536])
cmd.pseudoatom ("PseudoH115A", pos=[10.246819,-13.157224,-1.9895809])
cmd.pseudoatom ("PseudoH135A", pos=[9.106208,-11.912641,6.0121493])
cmd.pseudoatom ("PseudoH117A", pos=[8.1354475,-11.8447695,3.5863166])
cmd.pseudoatom ("PseudoH133A", pos=[4.148397,-7.9064593,6.5153937])
cmd.pseudoatom ("PseudoH119A", pos=[2.797527,-7.429001,4.5630655])
cmd.pseudoatom ("PseudoH131A", pos=[-0.74248123,-3.461099,6.853566])
cmd.pseudoatom ("PseudoH147A", pos=[3.0410664,-4.361371,11.051314])
cmd.pseudoatom ("PseudoH132A", pos=[1.7737987,-5.994734,9.658173])
cmd.pseudoatom ("PseudoH146A", pos=[6.751122,-5.9606175,12.928307])
cmd.pseudoatom ("PseudoH159A", pos=[5.874186,0.19099349,11.995863])
cmd.pseudoatom ("PseudoH148A", pos=[3.650511,0.055167466,11.337475])
cmd.pseudoatom ("PseudoH158A", pos=[6.28929,4.485764,12.849894])
cmd.pseudoatom ("PseudoH167A", pos=[8.940995,0.6517978,16.613894])
cmd.pseudoatom ("PseudoH191A", pos=[14.23784,4.0340834,10.991923])
cmd.pseudoatom ("PseudoH169A", pos=[11.995276,4.064068,12.436544])
cmd.pseudoatom ("PseudoH189A", pos=[10.377041,8.935828,8.973636])
cmd.pseudoatom ("PseudoH171A", pos=[8.363405,9.27564,9.697018])
cmd.pseudoatom ("PseudoH187A", pos=[7.7367644,14.933546,6.82511])
cmd.pseudoatom ("PseudoH188A", pos=[10.956987,11.963429,5.768116])
cmd.pseudoatom ("PseudoH39A", pos=[15.345954,9.523607,8.487458])
cmd.pseudoatom ("PseudoH190A", pos=[14.573871,8.459602,10.42646])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 41 & chain A & name O", "resi 57 & chain A & name N")
cmd.distance("StrongHBond", "resi 41 & chain A & name N", "resi 57 & chain A & name O")
cmd.distance("StrongHBond", "resi 43 & chain A & name O", "resi 55 & chain A & name N")
cmd.distance("StrongHBond", "resi 43 & chain A & name N", "resi 55 & chain A & name O")
cmd.distance("StrongHBond", "resi 54 & chain A & name O", "resi 67 & chain A & name N")
cmd.distance("StrongHBond", "resi 54 & chain A & name N", "resi 67 & chain A & name O")
cmd.distance("StrongHBond", "resi 56 & chain A & name O", "resi 65 & chain A & name N")
cmd.distance("StrongHBond", "resi 56 & chain A & name N", "resi 65 & chain A & name O")
cmd.distance("StrongHBond", "resi 66 & chain A & name O", "resi 81 & chain A & name N")
cmd.distance("StrongHBond", "resi 66 & chain A & name N", "resi 81 & chain A & name O")
cmd.distance("StrongHBond", "resi 68 & chain A & name O", "resi 79 & chain A & name N")
cmd.distance("StrongHBond", "resi 68 & chain A & name N", "resi 79 & chain A & name O")
cmd.distance("StrongHBond", "resi 78 & chain A & name O", "resi 91 & chain A & name N")
cmd.distance("StrongHBond", "resi 78 & chain A & name N", "resi 91 & chain A & name O")
cmd.distance("StrongHBond", "resi 80 & chain A & name O", "resi 89 & chain A & name N")
cmd.distance("StrongHBond", "resi 80 & chain A & name N", "resi 89 & chain A & name O")
cmd.distance("StrongHBond", "resi 90 & chain A & name O", "resi 105 & chain A & name N")
cmd.distance("StrongHBond", "resi 90 & chain A & name N", "resi 105 & chain A & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 103 & chain A & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 103 & chain A & name O")
cmd.distance("StrongHBond", "resi 102 & chain A & name O", "resi 119 & chain A & name N")
cmd.distance("StrongHBond", "resi 102 & chain A & name N", "resi 119 & chain A & name O")
cmd.distance("StrongHBond", "resi 104 & chain A & name O", "resi 117 & chain A & name N")
cmd.distance("StrongHBond", "resi 104 & chain A & name N", "resi 117 & chain A & name O")
cmd.distance("StrongHBond", "resi 118 & chain A & name O", "resi 134 & chain A & name N")
cmd.distance("StrongHBond", "resi 118 & chain A & name N", "resi 134 & chain A & name O")
cmd.distance("StrongHBond", "resi 120 & chain A & name O", "resi 132 & chain A & name N")
cmd.distance("StrongHBond", "resi 120 & chain A & name N", "resi 132 & chain A & name O")
cmd.distance("StrongHBond", "resi 131 & chain A & name O", "resi 148 & chain A & name N")
cmd.distance("StrongHBond", "resi 131 & chain A & name N", "resi 148 & chain A & name O")
cmd.distance("StrongHBond", "resi 133 & chain A & name O", "resi 146 & chain A & name N")
cmd.distance("StrongHBond", "resi 133 & chain A & name N", "resi 146 & chain A & name O")
cmd.distance("StrongHBond", "resi 147 & chain A & name O", "resi 160 & chain A & name N")
cmd.distance("StrongHBond", "resi 147 & chain A & name N", "resi 160 & chain A & name O")
cmd.distance("StrongHBond", "resi 149 & chain A & name O", "resi 158 & chain A & name N")
cmd.distance("StrongHBond", "resi 149 & chain A & name N", "resi 158 & chain A & name O")
cmd.distance("StrongHBond", "resi 159 & chain A & name O", "resi 169 & chain A & name N")
cmd.distance("StrongHBond", "resi 159 & chain A & name N", "resi 169 & chain A & name O")
cmd.distance("StrongHBond", "resi 170 & chain A & name O", "resi 190 & chain A & name N")
cmd.distance("StrongHBond", "resi 170 & chain A & name N", "resi 190 & chain A & name O")
cmd.distance("StrongHBond", "resi 172 & chain A & name O", "resi 188 & chain A & name N")
cmd.distance("StrongHBond", "resi 172 & chain A & name N", "resi 188 & chain A & name O")
cmd.distance("StrongHBond", "resi 189 & chain A & name O", "resi 40 & chain A & name N")
cmd.distance("StrongHBond", "resi 189 & chain A & name N", "resi 40 & chain A & name O")
cmd.distance("StrongHBond", "resi 191 & chain A & name O", "resi 38 & chain A & name N")
cmd.distance("StrongHBond", "resi 191 & chain A & name N", "resi 38 & chain A & name O")
cmd.distance("WeakHBond", "resi 39 & chain A & name O", "PseudoH58A")
cmd.distance("WeakHBond", "resi 57 & chain A & name O", "PseudoH40A")
cmd.distance("WeakHBond", "resi 41 & chain A & name O", "PseudoH56A")
cmd.distance("WeakHBond", "resi 55 & chain A & name O", "PseudoH42A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH66A")
cmd.distance("WeakHBond", "resi 65 & chain A & name O", "PseudoH55A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH65A")
cmd.distance("WeakHBond", "resi 66 & chain A & name O", "PseudoH80A")
cmd.distance("WeakHBond", "resi 79 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 68 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH77A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 80 & chain A & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 105 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH102A")
cmd.distance("WeakHBond", "resi 119 & chain A & name O", "PseudoH101A")
cmd.distance("WeakHBond", "resi 102 & chain A & name O", "PseudoH118A")
cmd.distance("WeakHBond", "resi 117 & chain A & name O", "PseudoH103A")
cmd.distance("WeakHBond", "resi 104 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH135A")
cmd.distance("WeakHBond", "resi 134 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH133A")
cmd.distance("WeakHBond", "resi 132 & chain A & name O", "PseudoH119A")
cmd.distance("WeakHBond", "resi 120 & chain A & name O", "PseudoH131A")
cmd.distance("WeakHBond", "resi 131 & chain A & name O", "PseudoH147A")
cmd.distance("WeakHBond", "resi 146 & chain A & name O", "PseudoH132A")
cmd.distance("WeakHBond", "resi 160 & chain A & name O", "PseudoH146A")
cmd.distance("WeakHBond", "resi 147 & chain A & name O", "PseudoH159A")
cmd.distance("WeakHBond", "resi 158 & chain A & name O", "PseudoH148A")
cmd.distance("WeakHBond", "resi 169 & chain A & name O", "PseudoH158A")
cmd.distance("WeakHBond", "resi 159 & chain A & name O", "PseudoH167A")
cmd.distance("WeakHBond", "resi 168 & chain A & name O", "PseudoH191A")
cmd.distance("WeakHBond", "resi 190 & chain A & name O", "PseudoH169A")
cmd.distance("WeakHBond", "resi 170 & chain A & name O", "PseudoH189A")
cmd.distance("WeakHBond", "resi 188 & chain A & name O", "PseudoH171A")
cmd.distance("WeakHBond", "resi 172 & chain A & name O", "PseudoH187A")
cmd.distance("WeakHBond", "resi 40 & chain A & name O", "PseudoH188A")
cmd.distance("WeakHBond", "resi 189 & chain A & name O", "PseudoH39A")
cmd.distance("WeakHBond", "resi 38 & chain A & name O", "PseudoH190A")
cmd.distance("NonHBond", "resi 40 & chain A & name CB", "resi 58 & chain A & name CB")
cmd.distance("NonHBond", "resi 42 & chain A & name CB", "resi 56 & chain A & name CB")
cmd.distance("NonHBond", "resi 55 & chain A & name CB", "resi 66 & chain A & name CB")
cmd.distance("NonHBond", "resi 57 & chain A & name CB", "resi 63 & chain A & name CB")
cmd.distance("NonHBond", "resi 67 & chain A & name CB", "resi 80 & chain A & name CB")
cmd.distance("NonHBond", "resi 77 & chain A & name CB", "resi 92 & chain A & name CB")
cmd.distance("NonHBond", "resi 79 & chain A & name CB", "resi 90 & chain A & name CB")
cmd.distance("NonHBond", "resi 81 & chain A & name CB", "resi 87 & chain A & name CB")
cmd.distance("NonHBond", "resi 91 & chain A & name CB", "resi 104 & chain A & name CB")
cmd.distance("NonHBond", "resi 101 & chain A & name CB", "resi 120 & chain A & name CB")
cmd.distance("NonHBond", "resi 103 & chain A & name CB", "resi 118 & chain A & name CB")
cmd.distance("NonHBond", "resi 105 & chain A & name CB", "resi 115 & chain A & name CB")
cmd.distance("NonHBond", "resi 117 & chain A & name CB", "resi 135 & chain A & name CB")
cmd.distance("NonHBond", "resi 119 & chain A & name CB", "resi 133 & chain A & name CB")
cmd.distance("NonHBond", "resi 132 & chain A & name CB", "resi 147 & chain A & name CB")
cmd.distance("NonHBond", "resi 146 & chain A & name CB", "resi 161 & chain A & name CB")
cmd.distance("NonHBond", "resi 148 & chain A & name CB", "resi 159 & chain A & name CB")
cmd.distance("NonHBond", "resi 158 & chain A & name CB", "resi 170 & chain A & name CB")
cmd.distance("NonHBond", "resi 160 & chain A & name CB", "resi 167 & chain A & name CB")
cmd.distance("NonHBond", "resi 169 & chain A & name CB", "resi 191 & chain A & name CB")
cmd.distance("NonHBond", "resi 171 & chain A & name CB", "resi 189 & chain A & name CB")
cmd.distance("NonHBond", "resi 173 & chain A & name CB", "resi 187 & chain A & name CB")
cmd.distance("NonHBond", "resi 188 & chain A & name CB", "resi 41 & chain A & name CB")
cmd.distance("NonHBond", "resi 190 & chain A & name CB", "resi 39 & chain A & name CB")
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