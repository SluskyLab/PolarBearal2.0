from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13+14+15+16+17+18+19+20+21+22+23+24 & chain A ")


cmd.select("Astrand1", "resi 32+33+34+35+36+37+38+39+40+41+42+43+44 & chain A ")


cmd.select("Astrand3", "resi 57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+72 & chain A ")


cmd.select("Astrand2", "resi 96+97+98+99+100+101+102+103+104+105+106+48+107+49+108+50+51+52+53+54 & chain A ")


cmd.select("Astrand7", "resi 111+112+113+114+115+116+117+118 & chain A ")


cmd.select("Astrand8", "resi 136+137+138+139+140+141+142+143+144+145 & chain A ")


cmd.select("Astrand9", "resi 150+151+152+153+154+155+156+157+158+159+160+161 & chain A ")


cmd.select("Astrand12", "resi 185+186+187+188+189+190+191+192+193 & chain A ")


cmd.select("Astrand13", "resi 198+199+200+201+202+203+204+205+206+207 & chain A ")


cmd.select("Astrand14", "resi 211+212+213+214+215+216+217+218+219+220+221+222+223 & chain A ")


cmd.select("Astrand15", "resi 228+229+230+231+232+233+234+235+236+237+238+239+240 & chain A ")


cmd.select("Astrand16", "resi 248+249+250+251+252+253+254+255+256+257+258+259+260 & chain A ")


cmd.select("Astrand17", "resi 263+264+265+266+267+268+269+270+271+272+273 & chain A ")


cmd.select("Astrand18", "resi 304+305+306+307+308+309+310+311+312+313 & chain A ")


cmd.select("Astrand19", "resi 321+322+323+324+325+326+327+328+329+330+331+332+333+334 & chain A ")


cmd.select("Astrand20", "resi 340+341+342+343+344+345+346+347+348+349+350+351+352+353 & chain A ")


cmd.select("Astrand21", "resi 362+363+364+365+366+367+368+369+370+371+372+373 & chain A ")


