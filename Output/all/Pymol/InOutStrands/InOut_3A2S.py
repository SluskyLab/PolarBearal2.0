from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3A2S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19 & chain X ")


cmd.select("Xstrand2", "resi 30+31+32+33+34+35+36+37+42+43+44+45+46+47+48+49 & chain X ")


cmd.select("Xstrand27", "resi 328+329+330+331+332+333+334+335+336+337+338+339+340 & chain X ")


cmd.select("Xstrand26", "resi 310+311+312+313+314+315+316+317+318+319+320+321+322+323 & chain X ")


cmd.select("Xstrand25", "resi 295+296+297+298+299+300+301+302+303+304+305+306+307 & chain X ")


cmd.select("Xstrand22", "resi 271+272+273+274+275+276+277+278+279+280 & chain X ")


cmd.select("Xstrand21", "resi 254+255+256+257+258+259+260+261+262+263+264+265+266+267+268 & chain X ")


cmd.select("Xstrand19", "resi 231+232+233+234+235+236+237+238+239+240+241+242+243 & chain X ")


cmd.select("Xstrand18", "resi 212+213+214+215+216+217+218+219+220+221+222+223+224+225+226+227+228 & chain X ")


cmd.select("Xstrand16", "resi 184+185+186+187+188+189+190+191+192+193+194+195+196+197+198 & chain X ")


cmd.select("Xstrand15", "resi 171+172+173+174+175+176+177+178+179+180 & chain X ")


cmd.select("Xstrand12", "resi 144+145+146+147+148+149+150+151 & chain X ")


cmd.select("Xstrand10", "resi 128+129+130+131+132+133+134+135+136+137 & chain X ")


cmd.select("Xstrand7", "resi 89+90+91+92+93+94+95 & chain X ")


cmd.select("Xstrand6", "resi 77+78+79+80+81+82+83+84+85 & chain X ")


cmd.select("Xstrand4", "resi 55+56+57+58+59+60+61+62+63+64+65+66 & chain X ")


cmd.select("barrel", "Xstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 2 & chain X")

cmd.select ("Outward", "resi 2 & chain X", merge=1)

cmd.color ("blue", "resi 3 & chain X")

cmd.select ("Outward", "resi 3 & chain X", merge=1)

cmd.color ("blue", "resi 4 & chain X")

cmd.select ("Outward", "resi 4 & chain X", merge=1)

cmd.color ("blue", "resi 5 & chain X")

cmd.select ("Outward", "resi 5 & chain X", merge=1)

cmd.color ("blue", "resi 6 & chain X")

cmd.select ("Outward", "resi 6 & chain X", merge=1)

cmd.color ("blue", "resi 7 & chain X")

cmd.select ("Outward", "resi 7 & chain X", merge=1)

cmd.color ("blue", "resi 8 & chain X")

cmd.select ("Outward", "resi 8 & chain X", merge=1)

cmd.color ("blue", "resi 9 & chain X")

cmd.select ("Outward", "resi 9 & chain X", merge=1)

cmd.color ("blue", "resi 10 & chain X")

cmd.select ("Outward", "resi 10 & chain X", merge=1)

cmd.color ("blue", "resi 11 & chain X")

cmd.select ("Outward", "resi 11 & chain X", merge=1)

cmd.color ("blue", "resi 12 & chain X")

cmd.select ("Outward", "resi 12 & chain X", merge=1)

cmd.color ("blue", "resi 13 & chain X")

cmd.select ("Outward", "resi 13 & chain X", merge=1)

cmd.color ("blue", "resi 14 & chain X")

cmd.select ("Outward", "resi 14 & chain X", merge=1)

cmd.color ("blue", "resi 15 & chain X")

cmd.select ("Outward", "resi 15 & chain X", merge=1)

cmd.color ("blue", "resi 16 & chain X")

cmd.select ("Outward", "resi 16 & chain X", merge=1)

