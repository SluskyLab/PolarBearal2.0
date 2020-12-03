from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5MDO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35 & chain A ")


cmd.select("Astrand1", "resi 47+48+49+50+51+52+55+56+57+58+59+60+61+62 & chain A ")


cmd.select("Astrand16", "resi 292+293+294+295+296+297+298+299+300+301+302+303+304 & chain A ")


cmd.select("Astrand13", "resi 268+269+270+271+272+273+274+275+276+277 & chain A ")


cmd.select("Astrand3", "resi 70+71+72+73+74+75+76 & chain A ")


cmd.select("Astrand4", "resi 96+97+98+99+100+101+102 & chain A ")


cmd.select("Astrand5", "resi 106+107+108+109+110+111+112+113+114 & chain A ")


cmd.select("Astrand6", "resi 148+149+150+151+152+153+154+155+156 & chain A ")


cmd.select("Astrand7", "resi 164+165+166+167+168+169+170+171+172 & chain A ")


cmd.select("Astrand8", "resi 184+185+186+187+188+189+190+191+192+193+194 & chain A ")


cmd.select("Astrand10", "resi 214+215+216+217+218+219+220+221+222+223+224+225+226+227+228 & chain A ")


cmd.select("Astrand9", "resi 197+198+199+200+201+202+203+204+205+206+207+208+209+210+211 & chain A ")


cmd.select("Astrand11", "resi 233+234+235+236+237+238+239+240+241+242+243+244+245+246 & chain A ")


cmd.select("Astrand12", "resi 251+252+253+254+255+256+257+258+259+260+261+262+263+264+265 & chain A ")


cmd.select("Astrand17", "resi 307+308+309+310+311+312+313+314+315+316+317 & chain A ")


cmd.select("Astrand18", "resi 338+339+340+341+342+343+344+345+346+347+348+349 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 25 & chain A")

cmd.select ("Outward", "resi 25 & chain A", merge=1)

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

cmd.color ("blue", "resi 31 & chain A")

cmd.select ("Outward", "resi 31 & chain A", merge=1)

cmd.color ("red", "resi 32 & chain A")

cmd.select ("Inward", "resi 32 & chain A", merge=1)

cmd.color ("blue", "resi 33 & chain A")

cmd.select ("Outward", "resi 33 & chain A", merge=1)

cmd.color ("red", "resi 34 & chain A")

cmd.select ("Inward", "resi 34 & chain A", merge=1)

cmd.color ("blue", "resi 35 & chain A")

cmd.select ("Outward", "resi 35 & chain A", merge=1)

cmd.color ("red", "resi 47 & chain A")

cmd.select ("Inward", "resi 47 & chain A", merge=1)

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

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("red", "resi 62 & chain A")

cmd.select ("Inward", "resi 62 & chain A", merge=1)

cmd.color ("red", "resi 292 & chain A")

