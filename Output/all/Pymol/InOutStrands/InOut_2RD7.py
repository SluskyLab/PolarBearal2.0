from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2RD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Cstrand0", "resi 29+30+31+32+33+34+35+36+37+38 & chain C ")


cmd.select("Cstrand1", "resi 54+55+56+57+58 & chain C ")


cmd.select("Cstrand2", "resi 65+66+67+68+69+70+71+72 & chain C ")


cmd.select("Cstrand3", "resi 75+76+77+78+79+80+81+82 & chain C ")


cmd.select("Cstrand4", "resi 91+92+93+94 & chain C ")


cmd.select("Cstrand5", "resi 103+104+105+106+107+108+109+110 & chain C ")


cmd.select("Cstrand6", "resi 115+116+117+118+119+120+121 & chain C ")


cmd.select("Cstrand7", "resi 127+128+129+130+131+132 & chain C ")


cmd.select("barrel", "Cstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 29 & chain C")

cmd.select ("Outward", "resi 29 & chain C", merge=1)

cmd.color ("blue", "resi 30 & chain C")

cmd.select ("Outward", "resi 30 & chain C", merge=1)

cmd.color ("red", "resi 31 & chain C")

cmd.select ("Inward", "resi 31 & chain C", merge=1)

cmd.color ("blue", "resi 32 & chain C")

cmd.select ("Outward", "resi 32 & chain C", merge=1)

cmd.color ("red", "resi 33 & chain C")

cmd.select ("Inward", "resi 33 & chain C", merge=1)

cmd.color ("blue", "resi 34 & chain C")

cmd.select ("Outward", "resi 34 & chain C", merge=1)

cmd.color ("blue", "resi 35 & chain C")

cmd.select ("Outward", "resi 35 & chain C", merge=1)

cmd.color ("red", "resi 36 & chain C")

cmd.select ("Inward", "resi 36 & chain C", merge=1)

cmd.color ("blue", "resi 37 & chain C")

cmd.select ("Outward", "resi 37 & chain C", merge=1)

cmd.color ("red", "resi 38 & chain C")

cmd.select ("Inward", "resi 38 & chain C", merge=1)

cmd.color ("red", "resi 54 & chain C")

cmd.select ("Inward", "resi 54 & chain C", merge=1)

cmd.color ("blue", "resi 55 & chain C")

cmd.select ("Outward", "resi 55 & chain C", merge=1)

cmd.color ("red", "resi 56 & chain C")

cmd.select ("Inward", "resi 56 & chain C", merge=1)

cmd.color ("blue", "resi 57 & chain C")

cmd.select ("Outward", "resi 57 & chain C", merge=1)

cmd.color ("red", "resi 58 & chain C")

cmd.select ("Inward", "resi 58 & chain C", merge=1)

cmd.color ("red", "resi 65 & chain C")

cmd.select ("Inward", "resi 65 & chain C", merge=1)

cmd.color ("blue", "resi 66 & chain C")

cmd.select ("Outward", "resi 66 & chain C", merge=1)

cmd.color ("red", "resi 67 & chain C")

cmd.select ("Inward", "resi 67 & chain C", merge=1)

cmd.color ("blue", "resi 68 & chain C")

cmd.select ("Outward", "resi 68 & chain C", merge=1)

cmd.color ("blue", "resi 69 & chain C")

cmd.select ("Outward", "resi 69 & chain C", merge=1)

cmd.color ("blue", "resi 70 & chain C")

cmd.select ("Outward", "resi 70 & chain C", merge=1)

cmd.color ("blue", "resi 71 & chain C")

cmd.select ("Outward", "resi 71 & chain C", merge=1)

cmd.color ("red", "resi 72 & chain C")

cmd.select ("Inward", "resi 72 & chain C", merge=1)

cmd.color ("blue", "resi 75 & chain C")

cmd.select ("Outward", "resi 75 & chain C", merge=1)

cmd.color ("red", "resi 76 & chain C")

cmd.select ("Inward", "resi 76 & chain C", merge=1)

