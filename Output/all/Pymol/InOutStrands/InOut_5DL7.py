from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19+20+21 & chain A ")


cmd.select("Astrand23", "resi 391+392+393+394+395+396+397+398+399+400+401+402+403 & chain A ")


cmd.select("Astrand2", "resi 51+52+53+54+55+56+57+58+59+60+61+62+63+64 & chain A ")


cmd.select("Astrand3", "resi 90+91+92+93+94+95+96+97+98+99+100+101+102 & chain A ")


cmd.select("Astrand4", "resi 105+106+107+108+109+110+111+112 & chain A ")


cmd.select("Astrand7", "resi 130+131+132+133+134+135+136+137+138 & chain A ")


cmd.select("Astrand11", "resi 183+184+185+186+187+188+189+190+191 & chain A ")


cmd.select("Astrand12", "resi 195+196+197+198+199+200+201+202+203+204 & chain A ")


cmd.select("Astrand13", "resi 208+209+210+211+212+213+214+215+216+217+218+219+220 & chain A ")


cmd.select("Astrand14", "resi 225+226+227+228+229+230+231+232+233+234+235+236+237+238 & chain A ")


cmd.select("Astrand15", "resi 248+249+250+251+252+253+254+255+256+257+258+259+260 & chain A ")


cmd.select("Astrand16", "resi 263+264+265+266+267+268+269+270+271+272+273 & chain A ")


cmd.select("Astrand8", "resi 144+145+146+147+148+149+150+151+152+153+154+155 & chain A ")


cmd.select("Astrand17", "resi 303+304+305+306+307+308+309+310+311+312 & chain A ")


