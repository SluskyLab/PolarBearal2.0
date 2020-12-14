from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GE1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22+23+24+25+26+27+28+29+30 & chain A ")


cmd.select("Astrand7", "resi 129+130+131+132+133+134+135+136+137+138+139 & chain A ")


cmd.select("Astrand6", "resi 119+120+121+122+123+124+125+126 & chain A ")


cmd.select("Astrand5", "resi 101+102+103+104+105+106+107+108+109+110+111+112+113+114 & chain A ")


cmd.select("Astrand4", "resi 87+88+89+90+91+92+93+94+95 & chain A ")


cmd.select("Astrand3", "resi 68+69+70+71+72+73+74+75+76+77 & chain A ")


cmd.select("Astrand2", "resi 54+55+56+57+58+59+60+61+62+63 & chain A ")


cmd.select("Astrand1", "resi 42+43+44+45+46+47+48+49 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 22 & chain A")

cmd.select ("Outward", "resi 22 & chain A", merge=1)

cmd.color ("red", "resi 23 & chain A")

cmd.select ("Inward", "resi 23 & chain A", merge=1)

cmd.color ("blue", "resi 24 & chain A")

cmd.select ("Outward", "resi 24 & chain A", merge=1)

cmd.color ("red", "resi 25 & chain A")

cmd.select ("Inward", "resi 25 & chain A", merge=1)

cmd.color ("red", "resi 26 & chain A")

cmd.select ("Inward", "resi 26 & chain A", merge=1)

cmd.color ("blue", "resi 27 & chain A")

cmd.select ("Outward", "resi 27 & chain A", merge=1)

cmd.color ("red", "resi 28 & chain A")

cmd.select ("Inward", "resi 28 & chain A", merge=1)

cmd.color ("blue", "resi 29 & chain A")

cmd.select ("Outward", "resi 29 & chain A", merge=1)

cmd.color ("red", "resi 30 & chain A")

cmd.select ("Inward", "resi 30 & chain A", merge=1)

cmd.color ("red", "resi 129 & chain A")

cmd.select ("Inward", "resi 129 & chain A", merge=1)

cmd.color ("blue", "resi 130 & chain A")

cmd.select ("Outward", "resi 130 & chain A", merge=1)

cmd.color ("red", "resi 131 & chain A")

cmd.select ("Inward", "resi 131 & chain A", merge=1)

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

cmd.color ("red", "resi 138 & chain A")

