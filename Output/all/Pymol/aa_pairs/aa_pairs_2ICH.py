from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 47+48+49+50+51+52+53+54+55+56+57 & chain A ")


cmd.select("Astrand1", "resi 182+183+184+185+186+187+188+189+190+191+192+193+194+195+196+197+198+199 & chain A ")


cmd.select("Astrand2", "resi 203+204+205+206+207+208+209+210+211+212+213+214+215+216+217 & chain A ")


cmd.select("Astrand3", "resi 121+122+123 & chain A ")


cmd.select("Astrand4", "resi 143+144+145+146+147+148 & chain A ")


cmd.select("Astrand5", "resi 127+128+129+130 & chain A ")


cmd.select("Astrand6", "resi 133+134+135+136+137 & chain A ")


cmd.select("Astrand7", "resi 106+107+108+109+110+111+112+113+114 & chain A ")


cmd.select("Astrand8", "resi 152+153+154+155+156+157+158+159 & chain A ")


cmd.select("Astrand9", "resi 89+90+91+92+93+94+95+96+97+98 & chain A ")


cmd.select("Astrand10", "resi 63+64+65+66+67+68+69+70+71+72+73 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH183A", pos=[-0.4391812,14.0905905,25.940979])
cmd.pseudoatom ("PseudoH215A", pos=[0.55029714,18.390081,22.088839])
cmd.pseudoatom ("PseudoH185A", pos=[-0.6263965,17.38699,20.356354])
cmd.pseudoatom ("PseudoH213A", pos=[2.7216609,20.278751,16.08973])
cmd.pseudoatom ("PseudoH187A", pos=[0.77734673,20.291399,14.633222])
cmd.pseudoatom ("PseudoH211A", pos=[4.549351,22.917683,10.027761])
cmd.pseudoatom ("PseudoH209A", pos=[6.641872,26.992329,4.6646905])
cmd.pseudoatom ("PseudoH192A", pos=[4.4727163,28.768251,3.9120977])
cmd.pseudoatom ("PseudoH207A", pos=[9.203881,33.120136,2.5692334])
cmd.pseudoatom ("PseudoH194A", pos=[7.783017,35.01466,4.192801])
cmd.pseudoatom ("PseudoH205A", pos=[12.898846,38.941517,4.268882])
cmd.pseudoatom ("PseudoH196A", pos=[12.96479,38.93149,6.560653])
cmd.pseudoatom ("PseudoH203A", pos=[17.541029,41.937904,7.8020144])
cmd.pseudoatom ("PseudoH127A", pos=[0.64244354,33.570923,21.705008])
cmd.pseudoatom ("PseudoH134A", pos=[7.169231,35.62352,22.285004])
cmd.pseudoatom ("PseudoH129A", pos=[6.918956,35.283054,24.537222])
cmd.pseudoatom ("PseudoH89A", pos=[6.3356676,26.14832,36.580025])
cmd.pseudoatom ("PseudoH72A", pos=[6.991618,25.70516,30.048655])
cmd.pseudoatom ("PseudoH91A", pos=[8.519554,27.575672,29.850594])
cmd.pseudoatom ("PseudoH70A", pos=[9.661233,27.25329,24.199034])
cmd.pseudoatom ("PseudoH93A", pos=[12.160632,27.41124,24.357092])
cmd.pseudoatom ("PseudoH68A", pos=[12.765223,27.867588,17.894415])
cmd.pseudoatom ("PseudoH95A", pos=[15.161086,28.191505,18.100916])
cmd.pseudoatom ("PseudoH66A", pos=[16.269896,27.22735,11.708606])
cmd.pseudoatom ("PseudoH97A", pos=[18.446787,28.544346,11.778553])
cmd.pseudoatom ("PseudoH64A", pos=[19.287752,27.454895,5.55232])
cmd.pseudoatom ("PseudoH63A", pos=[17.374142,28.027508,1.3980699])
cmd.pseudoatom ("PseudoH55A", pos=[14.084312,25.83555,5.9946275])
cmd.pseudoatom ("PseudoH65A", pos=[15.709804,25.800577,7.61373])
cmd.pseudoatom ("PseudoH53A", pos=[11.3614645,24.272749,12.537267])
cmd.pseudoatom ("PseudoH67A", pos=[12.54063,25.940096,13.825835])
cmd.pseudoatom ("PseudoH51A", pos=[8.427921,24.082056,18.617403])
cmd.pseudoatom ("PseudoH69A", pos=[9.94804,25.342169,20.184568])
cmd.pseudoatom ("PseudoH49A", pos=[5.8539295,23.030422,24.107275])
cmd.pseudoatom ("PseudoH71A", pos=[7.1882973,23.851091,26.024157])
cmd.pseudoatom ("PseudoH47A", pos=[4.3372355,20.987968,30.554115])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR65A", pos=[17.107658,24.872297,8.281532])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 184 & chain A & name O", "resi 216 & chain A & name N")
cmd.distance("StrongHBond", "resi 184 & chain A & name N", "resi 216 & chain A & name O")
cmd.distance("StrongHBond", "resi 186 & chain A & name O", "resi 214 & chain A & name N")
cmd.distance("StrongHBond", "resi 186 & chain A & name N", "resi 214 & chain A & name O")
cmd.distance("StrongHBond", "resi 188 & chain A & name O", "resi 212 & chain A & name N")
cmd.distance("StrongHBond", "resi 188 & chain A & name N", "resi 212 & chain A & name O")
cmd.distance("StrongHBond", "resi 191 & chain A & name O", "resi 210 & chain A & name N")
cmd.distance("StrongHBond", "resi 191 & chain A & name N", "resi 210 & chain A & name O")
cmd.distance("StrongHBond", "resi 193 & chain A & name O", "resi 208 & chain A & name N")
cmd.distance("StrongHBond", "resi 193 & chain A & name N", "resi 208 & chain A & name O")
cmd.distance("StrongHBond", "resi 195 & chain A & name O", "resi 206 & chain A & name N")
cmd.distance("StrongHBond", "resi 195 & chain A & name N", "resi 206 & chain A & name O")
cmd.distance("StrongHBond", "resi 197 & chain A & name O", "resi 204 & chain A & name N")
cmd.distance("StrongHBond", "resi 197 & chain A & name N", "resi 204 & chain A & name O")
cmd.distance("StrongHBond", "resi 128 & chain A & name O", "resi 135 & chain A & name N")
cmd.distance("StrongHBond", "resi 128 & chain A & name N", "resi 135 & chain A & name O")
cmd.distance("StrongHBond", "resi 130 & chain A & name O", "resi 133 & chain A & name N")
cmd.distance("StrongHBond", "resi 130 & chain A & name N", "resi 133 & chain A & name O")
cmd.distance("StrongHBond", "resi 90 & chain A & name O", "resi 73 & chain A & name N")
cmd.distance("StrongHBond", "resi 90 & chain A & name N", "resi 73 & chain A & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 71 & chain A & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 71 & chain A & name O")
cmd.distance("StrongHBond", "resi 94 & chain A & name O", "resi 69 & chain A & name N")
cmd.distance("StrongHBond", "resi 94 & chain A & name N", "resi 69 & chain A & name O")
cmd.distance("StrongHBond", "resi 96 & chain A & name O", "resi 67 & chain A & name N")
cmd.distance("StrongHBond", "resi 96 & chain A & name N", "resi 67 & chain A & name O")
cmd.distance("StrongHBond", "resi 98 & chain A & name O", "resi 65 & chain A & name N")
cmd.distance("StrongHBond", "resi 98 & chain A & name N", "resi 65 & chain A & name O")
cmd.distance("StrongHBond", "resi 64 & chain A & name O", "resi 56 & chain A & name N")
cmd.distance("StrongHBond", "resi 64 & chain A & name N", "resi 56 & chain A & name O")
cmd.distance("StrongHBond", "resi 66 & chain A & name O", "resi 54 & chain A & name N")
cmd.distance("StrongHBond", "resi 66 & chain A & name N", "resi 54 & chain A & name O")
cmd.distance("StrongHBond", "resi 68 & chain A & name O", "resi 52 & chain A & name N")
cmd.distance("StrongHBond", "resi 68 & chain A & name N", "resi 52 & chain A & name O")
cmd.distance("StrongHBond", "resi 70 & chain A & name O", "resi 50 & chain A & name N")
cmd.distance("StrongHBond", "resi 70 & chain A & name N", "resi 50 & chain A & name O")
cmd.distance("StrongHBond", "resi 72 & chain A & name O", "resi 48 & chain A & name N")
cmd.distance("StrongHBond", "resi 72 & chain A & name N", "resi 48 & chain A & name O")
cmd.distance("WeakHBond", "resi 216 & chain A & name O", "PseudoH183A")
cmd.distance("WeakHBond", "resi 184 & chain A & name O", "PseudoH215A")
cmd.distance("WeakHBond", "resi 214 & chain A & name O", "PseudoH185A")
cmd.distance("WeakHBond", "resi 186 & chain A & name O", "PseudoH213A")
cmd.distance("WeakHBond", "resi 212 & chain A & name O", "PseudoH187A")
cmd.distance("WeakHBond", "resi 188 & chain A & name O", "PseudoH211A")
cmd.distance("WeakHBond", "resi 191 & chain A & name O", "PseudoH209A")
cmd.distance("WeakHBond", "resi 208 & chain A & name O", "PseudoH192A")
cmd.distance("WeakHBond", "resi 193 & chain A & name O", "PseudoH207A")
cmd.distance("WeakHBond", "resi 206 & chain A & name O", "PseudoH194A")
cmd.distance("WeakHBond", "resi 195 & chain A & name O", "PseudoH205A")
cmd.distance("WeakHBond", "resi 204 & chain A & name O", "PseudoH196A")
cmd.distance("WeakHBond", "resi 197 & chain A & name O", "PseudoH203A")
cmd.distance("WeakHBond", "resi 135 & chain A & name O", "PseudoH127A")
cmd.distance("WeakHBond", "resi 128 & chain A & name O", "PseudoH134A")
cmd.distance("WeakHBond", "resi 133 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 73 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH72A")
cmd.distance("WeakHBond", "resi 71 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH70A")
cmd.distance("WeakHBond", "resi 69 & chain A & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH68A")
cmd.distance("WeakHBond", "resi 67 & chain A & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 96 & chain A & name O", "PseudoH66A")
cmd.distance("WeakHBond", "resi 65 & chain A & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH64A")
cmd.distance("WeakHBond", "resi 56 & chain A & name O", "PseudoH63A")
cmd.distance("WeakHBond", "resi 64 & chain A & name O", "PseudoH55A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH65A")
cmd.distance("WeakHBond", "resi 66 & chain A & name O", "PseudoH53A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 68 & chain A & name O", "PseudoH51A")
cmd.distance("WeakHBond", "resi 50 & chain A & name O", "PseudoH69A")
cmd.distance("WeakHBond", "resi 70 & chain A & name O", "PseudoH49A")
cmd.distance("WeakHBond", "resi 48 & chain A & name O", "PseudoH71A")
cmd.distance("WeakHBond", "resi 72 & chain A & name O", "PseudoH47A")
cmd.distance("NonHBond", "resi 185 & chain A & name CB", "resi 215 & chain A & name CB")
cmd.distance("NonHBond", "resi 187 & chain A & name CB", "resi 213 & chain A & name CB")
cmd.distance("NonHBond", "resi 189 & chain A & name CB", "resi 211 & chain A & name CB")
cmd.distance("NonHBond", "resi 192 & chain A & name CB", "resi 209 & chain A & name CB")
cmd.distance("NonHBond", "resi 194 & chain A & name CB", "resi 207 & chain A & name CB")
cmd.distance("NonHBond", "resi 196 & chain A & name CB", "resi 205 & chain A & name CB")
cmd.distance("NonHBond", "resi 198 & chain A & name CB", "resi 203 & chain A & name CB")
cmd.distance("NonHBond", "resi 127 & chain A & name CB", "resi 136 & chain A & name CB")
cmd.distance("NonHBond", "resi 129 & chain A & name CB", "resi 134 & chain A & name CB")
cmd.distance("NonHBond", "resi 91 & chain A & name CB", "resi 72 & chain A & name CB")
cmd.distance("NonHBond", "resi 93 & chain A & name CB", "resi 70 & chain A & name CB")
cmd.distance("NonHBond", "resi 95 & chain A & name CB", "resi 68 & chain A & name CB")
cmd.distance("NonHBond", "resi 97 & chain A & name CB", "resi 66 & chain A & name CB")
cmd.distance("NonHBond", "resi 63 & chain A & name CB", "resi 57 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR65A", "resi 55 & chain A & name CB")
cmd.distance("NonHBond", "resi 67 & chain A & name CB", "resi 53 & chain A & name CB")
cmd.distance("NonHBond", "resi 69 & chain A & name CB", "resi 51 & chain A & name CB")
cmd.distance("NonHBond", "resi 71 & chain A & name CB", "resi 49 & chain A & name CB")
cmd.distance("NonHBond", "resi 73 & chain A & name CB", "resi 47 & chain A & name CB")
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