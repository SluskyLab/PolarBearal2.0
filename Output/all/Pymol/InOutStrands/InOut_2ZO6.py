from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZO6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8+9+10+11+12+13+14+15+16+17+18 & chain A ")


cmd.select("Astrand1", "resi 21+22+23+24+25+26+27+28+29+30+31+32 & chain A ")


cmd.select("Astrand2", "resi 37+38+39+40+41+42+43+44+45+46 & chain A ")


cmd.select("Astrand11", "resi 203+204+205+206+207+208+209+210+211+212+213 & chain A ")


cmd.select("Astrand10", "resi 189+190+191+192+193+194+195+196+197+198+199+200 & chain A ")


cmd.select("Astrand6", "resi 135+136+137+138+141+142+143+144+145+146+147+148 & chain A ")


cmd.select("Astrand8", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain A ")


cmd.select("Astrand9", "resi 167+168+169+170+171+172+173+174+175+176+177+178 & chain A ")


cmd.select("Astrand3", "resi 87+88+89+90+91+92+93+94+95 & chain A ")


cmd.select("Astrand4", "resi 100+101+102+103+104+105+106+107+108+109+110 & chain A ")


cmd.select("Astrand5", "resi 113+114+115+116+117+118+119+120+121+122+123 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 8 & chain A")

cmd.select ("Inward", "resi 8 & chain A", merge=1)

cmd.color ("blue", "resi 9 & chain A")

cmd.select ("Outward", "resi 9 & chain A", merge=1)

cmd.color ("red", "resi 10 & chain A")

cmd.select ("Inward", "resi 10 & chain A", merge=1)

cmd.color ("blue", "resi 11 & chain A")

cmd.select ("Outward", "resi 11 & chain A", merge=1)

cmd.color ("red", "resi 12 & chain A")

cmd.select ("Inward", "resi 12 & chain A", merge=1)

cmd.color ("blue", "resi 13 & chain A")

cmd.select ("Outward", "resi 13 & chain A", merge=1)

cmd.color ("red", "resi 14 & chain A")

cmd.select ("Inward", "resi 14 & chain A", merge=1)

cmd.color ("blue", "resi 15 & chain A")

cmd.select ("Outward", "resi 15 & chain A", merge=1)

cmd.color ("red", "resi 16 & chain A")

cmd.select ("Inward", "resi 16 & chain A", merge=1)

cmd.color ("blue", "resi 17 & chain A")

cmd.select ("Outward", "resi 17 & chain A", merge=1)

cmd.color ("red", "resi 18 & chain A")

cmd.select ("Inward", "resi 18 & chain A", merge=1)

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

cmd.color ("blue", "resi 26 & chain A")

cmd.select ("Outward", "resi 26 & chain A", merge=1)

cmd.color ("red", "resi 27 & chain A")

cmd.select ("Inward", "resi 27 & chain A", merge=1)

cmd.color ("blue", "resi 28 & chain A")

cmd.select ("Outward", "resi 28 & chain A", merge=1)

cmd.color ("red", "resi 29 & chain A")

cmd.select ("Inward", "resi 29 & chain A", merge=1)

cmd.color ("blue", "resi 30 & chain A")

cmd.select ("Outward", "resi 30 & chain A", merge=1)

cmd.color ("red", "resi 31 & chain A")

cmd.select ("Inward", "resi 31 & chain A", merge=1)

cmd.color ("blue", "resi 32 & chain A")

cmd.select ("Outward", "resi 32 & chain A", merge=1)

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

cmd.color ("red", "resi 44 & chain A")

cmd.select ("Inward", "resi 44 & chain A", merge=1)

cmd.color ("red", "resi 45 & chain A")

cmd.select ("Inward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 46 & chain A")

cmd.select ("Outward", "resi 46 & chain A", merge=1)

cmd.color ("blue", "resi 203 & chain A")

cmd.select ("Outward", "resi 203 & chain A", merge=1)

cmd.color ("red", "resi 204 & chain A")

cmd.select ("Inward", "resi 204 & chain A", merge=1)

cmd.color ("blue", "resi 205 & chain A")

cmd.select ("Outward", "resi 205 & chain A", merge=1)

cmd.color ("red", "resi 206 & chain A")

cmd.select ("Inward", "resi 206 & chain A", merge=1)

cmd.color ("blue", "resi 207 & chain A")

cmd.select ("Outward", "resi 207 & chain A", merge=1)

cmd.color ("red", "resi 208 & chain A")

cmd.select ("Inward", "resi 208 & chain A", merge=1)

cmd.color ("blue", "resi 209 & chain A")

cmd.select ("Outward", "resi 209 & chain A", merge=1)

cmd.color ("red", "resi 210 & chain A")

cmd.select ("Inward", "resi 210 & chain A", merge=1)

cmd.color ("blue", "resi 211 & chain A")

cmd.select ("Outward", "resi 211 & chain A", merge=1)

cmd.color ("blue", "resi 212 & chain A")

cmd.select ("Outward", "resi 212 & chain A", merge=1)

cmd.color ("blue", "resi 213 & chain A")

cmd.select ("Outward", "resi 213 & chain A", merge=1)

cmd.color ("red", "resi 189 & chain A")

cmd.select ("Inward", "resi 189 & chain A", merge=1)

cmd.color ("blue", "resi 190 & chain A")

cmd.select ("Outward", "resi 190 & chain A", merge=1)

cmd.color ("red", "resi 191 & chain A")

cmd.select ("Inward", "resi 191 & chain A", merge=1)

cmd.color ("blue", "resi 192 & chain A")

cmd.select ("Outward", "resi 192 & chain A", merge=1)

cmd.color ("red", "resi 193 & chain A")

cmd.select ("Inward", "resi 193 & chain A", merge=1)

cmd.color ("blue", "resi 194 & chain A")

cmd.select ("Outward", "resi 194 & chain A", merge=1)

cmd.color ("red", "resi 195 & chain A")

cmd.select ("Inward", "resi 195 & chain A", merge=1)

cmd.color ("blue", "resi 196 & chain A")

cmd.select ("Outward", "resi 196 & chain A", merge=1)

cmd.color ("red", "resi 197 & chain A")

cmd.select ("Inward", "resi 197 & chain A", merge=1)

cmd.color ("blue", "resi 198 & chain A")

cmd.select ("Outward", "resi 198 & chain A", merge=1)

cmd.color ("red", "resi 199 & chain A")

cmd.select ("Inward", "resi 199 & chain A", merge=1)

cmd.color ("blue", "resi 200 & chain A")

cmd.select ("Outward", "resi 200 & chain A", merge=1)

cmd.color ("blue", "resi 135 & chain A")

cmd.select ("Outward", "resi 135 & chain A", merge=1)

cmd.color ("red", "resi 136 & chain A")

cmd.select ("Inward", "resi 136 & chain A", merge=1)

cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

cmd.color ("red", "resi 138 & chain A")

cmd.select ("Inward", "resi 138 & chain A", merge=1)

cmd.color ("red", "resi 141 & chain A")

cmd.select ("Inward", "resi 141 & chain A", merge=1)

cmd.color ("blue", "resi 142 & chain A")

cmd.select ("Outward", "resi 142 & chain A", merge=1)

cmd.color ("red", "resi 143 & chain A")

cmd.select ("Inward", "resi 143 & chain A", merge=1)

cmd.color ("blue", "resi 144 & chain A")

cmd.select ("Outward", "resi 144 & chain A", merge=1)

cmd.color ("blue", "resi 145 & chain A")

cmd.select ("Outward", "resi 145 & chain A", merge=1)

cmd.color ("blue", "resi 146 & chain A")

cmd.select ("Outward", "resi 146 & chain A", merge=1)

cmd.color ("blue", "resi 147 & chain A")

cmd.select ("Outward", "resi 147 & chain A", merge=1)

cmd.color ("red", "resi 148 & chain A")

cmd.select ("Inward", "resi 148 & chain A", merge=1)

cmd.color ("blue", "resi 151 & chain A")

cmd.select ("Outward", "resi 151 & chain A", merge=1)

cmd.color ("red", "resi 152 & chain A")

cmd.select ("Inward", "resi 152 & chain A", merge=1)

cmd.color ("blue", "resi 153 & chain A")

cmd.select ("Outward", "resi 153 & chain A", merge=1)

cmd.color ("red", "resi 154 & chain A")

cmd.select ("Inward", "resi 154 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("red", "resi 156 & chain A")

cmd.select ("Inward", "resi 156 & chain A", merge=1)

cmd.color ("blue", "resi 157 & chain A")

cmd.select ("Outward", "resi 157 & chain A", merge=1)

cmd.color ("red", "resi 158 & chain A")

cmd.select ("Inward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("red", "resi 160 & chain A")

cmd.select ("Inward", "resi 160 & chain A", merge=1)

cmd.color ("red", "resi 161 & chain A")

cmd.select ("Inward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 162 & chain A")

cmd.select ("Outward", "resi 162 & chain A", merge=1)

cmd.color ("blue", "resi 167 & chain A")

cmd.select ("Outward", "resi 167 & chain A", merge=1)

cmd.color ("red", "resi 168 & chain A")

cmd.select ("Inward", "resi 168 & chain A", merge=1)

cmd.color ("blue", "resi 169 & chain A")

cmd.select ("Outward", "resi 169 & chain A", merge=1)

cmd.color ("red", "resi 170 & chain A")

cmd.select ("Inward", "resi 170 & chain A", merge=1)

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

cmd.color ("blue", "resi 177 & chain A")

cmd.select ("Outward", "resi 177 & chain A", merge=1)

cmd.color ("blue", "resi 178 & chain A")

cmd.select ("Outward", "resi 178 & chain A", merge=1)

cmd.color ("red", "resi 87 & chain A")

cmd.select ("Inward", "resi 87 & chain A", merge=1)

cmd.color ("blue", "resi 88 & chain A")

cmd.select ("Outward", "resi 88 & chain A", merge=1)

cmd.color ("red", "resi 89 & chain A")

cmd.select ("Inward", "resi 89 & chain A", merge=1)

cmd.color ("blue", "resi 90 & chain A")

cmd.select ("Outward", "resi 90 & chain A", merge=1)

cmd.color ("red", "resi 91 & chain A")

cmd.select ("Inward", "resi 91 & chain A", merge=1)

cmd.color ("blue", "resi 92 & chain A")

cmd.select ("Outward", "resi 92 & chain A", merge=1)

cmd.color ("red", "resi 93 & chain A")

cmd.select ("Inward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("red", "resi 95 & chain A")

cmd.select ("Inward", "resi 95 & chain A", merge=1)

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

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("red", "resi 110 & chain A")

cmd.select ("Inward", "resi 110 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("red", "resi 114 & chain A")

cmd.select ("Inward", "resi 114 & chain A", merge=1)

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

cmd.color ("blue", "resi 123 & chain A")

cmd.select ("Outward", "resi 123 & chain A", merge=1)

cmd.load_cgo( [9.0, 5.828273,51.28545,19.058182, 5.828273, 51.28545, 19.058182, 1, 1,1,0,0,0,1], "axis" )
