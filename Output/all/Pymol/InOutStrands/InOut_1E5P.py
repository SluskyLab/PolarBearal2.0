from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand16", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19 & chain B ")


cmd.select("Bstrand18", "resi 35+36+37+38+39 & chain B ")


cmd.select("Bstrand19", "resi 44+45+46+47+48+49+50+51+52+53 & chain B ")


cmd.select("Bstrand20", "resi 56+57+58+59+60+61+62+63+64+65+66+67 & chain B ")


cmd.select("Bstrand21", "resi 71+72+73+74+75+76 & chain B ")


cmd.select("Bstrand22", "resi 79+80+81+82+83 & chain B ")


cmd.select("Bstrand24", "resi 91+92+93+94+95+96+97+98+99+100 & chain B ")


cmd.select("Bstrand25", "resi 105+106+107+108+109+110+111+112+113 & chain B ")


cmd.select("barrel", "Bstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 7 & chain B")

cmd.select ("Outward", "resi 7 & chain B", merge=1)

cmd.color ("blue", "resi 8 & chain B")

cmd.select ("Outward", "resi 8 & chain B", merge=1)

cmd.color ("blue", "resi 9 & chain B")

cmd.select ("Outward", "resi 9 & chain B", merge=1)

cmd.color ("blue", "resi 10 & chain B")

cmd.select ("Outward", "resi 10 & chain B", merge=1)

cmd.color ("blue", "resi 11 & chain B")

cmd.select ("Outward", "resi 11 & chain B", merge=1)

cmd.color ("blue", "resi 12 & chain B")

cmd.select ("Outward", "resi 12 & chain B", merge=1)

cmd.color ("blue", "resi 13 & chain B")

cmd.select ("Outward", "resi 13 & chain B", merge=1)

cmd.color ("blue", "resi 14 & chain B")

cmd.select ("Outward", "resi 14 & chain B", merge=1)

cmd.color ("blue", "resi 15 & chain B")

cmd.select ("Outward", "resi 15 & chain B", merge=1)

cmd.color ("blue", "resi 16 & chain B")

cmd.select ("Outward", "resi 16 & chain B", merge=1)

cmd.color ("blue", "resi 17 & chain B")

cmd.select ("Outward", "resi 17 & chain B", merge=1)

cmd.color ("blue", "resi 18 & chain B")

cmd.select ("Outward", "resi 18 & chain B", merge=1)

cmd.color ("blue", "resi 19 & chain B")

cmd.select ("Outward", "resi 19 & chain B", merge=1)

cmd.color ("blue", "resi 35 & chain B")

cmd.select ("Outward", "resi 35 & chain B", merge=1)

cmd.color ("blue", "resi 36 & chain B")

cmd.select ("Outward", "resi 36 & chain B", merge=1)

cmd.color ("blue", "resi 37 & chain B")

cmd.select ("Outward", "resi 37 & chain B", merge=1)

cmd.color ("blue", "resi 38 & chain B")

cmd.select ("Outward", "resi 38 & chain B", merge=1)

cmd.color ("blue", "resi 39 & chain B")

cmd.select ("Outward", "resi 39 & chain B", merge=1)

cmd.color ("blue", "resi 44 & chain B")

cmd.select ("Outward", "resi 44 & chain B", merge=1)

cmd.color ("blue", "resi 45 & chain B")

cmd.select ("Outward", "resi 45 & chain B", merge=1)

cmd.color ("blue", "resi 46 & chain B")

cmd.select ("Outward", "resi 46 & chain B", merge=1)

cmd.color ("blue", "resi 47 & chain B")

cmd.select ("Outward", "resi 47 & chain B", merge=1)

cmd.color ("blue", "resi 48 & chain B")

cmd.select ("Outward", "resi 48 & chain B", merge=1)

cmd.color ("blue", "resi 49 & chain B")

cmd.select ("Outward", "resi 49 & chain B", merge=1)

cmd.color ("blue", "resi 50 & chain B")

cmd.select ("Outward", "resi 50 & chain B", merge=1)

cmd.color ("blue", "resi 51 & chain B")

cmd.select ("Outward", "resi 51 & chain B", merge=1)

cmd.color ("blue", "resi 52 & chain B")

cmd.select ("Outward", "resi 52 & chain B", merge=1)

cmd.color ("blue", "resi 53 & chain B")

cmd.select ("Outward", "resi 53 & chain B", merge=1)

cmd.color ("blue", "resi 56 & chain B")

cmd.select ("Outward", "resi 56 & chain B", merge=1)

cmd.color ("blue", "resi 57 & chain B")

cmd.select ("Outward", "resi 57 & chain B", merge=1)

cmd.color ("blue", "resi 58 & chain B")

cmd.select ("Outward", "resi 58 & chain B", merge=1)

cmd.color ("blue", "resi 59 & chain B")

cmd.select ("Outward", "resi 59 & chain B", merge=1)