cmd.select ("Inward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("red", "resi 120 & chain A")

cmd.select ("Inward", "resi 120 & chain A", merge=1)

cmd.color ("blue", "resi 121 & chain A")

cmd.select ("Outward", "resi 121 & chain A", merge=1)

cmd.color ("red", "resi 122 & chain A")

cmd.select ("Inward", "resi 122 & chain A", merge=1)

cmd.color ("blue", "resi 123 & chain A")

cmd.select ("Outward", "resi 123 & chain A", merge=1)

cmd.color ("red", "resi 124 & chain A")

cmd.select ("Inward", "resi 124 & chain A", merge=1)

cmd.color ("blue", "resi 125 & chain A")

cmd.select ("Outward", "resi 125 & chain A", merge=1)

cmd.color ("red", "resi 126 & chain A")

cmd.select ("Inward", "resi 126 & chain A", merge=1)

cmd.color ("blue", "resi 101 & chain A")

cmd.select ("Outward", "resi 101 & chain A", merge=1)

cmd.color ("red", "resi 102 & chain A")

cmd.select ("Inward", "resi 102 & chain A", merge=1)

cmd.color ("red", "resi 103 & chain A")

cmd.select ("Inward", "resi 103 & chain A", merge=1)

cmd.color ("blue", "resi 104 & chain A")

cmd.select ("Outward", "resi 104 & chain A", merge=1)

cmd.color ("red", "resi 105 & chain A")

cmd.select ("Inward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("red", "resi 107 & chain A")

cmd.select ("Inward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("red", "resi 109 & chain A")

cmd.select ("Inward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("red", "resi 112 & chain A")

cmd.select ("Inward", "resi 112 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("red", "resi 114 & chain A")

cmd.select ("Inward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 87 & chain A")

cmd.select ("Outward", "resi 87 & chain A", merge=1)

cmd.color ("red", "resi 88 & chain A")

cmd.select ("Inward", "resi 88 & chain A", merge=1)

cmd.color ("blue", "resi 89 & chain A")

cmd.select ("Outward", "resi 89 & chain A", merge=1)

cmd.color ("red", "resi 90 & chain A")

cmd.select ("Inward", "resi 90 & chain A", merge=1)

cmd.color ("blue", "resi 91 & chain A")

cmd.select ("Outward", "resi 91 & chain A", merge=1)

cmd.color ("red", "resi 92 & chain A")

cmd.select ("Inward", "resi 92 & chain A", merge=1)

cmd.color ("blue", "resi 93 & chain A")

cmd.select ("Outward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("red", "resi 95 & chain A")

cmd.select ("Inward", "resi 95 & chain A", merge=1)

cmd.color ("red", "resi 68 & chain A")

cmd.select ("Inward", "resi 68 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

cmd.color ("red", "resi 70 & chain A")

cmd.select ("Inward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.color ("red", "resi 72 & chain A")

cmd.select ("Inward", "resi 72 & chain A", merge=1)

cmd.color ("blue", "resi 73 & chain A")

cmd.select ("Outward", "resi 73 & chain A", merge=1)

cmd.color ("red", "resi 74 & chain A")

cmd.select ("Inward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("red", "resi 76 & chain A")

cmd.select ("Inward", "resi 76 & chain A", merge=1)

cmd.color ("blue", "resi 77 & chain A")

cmd.select ("Outward", "resi 77 & chain A", merge=1)

cmd.color ("blue", "resi 54 & chain A")

cmd.select ("Outward", "resi 54 & chain A", merge=1)

cmd.color ("red", "resi 55 & chain A")

cmd.select ("Inward", "resi 55 & chain A", merge=1)

cmd.color ("blue", "resi 56 & chain A")

cmd.select ("Outward", "resi 56 & chain A", merge=1)

cmd.color ("red", "resi 57 & chain A")

cmd.select ("Inward", "resi 57 & chain A", merge=1)

cmd.color ("blue", "resi 58 & chain A")

cmd.select ("Outward", "resi 58 & chain A", merge=1)

cmd.color ("red", "resi 59 & chain A")

cmd.select ("Inward", "resi 59 & chain A", merge=1)

cmd.color ("blue", "resi 60 & chain A")

cmd.select ("Outward", "resi 60 & chain A", merge=1)

cmd.color ("red", "resi 61 & chain A")

cmd.select ("Inward", "resi 61 & chain A", merge=1)

cmd.color ("blue", "resi 62 & chain A")

cmd.select ("Outward", "resi 62 & chain A", merge=1)

cmd.color ("red", "resi 63 & chain A")

cmd.select ("Inward", "resi 63 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("red", "resi 43 & chain A")

cmd.select ("Inward", "resi 43 & chain A", merge=1)

cmd.color ("blue", "resi 44 & chain A")

cmd.select ("Outward", "resi 44 & chain A", merge=1)

cmd.color ("red", "resi 45 & chain A")

cmd.select ("Inward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 46 & chain A")

cmd.select ("Outward", "resi 46 & chain A", merge=1)

cmd.color ("red", "resi 47 & chain A")

cmd.select ("Inward", "resi 47 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("blue", "resi 49 & chain A")

cmd.select ("Outward", "resi 49 & chain A", merge=1)

cmd.load_cgo( [9.0, 8.1745,10.9385,44.82475, 8.1745, 10.9385, 44.82475, 1, 1,1,0,0,0,1], "axis" )
