from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ALO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand4", "resi 34+35+36+37+38+39+40+41+42+43 & chain A ")


cmd.select("Astrand12", "resi 128+129+130+131+132+133+134+135+136+137+138+139+140+141+142 & chain A ")


cmd.select("Astrand11", "resi 115+116+117+118+119+120+121+122+123+124 & chain A ")


cmd.select("Astrand10", "resi 100+101+102+103+104+105+106+107+108+109+110 & chain A ")


cmd.select("Astrand9", "resi 92+93+94+95+96+97 & chain A ")


cmd.select("Astrand7", "resi 62+63+64+65+66+67+68+69+70 & chain A ")


cmd.select("Astrand8", "resi 75+76+77+78+79+80+81+82+83+84 & chain A ")


cmd.select("Astrand6", "resi 165+166+167+168+169+53+54+55+56+57+58 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 34 & chain A")

cmd.select ("Outward", "resi 34 & chain A", merge=1)

cmd.color ("red", "resi 35 & chain A")

cmd.select ("Inward", "resi 35 & chain A", merge=1)

cmd.color ("blue", "resi 36 & chain A")

cmd.select ("Outward", "resi 36 & chain A", merge=1)

cmd.color ("blue", "resi 37 & chain A")

cmd.select ("Outward", "resi 37 & chain A", merge=1)

cmd.color ("red", "resi 38 & chain A")

cmd.select ("Inward", "resi 38 & chain A", merge=1)

cmd.color ("blue", "resi 39 & chain A")

cmd.select ("Outward", "resi 39 & chain A", merge=1)

cmd.color ("red", "resi 40 & chain A")

cmd.select ("Inward", "resi 40 & chain A", merge=1)

cmd.color ("blue", "resi 41 & chain A")

