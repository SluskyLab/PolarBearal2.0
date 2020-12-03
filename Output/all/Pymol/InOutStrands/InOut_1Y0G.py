from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1Y0G.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand11", "resi 24+25+26+27+34+35+36+37+38+39+40+41+42 & chain B ")


cmd.select("Bstrand14", "resi 46+47+48+49+50+51+52+55+56+57+58+59+60 & chain B ")


cmd.select("Bstrand15", "resi 70+71+72+73+74+75+76 & chain B ")


cmd.select("Bstrand17", "resi 104+105+106+107+108+109+110+111+112+113+114+115 & chain B ")


cmd.select("Bstrand18", "resi 118+119+120+121+122+123+124+125+126+127 & chain B ")


cmd.select("Bstrand19", "resi 130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145 & chain B ")


cmd.select("Bstrand20", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain B ")


cmd.select("Bstrand21", "resi 178+179+180+181+182+183+184+185+186+187+188+189 & chain B ")


cmd.select("barrel", "Bstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 24 & chain B")

cmd.select ("Outward", "resi 24 & chain B", merge=1)

cmd.color ("blue", "resi 25 & chain B")

cmd.select ("Outward", "resi 25 & chain B", merge=1)

cmd.color ("blue", "resi 26 & chain B")

cmd.select ("Outward", "resi 26 & chain B", merge=1)

cmd.color ("blue", "resi 27 & chain B")

cmd.select ("Outward", "resi 27 & chain B", merge=1)

cmd.color ("blue", "resi 34 & chain B")

cmd.select ("Outward", "resi 34 & chain B", merge=1)

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

cmd.color ("blue", "resi 40 & chain B")

cmd.select ("Outward", "resi 40 & chain B", merge=1)

cmd.color ("blue", "resi 41 & chain B")

cmd.select ("Outward", "resi 41 & chain B", merge=1)

cmd.color ("blue", "resi 42 & chain B")

cmd.select ("Outward", "resi 42 & chain B", merge=1)

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

cmd.color ("blue", "resi 55 & chain B")

cmd.select ("Outward", "resi 55 & chain B", merge=1)

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

cmd.color ("blue", "resi 70 & chain B")

cmd.select ("Outward", "resi 70 & chain B", merge=1)

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

cmd.color ("blue", "resi 104 & chain B")

cmd.select ("Outward", "resi 104 & chain B", merge=1)

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

cmd.color ("blue", "resi 114 & chain B")

cmd.select ("Outward", "resi 114 & chain B", merge=1)

cmd.color ("blue", "resi 115 & chain B")

cmd.select ("Outward", "resi 115 & chain B", merge=1)

cmd.color ("blue", "resi 118 & chain B")

cmd.select ("Outward", "resi 118 & chain B", merge=1)

cmd.color ("blue", "resi 119 & chain B")

cmd.select ("Outward", "resi 119 & chain B", merge=1)

cmd.color ("blue", "resi 120 & chain B")

cmd.select ("Outward", "resi 120 & chain B", merge=1)

cmd.color ("blue", "resi 121 & chain B")

cmd.select ("Outward", "resi 121 & chain B", merge=1)

cmd.color ("blue", "resi 122 & chain B")

cmd.select ("Outward", "resi 122 & chain B", merge=1)

cmd.color ("blue", "resi 123 & chain B")

cmd.select ("Outward", "resi 123 & chain B", merge=1)

cmd.color ("blue", "resi 124 & chain B")

cmd.select ("Outward", "resi 124 & chain B", merge=1)

cmd.color ("blue", "resi 125 & chain B")

cmd.select ("Outward", "resi 125 & chain B", merge=1)

cmd.color ("blue", "resi 126 & chain B")

cmd.select ("Outward", "resi 126 & chain B", merge=1)

cmd.color ("blue", "resi 127 & chain B")

cmd.select ("Outward", "resi 127 & chain B", merge=1)

cmd.color ("blue", "resi 130 & chain B")

cmd.select ("Outward", "resi 130 & chain B", merge=1)

cmd.color ("blue", "resi 131 & chain B")

cmd.select ("Outward", "resi 131 & chain B", merge=1)

cmd.color ("blue", "resi 132 & chain B")

cmd.select ("Outward", "resi 132 & chain B", merge=1)

cmd.color ("blue", "resi 133 & chain B")

cmd.select ("Outward", "resi 133 & chain B", merge=1)

cmd.color ("blue", "resi 134 & chain B")

cmd.select ("Outward", "resi 134 & chain B", merge=1)

cmd.color ("blue", "resi 135 & chain B")

cmd.select ("Outward", "resi 135 & chain B", merge=1)

cmd.color ("blue", "resi 136 & chain B")

cmd.select ("Outward", "resi 136 & chain B", merge=1)

cmd.color ("blue", "resi 137 & chain B")

cmd.select ("Outward", "resi 137 & chain B", merge=1)

cmd.color ("blue", "resi 138 & chain B")

cmd.select ("Outward", "resi 138 & chain B", merge=1)

cmd.color ("blue", "resi 139 & chain B")

cmd.select ("Outward", "resi 139 & chain B", merge=1)

cmd.color ("blue", "resi 140 & chain B")

cmd.select ("Outward", "resi 140 & chain B", merge=1)

cmd.color ("blue", "resi 141 & chain B")

cmd.select ("Outward", "resi 141 & chain B", merge=1)

cmd.color ("blue", "resi 142 & chain B")

cmd.select ("Outward", "resi 142 & chain B", merge=1)

cmd.color ("blue", "resi 143 & chain B")

cmd.select ("Outward", "resi 143 & chain B", merge=1)

cmd.color ("blue", "resi 144 & chain B")

cmd.select ("Outward", "resi 144 & chain B", merge=1)

cmd.color ("blue", "resi 145 & chain B")

cmd.select ("Outward", "resi 145 & chain B", merge=1)

cmd.color ("blue", "resi 151 & chain B")

cmd.select ("Outward", "resi 151 & chain B", merge=1)

cmd.color ("blue", "resi 152 & chain B")

cmd.select ("Outward", "resi 152 & chain B", merge=1)

cmd.color ("blue", "resi 153 & chain B")

cmd.select ("Outward", "resi 153 & chain B", merge=1)

cmd.color ("blue", "resi 154 & chain B")

cmd.select ("Outward", "resi 154 & chain B", merge=1)

cmd.color ("blue", "resi 155 & chain B")

cmd.select ("Outward", "resi 155 & chain B", merge=1)

cmd.color ("blue", "resi 156 & chain B")

cmd.select ("Outward", "resi 156 & chain B", merge=1)

cmd.color ("blue", "resi 157 & chain B")

cmd.select ("Outward", "resi 157 & chain B", merge=1)

cmd.color ("blue", "resi 158 & chain B")

cmd.select ("Outward", "resi 158 & chain B", merge=1)

cmd.color ("blue", "resi 159 & chain B")

cmd.select ("Outward", "resi 159 & chain B", merge=1)

cmd.color ("blue", "resi 160 & chain B")

cmd.select ("Outward", "resi 160 & chain B", merge=1)

cmd.color ("blue", "resi 161 & chain B")

cmd.select ("Outward", "resi 161 & chain B", merge=1)

cmd.color ("blue", "resi 162 & chain B")

cmd.select ("Outward", "resi 162 & chain B", merge=1)

cmd.color ("blue", "resi 178 & chain B")

cmd.select ("Outward", "resi 178 & chain B", merge=1)

cmd.color ("blue", "resi 179 & chain B")

cmd.select ("Outward", "resi 179 & chain B", merge=1)

cmd.color ("blue", "resi 180 & chain B")

cmd.select ("Outward", "resi 180 & chain B", merge=1)

cmd.color ("blue", "resi 181 & chain B")

cmd.select ("Outward", "resi 181 & chain B", merge=1)

cmd.color ("blue", "resi 182 & chain B")

cmd.select ("Outward", "resi 182 & chain B", merge=1)

cmd.color ("blue", "resi 183 & chain B")

cmd.select ("Outward", "resi 183 & chain B", merge=1)

cmd.color ("blue", "resi 184 & chain B")

cmd.select ("Outward", "resi 184 & chain B", merge=1)

cmd.color ("blue", "resi 185 & chain B")

cmd.select ("Outward", "resi 185 & chain B", merge=1)

cmd.color ("blue", "resi 186 & chain B")

cmd.select ("Outward", "resi 186 & chain B", merge=1)

cmd.color ("blue", "resi 187 & chain B")

cmd.select ("Outward", "resi 187 & chain B", merge=1)

cmd.color ("blue", "resi 188 & chain B")

cmd.select ("Outward", "resi 188 & chain B", merge=1)

cmd.color ("blue", "resi 189 & chain B")

cmd.select ("Outward", "resi 189 & chain B", merge=1)

cmd.load_cgo( [9.0, -18.139374,4.417375,42.641125, -37.01062, 21.095123, 34.5475, 1, 1,1,0,0,0,1], "axis" )
