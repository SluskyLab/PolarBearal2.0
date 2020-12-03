from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FID.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9 & chain A ")


cmd.select("Astrand1", "resi 33+34+35+36+37+38+39+40+41+42+43+44 & chain A ")


cmd.select("Astrand2", "resi 49+50+51+52+53+54+55+56+57+58+59+60 & chain A ")


cmd.select("Astrand3", "resi 80+81+82+83+84+85+86+87+88+89+90+91+92+93+94 & chain A ")


cmd.select("Astrand4", "resi 97+98+99+100+101+102+103+104+105+106+107+108 & chain A ")


cmd.select("Astrand5", "resi 140+141+142+143+144+145+146+147+148+149+150+151+154+155+156+157 & chain A ")


cmd.select("Astrand8", "resi 176+177+178+179+180+181+182+183+184+185+186+187+188 & chain A ")


cmd.select("Astrand7", "resi 160+161+162+163+164+165+166+167+168+169+170+171+172+173 & chain A ")


cmd.select("Astrand9", "resi 215+216+217+218+219+220+221+222+223+224+225+226+227+228+229+230+231 & chain A ")


cmd.select("Astrand10", "resi 251+252+253+254+255+256+257+258+259+260+261+262+263 & chain A ")


cmd.select("Astrand11", "resi 266+267+268+269+270+271+272+273+274+275 & chain A ")


cmd.select("Astrand12", "resi 285+286+287+288+289+290+291+292+293+294+295 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 2 & chain A")

cmd.select ("Inward", "resi 2 & chain A", merge=1)

cmd.color ("blue", "resi 3 & chain A")

cmd.select ("Outward", "resi 3 & chain A", merge=1)

cmd.color ("red", "resi 4 & chain A")

cmd.select ("Inward", "resi 4 & chain A", merge=1)

cmd.color ("blue", "resi 5 & chain A")

cmd.select ("Outward", "resi 5 & chain A", merge=1)

cmd.color ("red", "resi 6 & chain A")

cmd.select ("Inward", "resi 6 & chain A", merge=1)

cmd.color ("blue", "resi 7 & chain A")

cmd.select ("Outward", "resi 7 & chain A", merge=1)

cmd.color ("red", "resi 8 & chain A")

cmd.select ("Inward", "resi 8 & chain A", merge=1)

cmd.color ("blue", "resi 9 & chain A")

cmd.select ("Outward", "resi 9 & chain A", merge=1)

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

cmd.color ("blue", "resi 44 & chain A")

cmd.select ("Outward", "resi 44 & chain A", merge=1)

cmd.color ("blue", "resi 49 & chain A")

cmd.select ("Outward", "resi 49 & chain A", merge=1)

cmd.color ("red", "resi 50 & chain A")

cmd.select ("Inward", "resi 50 & chain A", merge=1)

cmd.color ("blue", "resi 51 & chain A")

cmd.select ("Outward", "resi 51 & chain A", merge=1)

cmd.color ("red", "resi 52 & chain A")

cmd.select ("Inward", "resi 52 & chain A", merge=1)

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

cmd.color ("blue", "resi 59 & chain A")

cmd.select ("Outward", "resi 59 & chain A", merge=1)

cmd.color ("red", "resi 60 & chain A")

cmd.select ("Inward", "resi 60 & chain A", merge=1)

cmd.color ("red", "resi 80 & chain A")

cmd.select ("Inward", "resi 80 & chain A", merge=1)

cmd.color ("blue", "resi 81 & chain A")

cmd.select ("Outward", "resi 81 & chain A", merge=1)

cmd.color ("red", "resi 82 & chain A")

cmd.select ("Inward", "resi 82 & chain A", merge=1)

cmd.color ("blue", "resi 83 & chain A")

cmd.select ("Outward", "resi 83 & chain A", merge=1)

cmd.color ("red", "resi 84 & chain A")

cmd.select ("Inward", "resi 84 & chain A", merge=1)

cmd.color ("blue", "resi 85 & chain A")

cmd.select ("Outward", "resi 85 & chain A", merge=1)

cmd.color ("red", "resi 86 & chain A")

cmd.select ("Inward", "resi 86 & chain A", merge=1)

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

cmd.color ("blue", "resi 92 & chain A")

cmd.select ("Outward", "resi 92 & chain A", merge=1)

cmd.color ("red", "resi 93 & chain A")