cmd.select("Astrand22", "resi 379+380+381+382+383+384+385+386+387+388+389+390+391 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("red", "resi 24 & chain A")

cmd.select ("Inward", "resi 24 & chain A", merge=1)

cmd.color ("red", "resi 32 & chain A")

cmd.select ("Inward", "resi 32 & chain A", merge=1)

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

cmd.color ("red", "resi 44 & chain A")

cmd.select ("Inward", "resi 44 & chain A", merge=1)

cmd.color ("red", "resi 57 & chain A")

cmd.select ("Inward", "resi 57 & chain A", merge=1)

cmd.color ("red", "resi 58 & chain A")

cmd.select ("Inward", "resi 58 & chain A", merge=1)

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

cmd.color ("red", "resi 66 & chain A")

cmd.select ("Inward", "resi 66 & chain A", merge=1)

cmd.color ("blue", "resi 67 & chain A")

cmd.select ("Outward", "resi 67 & chain A", merge=1)

cmd.color ("red", "resi 68 & chain A")

cmd.select ("Inward", "resi 68 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

cmd.color ("red", "resi 70 & chain A")

cmd.select ("Inward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.color ("blue", "resi 72 & chain A")

cmd.select ("Outward", "resi 72 & chain A", merge=1)

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

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("red", "resi 107 & chain A")

cmd.select ("Inward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 49 & chain A")

cmd.select ("Outward", "resi 49 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

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

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("red", "resi 112 & chain A")

cmd.select ("Inward", "resi 112 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("red", "resi 114 & chain A")

cmd.select ("Inward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 115 & chain A")

cmd.select ("Outward", "resi 115 & chain A", merge=1)

cmd.color ("blue", "resi 116 & chain A")

cmd.select ("Outward", "resi 116 & chain A", merge=1)

cmd.color ("blue", "resi 117 & chain A")

cmd.select ("Outward", "resi 117 & chain A", merge=1)

cmd.color ("red", "resi 118 & chain A")

cmd.select ("Inward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 136 & chain A")

cmd.select ("Outward", "resi 136 & chain A", merge=1)

cmd.color ("red", "resi 137 & chain A")

cmd.select ("Inward", "resi 137 & chain A", merge=1)

cmd.color ("blue", "resi 138 & chain A")

cmd.select ("Outward", "resi 138 & chain A", merge=1)

cmd.color ("red", "resi 139 & chain A")

cmd.select ("Inward", "resi 139 & chain A", merge=1)

cmd.color ("blue", "resi 140 & chain A")

cmd.select ("Outward", "resi 140 & chain A", merge=1)

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

cmd.color ("blue", "resi 156 & chain A")

cmd.select ("Outward", "resi 156 & chain A", merge=1)

cmd.color ("red", "resi 157 & chain A")

cmd.select ("Inward", "resi 157 & chain A", merge=1)

cmd.color ("blue", "resi 158 & chain A")

cmd.select ("Outward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("red", "resi 160 & chain A")

cmd.select ("Inward", "resi 160 & chain A", merge=1)

cmd.color ("blue", "resi 161 & chain A")

cmd.select ("Outward", "resi 161 & chain A", merge=1)

cmd.color ("red", "resi 185 & chain A")

cmd.select ("Inward", "resi 185 & chain A", merge=1)

cmd.color ("blue", "resi 186 & chain A")

cmd.select ("Outward", "resi 186 & chain A", merge=1)

cmd.color ("red", "resi 187 & chain A")

cmd.select ("Inward", "resi 187 & chain A", merge=1)

cmd.color ("blue", "resi 188 & chain A")

cmd.select ("Outward", "resi 188 & chain A", merge=1)

cmd.color ("red", "resi 189 & chain A")

cmd.select ("Inward", "resi 189 & chain A", merge=1)

cmd.color ("blue", "resi 190 & chain A")

cmd.select ("Outward", "resi 190 & chain A", merge=1)

cmd.color ("red", "resi 191 & chain A")

cmd.select ("Inward", "resi 191 & chain A", merge=1)

cmd.color ("blue", "resi 192 & chain A")

cmd.select ("Outward", "resi 192 & chain A", merge=1)

cmd.color ("blue", "resi 193 & chain A")

cmd.select ("Outward", "resi 193 & chain A", merge=1)

cmd.color ("blue", "resi 198 & chain A")

cmd.select ("Outward", "resi 198 & chain A", merge=1)

cmd.color ("red", "resi 199 & chain A")

cmd.select ("Inward", "resi 199 & chain A", merge=1)

cmd.color ("blue", "resi 200 & chain A")

cmd.select ("Outward", "resi 200 & chain A", merge=1)

cmd.color ("red", "resi 201 & chain A")

cmd.select ("Inward", "resi 201 & chain A", merge=1)

cmd.color ("blue", "resi 202 & chain A")

cmd.select ("Outward", "resi 202 & chain A", merge=1)

cmd.color ("red", "resi 203 & chain A")

cmd.select ("Inward", "resi 203 & chain A", merge=1)

cmd.color ("blue", "resi 204 & chain A")

cmd.select ("Outward", "resi 204 & chain A", merge=1)

cmd.color ("red", "resi 205 & chain A")

cmd.select ("Inward", "resi 205 & chain A", merge=1)

cmd.color ("blue", "resi 206 & chain A")

cmd.select ("Outward", "resi 206 & chain A", merge=1)

cmd.color ("red", "resi 207 & chain A")

cmd.select ("Inward", "resi 207 & chain A", merge=1)

cmd.color ("red", "resi 211 & chain A")

cmd.select ("Inward", "resi 211 & chain A", merge=1)

cmd.color ("blue", "resi 212 & chain A")

cmd.select ("Outward", "resi 212 & chain A", merge=1)

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

cmd.color ("blue", "resi 223 & chain A")

cmd.select ("Outward", "resi 223 & chain A", merge=1)

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

cmd.color ("red", "resi 238 & chain A")

cmd.select ("Inward", "resi 238 & chain A", merge=1)

cmd.color ("blue", "resi 239 & chain A")

cmd.select ("Outward", "resi 239 & chain A", merge=1)

cmd.color ("blue", "resi 240 & chain A")

cmd.select ("Outward", "resi 240 & chain A", merge=1)

cmd.color ("red", "resi 248 & chain A")

cmd.select ("Inward", "resi 248 & chain A", merge=1)

cmd.color ("red", "resi 249 & chain A")

cmd.select ("Inward", "resi 249 & chain A", merge=1)

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

cmd.color ("red", "resi 251 & chain A")

cmd.select ("Inward", "resi 251 & chain A", merge=1)

cmd.color ("blue", "resi 252 & chain A")

cmd.select ("Outward", "resi 252 & chain A", merge=1)

cmd.color ("red", "resi 253 & chain A")

cmd.select ("Inward", "resi 253 & chain A", merge=1)

cmd.color ("blue", "resi 254 & chain A")

cmd.select ("Outward", "resi 254 & chain A", merge=1)

cmd.color ("red", "resi 255 & chain A")

cmd.select ("Inward", "resi 255 & chain A", merge=1)

cmd.color ("blue", "resi 256 & chain A")

cmd.select ("Outward", "resi 256 & chain A", merge=1)

cmd.color ("red", "resi 257 & chain A")

cmd.select ("Inward", "resi 257 & chain A", merge=1)

cmd.color ("blue", "resi 258 & chain A")

cmd.select ("Outward", "resi 258 & chain A", merge=1)

cmd.color ("red", "resi 259 & chain A")

cmd.select ("Inward", "resi 259 & chain A", merge=1)

cmd.color ("blue", "resi 260 & chain A")

cmd.select ("Outward", "resi 260 & chain A", merge=1)

cmd.color ("blue", "resi 263 & chain A")

cmd.select ("Outward", "resi 263 & chain A", merge=1)

cmd.color ("red", "resi 264 & chain A")

cmd.select ("Inward", "resi 264 & chain A", merge=1)

cmd.color ("blue", "resi 265 & chain A")

cmd.select ("Outward", "resi 265 & chain A", merge=1)

cmd.color ("red", "resi 266 & chain A")

cmd.select ("Inward", "resi 266 & chain A", merge=1)

cmd.color ("blue", "resi 267 & chain A")

cmd.select ("Outward", "resi 267 & chain A", merge=1)

cmd.color ("red", "resi 268 & chain A")

cmd.select ("Inward", "resi 268 & chain A", merge=1)

cmd.color ("blue", "resi 269 & chain A")

cmd.select ("Outward", "resi 269 & chain A", merge=1)

cmd.color ("red", "resi 270 & chain A")

cmd.select ("Inward", "resi 270 & chain A", merge=1)

cmd.color ("blue", "resi 271 & chain A")

cmd.select ("Outward", "resi 271 & chain A", merge=1)

cmd.color ("red", "resi 272 & chain A")

cmd.select ("Inward", "resi 272 & chain A", merge=1)

cmd.color ("blue", "resi 273 & chain A")

cmd.select ("Outward", "resi 273 & chain A", merge=1)

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

cmd.color ("red", "resi 305 & chain A")

cmd.select ("Inward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 306 & chain A")

cmd.select ("Outward", "resi 306 & chain A", merge=1)

cmd.color ("red", "resi 307 & chain A")

cmd.select ("Inward", "resi 307 & chain A", merge=1)

cmd.color ("blue", "resi 308 & chain A")

cmd.select ("Outward", "resi 308 & chain A", merge=1)

cmd.color ("red", "resi 309 & chain A")

cmd.select ("Inward", "resi 309 & chain A", merge=1)

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

cmd.color ("red", "resi 311 & chain A")

cmd.select ("Inward", "resi 311 & chain A", merge=1)

cmd.color ("blue", "resi 312 & chain A")

cmd.select ("Outward", "resi 312 & chain A", merge=1)

cmd.color ("red", "resi 313 & chain A")

cmd.select ("Inward", "resi 313 & chain A", merge=1)

cmd.color ("blue", "resi 321 & chain A")

cmd.select ("Outward", "resi 321 & chain A", merge=1)

cmd.color ("red", "resi 322 & chain A")

cmd.select ("Inward", "resi 322 & chain A", merge=1)

cmd.color ("blue", "resi 323 & chain A")

cmd.select ("Outward", "resi 323 & chain A", merge=1)

cmd.color ("red", "resi 324 & chain A")

cmd.select ("Inward", "resi 324 & chain A", merge=1)

cmd.color ("blue", "resi 325 & chain A")

cmd.select ("Outward", "resi 325 & chain A", merge=1)

cmd.color ("red", "resi 326 & chain A")

cmd.select ("Inward", "resi 326 & chain A", merge=1)

cmd.color ("blue", "resi 327 & chain A")

cmd.select ("Outward", "resi 327 & chain A", merge=1)

cmd.color ("red", "resi 328 & chain A")

cmd.select ("Inward", "resi 328 & chain A", merge=1)

cmd.color ("blue", "resi 329 & chain A")

cmd.select ("Outward", "resi 329 & chain A", merge=1)

cmd.color ("red", "resi 330 & chain A")

cmd.select ("Inward", "resi 330 & chain A", merge=1)

cmd.color ("blue", "resi 331 & chain A")

cmd.select ("Outward", "resi 331 & chain A", merge=1)

cmd.color ("blue", "resi 332 & chain A")

cmd.select ("Outward", "resi 332 & chain A", merge=1)

cmd.color ("red", "resi 333 & chain A")

cmd.select ("Inward", "resi 333 & chain A", merge=1)

cmd.color ("blue", "resi 334 & chain A")

cmd.select ("Outward", "resi 334 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("red", "resi 341 & chain A")

cmd.select ("Inward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("red", "resi 343 & chain A")

cmd.select ("Inward", "resi 343 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("red", "resi 345 & chain A")

cmd.select ("Inward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("red", "resi 347 & chain A")

cmd.select ("Inward", "resi 347 & chain A", merge=1)

cmd.color ("blue", "resi 348 & chain A")

cmd.select ("Outward", "resi 348 & chain A", merge=1)

cmd.color ("red", "resi 349 & chain A")

cmd.select ("Inward", "resi 349 & chain A", merge=1)

cmd.color ("blue", "resi 350 & chain A")

cmd.select ("Outward", "resi 350 & chain A", merge=1)

cmd.color ("red", "resi 351 & chain A")

cmd.select ("Inward", "resi 351 & chain A", merge=1)

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("red", "resi 353 & chain A")

cmd.select ("Inward", "resi 353 & chain A", merge=1)

cmd.color ("blue", "resi 362 & chain A")

cmd.select ("Outward", "resi 362 & chain A", merge=1)

cmd.color ("red", "resi 363 & chain A")

cmd.select ("Inward", "resi 363 & chain A", merge=1)

cmd.color ("blue", "resi 364 & chain A")

cmd.select ("Outward", "resi 364 & chain A", merge=1)

cmd.color ("red", "resi 365 & chain A")

cmd.select ("Inward", "resi 365 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("red", "resi 367 & chain A")

cmd.select ("Inward", "resi 367 & chain A", merge=1)

cmd.color ("blue", "resi 368 & chain A")

cmd.select ("Outward", "resi 368 & chain A", merge=1)

cmd.color ("red", "resi 369 & chain A")

cmd.select ("Inward", "resi 369 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("red", "resi 371 & chain A")

cmd.select ("Inward", "resi 371 & chain A", merge=1)

cmd.color ("blue", "resi 372 & chain A")

cmd.select ("Outward", "resi 372 & chain A", merge=1)

cmd.color ("red", "resi 373 & chain A")

cmd.select ("Inward", "resi 373 & chain A", merge=1)

cmd.color ("red", "resi 379 & chain A")

cmd.select ("Inward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("red", "resi 381 & chain A")

cmd.select ("Inward", "resi 381 & chain A", merge=1)

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("red", "resi 383 & chain A")

cmd.select ("Inward", "resi 383 & chain A", merge=1)

cmd.color ("blue", "resi 384 & chain A")

cmd.select ("Outward", "resi 384 & chain A", merge=1)

cmd.color ("red", "resi 385 & chain A")

cmd.select ("Inward", "resi 385 & chain A", merge=1)

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("red", "resi 387 & chain A")

cmd.select ("Inward", "resi 387 & chain A", merge=1)

cmd.color ("blue", "resi 388 & chain A")

cmd.select ("Outward", "resi 388 & chain A", merge=1)

cmd.color ("red", "resi 389 & chain A")

cmd.select ("Inward", "resi 389 & chain A", merge=1)

cmd.color ("blue", "resi 390 & chain A")

cmd.select ("Outward", "resi 390 & chain A", merge=1)

cmd.color ("red", "resi 391 & chain A")

cmd.select ("Inward", "resi 391 & chain A", merge=1)

cmd.load_cgo( [9.0, -40.172832,12.244389,-31.49533, -40.172832, 12.244389, -31.49533, 1, 1,1,0,0,0,1], "axis" )
