from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NXR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand1", "resi 9+10+11+12+13+14+15+16+17+18+19+20+21+22+23 & chain A ")


cmd.select("Astrand21", "resi 343+344+345+346+347+348+349+350+351 & chain A ")


cmd.select("Astrand4", "resi 54+55+56+57+58+59+60+61+62+63+64+65 & chain A ")


cmd.select("Astrand20", "resi 316+317+318+319+320+321+322+323+324+325 & chain A ")


cmd.select("Astrand5", "resi 75+76+77+78+79+80+81+82+83+84+85+86 & chain A ")


cmd.select("Astrand19", "resi 298+299+300+301+302+303+304+305+306+307+308+309+310+311 & chain A ")


cmd.select("Astrand6", "resi 90+91+92+93+94+95+96+97+98 & chain A ")


cmd.select("Astrand18", "resi 277+278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")


cmd.select("Astrand7", "resi 129+130+131+132+133+134+135+136+137+138 & chain A ")


cmd.select("Astrand17", "resi 261+262+263+264+265+266+267+268+269+270+271 & chain A ")


cmd.select("Astrand13", "resi 222+223+224+225+226+227+228+229+230+231+232+233+234 & chain A ")


cmd.select("Astrand10", "resi 188+189+190+191+192+193+194+195+196+197+198 & chain A ")


cmd.select("Astrand9", "resi 175+176+177+178+179+180+181+182+183+184+185 & chain A ")


cmd.select("Astrand14", "resi 237+238+239+240+241+242+243+244+245+246+247 & chain A ")


cmd.select("Astrand8", "resi 148+149+150+151+152+153+154+155 & chain A ")


cmd.select("Astrand3", "resi 39+40+41+42+43+44+45+46+47+48+49 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 64 & chain A")

cmd.select ("Outward", "resi 64 & chain A", merge=1)

cmd.color ("blue", "resi 65 & chain A")

cmd.select ("Outward", "resi 65 & chain A", merge=1)

cmd.color ("blue", "resi 316 & chain A")

cmd.select ("Outward", "resi 316 & chain A", merge=1)

cmd.color ("red", "resi 317 & chain A")

cmd.select ("Inward", "resi 317 & chain A", merge=1)

cmd.color ("blue", "resi 318 & chain A")

cmd.select ("Outward", "resi 318 & chain A", merge=1)

cmd.color ("red", "resi 319 & chain A")

cmd.select ("Inward", "resi 319 & chain A", merge=1)

cmd.color ("blue", "resi 320 & chain A")

cmd.select ("Outward", "resi 320 & chain A", merge=1)

cmd.color ("red", "resi 321 & chain A")

cmd.select ("Inward", "resi 321 & chain A", merge=1)

cmd.color ("blue", "resi 322 & chain A")

cmd.select ("Outward", "resi 322 & chain A", merge=1)

cmd.color ("red", "resi 323 & chain A")

cmd.select ("Inward", "resi 323 & chain A", merge=1)

cmd.color ("blue", "resi 324 & chain A")

cmd.select ("Outward", "resi 324 & chain A", merge=1)

cmd.color ("blue", "resi 325 & chain A")

cmd.select ("Outward", "resi 325 & chain A", merge=1)

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

cmd.color ("red", "resi 85 & chain A")

cmd.select ("Inward", "resi 85 & chain A", merge=1)

cmd.color ("blue", "resi 86 & chain A")

cmd.select ("Outward", "resi 86 & chain A", merge=1)

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

cmd.color ("red", "resi 98 & chain A")

cmd.select ("Inward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 277 & chain A")

cmd.select ("Outward", "resi 277 & chain A", merge=1)

cmd.color ("red", "resi 278 & chain A")

cmd.select ("Inward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 279 & chain A")

cmd.select ("Outward", "resi 279 & chain A", merge=1)

cmd.color ("red", "resi 280 & chain A")

cmd.select ("Inward", "resi 280 & chain A", merge=1)

cmd.color ("blue", "resi 281 & chain A")

cmd.select ("Outward", "resi 281 & chain A", merge=1)

cmd.color ("red", "resi 282 & chain A")

cmd.select ("Inward", "resi 282 & chain A", merge=1)

cmd.color ("blue", "resi 283 & chain A")

cmd.select ("Outward", "resi 283 & chain A", merge=1)

cmd.color ("red", "resi 284 & chain A")

cmd.select ("Inward", "resi 284 & chain A", merge=1)