cmd.color ("blue", "resi 60 & chain B")

cmd.select ("Outward", "resi 60 & chain B", merge=1)

cmd.color ("blue", "resi 61 & chain B")

cmd.select ("Outward", "resi 61 & chain B", merge=1)

cmd.color ("blue", "resi 62 & chain B")

cmd.select ("Outward", "resi 62 & chain B", merge=1)

cmd.color ("blue", "resi 63 & chain B")

cmd.select ("Outward", "resi 63 & chain B", merge=1)

cmd.color ("blue", "resi 64 & chain B")

cmd.select ("Outward", "resi 64 & chain B", merge=1)

cmd.color ("blue", "resi 65 & chain B")

cmd.select ("Outward", "resi 65 & chain B", merge=1)

cmd.color ("blue", "resi 66 & chain B")

cmd.select ("Outward", "resi 66 & chain B", merge=1)

cmd.color ("blue", "resi 67 & chain B")

cmd.select ("Outward", "resi 67 & chain B", merge=1)

cmd.color ("blue", "resi 71 & chain B")

cmd.select ("Outward", "resi 71 & chain B", merge=1)

cmd.color ("blue", "resi 72 & chain B")

cmd.select ("Outward", "resi 72 & chain B", merge=1)

cmd.color ("blue", "resi 73 & chain B")

cmd.select ("Outward", "resi 73 & chain B", merge=1)

cmd.color ("blue", "resi 74 & chain B")

cmd.select ("Outward", "resi 74 & chain B", merge=1)

cmd.color ("blue", "resi 75 & chain B")

cmd.select ("Outward", "resi 75 & chain B", merge=1)

cmd.color ("blue", "resi 76 & chain B")

cmd.select ("Outward", "resi 76 & chain B", merge=1)

cmd.color ("blue", "resi 79 & chain B")

cmd.select ("Outward", "resi 79 & chain B", merge=1)

cmd.color ("blue", "resi 80 & chain B")

cmd.select ("Outward", "resi 80 & chain B", merge=1)

cmd.color ("blue", "resi 81 & chain B")

cmd.select ("Outward", "resi 81 & chain B", merge=1)

cmd.color ("blue", "resi 82 & chain B")

cmd.select ("Outward", "resi 82 & chain B", merge=1)

cmd.color ("blue", "resi 83 & chain B")

cmd.select ("Outward", "resi 83 & chain B", merge=1)

cmd.color ("blue", "resi 91 & chain B")

cmd.select ("Outward", "resi 91 & chain B", merge=1)

cmd.color ("blue", "resi 92 & chain B")

cmd.select ("Outward", "resi 92 & chain B", merge=1)

cmd.color ("blue", "resi 93 & chain B")

cmd.select ("Outward", "resi 93 & chain B", merge=1)

cmd.color ("blue", "resi 94 & chain B")

cmd.select ("Outward", "resi 94 & chain B", merge=1)

cmd.color ("blue", "resi 95 & chain B")

cmd.select ("Outward", "resi 95 & chain B", merge=1)

cmd.color ("blue", "resi 96 & chain B")

cmd.select ("Outward", "resi 96 & chain B", merge=1)

cmd.color ("blue", "resi 97 & chain B")

cmd.select ("Outward", "resi 97 & chain B", merge=1)

cmd.color ("blue", "resi 98 & chain B")

cmd.select ("Outward", "resi 98 & chain B", merge=1)

cmd.color ("blue", "resi 99 & chain B")

cmd.select ("Outward", "resi 99 & chain B", merge=1)

cmd.color ("blue", "resi 100 & chain B")

cmd.select ("Outward", "resi 100 & chain B", merge=1)

cmd.color ("blue", "resi 105 & chain B")

cmd.select ("Outward", "resi 105 & chain B", merge=1)

cmd.color ("blue", "resi 106 & chain B")

cmd.select ("Outward", "resi 106 & chain B", merge=1)

cmd.color ("blue", "resi 107 & chain B")

cmd.select ("Outward", "resi 107 & chain B", merge=1)

cmd.color ("blue", "resi 108 & chain B")

cmd.select ("Outward", "resi 108 & chain B", merge=1)

cmd.color ("blue", "resi 109 & chain B")

cmd.select ("Outward", "resi 109 & chain B", merge=1)

cmd.color ("blue", "resi 110 & chain B")

cmd.select ("Outward", "resi 110 & chain B", merge=1)

cmd.color ("blue", "resi 111 & chain B")

cmd.select ("Outward", "resi 111 & chain B", merge=1)

cmd.color ("blue", "resi 112 & chain B")

cmd.select ("Outward", "resi 112 & chain B", merge=1)

cmd.color ("blue", "resi 113 & chain B")

cmd.select ("Outward", "resi 113 & chain B", merge=1)

cmd.load_cgo( [9.0, -41.695625,55.382256,13.743626, -44.4715, 64.457375, 27.811249, 1, 1,1,0,0,0,1], "axis" )