cmd.select ("Outward", "resi 41 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("red", "resi 43 & chain A")

cmd.select ("Inward", "resi 43 & chain A", merge=1)

cmd.color ("red", "resi 128 & chain A")

cmd.select ("Inward", "resi 128 & chain A", merge=1)

cmd.color ("blue", "resi 129 & chain A")

cmd.select ("Outward", "resi 129 & chain A", merge=1)

cmd.color ("red", "resi 130 & chain A")

cmd.select ("Inward", "resi 130 & chain A", merge=1)

cmd.color ("blue", "resi 131 & chain A")

cmd.select ("Outward", "resi 131 & chain A", merge=1)

cmd.color ("red", "resi 132 & chain A")

cmd.select ("Inward", "resi 132 & chain A", merge=1)

cmd.color ("blue", "resi 133 & chain A")

cmd.select ("Outward", "resi 133 & chain A", merge=1)

cmd.color ("red", "resi 134 & chain A")

cmd.select ("Inward", "resi 134 & chain A", merge=1)

cmd.color ("blue", "resi 135 & chain A")

cmd.select ("Outward", "resi 135 & chain A", merge=1)

cmd.color ("red", "resi 136 & chain A")

cmd.select ("Inward", "resi 136 & chain A", merge=1)

cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

cmd.color ("blue", "resi 138 & chain A")

cmd.select ("Outward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("red", "resi 140 & chain A")

cmd.select ("Inward", "resi 140 & chain A", merge=1)

cmd.color ("red", "resi 141 & chain A")

cmd.select ("Inward", "resi 141 & chain A", merge=1)

cmd.color ("blue", "resi 142 & chain A")

cmd.select ("Outward", "resi 142 & chain A", merge=1)

cmd.color ("blue", "resi 115 & chain A")

cmd.select ("Outward", "resi 115 & chain A", merge=1)

cmd.color ("red", "resi 116 & chain A")

cmd.select ("Inward", "resi 116 & chain A", merge=1)

cmd.color ("blue", "resi 117 & chain A")

cmd.select ("Outward", "resi 117 & chain A", merge=1)

cmd.color ("red", "resi 118 & chain A")

cmd.select ("Inward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("red", "resi 120 & chain A")

cmd.select ("Inward", "resi 120 & chain A", merge=1)

cmd.color ("blue", "resi 121 & chain A")

cmd.select ("Outward", "resi 121 & chain A", merge=1)

cmd.color ("red", "resi 122 & chain A")

cmd.select ("Inward", "resi 122 & chain A", merge=1)

cmd.color ("red", "resi 123 & chain A")

cmd.select ("Inward", "resi 123 & chain A", merge=1)

cmd.color ("blue", "resi 124 & chain A")

cmd.select ("Outward", "resi 124 & chain A", merge=1)

cmd.color ("red", "resi 100 & chain A")

cmd.select ("Inward", "resi 100 & chain A", merge=1)

cmd.color ("red", "resi 101 & chain A")

cmd.select ("Inward", "resi 101 & chain A", merge=1)

cmd.color ("blue", "resi 102 & chain A")

cmd.select ("Outward", "resi 102 & chain A", merge=1)

cmd.color ("red", "resi 103 & chain A")

cmd.select ("Inward", "resi 103 & chain A", merge=1)

cmd.color ("blue", "resi 104 & chain A")

cmd.select ("Outward", "resi 104 & chain A", merge=1)

cmd.color ("red", "resi 105 & chain A")

cmd.select ("Inward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("red", "resi 108 & chain A")

cmd.select ("Inward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("red", "resi 110 & chain A")

cmd.select ("Inward", "resi 110 & chain A", merge=1)

cmd.color ("red", "resi 92 & chain A")

cmd.select ("Inward", "resi 92 & chain A", merge=1)

cmd.color ("red", "resi 93 & chain A")

cmd.select ("Inward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("red", "resi 95 & chain A")

cmd.select ("Inward", "resi 95 & chain A", merge=1)

cmd.color ("blue", "resi 96 & chain A")

cmd.select ("Outward", "resi 96 & chain A", merge=1)

cmd.color ("red", "resi 97 & chain A")

cmd.select ("Inward", "resi 97 & chain A", merge=1)

cmd.color ("blue", "resi 62 & chain A")

cmd.select ("Outward", "resi 62 & chain A", merge=1)

cmd.color ("red", "resi 63 & chain A")

cmd.select ("Inward", "resi 63 & chain A", merge=1)

cmd.color ("blue", "resi 64 & chain A")

cmd.select ("Outward", "resi 64 & chain A", merge=1)

cmd.color ("red", "resi 65 & chain A")

cmd.select ("Inward", "resi 65 & chain A", merge=1)

cmd.color ("blue", "resi 66 & chain A")

cmd.select ("Outward", "resi 66 & chain A", merge=1)

cmd.color ("red", "resi 67 & chain A")

cmd.select ("Inward", "resi 67 & chain A", merge=1)

cmd.color ("blue", "resi 68 & chain A")

cmd.select ("Outward", "resi 68 & chain A", merge=1)

cmd.color ("red", "resi 69 & chain A")

cmd.select ("Inward", "resi 69 & chain A", merge=1)

cmd.color ("blue", "resi 70 & chain A")

cmd.select ("Outward", "resi 70 & chain A", merge=1)

cmd.color ("red", "resi 75 & chain A")

cmd.select ("Inward", "resi 75 & chain A", merge=1)

cmd.color ("blue", "resi 76 & chain A")

cmd.select ("Outward", "resi 76 & chain A", merge=1)

cmd.color ("red", "resi 77 & chain A")

cmd.select ("Inward", "resi 77 & chain A", merge=1)

cmd.color ("blue", "resi 78 & chain A")

cmd.select ("Outward", "resi 78 & chain A", merge=1)

cmd.color ("red", "resi 79 & chain A")

cmd.select ("Inward", "resi 79 & chain A", merge=1)

cmd.color ("blue", "resi 80 & chain A")

cmd.select ("Outward", "resi 80 & chain A", merge=1)

cmd.color ("red", "resi 81 & chain A")

cmd.select ("Inward", "resi 81 & chain A", merge=1)

cmd.color ("blue", "resi 82 & chain A")

cmd.select ("Outward", "resi 82 & chain A", merge=1)

cmd.color ("red", "resi 83 & chain A")

cmd.select ("Inward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 84 & chain A")

cmd.select ("Outward", "resi 84 & chain A", merge=1)

cmd.color ("red", "resi 165 & chain A")

cmd.select ("Inward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 166 & chain A")

cmd.select ("Outward", "resi 166 & chain A", merge=1)

cmd.color ("red", "resi 167 & chain A")

cmd.select ("Inward", "resi 167 & chain A", merge=1)

cmd.color ("red", "resi 168 & chain A")

cmd.select ("Inward", "resi 168 & chain A", merge=1)

cmd.color ("blue", "resi 169 & chain A")

cmd.select ("Outward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 53 & chain A")

cmd.select ("Outward", "resi 53 & chain A", merge=1)

cmd.color ("red", "resi 54 & chain A")

cmd.select ("Inward", "resi 54 & chain A", merge=1)

cmd.color ("blue", "resi 55 & chain A")

cmd.select ("Outward", "resi 55 & chain A", merge=1)

cmd.color ("red", "resi 56 & chain A")

cmd.select ("Inward", "resi 56 & chain A", merge=1)

cmd.color ("blue", "resi 57 & chain A")

cmd.select ("Outward", "resi 57 & chain A", merge=1)

cmd.color ("red", "resi 58 & chain A")

cmd.select ("Inward", "resi 58 & chain A", merge=1)

cmd.load_cgo( [9.0, -5.419,1.850625,-2.9759998, -5.419, 1.850625, -2.9759998, 1, 1,1,0,0,0,1], "axis" )
