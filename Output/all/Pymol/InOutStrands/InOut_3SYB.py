from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 150+149+148+147+146+145+90+144+43+89+143+88+44+45+142+141+87+86+46+47+140+85+48+139+84+49+426+138+83+427+50+428+51+137+82+429+52+430+81+53+80+431+432+54+79+55+434+78+433+435+436+56+77 & chain A ")


cmd.select("Astrand1", "resi 153+154+155+98+156+99+100+101+157+102+160+103+158+159+104+105+106+457+107+455+456+454+453+108+109+452+451+110+450+449+111+448+447+445+446 & chain A ")


cmd.select("Astrand6", "resi 178+179+180+181+182+183+184+185+186+187+188+189 & chain A ")


cmd.select("Astrand7", "resi 192+193+194+195+196+197+198+199+200+201+202+203 & chain A ")


cmd.select("Astrand8", "resi 227+228+229+230+231+232+233+234+235+236+237 & chain A ")


cmd.select("Astrand9", "resi 240+241+242+243+244+245+246+247+248+249 & chain A ")


cmd.select("Astrand10", "resi 253+254+255+256+257+258+259+260+261+262+263+264 & chain A ")


cmd.select("Astrand11", "resi 272+273+274+275+276+277+278+279+280+281+282+283+284 & chain A ")


cmd.select("Astrand12", "resi 294+295+296+297+298+299+300+301+302+303+304+305+306 & chain A ")


cmd.select("Astrand13", "resi 309+310+311+312+313+314+315+316+317+318+319 & chain A ")


cmd.select("Astrand14", "resi 349+350+351+352+353+354+355+356+357+358 & chain A ")


cmd.select("Astrand15", "resi 367+368+369+370+371+372+373+374+375+376+377+378+379+380 & chain A ")


