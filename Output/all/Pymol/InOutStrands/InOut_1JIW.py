from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JIW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Istrand0", "resi 13+14+15+16+17+18+19 & chain I ")


cmd.select("Istrand1", "resi 25+26+27+28+29+30+31+32+33+34+35 & chain I ")


cmd.select("Istrand2", "resi 40+41+42+43+44+45 & chain I ")


cmd.select("Istrand3", "resi 60+61+62+63+64 & chain I ")


cmd.select("Istrand4", "resi 67+68+69+70+71 & chain I ")


cmd.select("Istrand5", "resi 77+78+79+80+81+82+83+84+85 & chain I ")


cmd.select("Istrand6", "resi 88+89+90+91+92 & chain I ")


cmd.select("Istrand7", "resi 98+99+100+101+102+103 & chain I ")


cmd.select("barrel", "Istrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 13 & chain I")

cmd.select ("Inward", "resi 13 & chain I", merge=1)

cmd.color ("blue", "resi 14 & chain I")

cmd.select ("Outward", "resi 14 & chain I", merge=1)

cmd.color ("red", "resi 15 & chain I")

cmd.select ("Inward", "resi 15 & chain I", merge=1)

cmd.color ("blue", "resi 16 & chain I")

cmd.select ("Outward", "resi 16 & chain I", merge=1)

cmd.color ("red", "resi 17 & chain I")

cmd.select ("Inward", "resi 17 & chain I", merge=1)

cmd.color ("blue", "resi 18 & chain I")

cmd.select ("Outward", "resi 18 & chain I", merge=1)

cmd.color ("blue", "resi 19 & chain I")

cmd.select ("Outward", "resi 19 & chain I", merge=1)

cmd.color ("blue", "resi 25 & chain I")

cmd.select ("Outward", "resi 25 & chain I", merge=1)

cmd.color ("red", "resi 26 & chain I")

cmd.select ("Inward", "resi 26 & chain I", merge=1)

cmd.color ("blue", "resi 27 & chain I")

cmd.select ("Outward", "resi 27 & chain I", merge=1)

cmd.color ("red", "resi 28 & chain I")

cmd.select ("Inward", "resi 28 & chain I", merge=1)

cmd.color ("blue", "resi 29 & chain I")

cmd.select ("Outward", "resi 29 & chain I", merge=1)

cmd.color ("red", "resi 30 & chain I")

cmd.select ("Inward", "resi 30 & chain I", merge=1)

cmd.color ("blue", "resi 31 & chain I")

cmd.select ("Outward", "resi 31 & chain I", merge=1)

cmd.color ("blue", "resi 32 & chain I")

cmd.select ("Outward", "resi 32 & chain I", merge=1)

cmd.color ("blue", "resi 33 & chain I")

cmd.select ("Outward", "resi 33 & chain I", merge=1)

cmd.color ("blue", "resi 34 & chain I")

cmd.select ("Outward", "resi 34 & chain I", merge=1)

cmd.color ("red", "resi 35 & chain I")

cmd.select ("Inward", "resi 35 & chain I", merge=1)

cmd.color ("blue", "resi 40 & chain I")

cmd.select ("Outward", "resi 40 & chain I", merge=1)

cmd.color ("red", "resi 41 & chain I")

cmd.select ("Inward", "resi 41 & chain I", merge=1)

cmd.color ("blue", "resi 42 & chain I")

cmd.select ("Outward", "resi 42 & chain I", merge=1)

cmd.color ("red", "resi 43 & chain I")

cmd.select ("Inward", "resi 43 & chain I", merge=1)

cmd.color ("red", "resi 44 & chain I")

cmd.select ("Inward", "resi 44 & chain I", merge=1)

cmd.color ("red", "resi 45 & chain I")

cmd.select ("Inward", "resi 45 & chain I", merge=1)

cmd.color ("blue", "resi 60 & chain I")

