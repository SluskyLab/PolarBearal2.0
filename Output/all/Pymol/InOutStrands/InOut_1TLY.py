from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1TLY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13+14+15+16+17+18+19+20+21+22+23 & chain A ")


cmd.select("Astrand1", "resi 35+36+37+38+39+40+41+42+43+44+45 & chain A ")


cmd.select("Astrand2", "resi 48+49+50+51+52+53+54+55+56+57 & chain A ")


cmd.select("Astrand8", "resi 179+180+181+182+183+184+185+186+187+188+189+190+191 & chain A ")


cmd.select("Astrand3", "resi 77+78+79+80+81+82+83+84+85 & chain A ")


cmd.select("Astrand4", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111 & chain A ")


cmd.select("Astrand7", "resi 159+160+161+162+163+164+165+166+167+168+169+170+171+172+173+174+175+176 & chain A ")


cmd.select("Astrand5", "resi 120+121+122+123+124+125+126+127+128+129+130+131 & chain A ")


cmd.select("Astrand6", "resi 138+139+140+141+142+143+144+145+146+147+148+149+150+151 & chain A ")


cmd.select("Astrand9", "resi 213+214+215+216+217+218+219+220+221+222+223 & chain A ")


cmd.select("Astrand10", "resi 227+228+229+230+231+232+233+234+235+236+237 & chain A ")


cmd.select("Astrand13", "resi 261+262+263+264+265+266+267+268+269+270+271+272 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 19 & chain A")

cmd.select ("Outward", "resi 19 & chain A", merge=1)

cmd.color ("red", "resi 20 & chain A")

cmd.select ("Inward", "resi 20 & chain A", merge=1)

cmd.color ("blue", "resi 21 & chain A")

cmd.select ("Outward", "resi 21 & chain A", merge=1)

cmd.color ("red", "resi 22 & chain A")

cmd.select ("Inward", "resi 22 & chain A", merge=1)

cmd.color ("blue", "resi 23 & chain A")

cmd.select ("Outward", "resi 23 & chain A", merge=1)

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

cmd.color ("blue", "resi 54 & chain A")

cmd.select ("Outward", "resi 54 & chain A", merge=1)

cmd.color ("red", "resi 55 & chain A")

cmd.select ("Inward", "resi 55 & chain A", merge=1)

cmd.color ("blue", "resi 56 & chain A")

cmd.select ("Outward", "resi 56 & chain A", merge=1)

cmd.color ("blue", "resi 57 & chain A")

cmd.select ("Outward", "resi 57 & chain A", merge=1)

cmd.color ("blue", "resi 179 & chain A")

cmd.select ("Outward", "resi 179 & chain A", merge=1)

cmd.color ("red", "resi 180 & chain A")

cmd.select ("Inward", "resi 180 & chain A", merge=1)

cmd.color ("blue", "resi 181 & chain A")

cmd.select ("Outward", "resi 181 & chain A", merge=1)

cmd.color ("red", "resi 182 & chain A")

cmd.select ("Inward", "resi 182 & chain A", merge=1)

cmd.color ("blue", "resi 183 & chain A")

cmd.select ("Outward", "resi 183 & chain A", merge=1)

cmd.color ("red", "resi 184 & chain A")

cmd.select ("Inward", "resi 184 & chain A", merge=1)

cmd.color ("blue", "resi 185 & chain A")

cmd.select ("Outward", "resi 185 & chain A", merge=1)

cmd.color ("red", "resi 186 & chain A")

cmd.select ("Inward", "resi 186 & chain A", merge=1)

cmd.color ("blue", "resi 187 & chain A")

cmd.select ("Outward", "resi 187 & chain A", merge=1)

cmd.color ("red", "resi 188 & chain A")

cmd.select ("Inward", "resi 188 & chain A", merge=1)

cmd.color ("blue", "resi 189 & chain A")

cmd.select ("Outward", "resi 189 & chain A", merge=1)

cmd.color ("red", "resi 190 & chain A")

cmd.select ("Inward", "resi 190 & chain A", merge=1)

cmd.color ("blue", "resi 191 & chain A")

cmd.select ("Outward", "resi 191 & chain A", merge=1)

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

cmd.color ("blue", "resi 85 & chain A")

cmd.select ("Outward", "resi 85 & chain A", merge=1)

cmd.color ("blue", "resi 99 & chain A")

cmd.select ("Outward", "resi 99 & chain A", merge=1)

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

cmd.color ("red", "resi 107 & chain A")

cmd.select ("Inward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("red", "resi 109 & chain A")

cmd.select ("Inward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

cmd.color ("red", "resi 111 & chain A")

cmd.select ("Inward", "resi 111 & chain A", merge=1)

cmd.color ("red", "resi 159 & chain A")

cmd.select ("Inward", "resi 159 & chain A", merge=1)

cmd.color ("blue", "resi 160 & chain A")

cmd.select ("Outward", "resi 160 & chain A", merge=1)

cmd.color ("red", "resi 161 & chain A")

cmd.select ("Inward", "resi 161 & chain A", merge=1)

cmd.color ("red", "resi 162 & chain A")

cmd.select ("Inward", "resi 162 & chain A", merge=1)

cmd.color ("blue", "resi 163 & chain A")

cmd.select ("Outward", "resi 163 & chain A", merge=1)

cmd.color ("red", "resi 164 & chain A")

cmd.select ("Inward", "resi 164 & chain A", merge=1)

cmd.color ("blue", "resi 165 & chain A")

cmd.select ("Outward", "resi 165 & chain A", merge=1)

cmd.color ("red", "resi 166 & chain A")

cmd.select ("Inward", "resi 166 & chain A", merge=1)

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

cmd.color ("blue", "resi 172 & chain A")

cmd.select ("Outward", "resi 172 & chain A", merge=1)

cmd.color ("red", "resi 173 & chain A")

cmd.select ("Inward", "resi 173 & chain A", merge=1)

cmd.color ("blue", "resi 174 & chain A")

cmd.select ("Outward", "resi 174 & chain A", merge=1)

cmd.color ("blue", "resi 175 & chain A")

cmd.select ("Outward", "resi 175 & chain A", merge=1)

cmd.color ("red", "resi 176 & chain A")

cmd.select ("Inward", "resi 176 & chain A", merge=1)

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

cmd.color ("blue", "resi 127 & chain A")

cmd.select ("Outward", "resi 127 & chain A", merge=1)

cmd.color ("red", "resi 128 & chain A")

cmd.select ("Inward", "resi 128 & chain A", merge=1)

cmd.color ("blue", "resi 129 & chain A")

cmd.select ("Outward", "resi 129 & chain A", merge=1)

cmd.color ("blue", "resi 130 & chain A")

cmd.select ("Outward", "resi 130 & chain A", merge=1)

cmd.color ("red", "resi 131 & chain A")

cmd.select ("Inward", "resi 131 & chain A", merge=1)

cmd.color ("red", "resi 138 & chain A")

cmd.select ("Inward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("red", "resi 140 & chain A")

cmd.select ("Inward", "resi 140 & chain A", merge=1)

cmd.color ("blue", "resi 141 & chain A")

cmd.select ("Outward", "resi 141 & chain A", merge=1)

cmd.color ("red", "resi 142 & chain A")

cmd.select ("Inward", "resi 142 & chain A", merge=1)

cmd.color ("blue", "resi 143 & chain A")

cmd.select ("Outward", "resi 143 & chain A", merge=1)

cmd.color ("red", "resi 144 & chain A")

cmd.select ("Inward", "resi 144 & chain A", merge=1)

cmd.color ("blue", "resi 145 & chain A")

cmd.select ("Outward", "resi 145 & chain A", merge=1)

cmd.color ("red", "resi 146 & chain A")

cmd.select ("Inward", "resi 146 & chain A", merge=1)

cmd.color ("blue", "resi 147 & chain A")

cmd.select ("Outward", "resi 147 & chain A", merge=1)

cmd.color ("red", "resi 148 & chain A")

cmd.select ("Inward", "resi 148 & chain A", merge=1)

cmd.color ("red", "resi 149 & chain A")

cmd.select ("Inward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("red", "resi 151 & chain A")

cmd.select ("Inward", "resi 151 & chain A", merge=1)

cmd.color ("red", "resi 213 & chain A")

cmd.select ("Inward", "resi 213 & chain A", merge=1)

cmd.color ("blue", "resi 214 & chain A")

cmd.select ("Outward", "resi 214 & chain A", merge=1)

cmd.color ("red", "resi 215 & chain A")

cmd.select ("Inward", "resi 215 & chain A", merge=1)

cmd.color ("blue", "resi 216 & chain A")

cmd.select ("Outward", "resi 216 & chain A", merge=1)

cmd.color ("red", "resi 217 & chain A")

cmd.select ("Inward", "resi 217 & chain A", merge=1)

cmd.color ("blue", "resi 218 & chain A")

cmd.select ("Outward", "resi 218 & chain A", merge=1)

cmd.color ("red", "resi 219 & chain A")

cmd.select ("Inward", "resi 219 & chain A", merge=1)

cmd.color ("blue", "resi 220 & chain A")

cmd.select ("Outward", "resi 220 & chain A", merge=1)

cmd.color ("red", "resi 221 & chain A")

cmd.select ("Inward", "resi 221 & chain A", merge=1)

cmd.color ("blue", "resi 222 & chain A")

cmd.select ("Outward", "resi 222 & chain A", merge=1)

cmd.color ("red", "resi 223 & chain A")

cmd.select ("Inward", "resi 223 & chain A", merge=1)

cmd.color ("blue", "resi 227 & chain A")

cmd.select ("Outward", "resi 227 & chain A", merge=1)

cmd.color ("red", "resi 228 & chain A")

cmd.select ("Inward", "resi 228 & chain A", merge=1)

cmd.color ("blue", "resi 229 & chain A")

cmd.select ("Outward", "resi 229 & chain A", merge=1)

cmd.color ("red", "resi 230 & chain A")

cmd.select ("Inward", "resi 230 & chain A", merge=1)

cmd.color ("blue", "resi 231 & chain A")

cmd.select ("Outward", "resi 231 & chain A", merge=1)

cmd.color ("red", "resi 232 & chain A")

cmd.select ("Inward", "resi 232 & chain A", merge=1)

cmd.color ("blue", "resi 233 & chain A")

cmd.select ("Outward", "resi 233 & chain A", merge=1)

cmd.color ("red", "resi 234 & chain A")

cmd.select ("Inward", "resi 234 & chain A", merge=1)

cmd.color ("blue", "resi 235 & chain A")

cmd.select ("Outward", "resi 235 & chain A", merge=1)

cmd.color ("red", "resi 236 & chain A")

cmd.select ("Inward", "resi 236 & chain A", merge=1)

cmd.color ("blue", "resi 237 & chain A")

cmd.select ("Outward", "resi 237 & chain A", merge=1)

cmd.color ("red", "resi 261 & chain A")

cmd.select ("Inward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 262 & chain A")

cmd.select ("Outward", "resi 262 & chain A", merge=1)

cmd.color ("red", "resi 263 & chain A")

cmd.select ("Inward", "resi 263 & chain A", merge=1)

cmd.color ("blue", "resi 264 & chain A")

cmd.select ("Outward", "resi 264 & chain A", merge=1)

cmd.color ("red", "resi 265 & chain A")

cmd.select ("Inward", "resi 265 & chain A", merge=1)

cmd.color ("blue", "resi 266 & chain A")

cmd.select ("Outward", "resi 266 & chain A", merge=1)

cmd.color ("red", "resi 267 & chain A")

cmd.select ("Inward", "resi 267 & chain A", merge=1)

cmd.color ("blue", "resi 268 & chain A")

cmd.select ("Outward", "resi 268 & chain A", merge=1)

cmd.color ("red", "resi 269 & chain A")

cmd.select ("Inward", "resi 269 & chain A", merge=1)

cmd.color ("blue", "resi 270 & chain A")

cmd.select ("Outward", "resi 270 & chain A", merge=1)

cmd.color ("red", "resi 271 & chain A")

cmd.select ("Inward", "resi 271 & chain A", merge=1)

cmd.color ("red", "resi 272 & chain A")

cmd.select ("Inward", "resi 272 & chain A", merge=1)

cmd.load_cgo( [9.0, -15.1435,95.52234,0.5349998, -15.1435, 95.52234, 0.5349998, 1, 1,1,0,0,0,1], "axis" )
