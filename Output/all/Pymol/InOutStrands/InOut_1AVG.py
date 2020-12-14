from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AVG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Istrand12", "resi 24+25+26+27+28 & chain I ")


cmd.select("Istrand14", "resi 51+52+53+54+55+56 & chain I ")


cmd.select("Istrand13", "resi 37+38+39+40+41+42+43 & chain I ")


cmd.select("Istrand15", "resi 66+67+68+69+70+71 & chain I ")


cmd.select("Istrand16", "resi 80+81+82+83+84+85+86 & chain I ")


cmd.select("Istrand17", "resi 92+93+94+95+96+97+98+99+100+101 & chain I ")


cmd.select("Istrand18", "resi 106+107+108+109+110+111+112+113+114+115 & chain I ")


cmd.select("Istrand19", "resi 122+123+124+125+126+127+128 & chain I ")


cmd.select("barrel", "Istrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 24 & chain I")

cmd.select ("Outward", "resi 24 & chain I", merge=1)

cmd.color ("red", "resi 25 & chain I")

cmd.select ("Inward", "resi 25 & chain I", merge=1)

cmd.color ("blue", "resi 26 & chain I")

cmd.select ("Outward", "resi 26 & chain I", merge=1)

cmd.color ("red", "resi 27 & chain I")

cmd.select ("Inward", "resi 27 & chain I", merge=1)

cmd.color ("blue", "resi 28 & chain I")

cmd.select ("Outward", "resi 28 & chain I", merge=1)

cmd.color ("red", "resi 51 & chain I")

cmd.select ("Inward", "resi 51 & chain I", merge=1)

cmd.color ("blue", "resi 52 & chain I")

cmd.select ("Outward", "resi 52 & chain I", merge=1)

cmd.color ("red", "resi 53 & chain I")

cmd.select ("Inward", "resi 53 & chain I", merge=1)

cmd.color ("blue", "resi 54 & chain I")

cmd.select ("Outward", "resi 54 & chain I", merge=1)

cmd.color ("red", "resi 55 & chain I")

cmd.select ("Inward", "resi 55 & chain I", merge=1)

cmd.color ("blue", "resi 56 & chain I")

cmd.select ("Outward", "resi 56 & chain I", merge=1)

cmd.color ("blue", "resi 37 & chain I")

cmd.select ("Outward", "resi 37 & chain I", merge=1)

cmd.color ("red", "resi 38 & chain I")

cmd.select ("Inward", "resi 38 & chain I", merge=1)

cmd.color ("blue", "resi 39 & chain I")

cmd.select ("Outward", "resi 39 & chain I", merge=1)

cmd.color ("red", "resi 40 & chain I")

cmd.select ("Inward", "resi 40 & chain I", merge=1)

cmd.color ("blue", "resi 41 & chain I")

cmd.select ("Outward", "resi 41 & chain I", merge=1)

cmd.color ("red", "resi 42 & chain I")

cmd.select ("Inward", "resi 42 & chain I", merge=1)

cmd.color ("blue", "resi 43 & chain I")

cmd.select ("Outward", "resi 43 & chain I", merge=1)

cmd.color ("blue", "resi 66 & chain I")

cmd.select ("Outward", "resi 66 & chain I", merge=1)

cmd.color ("red", "resi 67 & chain I")

cmd.select ("Inward", "resi 67 & chain I", merge=1)

cmd.color ("blue", "resi 68 & chain I")

cmd.select ("Outward", "resi 68 & chain I", merge=1)

cmd.color ("red", "resi 69 & chain I")

cmd.select ("Inward", "resi 69 & chain I", merge=1)

cmd.color ("blue", "resi 70 & chain I")

cmd.select ("Outward", "resi 70 & chain I", merge=1)

cmd.color ("blue", "resi 71 & chain I")

cmd.select ("Outward", "resi 71 & chain I", merge=1)

cmd.color ("red", "resi 80 & chain I")

cmd.select ("Inward", "resi 80 & chain I", merge=1)

cmd.color ("blue", "resi 81 & chain I")

cmd.select ("Outward", "resi 81 & chain I", merge=1)

cmd.color ("red", "resi 82 & chain I")

