from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DZM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3+4+5+6+7+8+9+10+11+12+13 & chain A ")


cmd.select("Astrand9", "resi 195+196+197+198+199+200+201+202+203+204+205+206 & chain A ")


cmd.select("Astrand6", "resi 144+145+146+147+148+149+150+151+152+153+154+155 & chain A ")


cmd.select("Astrand5", "resi 120+121+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141 & chain A ")


cmd.select("Astrand4", "resi 93+94+95+96+97+98+99+100+101+102+103+104+105+106+107+160+108+161+109+162+110+163+164+165 & chain A ")


cmd.select("Astrand3", "resi 171+172+173+174+175+176+70+69+71+72+73+74+75+76+77+78+79+80+81+82+83 & chain A ")


cmd.select("Astrand2", "resi 33+34+35+36+37+38+39+40+41+42+43 & chain A ")


cmd.select("Astrand1", "resi 16+17+18+19+20+21+22+23+24+25 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 3 & chain A")

cmd.select ("Inward", "resi 3 & chain A", merge=1)

cmd.color ("blue", "resi 4 & chain A")

cmd.select ("Outward", "resi 4 & chain A", merge=1)

cmd.color ("red", "resi 5 & chain A")

cmd.select ("Inward", "resi 5 & chain A", merge=1)

cmd.color ("blue", "resi 6 & chain A")

cmd.select ("Outward", "resi 6 & chain A", merge=1)

cmd.color ("red", "resi 7 & chain A")

cmd.select ("Inward", "resi 7 & chain A", merge=1)

cmd.color ("blue", "resi 8 & chain A")

cmd.select ("Outward", "resi 8 & chain A", merge=1)

cmd.color ("red", "resi 9 & chain A")

cmd.select ("Inward", "resi 9 & chain A", merge=1)

cmd.color ("blue", "resi 10 & chain A")

cmd.select ("Outward", "resi 10 & chain A", merge=1)

cmd.color ("red", "resi 11 & chain A")

cmd.select ("Inward", "resi 11 & chain A", merge=1)

cmd.color ("blue", "resi 12 & chain A")

cmd.select ("Outward", "resi 12 & chain A", merge=1)

cmd.color ("red", "resi 13 & chain A")

cmd.select ("Inward", "resi 13 & chain A", merge=1)

cmd.color ("blue", "resi 195 & chain A")

cmd.select ("Outward", "resi 195 & chain A", merge=1)

cmd.color ("red", "resi 196 & chain A")

cmd.select ("Inward", "resi 196 & chain A", merge=1)

cmd.color ("blue", "resi 197 & chain A")

cmd.select ("Outward", "resi 197 & chain A", merge=1)

cmd.color ("red", "resi 198 & chain A")

cmd.select ("Inward", "resi 198 & chain A", merge=1)

cmd.color ("blue", "resi 199 & chain A")

cmd.select ("Outward", "resi 199 & chain A", merge=1)

cmd.color ("red", "resi 200 & chain A")

cmd.select ("Inward", "resi 200 & chain A", merge=1)

cmd.color ("blue", "resi 201 & chain A")

cmd.select ("Outward", "resi 201 & chain A", merge=1)

cmd.color ("red", "resi 202 & chain A")

cmd.select ("Inward", "resi 202 & chain A", merge=1)

cmd.color ("blue", "resi 203 & chain A")

cmd.select ("Outward", "resi 203 & chain A", merge=1)

cmd.color ("red", "resi 204 & chain A")

cmd.select ("Inward", "resi 204 & chain A", merge=1)

cmd.color ("red", "resi 205 & chain A")

cmd.select ("Inward", "resi 205 & chain A", merge=1)

cmd.color ("blue", "resi 206 & chain A")

cmd.select ("Outward", "resi 206 & chain A", merge=1)

cmd.color ("blue", "resi 144 & chain A")

cmd.select ("Outward", "resi 144 & chain A", merge=1)

cmd.color ("red", "resi 145 & chain A")

cmd.select ("Inward", "resi 145 & chain A", merge=1)