cmd.color ("blue", "resi 285 & chain A")

cmd.select ("Outward", "resi 285 & chain A", merge=1)

cmd.color ("red", "resi 286 & chain A")

cmd.select ("Inward", "resi 286 & chain A", merge=1)

cmd.color ("blue", "resi 287 & chain A")

cmd.select ("Outward", "resi 287 & chain A", merge=1)

cmd.color ("red", "resi 288 & chain A")

cmd.select ("Inward", "resi 288 & chain A", merge=1)

cmd.color ("red", "resi 289 & chain A")

cmd.select ("Inward", "resi 289 & chain A", merge=1)

cmd.color ("blue", "resi 129 & chain A")

cmd.select ("Outward", "resi 129 & chain A", merge=1)

cmd.color ("red", "resi 130 & chain A")

cmd.select ("Inward", "resi 130 & chain A", merge=1)

cmd.color ("blue", "resi 131 & chain A")

cmd.select ("Outward", "resi 131 & chain A", merge=1)

cmd.color ("red", "resi 132 & chain A")

cmd.select ("Inward", "resi 132 & chain A", merge=1)

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

cmd.color ("blue", "resi 222 & chain A")

cmd.select ("Outward", "resi 222 & chain A", merge=1)

cmd.color ("red", "resi 223 & chain A")

cmd.select ("Inward", "resi 223 & chain A", merge=1)

cmd.color ("blue", "resi 224 & chain A")

cmd.select ("Outward", "resi 224 & chain A", merge=1)

cmd.color ("red", "resi 225 & chain A")

cmd.select ("Inward", "resi 225 & chain A", merge=1)

cmd.color ("blue", "resi 226 & chain A")

cmd.select ("Outward", "resi 226 & chain A", merge=1)

cmd.color ("red", "resi 227 & chain A")

cmd.select ("Inward", "resi 227 & chain A", merge=1)

cmd.color ("blue", "resi 228 & chain A")

cmd.select ("Outward", "resi 228 & chain A", merge=1)

cmd.color ("red", "resi 229 & chain A")

cmd.select ("Inward", "resi 229 & chain A", merge=1)

cmd.color ("blue", "resi 230 & chain A")

cmd.select ("Outward", "resi 230 & chain A", merge=1)

cmd.color ("red", "resi 231 & chain A")

cmd.select ("Inward", "resi 231 & chain A", merge=1)

cmd.color ("blue", "resi 232 & chain A")

cmd.select ("Outward", "resi 232 & chain A", merge=1)

cmd.color ("red", "resi 233 & chain A")

cmd.select ("Inward", "resi 233 & chain A", merge=1)

cmd.color ("blue", "resi 234 & chain A")

cmd.select ("Outward", "resi 234 & chain A", merge=1)

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

cmd.color ("red", "resi 175 & chain A")

cmd.select ("Inward", "resi 175 & chain A", merge=1)

cmd.color ("blue", "resi 176 & chain A")

cmd.select ("Outward", "resi 176 & chain A", merge=1)

cmd.color ("red", "resi 177 & chain A")

cmd.select ("Inward", "resi 177 & chain A", merge=1)

cmd.color ("blue", "resi 178 & chain A")

cmd.select ("Outward", "resi 178 & chain A", merge=1)

cmd.color ("red", "resi 179 & chain A")

cmd.select ("Inward", "resi 179 & chain A", merge=1)

cmd.color ("blue", "resi 180 & chain A")

cmd.select ("Outward", "resi 180 & chain A", merge=1)

cmd.color ("red", "resi 181 & chain A")

cmd.select ("Inward", "resi 181 & chain A", merge=1)

cmd.color ("blue", "resi 182 & chain A")

cmd.select ("Outward", "resi 182 & chain A", merge=1)

cmd.color ("red", "resi 183 & chain A")

cmd.select ("Inward", "resi 183 & chain A", merge=1)

cmd.color ("red", "resi 184 & chain A")

cmd.select ("Inward", "resi 184 & chain A", merge=1)

cmd.color ("blue", "resi 185 & chain A")

cmd.select ("Outward", "resi 185 & chain A", merge=1)

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

cmd.color ("blue", "resi 247 & chain A")

cmd.select ("Outward", "resi 247 & chain A", merge=1)

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

cmd.load_cgo( [9.0, -10.615251,38.60875,-41.32006, -10.615251, 38.60875, -41.32006, 1, 1,1,0,0,0,1], "axis" )