cmd.select ("Outward", "resi 60 & chain I", merge=1)

cmd.color ("red", "resi 61 & chain I")

cmd.select ("Inward", "resi 61 & chain I", merge=1)

cmd.color ("blue", "resi 62 & chain I")

cmd.select ("Outward", "resi 62 & chain I", merge=1)

cmd.color ("blue", "resi 63 & chain I")

cmd.select ("Outward", "resi 63 & chain I", merge=1)

cmd.color ("red", "resi 64 & chain I")

cmd.select ("Inward", "resi 64 & chain I", merge=1)

cmd.color ("blue", "resi 67 & chain I")

cmd.select ("Outward", "resi 67 & chain I", merge=1)

cmd.color ("red", "resi 68 & chain I")

cmd.select ("Inward", "resi 68 & chain I", merge=1)

cmd.color ("blue", "resi 69 & chain I")

cmd.select ("Outward", "resi 69 & chain I", merge=1)

cmd.color ("red", "resi 70 & chain I")

cmd.select ("Inward", "resi 70 & chain I", merge=1)

cmd.color ("red", "resi 71 & chain I")

cmd.select ("Inward", "resi 71 & chain I", merge=1)

cmd.color ("blue", "resi 77 & chain I")

cmd.select ("Outward", "resi 77 & chain I", merge=1)

cmd.color ("red", "resi 78 & chain I")

cmd.select ("Inward", "resi 78 & chain I", merge=1)

cmd.color ("red", "resi 79 & chain I")

cmd.select ("Inward", "resi 79 & chain I", merge=1)

cmd.color ("blue", "resi 80 & chain I")

cmd.select ("Outward", "resi 80 & chain I", merge=1)

cmd.color ("red", "resi 81 & chain I")

cmd.select ("Inward", "resi 81 & chain I", merge=1)

cmd.color ("blue", "resi 82 & chain I")

cmd.select ("Outward", "resi 82 & chain I", merge=1)

cmd.color ("blue", "resi 83 & chain I")

cmd.select ("Outward", "resi 83 & chain I", merge=1)

cmd.color ("red", "resi 84 & chain I")

cmd.select ("Inward", "resi 84 & chain I", merge=1)

cmd.color ("blue", "resi 85 & chain I")

cmd.select ("Outward", "resi 85 & chain I", merge=1)

cmd.color ("blue", "resi 88 & chain I")

cmd.select ("Outward", "resi 88 & chain I", merge=1)

cmd.color ("red", "resi 89 & chain I")

cmd.select ("Inward", "resi 89 & chain I", merge=1)

cmd.color ("blue", "resi 90 & chain I")

cmd.select ("Outward", "resi 90 & chain I", merge=1)

cmd.color ("red", "resi 91 & chain I")

cmd.select ("Inward", "resi 91 & chain I", merge=1)

cmd.color ("blue", "resi 92 & chain I")

cmd.select ("Outward", "resi 92 & chain I", merge=1)

cmd.color ("blue", "resi 98 & chain I")

cmd.select ("Outward", "resi 98 & chain I", merge=1)

cmd.color ("red", "resi 99 & chain I")

cmd.select ("Inward", "resi 99 & chain I", merge=1)

cmd.color ("blue", "resi 100 & chain I")

cmd.select ("Outward", "resi 100 & chain I", merge=1)

cmd.color ("red", "resi 101 & chain I")

cmd.select ("Inward", "resi 101 & chain I", merge=1)

cmd.color ("blue", "resi 102 & chain I")

cmd.select ("Outward", "resi 102 & chain I", merge=1)

cmd.color ("blue", "resi 103 & chain I")

cmd.select ("Outward", "resi 103 & chain I", merge=1)

cmd.load_cgo( [9.0, 44.895874,49.86,-27.770126, 44.895874, 49.86, -27.770126, 1, 1,1,0,0,0,1], "axis" )