cmd.select ("Inward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("blue", "resi 97 & chain A")

cmd.select ("Outward", "resi 97 & chain A", merge=1)

cmd.color ("red", "resi 98 & chain A")

cmd.select ("Inward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 99 & chain A")

cmd.select ("Outward", "resi 99 & chain A", merge=1)

cmd.color ("red", "resi 100 & chain A")

cmd.select ("Inward", "resi 100 & chain A", merge=1)

cmd.color ("blue", "resi 101 & chain A")

cmd.select ("Outward", "resi 101 & chain A", merge=1)

cmd.color ("red", "resi 102 & chain A")

cmd.select ("Inward", "resi 102 & chain A", merge=1)

cmd.color ("blue", "resi 103 & chain A")

cmd.select ("Outward", "resi 103 & chain A", merge=1)

cmd.color ("red", "resi 104 & chain A")

cmd.select ("Inward", "resi 104 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("red", "resi 106 & chain A")

cmd.select ("Inward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("red", "resi 108 & chain A")

cmd.select ("Inward", "resi 108 & chain A", merge=1)

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

cmd.color ("blue", "resi 149 & chain A")

cmd.select ("Outward", "resi 149 & chain A", merge=1)

cmd.color ("red", "resi 150 & chain A")

cmd.select ("Inward", "resi 150 & chain A", merge=1)

cmd.color ("blue", "resi 151 & chain A")

cmd.select ("Outward", "resi 151 & chain A", merge=1)

cmd.color ("red", "resi 154 & chain A")

cmd.select ("Inward", "resi 154 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 156 & chain A")

cmd.select ("Outward", "resi 156 & chain A", merge=1)

cmd.color ("red", "resi 157 & chain A")

cmd.select ("Inward", "resi 157 & chain A", merge=1)

cmd.color ("red", "resi 176 & chain A")

cmd.select ("Inward", "resi 176 & chain A", merge=1)

cmd.color ("blue", "resi 177 & chain A")

cmd.select ("Outward", "resi 177 & chain A", merge=1)

cmd.color ("red", "resi 178 & chain A")

cmd.select ("Inward", "resi 178 & chain A", merge=1)

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

cmd.color ("blue", "resi 160 & chain A")

cmd.select ("Outward", "resi 160 & chain A", merge=1)

cmd.color ("red", "resi 161 & chain A")

cmd.select ("Inward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 162 & chain A")

cmd.select ("Outward", "resi 162 & chain A", merge=1)

cmd.color ("red", "resi 163 & chain A")

cmd.select ("Inward", "resi 163 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

cmd.color ("red", "resi 165 & chain A")

cmd.select ("Inward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 166 & chain A")

cmd.select ("Outward", "resi 166 & chain A", merge=1)

cmd.color ("red", "resi 167 & chain A")

cmd.select ("Inward", "resi 167 & chain A", merge=1)

cmd.color ("blue", "resi 168 & chain A")

cmd.select ("Outward", "resi 168 & chain A", merge=1)

cmd.color ("red", "resi 169 & chain A")

cmd.select ("Inward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 170 & chain A")

cmd.select ("Outward", "resi 170 & chain A", merge=1)

cmd.color ("red", "resi 171 & chain A")

cmd.select ("Inward", "resi 171 & chain A", merge=1)

cmd.color ("blue", "resi 172 & chain A")

cmd.select ("Outward", "resi 172 & chain A", merge=1)

cmd.color ("red", "resi 173 & chain A")

cmd.select ("Inward", "resi 173 & chain A", merge=1)

cmd.color ("blue", "resi 215 & chain A")

cmd.select ("Outward", "resi 215 & chain A", merge=1)

cmd.color ("red", "resi 216 & chain A")

cmd.select ("Inward", "resi 216 & chain A", merge=1)

cmd.color ("blue", "resi 217 & chain A")

cmd.select ("Outward", "resi 217 & chain A", merge=1)

cmd.color ("red", "resi 218 & chain A")

cmd.select ("Inward", "resi 218 & chain A", merge=1)

cmd.color ("blue", "resi 219 & chain A")

cmd.select ("Outward", "resi 219 & chain A", merge=1)

cmd.color ("red", "resi 220 & chain A")

cmd.select ("Inward", "resi 220 & chain A", merge=1)

cmd.color ("blue", "resi 221 & chain A")

cmd.select ("Outward", "resi 221 & chain A", merge=1)

cmd.color ("red", "resi 222 & chain A")

cmd.select ("Inward", "resi 222 & chain A", merge=1)

cmd.color ("blue", "resi 223 & chain A")

cmd.select ("Outward", "resi 223 & chain A", merge=1)

cmd.color ("red", "resi 224 & chain A")

cmd.select ("Inward", "resi 224 & chain A", merge=1)

cmd.color ("blue", "resi 225 & chain A")

cmd.select ("Outward", "resi 225 & chain A", merge=1)

cmd.color ("red", "resi 226 & chain A")

cmd.select ("Inward", "resi 226 & chain A", merge=1)

cmd.color ("blue", "resi 227 & chain A")

cmd.select ("Outward", "resi 227 & chain A", merge=1)

cmd.color ("red", "resi 228 & chain A")

cmd.select ("Inward", "resi 228 & chain A", merge=1)

cmd.color ("blue", "resi 229 & chain A")

cmd.select ("Outward", "resi 229 & chain A", merge=1)

cmd.color ("blue", "resi 230 & chain A")

cmd.select ("Outward", "resi 230 & chain A", merge=1)

cmd.color ("red", "resi 231 & chain A")

cmd.select ("Inward", "resi 231 & chain A", merge=1)

cmd.color ("blue", "resi 251 & chain A")

cmd.select ("Outward", "resi 251 & chain A", merge=1)

cmd.color ("red", "resi 252 & chain A")

cmd.select ("Inward", "resi 252 & chain A", merge=1)

cmd.color ("blue", "resi 253 & chain A")

cmd.select ("Outward", "resi 253 & chain A", merge=1)

cmd.color ("red", "resi 254 & chain A")

cmd.select ("Inward", "resi 254 & chain A", merge=1)

cmd.color ("blue", "resi 255 & chain A")

cmd.select ("Outward", "resi 255 & chain A", merge=1)

cmd.color ("red", "resi 256 & chain A")

cmd.select ("Inward", "resi 256 & chain A", merge=1)

cmd.color ("blue", "resi 257 & chain A")

cmd.select ("Outward", "resi 257 & chain A", merge=1)

cmd.color ("red", "resi 258 & chain A")

cmd.select ("Inward", "resi 258 & chain A", merge=1)

cmd.color ("blue", "resi 259 & chain A")

cmd.select ("Outward", "resi 259 & chain A", merge=1)

cmd.color ("red", "resi 260 & chain A")

cmd.select ("Inward", "resi 260 & chain A", merge=1)

cmd.color ("blue", "resi 261 & chain A")

cmd.select ("Outward", "resi 261 & chain A", merge=1)

cmd.color ("red", "resi 262 & chain A")

cmd.select ("Inward", "resi 262 & chain A", merge=1)

cmd.color ("blue", "resi 263 & chain A")

cmd.select ("Outward", "resi 263 & chain A", merge=1)

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

cmd.color ("blue", "resi 272 & chain A")

cmd.select ("Outward", "resi 272 & chain A", merge=1)

cmd.color ("red", "resi 273 & chain A")

cmd.select ("Inward", "resi 273 & chain A", merge=1)

cmd.color ("blue", "resi 274 & chain A")

cmd.select ("Outward", "resi 274 & chain A", merge=1)

cmd.color ("red", "resi 275 & chain A")

cmd.select ("Inward", "resi 275 & chain A", merge=1)

cmd.color ("red", "resi 285 & chain A")

cmd.select ("Inward", "resi 285 & chain A", merge=1)

cmd.color ("blue", "resi 286 & chain A")

cmd.select ("Outward", "resi 286 & chain A", merge=1)

cmd.color ("red", "resi 287 & chain A")

cmd.select ("Inward", "resi 287 & chain A", merge=1)

cmd.color ("blue", "resi 288 & chain A")

cmd.select ("Outward", "resi 288 & chain A", merge=1)

cmd.color ("red", "resi 289 & chain A")

cmd.select ("Inward", "resi 289 & chain A", merge=1)

cmd.color ("blue", "resi 290 & chain A")

cmd.select ("Outward", "resi 290 & chain A", merge=1)

cmd.color ("red", "resi 291 & chain A")

cmd.select ("Inward", "resi 291 & chain A", merge=1)

cmd.color ("blue", "resi 292 & chain A")

cmd.select ("Outward", "resi 292 & chain A", merge=1)

cmd.color ("red", "resi 293 & chain A")

cmd.select ("Inward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("red", "resi 295 & chain A")

cmd.select ("Inward", "resi 295 & chain A", merge=1)

cmd.load_cgo( [9.0, 40.493336,20.378584,23.933418, 40.493336, 20.378584, 23.933418, 1, 1,1,0,0,0,1], "axis" )