cmd.color ("blue", "resi 17 & chain X")

cmd.select ("Outward", "resi 17 & chain X", merge=1)

cmd.color ("blue", "resi 18 & chain X")

cmd.select ("Outward", "resi 18 & chain X", merge=1)

cmd.color ("blue", "resi 19 & chain X")

cmd.select ("Outward", "resi 19 & chain X", merge=1)

cmd.color ("blue", "resi 30 & chain X")

cmd.select ("Outward", "resi 30 & chain X", merge=1)

cmd.color ("blue", "resi 31 & chain X")

cmd.select ("Outward", "resi 31 & chain X", merge=1)

cmd.color ("blue", "resi 32 & chain X")

cmd.select ("Outward", "resi 32 & chain X", merge=1)

cmd.color ("blue", "resi 33 & chain X")

cmd.select ("Outward", "resi 33 & chain X", merge=1)

cmd.color ("blue", "resi 34 & chain X")

cmd.select ("Outward", "resi 34 & chain X", merge=1)

cmd.color ("blue", "resi 35 & chain X")

cmd.select ("Outward", "resi 35 & chain X", merge=1)

cmd.color ("blue", "resi 36 & chain X")

cmd.select ("Outward", "resi 36 & chain X", merge=1)

cmd.color ("blue", "resi 37 & chain X")

cmd.select ("Outward", "resi 37 & chain X", merge=1)

cmd.color ("blue", "resi 42 & chain X")

cmd.select ("Outward", "resi 42 & chain X", merge=1)

cmd.color ("blue", "resi 43 & chain X")

cmd.select ("Outward", "resi 43 & chain X", merge=1)

cmd.color ("blue", "resi 44 & chain X")

cmd.select ("Outward", "resi 44 & chain X", merge=1)

cmd.color ("blue", "resi 45 & chain X")

cmd.select ("Outward", "resi 45 & chain X", merge=1)

cmd.color ("blue", "resi 46 & chain X")

cmd.select ("Outward", "resi 46 & chain X", merge=1)

cmd.color ("blue", "resi 47 & chain X")

cmd.select ("Outward", "resi 47 & chain X", merge=1)

cmd.color ("blue", "resi 48 & chain X")

cmd.select ("Outward", "resi 48 & chain X", merge=1)

cmd.color ("blue", "resi 49 & chain X")

cmd.select ("Outward", "resi 49 & chain X", merge=1)

cmd.color ("blue", "resi 328 & chain X")

cmd.select ("Outward", "resi 328 & chain X", merge=1)

cmd.color ("blue", "resi 329 & chain X")

cmd.select ("Outward", "resi 329 & chain X", merge=1)

cmd.color ("blue", "resi 330 & chain X")

cmd.select ("Outward", "resi 330 & chain X", merge=1)

cmd.color ("blue", "resi 331 & chain X")

cmd.select ("Outward", "resi 331 & chain X", merge=1)

cmd.color ("blue", "resi 332 & chain X")

cmd.select ("Outward", "resi 332 & chain X", merge=1)

cmd.color ("blue", "resi 333 & chain X")

cmd.select ("Outward", "resi 333 & chain X", merge=1)

cmd.color ("blue", "resi 334 & chain X")

cmd.select ("Outward", "resi 334 & chain X", merge=1)

cmd.color ("blue", "resi 335 & chain X")

cmd.select ("Outward", "resi 335 & chain X", merge=1)

cmd.color ("blue", "resi 336 & chain X")

cmd.select ("Outward", "resi 336 & chain X", merge=1)

cmd.color ("blue", "resi 337 & chain X")

cmd.select ("Outward", "resi 337 & chain X", merge=1)

cmd.color ("blue", "resi 338 & chain X")

cmd.select ("Outward", "resi 338 & chain X", merge=1)

cmd.color ("blue", "resi 339 & chain X")

cmd.select ("Outward", "resi 339 & chain X", merge=1)

cmd.color ("blue", "resi 340 & chain X")

