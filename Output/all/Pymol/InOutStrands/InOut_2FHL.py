from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8+9+10+11+12 & chain A ")


cmd.select("Astrand1", "resi 17+18+19+20 & chain A ")


cmd.select("Astrand2", "resi 28+29+30+31+32+33+34 & chain A ")


cmd.select("Astrand3", "resi 47+48+49+50+51+52+53 & chain A ")


cmd.select("Astrand4", "resi 61+62+63+64+65+66+67 & chain A ")


cmd.select("Astrand5", "resi 74+75+76+77+78+79+80+81+82+83 & chain A ")


cmd.select("Astrand6", "resi 89+90+91+92+93+94+95+96+97+98 & chain A ")


cmd.select("Astrand7", "resi 111+112+113+114+115+116+117+118+119+120 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 8 & chain A")

cmd.select ("Outward", "resi 8 & chain A", merge=1)

cmd.color ("blue", "resi 9 & chain A")

cmd.select ("Outward", "resi 9 & chain A", merge=1)

cmd.color ("blue", "resi 10 & chain A")

cmd.select ("Outward", "resi 10 & chain A", merge=1)

cmd.color ("blue", "resi 11 & chain A")

cmd.select ("Outward", "resi 11 & chain A", merge=1)

cmd.color ("blue", "resi 12 & chain A")

cmd.select ("Outward", "resi 12 & chain A", merge=1)

cmd.color ("blue", "resi 17 & chain A")

cmd.select ("Outward", "resi 17 & chain A", merge=1)

cmd.color ("blue", "resi 18 & chain A")

cmd.select ("Outward", "resi 18 & chain A", merge=1)

cmd.color ("blue", "resi 19 & chain A")

cmd.select ("Outward", "resi 19 & chain A", merge=1)

cmd.color ("blue", "resi 20 & chain A")

cmd.select ("Outward", "resi 20 & chain A", merge=1)

cmd.color ("blue", "resi 28 & chain A")

cmd.select ("Outward", "resi 28 & chain A", merge=1)

cmd.color ("blue", "resi 29 & chain A")

cmd.select ("Outward", "resi 29 & chain A", merge=1)

cmd.color ("blue", "resi 30 & chain A")

cmd.select ("Outward", "resi 30 & chain A", merge=1)

cmd.color ("blue", "resi 31 & chain A")

cmd.select ("Outward", "resi 31 & chain A", merge=1)

cmd.color ("blue", "resi 32 & chain A")

cmd.select ("Outward", "resi 32 & chain A", merge=1)

cmd.color ("blue", "resi 33 & chain A")

cmd.select ("Outward", "resi 33 & chain A", merge=1)

cmd.color ("blue", "resi 34 & chain A")

cmd.select ("Outward", "resi 34 & chain A", merge=1)

cmd.color ("blue", "resi 47 & chain A")

cmd.select ("Outward", "resi 47 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("blue", "resi 49 & chain A")

cmd.select ("Outward", "resi 49 & chain A", merge=1)

cmd.color ("blue", "resi 50 & chain A")

cmd.select ("Outward", "resi 50 & chain A", merge=1)

cmd.color ("blue", "resi 51 & chain A")

cmd.select ("Outward", "resi 51 & chain A", merge=1)

cmd.color ("blue", "resi 52 & chain A")

cmd.select ("Outward", "resi 52 & chain A", merge=1)

cmd.color ("blue", "resi 53 & chain A")

cmd.select ("Outward", "resi 53 & chain A", merge=1)

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("blue", "resi 62 & chain A")

cmd.select ("Outward", "resi 62 & chain A", merge=1)

cmd.color ("blue", "resi 63 & chain A")

cmd.select ("Outward", "resi 63 & chain A", merge=1)

cmd.color ("blue", "resi 64 & chain A")

cmd.select ("Outward", "resi 64 & chain A", merge=1)

cmd.color ("blue", "resi 65 & chain A")

cmd.select ("Outward", "resi 65 & chain A", merge=1)

cmd.color ("blue", "resi 66 & chain A")

cmd.select ("Outward", "resi 66 & chain A", merge=1)

cmd.color ("blue", "resi 67 & chain A")

cmd.select ("Outward", "resi 67 & chain A", merge=1)

cmd.color ("blue", "resi 74 & chain A")

cmd.select ("Outward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("blue", "resi 76 & chain A")

cmd.select ("Outward", "resi 76 & chain A", merge=1)

cmd.color ("blue", "resi 77 & chain A")

cmd.select ("Outward", "resi 77 & chain A", merge=1)

cmd.color ("blue", "resi 78 & chain A")

cmd.select ("Outward", "resi 78 & chain A", merge=1)

cmd.color ("blue", "resi 79 & chain A")

cmd.select ("Outward", "resi 79 & chain A", merge=1)

cmd.color ("blue", "resi 80 & chain A")

cmd.select ("Outward", "resi 80 & chain A", merge=1)

cmd.color ("blue", "resi 81 & chain A")

cmd.select ("Outward", "resi 81 & chain A", merge=1)

cmd.color ("blue", "resi 82 & chain A")

cmd.select ("Outward", "resi 82 & chain A", merge=1)

cmd.color ("blue", "resi 83 & chain A")

cmd.select ("Outward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 89 & chain A")

cmd.select ("Outward", "resi 89 & chain A", merge=1)

cmd.color ("blue", "resi 90 & chain A")

cmd.select ("Outward", "resi 90 & chain A", merge=1)

cmd.color ("blue", "resi 91 & chain A")

cmd.select ("Outward", "resi 91 & chain A", merge=1)

cmd.color ("blue", "resi 92 & chain A")

cmd.select ("Outward", "resi 92 & chain A", merge=1)

cmd.color ("blue", "resi 93 & chain A")

cmd.select ("Outward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("blue", "resi 95 & chain A")

cmd.select ("Outward", "resi 95 & chain A", merge=1)

cmd.color ("blue", "resi 96 & chain A")

cmd.select ("Outward", "resi 96 & chain A", merge=1)

cmd.color ("blue", "resi 97 & chain A")

cmd.select ("Outward", "resi 97 & chain A", merge=1)

cmd.color ("blue", "resi 98 & chain A")

cmd.select ("Outward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("blue", "resi 112 & chain A")

cmd.select ("Outward", "resi 112 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("blue", "resi 114 & chain A")

cmd.select ("Outward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 115 & chain A")

cmd.select ("Outward", "resi 115 & chain A", merge=1)

cmd.color ("blue", "resi 116 & chain A")

cmd.select ("Outward", "resi 116 & chain A", merge=1)

cmd.color ("blue", "resi 117 & chain A")

cmd.select ("Outward", "resi 117 & chain A", merge=1)

cmd.color ("blue", "resi 118 & chain A")

cmd.select ("Outward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("blue", "resi 120 & chain A")

cmd.select ("Outward", "resi 120 & chain A", merge=1)

cmd.load_cgo( [9.0, 8.944374,48.37063,16.502625, 24.072124, 53.524624, 12.434626, 1, 1,1,0,0,0,1], "axis" )