cmd.color ("blue", "resi 146 & chain A")

cmd.select ("Outward", "resi 146 & chain A", merge=1)

cmd.color ("red", "resi 147 & chain A")

cmd.select ("Inward", "resi 147 & chain A", merge=1)

cmd.color ("blue", "resi 148 & chain A")

cmd.select ("Outward", "resi 148 & chain A", merge=1)

cmd.color ("red", "resi 149 & chain A")

cmd.select ("Inward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("red", "resi 151 & chain A")

cmd.select ("Inward", "resi 151 & chain A", merge=1)

cmd.color ("blue", "resi 152 & chain A")

cmd.select ("Outward", "resi 152 & chain A", merge=1)

cmd.color ("red", "resi 153 & chain A")

cmd.select ("Inward", "resi 153 & chain A", merge=1)

cmd.color ("blue", "resi 154 & chain A")

cmd.select ("Outward", "resi 154 & chain A", merge=1)

cmd.color ("red", "resi 155 & chain A")

cmd.select ("Inward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 120 & chain A")

cmd.select ("Outward", "resi 120 & chain A", merge=1)

cmd.color ("red", "resi 121 & chain A")

cmd.select ("Inward", "resi 121 & chain A", merge=1)

cmd.color ("blue", "resi 122 & chain A")

cmd.select ("Outward", "resi 122 & chain A", merge=1)

cmd.color ("red", "resi 123 & chain A")

cmd.select ("Inward", "resi 123 & chain A", merge=1)

cmd.color ("blue", "resi 124 & chain A")

cmd.select ("Outward", "resi 124 & chain A", merge=1)

cmd.color ("red", "resi 125 & chain A")

cmd.select ("Inward", "resi 125 & chain A", merge=1)

cmd.color ("blue", "resi 126 & chain A")

cmd.select ("Outward", "resi 126 & chain A", merge=1)

cmd.color ("red", "resi 127 & chain A")

cmd.select ("Inward", "resi 127 & chain A", merge=1)

cmd.color ("blue", "resi 128 & chain A")

cmd.select ("Outward", "resi 128 & chain A", merge=1)

cmd.color ("red", "resi 129 & chain A")

cmd.select ("Inward", "resi 129 & chain A", merge=1)

cmd.color ("blue", "resi 130 & chain A")

cmd.select ("Outward", "resi 130 & chain A", merge=1)

cmd.color ("red", "resi 131 & chain A")

cmd.select ("Inward", "resi 131 & chain A", merge=1)

cmd.color ("blue", "resi 132 & chain A")

cmd.select ("Outward", "resi 132 & chain A", merge=1)

cmd.color ("red", "resi 133 & chain A")

cmd.select ("Inward", "resi 133 & chain A", merge=1)

cmd.color ("blue", "resi 134 & chain A")

cmd.select ("Outward", "resi 134 & chain A", merge=1)

cmd.color ("red", "resi 135 & chain A")

cmd.select ("Inward", "resi 135 & chain A", merge=1)

cmd.color ("blue", "resi 136 & chain A")

cmd.select ("Outward", "resi 136 & chain A", merge=1)

cmd.color ("red", "resi 137 & chain A")

cmd.select ("Inward", "resi 137 & chain A", merge=1)

cmd.color ("blue", "resi 138 & chain A")

cmd.select ("Outward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("red", "resi 140 & chain A")

cmd.select ("Inward", "resi 140 & chain A", merge=1)

cmd.color ("blue", "resi 141 & chain A")

cmd.select ("Outward", "resi 141 & chain A", merge=1)

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

cmd.color ("red", "resi 99 & chain A")

cmd.select ("Inward", "resi 99 & chain A", merge=1)

cmd.color ("blue", "resi 100 & chain A")

cmd.select ("Outward", "resi 100 & chain A", merge=1)

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

cmd.color ("red", "resi 107 & chain A")

cmd.select ("Inward", "resi 107 & chain A", merge=1)

cmd.color ("red", "resi 160 & chain A")

cmd.select ("Inward", "resi 160 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 161 & chain A")

cmd.select ("Outward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 162 & chain A")

cmd.select ("Outward", "resi 162 & chain A", merge=1)

cmd.color ("red", "resi 110 & chain A")

cmd.select ("Inward", "resi 110 & chain A", merge=1)

cmd.color ("red", "resi 163 & chain A")

cmd.select ("Inward", "resi 163 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

cmd.color ("red", "resi 165 & chain A")

cmd.select ("Inward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 171 & chain A")

cmd.select ("Outward", "resi 171 & chain A", merge=1)

cmd.color ("red", "resi 172 & chain A")

cmd.select ("Inward", "resi 172 & chain A", merge=1)

cmd.color ("blue", "resi 173 & chain A")

cmd.select ("Outward", "resi 173 & chain A", merge=1)

cmd.color ("red", "resi 174 & chain A")

cmd.select ("Inward", "resi 174 & chain A", merge=1)

cmd.color ("blue", "resi 175 & chain A")

cmd.select ("Outward", "resi 175 & chain A", merge=1)

cmd.color ("red", "resi 176 & chain A")

cmd.select ("Inward", "resi 176 & chain A", merge=1)

cmd.color ("red", "resi 70 & chain A")

cmd.select ("Inward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

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

cmd.color ("red", "resi 78 & chain A")

cmd.select ("Inward", "resi 78 & chain A", merge=1)

cmd.color ("blue", "resi 79 & chain A")

cmd.select ("Outward", "resi 79 & chain A", merge=1)

cmd.color ("red", "resi 80 & chain A")

cmd.select ("Inward", "resi 80 & chain A", merge=1)

cmd.color ("blue", "resi 81 & chain A")

cmd.select ("Outward", "resi 81 & chain A", merge=1)

cmd.color ("red", "resi 82 & chain A")

cmd.select ("Inward", "resi 82 & chain A", merge=1)

cmd.color ("blue", "resi 83 & chain A")

cmd.select ("Outward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 33 & chain A")

cmd.select ("Outward", "resi 33 & chain A", merge=1)

cmd.color ("red", "resi 34 & chain A")

cmd.select ("Inward", "resi 34 & chain A", merge=1)

cmd.color ("blue", "resi 35 & chain A")

cmd.select ("Outward", "resi 35 & chain A", merge=1)

cmd.color ("red", "resi 36 & chain A")

cmd.select ("Inward", "resi 36 & chain A", merge=1)

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

cmd.color ("red", "resi 42 & chain A")

cmd.select ("Inward", "resi 42 & chain A", merge=1)

cmd.color ("blue", "resi 43 & chain A")

cmd.select ("Outward", "resi 43 & chain A", merge=1)

cmd.color ("blue", "resi 16 & chain A")

cmd.select ("Outward", "resi 16 & chain A", merge=1)

cmd.color ("red", "resi 17 & chain A")

cmd.select ("Inward", "resi 17 & chain A", merge=1)

cmd.color ("blue", "resi 18 & chain A")

cmd.select ("Outward", "resi 18 & chain A", merge=1)

cmd.color ("red", "resi 19 & chain A")

cmd.select ("Inward", "resi 19 & chain A", merge=1)

cmd.color ("blue", "resi 20 & chain A")

cmd.select ("Outward", "resi 20 & chain A", merge=1)

cmd.color ("red", "resi 21 & chain A")

cmd.select ("Inward", "resi 21 & chain A", merge=1)

cmd.color ("blue", "resi 22 & chain A")

cmd.select ("Outward", "resi 22 & chain A", merge=1)

cmd.color ("red", "resi 23 & chain A")

cmd.select ("Inward", "resi 23 & chain A", merge=1)

cmd.color ("blue", "resi 24 & chain A")

cmd.select ("Outward", "resi 24 & chain A", merge=1)

cmd.color ("red", "resi 25 & chain A")

cmd.select ("Inward", "resi 25 & chain A", merge=1)

cmd.load_cgo( [9.0, 62.587624,-71.627625,-28.15525, 62.587624, -71.627625, -28.15525, 1, 1,1,0,0,0,1], "axis" )