cmd.select ("Outward", "resi 340 & chain X", merge=1)

cmd.color ("blue", "resi 310 & chain X")

cmd.select ("Outward", "resi 310 & chain X", merge=1)

cmd.color ("blue", "resi 311 & chain X")

cmd.select ("Outward", "resi 311 & chain X", merge=1)

cmd.color ("blue", "resi 312 & chain X")

cmd.select ("Outward", "resi 312 & chain X", merge=1)

cmd.color ("blue", "resi 313 & chain X")

cmd.select ("Outward", "resi 313 & chain X", merge=1)

cmd.color ("blue", "resi 314 & chain X")

cmd.select ("Outward", "resi 314 & chain X", merge=1)

cmd.color ("blue", "resi 315 & chain X")

cmd.select ("Outward", "resi 315 & chain X", merge=1)

cmd.color ("blue", "resi 316 & chain X")

cmd.select ("Outward", "resi 316 & chain X", merge=1)

cmd.color ("blue", "resi 317 & chain X")

cmd.select ("Outward", "resi 317 & chain X", merge=1)

cmd.color ("blue", "resi 318 & chain X")

cmd.select ("Outward", "resi 318 & chain X", merge=1)

cmd.color ("blue", "resi 319 & chain X")

cmd.select ("Outward", "resi 319 & chain X", merge=1)

cmd.color ("blue", "resi 320 & chain X")

cmd.select ("Outward", "resi 320 & chain X", merge=1)

cmd.color ("blue", "resi 321 & chain X")

cmd.select ("Outward", "resi 321 & chain X", merge=1)

cmd.color ("blue", "resi 322 & chain X")

cmd.select ("Outward", "resi 322 & chain X", merge=1)

cmd.color ("blue", "resi 323 & chain X")

cmd.select ("Outward", "resi 323 & chain X", merge=1)

cmd.color ("blue", "resi 295 & chain X")

cmd.select ("Outward", "resi 295 & chain X", merge=1)

cmd.color ("blue", "resi 296 & chain X")

cmd.select ("Outward", "resi 296 & chain X", merge=1)

cmd.color ("blue", "resi 297 & chain X")

cmd.select ("Outward", "resi 297 & chain X", merge=1)

cmd.color ("blue", "resi 298 & chain X")

cmd.select ("Outward", "resi 298 & chain X", merge=1)

cmd.color ("blue", "resi 299 & chain X")

cmd.select ("Outward", "resi 299 & chain X", merge=1)

cmd.color ("blue", "resi 300 & chain X")

cmd.select ("Outward", "resi 300 & chain X", merge=1)

cmd.color ("blue", "resi 301 & chain X")

cmd.select ("Outward", "resi 301 & chain X", merge=1)

cmd.color ("blue", "resi 302 & chain X")

cmd.select ("Outward", "resi 302 & chain X", merge=1)

cmd.color ("blue", "resi 303 & chain X")

cmd.select ("Outward", "resi 303 & chain X", merge=1)

cmd.color ("blue", "resi 304 & chain X")

cmd.select ("Outward", "resi 304 & chain X", merge=1)

cmd.color ("blue", "resi 305 & chain X")

cmd.select ("Outward", "resi 305 & chain X", merge=1)

cmd.color ("blue", "resi 306 & chain X")

cmd.select ("Outward", "resi 306 & chain X", merge=1)

cmd.color ("blue", "resi 307 & chain X")

cmd.select ("Outward", "resi 307 & chain X", merge=1)

cmd.color ("blue", "resi 271 & chain X")

cmd.select ("Outward", "resi 271 & chain X", merge=1)

cmd.color ("blue", "resi 272 & chain X")

cmd.select ("Outward", "resi 272 & chain X", merge=1)

cmd.color ("blue", "resi 273 & chain X")

cmd.select ("Outward", "resi 273 & chain X", merge=1)

cmd.color ("blue", "resi 274 & chain X")