cmd.select("Astrand16", "resi 402+403+404+405+406+407+408+409+410+411+412+413+414+415+416 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("red", "resi 149 & chain A")

cmd.select ("Inward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 148 & chain A")

cmd.select ("Outward", "resi 148 & chain A", merge=1)

cmd.color ("red", "resi 147 & chain A")

cmd.select ("Inward", "resi 147 & chain A", merge=1)

cmd.color ("red", "resi 146 & chain A")

cmd.select ("Inward", "resi 146 & chain A", merge=1)

cmd.color ("blue", "resi 145 & chain A")

cmd.select ("Outward", "resi 145 & chain A", merge=1)

cmd.color ("blue", "resi 90 & chain A")

cmd.select ("Outward", "resi 90 & chain A", merge=1)

cmd.color ("blue", "resi 144 & chain A")

cmd.select ("Outward", "resi 144 & chain A", merge=1)

cmd.color ("red", "resi 43 & chain A")

cmd.select ("Inward", "resi 43 & chain A", merge=1)

cmd.color ("red", "resi 89 & chain A")

cmd.select ("Inward", "resi 89 & chain A", merge=1)

cmd.color ("red", "resi 143 & chain A")

cmd.select ("Inward", "resi 143 & chain A", merge=1)

cmd.color ("blue", "resi 88 & chain A")

cmd.select ("Outward", "resi 88 & chain A", merge=1)

cmd.color ("blue", "resi 44 & chain A")

cmd.select ("Outward", "resi 44 & chain A", merge=1)

cmd.color ("red", "resi 45 & chain A")

cmd.select ("Inward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 142 & chain A")

cmd.select ("Outward", "resi 142 & chain A", merge=1)

cmd.color ("red", "resi 141 & chain A")

cmd.select ("Inward", "resi 141 & chain A", merge=1)

cmd.color ("red", "resi 87 & chain A")

cmd.select ("Inward", "resi 87 & chain A", merge=1)

cmd.color ("blue", "resi 86 & chain A")

cmd.select ("Outward", "resi 86 & chain A", merge=1)

cmd.color ("blue", "resi 46 & chain A")

cmd.select ("Outward", "resi 46 & chain A", merge=1)

cmd.color ("red", "resi 47 & chain A")

cmd.select ("Inward", "resi 47 & chain A", merge=1)

cmd.color ("blue", "resi 140 & chain A")

cmd.select ("Outward", "resi 140 & chain A", merge=1)

cmd.color ("red", "resi 85 & chain A")

cmd.select ("Inward", "resi 85 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("red", "resi 139 & chain A")

cmd.select ("Inward", "resi 139 & chain A", merge=1)

cmd.color ("blue", "resi 84 & chain A")

cmd.select ("Outward", "resi 84 & chain A", merge=1)

cmd.color ("red", "resi 49 & chain A")

cmd.select ("Inward", "resi 49 & chain A", merge=1)

cmd.color ("red", "resi 426 & chain A")

cmd.select ("Inward", "resi 426 & chain A", merge=1)

cmd.color ("blue", "resi 138 & chain A")

cmd.select ("Outward", "resi 138 & chain A", merge=1)

cmd.color ("red", "resi 83 & chain A")

cmd.select ("Inward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 427 & chain A")

cmd.select ("Outward", "resi 427 & chain A", merge=1)

cmd.color ("blue", "resi 50 & chain A")

cmd.select ("Outward", "resi 50 & chain A", merge=1)

cmd.color ("red", "resi 428 & chain A")

cmd.select ("Inward", "resi 428 & chain A", merge=1)

cmd.color ("red", "resi 51 & chain A")

cmd.select ("Inward", "resi 51 & chain A", merge=1)

cmd.color ("red", "resi 137 & chain A")

cmd.select ("Inward", "resi 137 & chain A", merge=1)

cmd.color ("blue", "resi 82 & chain A")

cmd.select ("Outward", "resi 82 & chain A", merge=1)

cmd.color ("blue", "resi 429 & chain A")

cmd.select ("Outward", "resi 429 & chain A", merge=1)

cmd.color ("blue", "resi 52 & chain A")

cmd.select ("Outward", "resi 52 & chain A", merge=1)

cmd.color ("red", "resi 430 & chain A")

cmd.select ("Inward", "resi 430 & chain A", merge=1)

cmd.color ("red", "resi 81 & chain A")

cmd.select ("Inward", "resi 81 & chain A", merge=1)

cmd.color ("red", "resi 53 & chain A")

cmd.select ("Inward", "resi 53 & chain A", merge=1)

cmd.color ("red", "resi 80 & chain A")

cmd.select ("Inward", "resi 80 & chain A", merge=1)

cmd.color ("blue", "resi 431 & chain A")

cmd.select ("Outward", "resi 431 & chain A", merge=1)

cmd.color ("red", "resi 432 & chain A")

cmd.select ("Inward", "resi 432 & chain A", merge=1)

cmd.color ("blue", "resi 54 & chain A")

cmd.select ("Outward", "resi 54 & chain A", merge=1)

cmd.color ("red", "resi 79 & chain A")

cmd.select ("Inward", "resi 79 & chain A", merge=1)

cmd.color ("red", "resi 55 & chain A")

cmd.select ("Inward", "resi 55 & chain A", merge=1)

cmd.color ("red", "resi 434 & chain A")

cmd.select ("Inward", "resi 434 & chain A", merge=1)

cmd.color ("blue", "resi 78 & chain A")

cmd.select ("Outward", "resi 78 & chain A", merge=1)

cmd.color ("blue", "resi 433 & chain A")

cmd.select ("Outward", "resi 433 & chain A", merge=1)

cmd.color ("blue", "resi 435 & chain A")

cmd.select ("Outward", "resi 435 & chain A", merge=1)

cmd.color ("red", "resi 436 & chain A")

cmd.select ("Inward", "resi 436 & chain A", merge=1)

cmd.color ("blue", "resi 56 & chain A")

cmd.select ("Outward", "resi 56 & chain A", merge=1)

cmd.color ("red", "resi 77 & chain A")

cmd.select ("Inward", "resi 77 & chain A", merge=1)

cmd.color ("blue", "resi 153 & chain A")

cmd.select ("Outward", "resi 153 & chain A", merge=1)

cmd.color ("red", "resi 154 & chain A")

cmd.select ("Inward", "resi 154 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 98 & chain A")

cmd.select ("Outward", "resi 98 & chain A", merge=1)

cmd.color ("red", "resi 156 & chain A")

cmd.select ("Inward", "resi 156 & chain A", merge=1)

cmd.color ("red", "resi 99 & chain A")

cmd.select ("Inward", "resi 99 & chain A", merge=1)

cmd.color ("blue", "resi 100 & chain A")

cmd.select ("Outward", "resi 100 & chain A", merge=1)

cmd.color ("red", "resi 101 & chain A")

cmd.select ("Inward", "resi 101 & chain A", merge=1)

cmd.color ("blue", "resi 157 & chain A")

cmd.select ("Outward", "resi 157 & chain A", merge=1)

cmd.color ("blue", "resi 102 & chain A")

cmd.select ("Outward", "resi 102 & chain A", merge=1)

cmd.color ("red", "resi 160 & chain A")

cmd.select ("Inward", "resi 160 & chain A", merge=1)

cmd.color ("red", "resi 103 & chain A")

cmd.select ("Inward", "resi 103 & chain A", merge=1)

cmd.color ("blue", "resi 158 & chain A")

cmd.select ("Outward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("blue", "resi 104 & chain A")

cmd.select ("Outward", "resi 104 & chain A", merge=1)

cmd.color ("red", "resi 105 & chain A")

cmd.select ("Inward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("red", "resi 457 & chain A")

cmd.select ("Inward", "resi 457 & chain A", merge=1)

cmd.color ("red", "resi 107 & chain A")

cmd.select ("Inward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 455 & chain A")

cmd.select ("Outward", "resi 455 & chain A", merge=1)

cmd.color ("red", "resi 456 & chain A")

cmd.select ("Inward", "resi 456 & chain A", merge=1)

cmd.color ("red", "resi 454 & chain A")

cmd.select ("Inward", "resi 454 & chain A", merge=1)

cmd.color ("blue", "resi 453 & chain A")

cmd.select ("Outward", "resi 453 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("red", "resi 109 & chain A")

cmd.select ("Inward", "resi 109 & chain A", merge=1)

cmd.color ("red", "resi 452 & chain A")

cmd.select ("Inward", "resi 452 & chain A", merge=1)

cmd.color ("blue", "resi 451 & chain A")

cmd.select ("Outward", "resi 451 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

cmd.color ("red", "resi 450 & chain A")

cmd.select ("Inward", "resi 450 & chain A", merge=1)

cmd.color ("blue", "resi 449 & chain A")

cmd.select ("Outward", "resi 449 & chain A", merge=1)

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("red", "resi 448 & chain A")

cmd.select ("Inward", "resi 448 & chain A", merge=1)

cmd.color ("blue", "resi 447 & chain A")

cmd.select ("Outward", "resi 447 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("red", "resi 446 & chain A")

cmd.select ("Inward", "resi 446 & chain A", merge=1)

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

cmd.color ("blue", "resi 189 & chain A")

cmd.select ("Outward", "resi 189 & chain A", merge=1)

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

cmd.color ("blue", "resi 201 & chain A")

cmd.select ("Outward", "resi 201 & chain A", merge=1)

cmd.color ("red", "resi 202 & chain A")

cmd.select ("Inward", "resi 202 & chain A", merge=1)

cmd.color ("blue", "resi 203 & chain A")

cmd.select ("Outward", "resi 203 & chain A", merge=1)

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

cmd.color ("red", "resi 235 & chain A")

cmd.select ("Inward", "resi 235 & chain A", merge=1)

cmd.color ("red", "resi 236 & chain A")

cmd.select ("Inward", "resi 236 & chain A", merge=1)

cmd.color ("blue", "resi 237 & chain A")

cmd.select ("Outward", "resi 237 & chain A", merge=1)

cmd.color ("blue", "resi 240 & chain A")

cmd.select ("Outward", "resi 240 & chain A", merge=1)

cmd.color ("red", "resi 241 & chain A")

cmd.select ("Inward", "resi 241 & chain A", merge=1)

cmd.color ("blue", "resi 242 & chain A")

cmd.select ("Outward", "resi 242 & chain A", merge=1)

cmd.color ("red", "resi 243 & chain A")

cmd.select ("Inward", "resi 243 & chain A", merge=1)

cmd.color ("blue", "resi 244 & chain A")

cmd.select ("Outward", "resi 244 & chain A", merge=1)

cmd.color ("red", "resi 245 & chain A")

cmd.select ("Inward", "resi 245 & chain A", merge=1)

cmd.color ("blue", "resi 246 & chain A")

cmd.select ("Outward", "resi 246 & chain A", merge=1)

cmd.color ("red", "resi 247 & chain A")

cmd.select ("Inward", "resi 247 & chain A", merge=1)

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

cmd.color ("red", "resi 249 & chain A")

cmd.select ("Inward", "resi 249 & chain A", merge=1)

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

cmd.color ("red", "resi 261 & chain A")

cmd.select ("Inward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 262 & chain A")

cmd.select ("Outward", "resi 262 & chain A", merge=1)

cmd.color ("red", "resi 263 & chain A")

cmd.select ("Inward", "resi 263 & chain A", merge=1)

cmd.color ("blue", "resi 264 & chain A")

cmd.select ("Outward", "resi 264 & chain A", merge=1)

cmd.color ("red", "resi 272 & chain A")

cmd.select ("Inward", "resi 272 & chain A", merge=1)

cmd.color ("blue", "resi 273 & chain A")

cmd.select ("Outward", "resi 273 & chain A", merge=1)

cmd.color ("red", "resi 274 & chain A")

cmd.select ("Inward", "resi 274 & chain A", merge=1)

cmd.color ("blue", "resi 275 & chain A")

cmd.select ("Outward", "resi 275 & chain A", merge=1)

cmd.color ("red", "resi 276 & chain A")

cmd.select ("Inward", "resi 276 & chain A", merge=1)

cmd.color ("blue", "resi 277 & chain A")

cmd.select ("Outward", "resi 277 & chain A", merge=1)

cmd.color ("red", "resi 278 & chain A")

cmd.select ("Inward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 279 & chain A")

cmd.select ("Outward", "resi 279 & chain A", merge=1)

cmd.color ("blue", "resi 280 & chain A")

cmd.select ("Outward", "resi 280 & chain A", merge=1)

cmd.color ("blue", "resi 281 & chain A")

cmd.select ("Outward", "resi 281 & chain A", merge=1)

cmd.color ("red", "resi 282 & chain A")

cmd.select ("Inward", "resi 282 & chain A", merge=1)

cmd.color ("blue", "resi 283 & chain A")

cmd.select ("Outward", "resi 283 & chain A", merge=1)

cmd.color ("blue", "resi 284 & chain A")

cmd.select ("Outward", "resi 284 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("red", "resi 295 & chain A")

cmd.select ("Inward", "resi 295 & chain A", merge=1)

cmd.color ("blue", "resi 296 & chain A")

cmd.select ("Outward", "resi 296 & chain A", merge=1)

cmd.color ("red", "resi 297 & chain A")

cmd.select ("Inward", "resi 297 & chain A", merge=1)

cmd.color ("blue", "resi 298 & chain A")

cmd.select ("Outward", "resi 298 & chain A", merge=1)

cmd.color ("red", "resi 299 & chain A")

cmd.select ("Inward", "resi 299 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.color ("red", "resi 301 & chain A")

cmd.select ("Inward", "resi 301 & chain A", merge=1)

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

cmd.color ("blue", "resi 318 & chain A")

cmd.select ("Outward", "resi 318 & chain A", merge=1)

cmd.color ("red", "resi 319 & chain A")

cmd.select ("Inward", "resi 319 & chain A", merge=1)

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

cmd.color ("blue", "resi 367 & chain A")

cmd.select ("Outward", "resi 367 & chain A", merge=1)

cmd.color ("red", "resi 368 & chain A")

cmd.select ("Inward", "resi 368 & chain A", merge=1)

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

cmd.color ("red", "resi 379 & chain A")

cmd.select ("Inward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("red", "resi 402 & chain A")

cmd.select ("Inward", "resi 402 & chain A", merge=1)

cmd.color ("blue", "resi 403 & chain A")

cmd.select ("Outward", "resi 403 & chain A", merge=1)

cmd.color ("red", "resi 404 & chain A")

cmd.select ("Inward", "resi 404 & chain A", merge=1)

cmd.color ("blue", "resi 405 & chain A")

cmd.select ("Outward", "resi 405 & chain A", merge=1)

cmd.color ("red", "resi 406 & chain A")

cmd.select ("Inward", "resi 406 & chain A", merge=1)

cmd.color ("blue", "resi 407 & chain A")

cmd.select ("Outward", "resi 407 & chain A", merge=1)

cmd.color ("red", "resi 408 & chain A")

cmd.select ("Inward", "resi 408 & chain A", merge=1)

cmd.color ("blue", "resi 409 & chain A")

cmd.select ("Outward", "resi 409 & chain A", merge=1)

cmd.color ("red", "resi 410 & chain A")

cmd.select ("Inward", "resi 410 & chain A", merge=1)

cmd.color ("blue", "resi 411 & chain A")

cmd.select ("Outward", "resi 411 & chain A", merge=1)

cmd.color ("red", "resi 412 & chain A")

cmd.select ("Inward", "resi 412 & chain A", merge=1)

cmd.color ("blue", "resi 413 & chain A")

cmd.select ("Outward", "resi 413 & chain A", merge=1)

cmd.color ("red", "resi 414 & chain A")

cmd.select ("Inward", "resi 414 & chain A", merge=1)

cmd.color ("blue", "resi 415 & chain A")

cmd.select ("Outward", "resi 415 & chain A", merge=1)

cmd.color ("red", "resi 416 & chain A")

cmd.select ("Inward", "resi 416 & chain A", merge=1)

cmd.load_cgo( [9.0, 18.261845,31.915073,7.502923, 18.261845, 31.915073, 7.502923, 1, 1,1,0,0,0,1], "axis" )
