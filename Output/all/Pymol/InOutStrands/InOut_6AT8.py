from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6AT8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14 & chain A ")


cmd.select("Astrand1", "resi 39+40+41+42+43+44+45 & chain A ")


cmd.select("Astrand2", "resi 48+49+50+51+52+53+54 & chain A ")


cmd.select("Astrand3", "resi 59+60+61+62+63+64+65 & chain A ")


cmd.select("Astrand4", "resi 70+71+72 & chain A ")


cmd.select("Astrand5", "resi 82+83+84+85+86+87+88+89 & chain A ")


cmd.select("Astrand6", "resi 92+93+94+95+96+97+98 & chain A ")


cmd.select("Astrand7", "resi 105+106+107+108+109+110+111 & chain A ")


cmd.select("Astrand8", "resi 114+115+116+117+118+119+120+121 & chain A ")


cmd.select("Astrand9", "resi 124+125+126+127+128+129+130+131+132 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 6 & chain A")

cmd.select ("Inward", "resi 6 & chain A", merge=1)

cmd.color ("blue", "resi 7 & chain A")

cmd.select ("Outward", "resi 7 & chain A", merge=1)

cmd.color ("red", "resi 8 & chain A")

cmd.select ("Inward", "resi 8 & chain A", merge=1)

cmd.color ("red", "resi 9 & chain A")

cmd.select ("Inward", "resi 9 & chain A", merge=1)

cmd.color ("blue", "resi 10 & chain A")

cmd.select ("Outward", "resi 10 & chain A", merge=1)

cmd.color ("red", "resi 11 & chain A")

cmd.select ("Inward", "resi 11 & chain A", merge=1)

cmd.color ("red", "resi 12 & chain A")

cmd.select ("Inward", "resi 12 & chain A", merge=1)

cmd.color ("red", "resi 13 & chain A")

cmd.select ("Inward", "resi 13 & chain A", merge=1)

cmd.color ("blue", "resi 14 & chain A")

cmd.select ("Outward", "resi 14 & chain A", merge=1)

cmd.color ("blue", "resi 39 & chain A")

cmd.select ("Outward", "resi 39 & chain A", merge=1)

cmd.color ("red", "resi 40 & chain A")

cmd.select ("Inward", "resi 40 & chain A", merge=1)

cmd.color ("blue", "resi 41 & chain A")

cmd.select ("Outward", "resi 41 & chain A", merge=1)

cmd.color ("red", "resi 42 & chain A")

cmd.select ("Inward", "resi 42 & chain A", merge=1)

cmd.color ("blue", "resi 43 & chain A")

cmd.select ("Outward", "resi 43 & chain A", merge=1)

cmd.color ("red", "resi 44 & chain A")

cmd.select ("Inward", "resi 44 & chain A", merge=1)

cmd.color ("blue", "resi 45 & chain A")