cmd.select ("Inward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("red", "resi 294 & chain A")

cmd.select ("Inward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("red", "resi 296 & chain A")

cmd.select ("Inward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("red", "resi 298 & chain A")

cmd.select ("Inward", "resi 298 & chain A", merge=1)

cmd.color ("blue", "resi 299 & chain A")

cmd.select ("Outward", "resi 299 & chain A", merge=1)

cmd.color ("red", "resi 300 & chain A")

cmd.select ("Inward", "resi 300 & chain A", merge=1)

cmd.color ("blue", "resi 301 & chain A")

cmd.select ("Outward", "resi 301 & chain A", merge=1)

cmd.color ("blue", "resi 302 & chain A")

cmd.select ("Outward", "resi 302 & chain A", merge=1)

cmd.color ("red", "resi 303 & chain A")

cmd.select ("Inward", "resi 303 & chain A", merge=1)

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

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

cmd.color ("blue", "resi 276 & chain A")

cmd.select ("Outward", "resi 276 & chain A", merge=1)

cmd.color ("red", "resi 277 & chain A")

cmd.select ("Inward", "resi 277 & chain A", merge=1)

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

cmd.color ("red", "resi 96 & chain A")

cmd.select ("Inward", "resi 96 & chain A", merge=1)

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

cmd.color ("red", "resi 106 & chain A")

cmd.select ("Inward", "resi 106 & chain A", merge=1)

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

cmd.color ("blue", "resi 112 & chain A")

cmd.select ("Outward", "resi 112 & chain A", merge=1)

cmd.color ("red", "resi 113 & chain A")

cmd.select ("Inward", "resi 113 & chain A", merge=1)

cmd.color ("blue", "resi 114 & chain A")

cmd.select ("Outward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 148 & chain A")

cmd.select ("Outward", "resi 148 & chain A", merge=1)

cmd.color ("red", "resi 149 & chain A")

cmd.select ("Inward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("red", "resi 151 & chain A")

cmd.select ("Inward", "resi 151 & chain A", merge=1)

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

cmd.color ("blue", "resi 192 & chain A")

cmd.select ("Outward", "resi 192 & chain A", merge=1)

cmd.color ("blue", "resi 193 & chain A")

cmd.select ("Outward", "resi 193 & chain A", merge=1)

cmd.color ("red", "resi 194 & chain A")

cmd.select ("Inward", "resi 194 & chain A", merge=1)

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

cmd.color ("blue", "resi 205 & chain A")

cmd.select ("Outward", "resi 205 & chain A", merge=1)

cmd.color ("red", "resi 206 & chain A")

cmd.select ("Inward", "resi 206 & chain A", merge=1)

cmd.color ("blue", "resi 207 & chain A")

cmd.select ("Outward", "resi 207 & chain A", merge=1)

cmd.color ("blue", "resi 208 & chain A")

cmd.select ("Outward", "resi 208 & chain A", merge=1)

cmd.color ("red", "resi 209 & chain A")

cmd.select ("Inward", "resi 209 & chain A", merge=1)

cmd.color ("blue", "resi 210 & chain A")

cmd.select ("Outward", "resi 210 & chain A", merge=1)

cmd.color ("red", "resi 211 & chain A")

cmd.select ("Inward", "resi 211 & chain A", merge=1)

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

cmd.color ("red", "resi 240 & chain A")

cmd.select ("Inward", "resi 240 & chain A", merge=1)

cmd.color ("blue", "resi 241 & chain A")

cmd.select ("Outward", "resi 241 & chain A", merge=1)

cmd.color ("red", "resi 242 & chain A")

cmd.select ("Inward", "resi 242 & chain A", merge=1)

cmd.color ("blue", "resi 243 & chain A")

cmd.select ("Outward", "resi 243 & chain A", merge=1)

cmd.color ("red", "resi 244 & chain A")

cmd.select ("Inward", "resi 244 & chain A", merge=1)

cmd.color ("blue", "resi 245 & chain A")

cmd.select ("Outward", "resi 245 & chain A", merge=1)

cmd.color ("red", "resi 246 & chain A")

cmd.select ("Inward", "resi 246 & chain A", merge=1)

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

cmd.color ("red", "resi 264 & chain A")

cmd.select ("Inward", "resi 264 & chain A", merge=1)

cmd.color ("blue", "resi 265 & chain A")

cmd.select ("Outward", "resi 265 & chain A", merge=1)

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

cmd.color ("blue", "resi 313 & chain A")

cmd.select ("Outward", "resi 313 & chain A", merge=1)

cmd.color ("red", "resi 314 & chain A")

cmd.select ("Inward", "resi 314 & chain A", merge=1)

cmd.color ("blue", "resi 315 & chain A")

cmd.select ("Outward", "resi 315 & chain A", merge=1)

cmd.color ("red", "resi 316 & chain A")

cmd.select ("Inward", "resi 316 & chain A", merge=1)

cmd.color ("blue", "resi 317 & chain A")

cmd.select ("Outward", "resi 317 & chain A", merge=1)

cmd.color ("blue", "resi 338 & chain A")

cmd.select ("Outward", "resi 338 & chain A", merge=1)

cmd.color ("red", "resi 339 & chain A")

cmd.select ("Inward", "resi 339 & chain A", merge=1)

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

cmd.load_cgo( [9.0, -4.3026876,13.851812,34.96881, -4.3026876, 13.851812, 34.96881, 1, 1,1,0,0,0,1], "axis" )