cmd.select ("Outward", "resi 274 & chain X", merge=1)

cmd.color ("blue", "resi 275 & chain X")

cmd.select ("Outward", "resi 275 & chain X", merge=1)

cmd.color ("blue", "resi 276 & chain X")

cmd.select ("Outward", "resi 276 & chain X", merge=1)

cmd.color ("blue", "resi 277 & chain X")

cmd.select ("Outward", "resi 277 & chain X", merge=1)

cmd.color ("blue", "resi 278 & chain X")

cmd.select ("Outward", "resi 278 & chain X", merge=1)

cmd.color ("blue", "resi 279 & chain X")

cmd.select ("Outward", "resi 279 & chain X", merge=1)

cmd.color ("blue", "resi 280 & chain X")

cmd.select ("Outward", "resi 280 & chain X", merge=1)

cmd.color ("blue", "resi 254 & chain X")

cmd.select ("Outward", "resi 254 & chain X", merge=1)

cmd.color ("blue", "resi 255 & chain X")

cmd.select ("Outward", "resi 255 & chain X", merge=1)

cmd.color ("blue", "resi 256 & chain X")

cmd.select ("Outward", "resi 256 & chain X", merge=1)

cmd.color ("blue", "resi 257 & chain X")

cmd.select ("Outward", "resi 257 & chain X", merge=1)

cmd.color ("blue", "resi 258 & chain X")

cmd.select ("Outward", "resi 258 & chain X", merge=1)

cmd.color ("blue", "resi 259 & chain X")

cmd.select ("Outward", "resi 259 & chain X", merge=1)

cmd.color ("blue", "resi 260 & chain X")

cmd.select ("Outward", "resi 260 & chain X", merge=1)

cmd.color ("blue", "resi 261 & chain X")

cmd.select ("Outward", "resi 261 & chain X", merge=1)

cmd.color ("blue", "resi 262 & chain X")

cmd.select ("Outward", "resi 262 & chain X", merge=1)

cmd.color ("blue", "resi 263 & chain X")

cmd.select ("Outward", "resi 263 & chain X", merge=1)

cmd.color ("blue", "resi 264 & chain X")

cmd.select ("Outward", "resi 264 & chain X", merge=1)

cmd.color ("blue", "resi 265 & chain X")

cmd.select ("Outward", "resi 265 & chain X", merge=1)

cmd.color ("blue", "resi 266 & chain X")

cmd.select ("Outward", "resi 266 & chain X", merge=1)

cmd.color ("blue", "resi 267 & chain X")

cmd.select ("Outward", "resi 267 & chain X", merge=1)

cmd.color ("blue", "resi 268 & chain X")

cmd.select ("Outward", "resi 268 & chain X", merge=1)

cmd.color ("blue", "resi 231 & chain X")

cmd.select ("Outward", "resi 231 & chain X", merge=1)

cmd.color ("blue", "resi 232 & chain X")

cmd.select ("Outward", "resi 232 & chain X", merge=1)

cmd.color ("blue", "resi 233 & chain X")

cmd.select ("Outward", "resi 233 & chain X", merge=1)

cmd.color ("blue", "resi 234 & chain X")

cmd.select ("Outward", "resi 234 & chain X", merge=1)

cmd.color ("blue", "resi 235 & chain X")

cmd.select ("Outward", "resi 235 & chain X", merge=1)

cmd.color ("blue", "resi 236 & chain X")

cmd.select ("Outward", "resi 236 & chain X", merge=1)

cmd.color ("blue", "resi 237 & chain X")

cmd.select ("Outward", "resi 237 & chain X", merge=1)

cmd.color ("blue", "resi 238 & chain X")

cmd.select ("Outward", "resi 238 & chain X", merge=1)

cmd.color ("blue", "resi 239 & chain X")

cmd.select ("Outward", "resi 239 & chain X", merge=1)

cmd.color ("blue", "resi 240 & chain X")

