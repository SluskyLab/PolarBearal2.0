from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4R0B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17+18+19+20+21+22+23+24+25+26 & chain A ")


cmd.select("Astrand1", "resi 149+150+151+152+42+43+44+45+46+47+48 & chain A ")


cmd.select("Astrand2", "resi 54+55+56+57+58+59+60+61 & chain A ")


cmd.select("Astrand3", "resi 66+67+68+69+70+71+72+73+74+75 & chain A ")


cmd.select("Astrand4", "resi 81+82+83+84+85+86 & chain A ")


cmd.select("Astrand5", "resi 89+90+91+92+93+94+95+96+97 & chain A ")


cmd.select("Astrand6", "resi 102+103+104+105+106+107+108+109 & chain A ")


cmd.select("Astrand7", "resi 116+117+118+119+120+121+122+123 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 17 & chain A")

cmd.select ("Outward", "resi 17 & chain A", merge=1)

cmd.color ("blue", "resi 18 & chain A")

cmd.select ("Outward", "resi 18 & chain A", merge=1)

cmd.color ("blue", "resi 19 & chain A")

cmd.select ("Outward", "resi 19 & chain A", merge=1)

cmd.color ("blue", "resi 20 & chain A")

cmd.select ("Outward", "resi 20 & chain A", merge=1)

cmd.color ("blue", "resi 21 & chain A")

cmd.select ("Outward", "resi 21 & chain A", merge=1)

cmd.color ("blue", "resi 22 & chain A")

cmd.select ("Outward", "resi 22 & chain A", merge=1)

cmd.color ("blue", "resi 23 & chain A")

cmd.select ("Outward", "resi 23 & chain A", merge=1)

cmd.color ("blue", "resi 24 & chain A")

cmd.select ("Outward", "resi 24 & chain A", merge=1)

cmd.color ("blue", "resi 25 & chain A")

cmd.select ("Outward", "resi 25 & chain A", merge=1)

cmd.color ("blue", "resi 26 & chain A")

cmd.select ("Outward", "resi 26 & chain A", merge=1)

cmd.color ("blue", "resi 149 & chain A")

cmd.select ("Outward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("blue", "resi 151 & chain A")

cmd.select ("Outward", "resi 151 & chain A", merge=1)

cmd.color ("blue", "resi 152 & chain A")

cmd.select ("Outward", "resi 152 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("blue", "resi 43 & chain A")

cmd.select ("Outward", "resi 43 & chain A", merge=1)

cmd.color ("blue", "resi 44 & chain A")

cmd.select ("Outward", "resi 44 & chain A", merge=1)

cmd.color ("blue", "resi 45 & chain A")

cmd.select ("Outward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 46 & chain A")

cmd.select ("Outward", "resi 46 & chain A", merge=1)

cmd.color ("blue", "resi 47 & chain A")

cmd.select ("Outward", "resi 47 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("blue", "resi 54 & chain A")

cmd.select ("Outward", "resi 54 & chain A", merge=1)

cmd.color ("blue", "resi 55 & chain A")

cmd.select ("Outward", "resi 55 & chain A", merge=1)

cmd.color ("blue", "resi 56 & chain A")

cmd.select ("Outward", "resi 56 & chain A", merge=1)

cmd.color ("blue", "resi 57 & chain A")

cmd.select ("Outward", "resi 57 & chain A", merge=1)

cmd.color ("blue", "resi 58 & chain A")

cmd.select ("Outward", "resi 58 & chain A", merge=1)

cmd.color ("blue", "resi 59 & chain A")

cmd.select ("Outward", "resi 59 & chain A", merge=1)

cmd.color ("blue", "resi 60 & chain A")

cmd.select ("Outward", "resi 60 & chain A", merge=1)

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("blue", "resi 66 & chain A")

cmd.select ("Outward", "resi 66 & chain A", merge=1)

cmd.color ("blue", "resi 67 & chain A")

cmd.select ("Outward", "resi 67 & chain A", merge=1)

cmd.color ("blue", "resi 68 & chain A")

cmd.select ("Outward", "resi 68 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

cmd.color ("blue", "resi 70 & chain A")

cmd.select ("Outward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.color ("blue", "resi 72 & chain A")

cmd.select ("Outward", "resi 72 & chain A", merge=1)

cmd.color ("blue", "resi 73 & chain A")

cmd.select ("Outward", "resi 73 & chain A", merge=1)

cmd.color ("blue", "resi 74 & chain A")

cmd.select ("Outward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("blue", "resi 81 & chain A")

cmd.select ("Outward", "resi 81 & chain A", merge=1)

cmd.color ("blue", "resi 82 & chain A")

cmd.select ("Outward", "resi 82 & chain A", merge=1)

cmd.color ("blue", "resi 83 & chain A")

cmd.select ("Outward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 84 & chain A")

cmd.select ("Outward", "resi 84 & chain A", merge=1)

cmd.color ("blue", "resi 85 & chain A")

cmd.select ("Outward", "resi 85 & chain A", merge=1)

cmd.color ("blue", "resi 86 & chain A")

cmd.select ("Outward", "resi 86 & chain A", merge=1)

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

cmd.color ("blue", "resi 102 & chain A")

cmd.select ("Outward", "resi 102 & chain A", merge=1)

cmd.color ("blue", "resi 103 & chain A")

cmd.select ("Outward", "resi 103 & chain A", merge=1)

cmd.color ("blue", "resi 104 & chain A")

cmd.select ("Outward", "resi 104 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

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

cmd.color ("blue", "resi 121 & chain A")

cmd.select ("Outward", "resi 121 & chain A", merge=1)

cmd.color ("blue", "resi 122 & chain A")

cmd.select ("Outward", "resi 122 & chain A", merge=1)

cmd.color ("blue", "resi 123 & chain A")

cmd.select ("Outward", "resi 123 & chain A", merge=1)

cmd.load_cgo( [9.0, -15.553125,28.892626,-2.1815002, -6.925125, 16.143, -9.327999, 1, 1,1,0,0,0,1], "axis" )