cmd.select ("Outward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("red", "resi 49 & chain A")

cmd.select ("Inward", "resi 49 & chain A", merge=1)

cmd.color ("blue", "resi 50 & chain A")

cmd.select ("Outward", "resi 50 & chain A", merge=1)

cmd.color ("red", "resi 51 & chain A")

cmd.select ("Inward", "resi 51 & chain A", merge=1)

cmd.color ("blue", "resi 52 & chain A")

cmd.select ("Outward", "resi 52 & chain A", merge=1)

cmd.color ("red", "resi 53 & chain A")

cmd.select ("Inward", "resi 53 & chain A", merge=1)

cmd.color ("red", "resi 54 & chain A")

cmd.select ("Inward", "resi 54 & chain A", merge=1)

cmd.color ("blue", "resi 59 & chain A")

cmd.select ("Outward", "resi 59 & chain A", merge=1)

cmd.color ("red", "resi 60 & chain A")

cmd.select ("Inward", "resi 60 & chain A", merge=1)

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("red", "resi 62 & chain A")

cmd.select ("Inward", "resi 62 & chain A", merge=1)

cmd.color ("blue", "resi 63 & chain A")

cmd.select ("Outward", "resi 63 & chain A", merge=1)

cmd.color ("red", "resi 64 & chain A")

cmd.select ("Inward", "resi 64 & chain A", merge=1)

cmd.color ("blue", "resi 65 & chain A")

cmd.select ("Outward", "resi 65 & chain A", merge=1)

cmd.color ("red", "resi 70 & chain A")

cmd.select ("Inward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.color ("red", "resi 72 & chain A")

cmd.select ("Inward", "resi 72 & chain A", merge=1)

cmd.color ("red", "resi 82 & chain A")

cmd.select ("Inward", "resi 82 & chain A", merge=1)

cmd.color ("red", "resi 83 & chain A")

cmd.select ("Inward", "resi 83 & chain A", merge=1)

cmd.color ("red", "resi 84 & chain A")

cmd.select ("Inward", "resi 84 & chain A", merge=1)

cmd.color ("blue", "resi 85 & chain A")

cmd.select ("Outward", "resi 85 & chain A", merge=1)

cmd.color ("red", "resi 86 & chain A")

cmd.select ("Inward", "resi 86 & chain A", merge=1)

cmd.color ("blue", "resi 87 & chain A")

cmd.select ("Outward", "resi 87 & chain A", merge=1)

cmd.color ("blue", "resi 88 & chain A")

cmd.select ("Outward", "resi 88 & chain A", merge=1)

cmd.color ("red", "resi 89 & chain A")

cmd.select ("Inward", "resi 89 & chain A", merge=1)

cmd.color ("blue", "resi 92 & chain A")

cmd.select ("Outward", "resi 92 & chain A", merge=1)

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

cmd.color ("blue", "resi 98 & chain A")

cmd.select ("Outward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("red", "resi 106 & chain A")

cmd.select ("Inward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

cmd.color ("red", "resi 111 & chain A")

cmd.select ("Inward", "resi 111 & chain A", merge=1)

cmd.color ("blue", "resi 114 & chain A")

cmd.select ("Outward", "resi 114 & chain A", merge=1)

cmd.color ("red", "resi 115 & chain A")

cmd.select ("Inward", "resi 115 & chain A", merge=1)

cmd.color ("blue", "resi 116 & chain A")

cmd.select ("Outward", "resi 116 & chain A", merge=1)

cmd.color ("red", "resi 117 & chain A")

cmd.select ("Inward", "resi 117 & chain A", merge=1)

cmd.color ("blue", "resi 118 & chain A")

cmd.select ("Outward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("blue", "resi 120 & chain A")

cmd.select ("Outward", "resi 120 & chain A", merge=1)

cmd.color ("red", "resi 121 & chain A")

cmd.select ("Inward", "resi 121 & chain A", merge=1)

cmd.color ("red", "resi 124 & chain A")

cmd.select ("Inward", "resi 124 & chain A", merge=1)

cmd.color ("blue", "resi 125 & chain A")

cmd.select ("Outward", "resi 125 & chain A", merge=1)

cmd.color ("red", "resi 126 & chain A")

cmd.select ("Inward", "resi 126 & chain A", merge=1)

cmd.color ("blue", "resi 127 & chain A")

cmd.select ("Outward", "resi 127 & chain A", merge=1)

cmd.color ("red", "resi 128 & chain A")

cmd.select ("Inward", "resi 128 & chain A", merge=1)

cmd.color ("blue", "resi 129 & chain A")

cmd.select ("Outward", "resi 129 & chain A", merge=1)

cmd.color ("red", "resi 130 & chain A")

cmd.select ("Inward", "resi 130 & chain A", merge=1)

cmd.color ("blue", "resi 131 & chain A")

cmd.select ("Outward", "resi 131 & chain A", merge=1)

cmd.color ("blue", "resi 132 & chain A")

cmd.select ("Outward", "resi 132 & chain A", merge=1)

cmd.load_cgo( [9.0, -2.4538748,1.49325,20.746874, -2.4538748, 1.49325, 20.746874, 1, 1,1,0,0,0,1], "axis" )