cmd.select("Astrand20", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338 & chain A ")


cmd.select("Astrand21", "resi 348+349+350+351+352+353+354+355+356+357+358+359+360 & chain A ")


cmd.select("Astrand22", "resi 369+370+371+372+373+374+375+376+377+378+379+380 & chain A ")


cmd.select("Astrand1", "resi 31+32+33+34+35+36+37+38+39+40+41+42+43 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 14 & chain A")

cmd.select ("Outward", "resi 14 & chain A", merge=1)

cmd.color ("red", "resi 15 & chain A")

cmd.select ("Inward", "resi 15 & chain A", merge=1)

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

cmd.color ("blue", "resi 21 & chain A")

cmd.select ("Outward", "resi 21 & chain A", merge=1)

cmd.color ("red", "resi 391 & chain A")

cmd.select ("Inward", "resi 391 & chain A", merge=1)

cmd.color ("blue", "resi 392 & chain A")

cmd.select ("Outward", "resi 392 & chain A", merge=1)

cmd.color ("red", "resi 393 & chain A")

cmd.select ("Inward", "resi 393 & chain A", merge=1)

cmd.color ("blue", "resi 394 & chain A")

cmd.select ("Outward", "resi 394 & chain A", merge=1)

cmd.color ("red", "resi 395 & chain A")

cmd.select ("Inward", "resi 395 & chain A", merge=1)

cmd.color ("blue", "resi 396 & chain A")

cmd.select ("Outward", "resi 396 & chain A", merge=1)

cmd.color ("red", "resi 397 & chain A")

cmd.select ("Inward", "resi 397 & chain A", merge=1)

cmd.color ("blue", "resi 398 & chain A")

cmd.select ("Outward", "resi 398 & chain A", merge=1)

cmd.color ("red", "resi 399 & chain A")

cmd.select ("Inward", "resi 399 & chain A", merge=1)

cmd.color ("blue", "resi 400 & chain A")

cmd.select ("Outward", "resi 400 & chain A", merge=1)

cmd.color ("red", "resi 401 & chain A")

cmd.select ("Inward", "resi 401 & chain A", merge=1)

cmd.color ("blue", "resi 402 & chain A")

cmd.select ("Outward", "resi 402 & chain A", merge=1)

cmd.color ("red", "resi 403 & chain A")

cmd.select ("Inward", "resi 403 & chain A", merge=1)

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

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("red", "resi 62 & chain A")

cmd.select ("Inward", "resi 62 & chain A", merge=1)

cmd.color ("blue", "resi 63 & chain A")

cmd.select ("Outward", "resi 63 & chain A", merge=1)

cmd.color ("blue", "resi 64 & chain A")

cmd.select ("Outward", "resi 64 & chain A", merge=1)

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

cmd.color ("blue", "resi 101 & chain A")

cmd.select ("Outward", "resi 101 & chain A", merge=1)

cmd.color ("blue", "resi 102 & chain A")

cmd.select ("Outward", "resi 102 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("red", "resi 106 & chain A")

cmd.select ("Inward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("red", "resi 108 & chain A")

cmd.select ("Inward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("red", "resi 112 & chain A")

cmd.select ("Inward", "resi 112 & chain A", merge=1)

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

cmd.color ("red", "resi 183 & chain A")

cmd.select ("Inward", "resi 183 & chain A", merge=1)

cmd.color ("blue", "resi 184 & chain A")

cmd.select ("Outward", "resi 184 & chain A", merge=1)

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

cmd.color ("red", "resi 208 & chain A")

cmd.select ("Inward", "resi 208 & chain A", merge=1)

cmd.color ("blue", "resi 209 & chain A")

cmd.select ("Outward", "resi 209 & chain A", merge=1)

cmd.color ("red", "resi 210 & chain A")

cmd.select ("Inward", "resi 210 & chain A", merge=1)

cmd.color ("blue", "resi 211 & chain A")

cmd.select ("Outward", "resi 211 & chain A", merge=1)

cmd.color ("red", "resi 212 & chain A")

cmd.select ("Inward", "resi 212 & chain A", merge=1)

cmd.color ("blue", "resi 213 & chain A")

cmd.select ("Outward", "resi 213 & chain A", merge=1)

cmd.color ("red", "resi 214 & chain A")

cmd.select ("Inward", "resi 214 & chain A", merge=1)

cmd.color ("blue", "resi 215 & chain A")

cmd.select ("Outward", "resi 215 & chain A", merge=1)

cmd.color ("red", "resi 216 & chain A")

cmd.select ("Inward", "resi 216 & chain A", merge=1)

cmd.color ("blue", "resi 217 & chain A")

cmd.select ("Outward", "resi 217 & chain A", merge=1)

cmd.color ("red", "resi 218 & chain A")

cmd.select ("Inward", "resi 218 & chain A", merge=1)

cmd.color ("red", "resi 219 & chain A")

cmd.select ("Inward", "resi 219 & chain A", merge=1)

cmd.color ("blue", "resi 220 & chain A")

cmd.select ("Outward", "resi 220 & chain A", merge=1)

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

cmd.color ("blue", "resi 238 & chain A")

cmd.select ("Outward", "resi 238 & chain A", merge=1)

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

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

cmd.color ("blue", "resi 153 & chain A")

cmd.select ("Outward", "resi 153 & chain A", merge=1)

cmd.color ("red", "resi 154 & chain A")

cmd.select ("Inward", "resi 154 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 303 & chain A")

cmd.select ("Outward", "resi 303 & chain A", merge=1)

cmd.color ("red", "resi 304 & chain A")

cmd.select ("Inward", "resi 304 & chain A", merge=1)

cmd.color ("blue", "resi 305 & chain A")

cmd.select ("Outward", "resi 305 & chain A", merge=1)

cmd.color ("red", "resi 306 & chain A")

cmd.select ("Inward", "resi 306 & chain A", merge=1)

cmd.color ("blue", "resi 307 & chain A")

cmd.select ("Outward", "resi 307 & chain A", merge=1)

cmd.color ("red", "resi 308 & chain A")

cmd.select ("Inward", "resi 308 & chain A", merge=1)

cmd.color ("blue", "resi 309 & chain A")

cmd.select ("Outward", "resi 309 & chain A", merge=1)

cmd.color ("red", "resi 310 & chain A")

cmd.select ("Inward", "resi 310 & chain A", merge=1)

cmd.color ("blue", "resi 311 & chain A")

cmd.select ("Outward", "resi 311 & chain A", merge=1)

cmd.color ("red", "resi 312 & chain A")

cmd.select ("Inward", "resi 312 & chain A", merge=1)

cmd.color ("blue", "resi 326 & chain A")

cmd.select ("Outward", "resi 326 & chain A", merge=1)

cmd.color ("red", "resi 327 & chain A")

cmd.select ("Inward", "resi 327 & chain A", merge=1)

cmd.color ("blue", "resi 328 & chain A")

cmd.select ("Outward", "resi 328 & chain A", merge=1)

cmd.color ("red", "resi 329 & chain A")

cmd.select ("Inward", "resi 329 & chain A", merge=1)

cmd.color ("blue", "resi 330 & chain A")

cmd.select ("Outward", "resi 330 & chain A", merge=1)

cmd.color ("red", "resi 331 & chain A")

cmd.select ("Inward", "resi 331 & chain A", merge=1)

cmd.color ("blue", "resi 332 & chain A")

cmd.select ("Outward", "resi 332 & chain A", merge=1)

cmd.color ("red", "resi 333 & chain A")

cmd.select ("Inward", "resi 333 & chain A", merge=1)

cmd.color ("blue", "resi 334 & chain A")

cmd.select ("Outward", "resi 334 & chain A", merge=1)

cmd.color ("red", "resi 335 & chain A")

cmd.select ("Inward", "resi 335 & chain A", merge=1)

cmd.color ("blue", "resi 336 & chain A")

cmd.select ("Outward", "resi 336 & chain A", merge=1)

cmd.color ("blue", "resi 337 & chain A")

cmd.select ("Outward", "resi 337 & chain A", merge=1)

cmd.color ("red", "resi 338 & chain A")

cmd.select ("Inward", "resi 338 & chain A", merge=1)

cmd.color ("red", "resi 348 & chain A")

cmd.select ("Inward", "resi 348 & chain A", merge=1)

cmd.color ("blue", "resi 349 & chain A")

cmd.select ("Outward", "resi 349 & chain A", merge=1)

cmd.color ("red", "resi 350 & chain A")

cmd.select ("Inward", "resi 350 & chain A", merge=1)

cmd.color ("blue", "resi 351 & chain A")

cmd.select ("Outward", "resi 351 & chain A", merge=1)

cmd.color ("red", "resi 352 & chain A")

cmd.select ("Inward", "resi 352 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("red", "resi 354 & chain A")

cmd.select ("Inward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("red", "resi 356 & chain A")

cmd.select ("Inward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("red", "resi 358 & chain A")

cmd.select ("Inward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("red", "resi 360 & chain A")

cmd.select ("Inward", "resi 360 & chain A", merge=1)

cmd.color ("blue", "resi 369 & chain A")

cmd.select ("Outward", "resi 369 & chain A", merge=1)

cmd.color ("red", "resi 370 & chain A")

cmd.select ("Inward", "resi 370 & chain A", merge=1)

cmd.color ("blue", "resi 371 & chain A")

cmd.select ("Outward", "resi 371 & chain A", merge=1)

cmd.color ("red", "resi 372 & chain A")

cmd.select ("Inward", "resi 372 & chain A", merge=1)

cmd.color ("blue", "resi 373 & chain A")

cmd.select ("Outward", "resi 373 & chain A", merge=1)

cmd.color ("red", "resi 374 & chain A")

cmd.select ("Inward", "resi 374 & chain A", merge=1)

cmd.color ("blue", "resi 375 & chain A")

cmd.select ("Outward", "resi 375 & chain A", merge=1)

cmd.color ("red", "resi 376 & chain A")

cmd.select ("Inward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 377 & chain A")

cmd.select ("Outward", "resi 377 & chain A", merge=1)

cmd.color ("red", "resi 378 & chain A")

cmd.select ("Inward", "resi 378 & chain A", merge=1)

cmd.color ("blue", "resi 379 & chain A")

cmd.select ("Outward", "resi 379 & chain A", merge=1)

cmd.color ("red", "resi 380 & chain A")

cmd.select ("Inward", "resi 380 & chain A", merge=1)

cmd.color ("red", "resi 31 & chain A")

cmd.select ("Inward", "resi 31 & chain A", merge=1)

cmd.color ("blue", "resi 32 & chain A")

cmd.select ("Outward", "resi 32 & chain A", merge=1)

cmd.color ("red", "resi 33 & chain A")

cmd.select ("Inward", "resi 33 & chain A", merge=1)

cmd.color ("blue", "resi 34 & chain A")

cmd.select ("Outward", "resi 34 & chain A", merge=1)

cmd.color ("red", "resi 35 & chain A")

cmd.select ("Inward", "resi 35 & chain A", merge=1)

cmd.color ("blue", "resi 36 & chain A")

cmd.select ("Outward", "resi 36 & chain A", merge=1)

cmd.color ("red", "resi 37 & chain A")

cmd.select ("Inward", "resi 37 & chain A", merge=1)

cmd.color ("blue", "resi 38 & chain A")

cmd.select ("Outward", "resi 38 & chain A", merge=1)

cmd.color ("red", "resi 39 & chain A")

cmd.select ("Inward", "resi 39 & chain A", merge=1)

cmd.color ("blue", "resi 40 & chain A")

cmd.select ("Outward", "resi 40 & chain A", merge=1)

cmd.color ("red", "resi 41 & chain A")

cmd.select ("Inward", "resi 41 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("red", "resi 43 & chain A")

cmd.select ("Inward", "resi 43 & chain A", merge=1)

cmd.load_cgo( [9.0, -2.8926113,-47.464886,-23.482277, -2.8926113, -47.464886, -23.482277, 1, 1,1,0,0,0,1], "axis" )