cmd.select ("Outward", "resi 240 & chain X", merge=1)

cmd.color ("blue", "resi 241 & chain X")

cmd.select ("Outward", "resi 241 & chain X", merge=1)

cmd.color ("blue", "resi 242 & chain X")

cmd.select ("Outward", "resi 242 & chain X", merge=1)

cmd.color ("blue", "resi 243 & chain X")

cmd.select ("Outward", "resi 243 & chain X", merge=1)

cmd.color ("blue", "resi 212 & chain X")

cmd.select ("Outward", "resi 212 & chain X", merge=1)

cmd.color ("blue", "resi 213 & chain X")

cmd.select ("Outward", "resi 213 & chain X", merge=1)

cmd.color ("blue", "resi 214 & chain X")

cmd.select ("Outward", "resi 214 & chain X", merge=1)

cmd.color ("blue", "resi 215 & chain X")

cmd.select ("Outward", "resi 215 & chain X", merge=1)

cmd.color ("blue", "resi 216 & chain X")

cmd.select ("Outward", "resi 216 & chain X", merge=1)

cmd.color ("blue", "resi 217 & chain X")

cmd.select ("Outward", "resi 217 & chain X", merge=1)

cmd.color ("blue", "resi 218 & chain X")

cmd.select ("Outward", "resi 218 & chain X", merge=1)

cmd.color ("blue", "resi 219 & chain X")

cmd.select ("Outward", "resi 219 & chain X", merge=1)

cmd.color ("blue", "resi 220 & chain X")

cmd.select ("Outward", "resi 220 & chain X", merge=1)

cmd.color ("blue", "resi 221 & chain X")

cmd.select ("Outward", "resi 221 & chain X", merge=1)

cmd.color ("blue", "resi 222 & chain X")

cmd.select ("Outward", "resi 222 & chain X", merge=1)

cmd.color ("blue", "resi 223 & chain X")

cmd.select ("Outward", "resi 223 & chain X", merge=1)

cmd.color ("blue", "resi 224 & chain X")

cmd.select ("Outward", "resi 224 & chain X", merge=1)

cmd.color ("blue", "resi 225 & chain X")

cmd.select ("Outward", "resi 225 & chain X", merge=1)

cmd.color ("blue", "resi 226 & chain X")

cmd.select ("Outward", "resi 226 & chain X", merge=1)

cmd.color ("blue", "resi 227 & chain X")

cmd.select ("Outward", "resi 227 & chain X", merge=1)

cmd.color ("blue", "resi 228 & chain X")

cmd.select ("Outward", "resi 228 & chain X", merge=1)

cmd.color ("blue", "resi 184 & chain X")

cmd.select ("Outward", "resi 184 & chain X", merge=1)

cmd.color ("blue", "resi 185 & chain X")

cmd.select ("Outward", "resi 185 & chain X", merge=1)

cmd.color ("blue", "resi 186 & chain X")

cmd.select ("Outward", "resi 186 & chain X", merge=1)

cmd.color ("blue", "resi 187 & chain X")

cmd.select ("Outward", "resi 187 & chain X", merge=1)

cmd.color ("blue", "resi 188 & chain X")

cmd.select ("Outward", "resi 188 & chain X", merge=1)

cmd.color ("blue", "resi 189 & chain X")

cmd.select ("Outward", "resi 189 & chain X", merge=1)

cmd.color ("blue", "resi 190 & chain X")

cmd.select ("Outward", "resi 190 & chain X", merge=1)

cmd.color ("blue", "resi 191 & chain X")

cmd.select ("Outward", "resi 191 & chain X", merge=1)

cmd.color ("blue", "resi 192 & chain X")

cmd.select ("Outward", "resi 192 & chain X", merge=1)

cmd.color ("blue", "resi 193 & chain X")

cmd.select ("Outward", "resi 193 & chain X", merge=1)

cmd.color ("blue", "resi 194 & chain X")