cmd.color ("blue", "resi 77 & chain C")

cmd.select ("Outward", "resi 77 & chain C", merge=1)

cmd.color ("red", "resi 78 & chain C")

cmd.select ("Inward", "resi 78 & chain C", merge=1)

cmd.color ("blue", "resi 79 & chain C")

cmd.select ("Outward", "resi 79 & chain C", merge=1)

cmd.color ("blue", "resi 80 & chain C")

cmd.select ("Outward", "resi 80 & chain C", merge=1)

cmd.color ("red", "resi 81 & chain C")

cmd.select ("Inward", "resi 81 & chain C", merge=1)

cmd.color ("blue", "resi 82 & chain C")

cmd.select ("Outward", "resi 82 & chain C", merge=1)

cmd.color ("blue", "resi 91 & chain C")

cmd.select ("Outward", "resi 91 & chain C", merge=1)

cmd.color ("red", "resi 92 & chain C")

cmd.select ("Inward", "resi 92 & chain C", merge=1)

cmd.color ("blue", "resi 93 & chain C")

cmd.select ("Outward", "resi 93 & chain C", merge=1)

cmd.color ("red", "resi 94 & chain C")

cmd.select ("Inward", "resi 94 & chain C", merge=1)

cmd.color ("blue", "resi 103 & chain C")

cmd.select ("Outward", "resi 103 & chain C", merge=1)

cmd.color ("red", "resi 104 & chain C")

cmd.select ("Inward", "resi 104 & chain C", merge=1)

cmd.color ("blue", "resi 105 & chain C")

cmd.select ("Outward", "resi 105 & chain C", merge=1)

cmd.color ("red", "resi 106 & chain C")

cmd.select ("Inward", "resi 106 & chain C", merge=1)

cmd.color ("blue", "resi 107 & chain C")

cmd.select ("Outward", "resi 107 & chain C", merge=1)

cmd.color ("red", "resi 108 & chain C")

cmd.select ("Inward", "resi 108 & chain C", merge=1)

cmd.color ("blue", "resi 109 & chain C")

cmd.select ("Outward", "resi 109 & chain C", merge=1)

cmd.color ("blue", "resi 110 & chain C")

cmd.select ("Outward", "resi 110 & chain C", merge=1)

cmd.color ("red", "resi 115 & chain C")

cmd.select ("Inward", "resi 115 & chain C", merge=1)

cmd.color ("blue", "resi 116 & chain C")

cmd.select ("Outward", "resi 116 & chain C", merge=1)

cmd.color ("red", "resi 117 & chain C")

cmd.select ("Inward", "resi 117 & chain C", merge=1)

cmd.color ("blue", "resi 118 & chain C")

cmd.select ("Outward", "resi 118 & chain C", merge=1)

cmd.color ("red", "resi 119 & chain C")

cmd.select ("Inward", "resi 119 & chain C", merge=1)

cmd.color ("blue", "resi 120 & chain C")

cmd.select ("Outward", "resi 120 & chain C", merge=1)

cmd.color ("red", "resi 121 & chain C")

cmd.select ("Inward", "resi 121 & chain C", merge=1)

cmd.color ("blue", "resi 127 & chain C")

cmd.select ("Outward", "resi 127 & chain C", merge=1)

cmd.color ("red", "resi 128 & chain C")

cmd.select ("Inward", "resi 128 & chain C", merge=1)

cmd.color ("blue", "resi 129 & chain C")

cmd.select ("Outward", "resi 129 & chain C", merge=1)

cmd.color ("blue", "resi 130 & chain C")

cmd.select ("Outward", "resi 130 & chain C", merge=1)

cmd.color ("red", "resi 131 & chain C")

cmd.select ("Inward", "resi 131 & chain C", merge=1)

cmd.color ("blue", "resi 132 & chain C")

cmd.select ("Outward", "resi 132 & chain C", merge=1)

cmd.load_cgo( [9.0, -30.5625,10.023999,28.50425, -30.5625, 10.023999, 28.50425, 1, 1,1,0,0,0,1], "axis" )