cmd.select ("Inward", "resi 82 & chain I", merge=1)

cmd.color ("blue", "resi 83 & chain I")

cmd.select ("Outward", "resi 83 & chain I", merge=1)

cmd.color ("red", "resi 84 & chain I")

cmd.select ("Inward", "resi 84 & chain I", merge=1)

cmd.color ("blue", "resi 85 & chain I")

cmd.select ("Outward", "resi 85 & chain I", merge=1)

cmd.color ("red", "resi 86 & chain I")

cmd.select ("Inward", "resi 86 & chain I", merge=1)

cmd.color ("red", "resi 92 & chain I")

cmd.select ("Inward", "resi 92 & chain I", merge=1)

cmd.color ("blue", "resi 93 & chain I")

cmd.select ("Outward", "resi 93 & chain I", merge=1)

cmd.color ("red", "resi 94 & chain I")

cmd.select ("Inward", "resi 94 & chain I", merge=1)

cmd.color ("blue", "resi 95 & chain I")

cmd.select ("Outward", "resi 95 & chain I", merge=1)

cmd.color ("red", "resi 96 & chain I")

cmd.select ("Inward", "resi 96 & chain I", merge=1)

cmd.color ("blue", "resi 97 & chain I")

cmd.select ("Outward", "resi 97 & chain I", merge=1)

cmd.color ("blue", "resi 98 & chain I")

cmd.select ("Outward", "resi 98 & chain I", merge=1)

cmd.color ("red", "resi 99 & chain I")

cmd.select ("Inward", "resi 99 & chain I", merge=1)

cmd.color ("blue", "resi 100 & chain I")

cmd.select ("Outward", "resi 100 & chain I", merge=1)

cmd.color ("red", "resi 101 & chain I")

cmd.select ("Inward", "resi 101 & chain I", merge=1)

cmd.color ("blue", "resi 106 & chain I")

cmd.select ("Outward", "resi 106 & chain I", merge=1)

cmd.color ("red", "resi 107 & chain I")

cmd.select ("Inward", "resi 107 & chain I", merge=1)

cmd.color ("blue", "resi 108 & chain I")

cmd.select ("Outward", "resi 108 & chain I", merge=1)

cmd.color ("red", "resi 109 & chain I")

cmd.select ("Inward", "resi 109 & chain I", merge=1)

cmd.color ("blue", "resi 110 & chain I")

cmd.select ("Outward", "resi 110 & chain I", merge=1)

cmd.color ("red", "resi 111 & chain I")

cmd.select ("Inward", "resi 111 & chain I", merge=1)

cmd.color ("blue", "resi 112 & chain I")

cmd.select ("Outward", "resi 112 & chain I", merge=1)

cmd.color ("red", "resi 113 & chain I")

cmd.select ("Inward", "resi 113 & chain I", merge=1)

cmd.color ("blue", "resi 114 & chain I")

cmd.select ("Outward", "resi 114 & chain I", merge=1)

cmd.color ("red", "resi 115 & chain I")

cmd.select ("Inward", "resi 115 & chain I", merge=1)

cmd.color ("blue", "resi 122 & chain I")

cmd.select ("Outward", "resi 122 & chain I", merge=1)

cmd.color ("red", "resi 123 & chain I")

cmd.select ("Inward", "resi 123 & chain I", merge=1)

cmd.color ("blue", "resi 124 & chain I")

cmd.select ("Outward", "resi 124 & chain I", merge=1)

cmd.color ("red", "resi 125 & chain I")

cmd.select ("Inward", "resi 125 & chain I", merge=1)

cmd.color ("blue", "resi 126 & chain I")

cmd.select ("Outward", "resi 126 & chain I", merge=1)

cmd.color ("red", "resi 127 & chain I")

cmd.select ("Inward", "resi 127 & chain I", merge=1)

cmd.color ("blue", "resi 128 & chain I")

cmd.select ("Outward", "resi 128 & chain I", merge=1)

cmd.load_cgo( [9.0, -2.6197505,28.222376,97.617004, -2.6197505, 28.222376, 97.617004, 1, 1,1,0,0,0,1], "axis" )