cmd.select ("Outward", "resi 194 & chain X", merge=1)

cmd.color ("blue", "resi 195 & chain X")

cmd.select ("Outward", "resi 195 & chain X", merge=1)

cmd.color ("blue", "resi 196 & chain X")

cmd.select ("Outward", "resi 196 & chain X", merge=1)

cmd.color ("blue", "resi 197 & chain X")

cmd.select ("Outward", "resi 197 & chain X", merge=1)

cmd.color ("blue", "resi 198 & chain X")

cmd.select ("Outward", "resi 198 & chain X", merge=1)

cmd.color ("blue", "resi 171 & chain X")

cmd.select ("Outward", "resi 171 & chain X", merge=1)

cmd.color ("blue", "resi 172 & chain X")

cmd.select ("Outward", "resi 172 & chain X", merge=1)

cmd.color ("blue", "resi 173 & chain X")

cmd.select ("Outward", "resi 173 & chain X", merge=1)

cmd.color ("blue", "resi 174 & chain X")

cmd.select ("Outward", "resi 174 & chain X", merge=1)

cmd.color ("blue", "resi 175 & chain X")

cmd.select ("Outward", "resi 175 & chain X", merge=1)

cmd.color ("blue", "resi 176 & chain X")

cmd.select ("Outward", "resi 176 & chain X", merge=1)

cmd.color ("blue", "resi 177 & chain X")

cmd.select ("Outward", "resi 177 & chain X", merge=1)

cmd.color ("blue", "resi 178 & chain X")

cmd.select ("Outward", "resi 178 & chain X", merge=1)

cmd.color ("blue", "resi 179 & chain X")

cmd.select ("Outward", "resi 179 & chain X", merge=1)

cmd.color ("blue", "resi 180 & chain X")

cmd.select ("Outward", "resi 180 & chain X", merge=1)

cmd.color ("blue", "resi 144 & chain X")

cmd.select ("Outward", "resi 144 & chain X", merge=1)

cmd.color ("blue", "resi 145 & chain X")

cmd.select ("Outward", "resi 145 & chain X", merge=1)

cmd.color ("blue", "resi 146 & chain X")

cmd.select ("Outward", "resi 146 & chain X", merge=1)

cmd.color ("blue", "resi 147 & chain X")

cmd.select ("Outward", "resi 147 & chain X", merge=1)

cmd.color ("blue", "resi 148 & chain X")

cmd.select ("Outward", "resi 148 & chain X", merge=1)

cmd.color ("blue", "resi 149 & chain X")

cmd.select ("Outward", "resi 149 & chain X", merge=1)

cmd.color ("blue", "resi 150 & chain X")

cmd.select ("Outward", "resi 150 & chain X", merge=1)

cmd.color ("blue", "resi 151 & chain X")

cmd.select ("Outward", "resi 151 & chain X", merge=1)

cmd.color ("blue", "resi 128 & chain X")

cmd.select ("Outward", "resi 128 & chain X", merge=1)

cmd.color ("blue", "resi 129 & chain X")

cmd.select ("Outward", "resi 129 & chain X", merge=1)

cmd.color ("blue", "resi 130 & chain X")

cmd.select ("Outward", "resi 130 & chain X", merge=1)

cmd.color ("blue", "resi 131 & chain X")

cmd.select ("Outward", "resi 131 & chain X", merge=1)

cmd.color ("blue", "resi 132 & chain X")

cmd.select ("Outward", "resi 132 & chain X", merge=1)

cmd.color ("blue", "resi 133 & chain X")

cmd.select ("Outward", "resi 133 & chain X", merge=1)

cmd.color ("blue", "resi 134 & chain X")

cmd.select ("Outward", "resi 134 & chain X", merge=1)

cmd.color ("blue", "resi 135 & chain X")

cmd.select ("Outward", "resi 135 & chain X", merge=1)

cmd.color ("blue", "resi 136 & chain X")

cmd.select ("Outward", "resi 136 & chain X", merge=1)

cmd.color ("blue", "resi 137 & chain X")

cmd.select ("Outward", "resi 137 & chain X", merge=1)

cmd.color ("blue", "resi 89 & chain X")

cmd.select ("Outward", "resi 89 & chain X", merge=1)

cmd.color ("blue", "resi 90 & chain X")

cmd.select ("Outward", "resi 90 & chain X", merge=1)

cmd.color ("blue", "resi 91 & chain X")

cmd.select ("Outward", "resi 91 & chain X", merge=1)

cmd.color ("blue", "resi 92 & chain X")

cmd.select ("Outward", "resi 92 & chain X", merge=1)

cmd.color ("blue", "resi 93 & chain X")

cmd.select ("Outward", "resi 93 & chain X", merge=1)

cmd.color ("blue", "resi 94 & chain X")

cmd.select ("Outward", "resi 94 & chain X", merge=1)

cmd.color ("blue", "resi 95 & chain X")

cmd.select ("Outward", "resi 95 & chain X", merge=1)

cmd.color ("blue", "resi 77 & chain X")

cmd.select ("Outward", "resi 77 & chain X", merge=1)

cmd.color ("blue", "resi 78 & chain X")

cmd.select ("Outward", "resi 78 & chain X", merge=1)

cmd.color ("blue", "resi 79 & chain X")

cmd.select ("Outward", "resi 79 & chain X", merge=1)

cmd.color ("blue", "resi 80 & chain X")

cmd.select ("Outward", "resi 80 & chain X", merge=1)

cmd.color ("blue", "resi 81 & chain X")

cmd.select ("Outward", "resi 81 & chain X", merge=1)

cmd.color ("blue", "resi 82 & chain X")

cmd.select ("Outward", "resi 82 & chain X", merge=1)

cmd.color ("blue", "resi 83 & chain X")

cmd.select ("Outward", "resi 83 & chain X", merge=1)

cmd.color ("blue", "resi 84 & chain X")

cmd.select ("Outward", "resi 84 & chain X", merge=1)

cmd.color ("blue", "resi 85 & chain X")

cmd.select ("Outward", "resi 85 & chain X", merge=1)

cmd.color ("blue", "resi 55 & chain X")

cmd.select ("Outward", "resi 55 & chain X", merge=1)

cmd.color ("blue", "resi 56 & chain X")

cmd.select ("Outward", "resi 56 & chain X", merge=1)

cmd.color ("blue", "resi 57 & chain X")

cmd.select ("Outward", "resi 57 & chain X", merge=1)

cmd.color ("blue", "resi 58 & chain X")

cmd.select ("Outward", "resi 58 & chain X", merge=1)

cmd.color ("blue", "resi 59 & chain X")

cmd.select ("Outward", "resi 59 & chain X", merge=1)

cmd.color ("blue", "resi 60 & chain X")

cmd.select ("Outward", "resi 60 & chain X", merge=1)

cmd.color ("blue", "resi 61 & chain X")

cmd.select ("Outward", "resi 61 & chain X", merge=1)

cmd.color ("blue", "resi 62 & chain X")

cmd.select ("Outward", "resi 62 & chain X", merge=1)

cmd.color ("blue", "resi 63 & chain X")

cmd.select ("Outward", "resi 63 & chain X", merge=1)

cmd.color ("blue", "resi 64 & chain X")

cmd.select ("Outward", "resi 64 & chain X", merge=1)

cmd.color ("blue", "resi 65 & chain X")

cmd.select ("Outward", "resi 65 & chain X", merge=1)

cmd.color ("blue", "resi 66 & chain X")

cmd.select ("Outward", "resi 66 & chain X", merge=1)

cmd.load_cgo( [9.0, 24.556686,7.7831244,0.602625, 21.718748, 8.224625, 28.309624, 1, 1,1,0,0,0,1], "axis" )
