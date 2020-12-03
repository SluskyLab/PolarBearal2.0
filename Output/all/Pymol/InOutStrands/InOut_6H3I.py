from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H3I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Fstrand79", "resi 72+73+74+75+76+77+78 & chain F ")


cmd.select("Fstrand92", "resi 389+390+391+392+393+394 & chain F ")


cmd.select("Fstrand80", "resi 88+89+90+91+92+93+94+95+96+97+98 & chain F ")


cmd.select("Fstrand91", "resi 367+368+369+370+371+372 & chain F ")


cmd.select("Fstrand90", "resi 357+358+359+360+361+362 & chain F ")


cmd.select("Fstrand89", "resi 336+337+338+339+340+341+342+343+344 & chain F ")


cmd.select("Fstrand87", "resi 246+247+248+249+250+251+252+253+254 & chain F ")


cmd.select("Fstrand88", "resi 323+324+325+326+327+328 & chain F ")


cmd.select("Fstrand85", "resi 201+202+203+204+205+206+207+208 & chain F ")


cmd.select("Fstrand86", "resi 231+232+233+234+235+236+237+238+239+240 & chain F ")


cmd.select("Fstrand84", "resi 178+179+180+181+182+183+184+185+186+187+188+189 & chain F ")


cmd.select("Fstrand83", "resi 152+153+154+155+156+157+158+159+160+161+162 & chain F ")


cmd.select("Fstrand82", "resi 139+140+141+142+143+144+145+146 & chain F ")


cmd.select("Fstrand81", "resi 104+105+106+107+108+109+110+111+112+113+114+115+116 & chain F ")


cmd.select("barrel", "Fstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 72 & chain F")

cmd.select ("Outward", "resi 72 & chain F", merge=1)

cmd.color ("red", "resi 73 & chain F")

cmd.select ("Inward", "resi 73 & chain F", merge=1)

cmd.color ("blue", "resi 74 & chain F")

cmd.select ("Outward", "resi 74 & chain F", merge=1)

cmd.color ("red", "resi 75 & chain F")

cmd.select ("Inward", "resi 75 & chain F", merge=1)

cmd.color ("blue", "resi 76 & chain F")

cmd.select ("Outward", "resi 76 & chain F", merge=1)

cmd.color ("red", "resi 77 & chain F")

cmd.select ("Inward", "resi 77 & chain F", merge=1)

cmd.color ("blue", "resi 78 & chain F")

cmd.select ("Outward", "resi 78 & chain F", merge=1)

cmd.color ("blue", "resi 389 & chain F")

cmd.select ("Outward", "resi 389 & chain F", merge=1)

cmd.color ("red", "resi 390 & chain F")

cmd.select ("Inward", "resi 390 & chain F", merge=1)

cmd.color ("blue", "resi 391 & chain F")

cmd.select ("Outward", "resi 391 & chain F", merge=1)

cmd.color ("red", "resi 392 & chain F")

cmd.select ("Inward", "resi 392 & chain F", merge=1)

cmd.color ("blue", "resi 393 & chain F")

cmd.select ("Outward", "resi 393 & chain F", merge=1)

cmd.color ("blue", "resi 394 & chain F")

cmd.select ("Outward", "resi 394 & chain F", merge=1)

cmd.color ("blue", "resi 88 & chain F")

cmd.select ("Outward", "resi 88 & chain F", merge=1)

cmd.color ("red", "resi 89 & chain F")

cmd.select ("Inward", "resi 89 & chain F", merge=1)

cmd.color ("blue", "resi 90 & chain F")

cmd.select ("Outward", "resi 90 & chain F", merge=1)

cmd.color ("red", "resi 91 & chain F")

cmd.select ("Inward", "resi 91 & chain F", merge=1)

cmd.color ("blue", "resi 92 & chain F")

cmd.select ("Outward", "resi 92 & chain F", merge=1)

cmd.color ("red", "resi 93 & chain F")

cmd.select ("Inward", "resi 93 & chain F", merge=1)

cmd.color ("blue", "resi 94 & chain F")

cmd.select ("Outward", "resi 94 & chain F", merge=1)

cmd.color ("red", "resi 95 & chain F")

cmd.select ("Inward", "resi 95 & chain F", merge=1)

cmd.color ("blue", "resi 96 & chain F")

cmd.select ("Outward", "resi 96 & chain F", merge=1)

cmd.color ("red", "resi 97 & chain F")

cmd.select ("Inward", "resi 97 & chain F", merge=1)

cmd.color ("blue", "resi 98 & chain F")

cmd.select ("Outward", "resi 98 & chain F", merge=1)

cmd.color ("red", "resi 367 & chain F")

cmd.select ("Inward", "resi 367 & chain F", merge=1)

cmd.color ("blue", "resi 368 & chain F")

cmd.select ("Outward", "resi 368 & chain F", merge=1)

cmd.color ("red", "resi 369 & chain F")

cmd.select ("Inward", "resi 369 & chain F", merge=1)

cmd.color ("blue", "resi 370 & chain F")

cmd.select ("Outward", "resi 370 & chain F", merge=1)

cmd.color ("red", "resi 371 & chain F")

cmd.select ("Inward", "resi 371 & chain F", merge=1)

cmd.color ("blue", "resi 372 & chain F")

cmd.select ("Outward", "resi 372 & chain F", merge=1)

cmd.color ("blue", "resi 357 & chain F")

cmd.select ("Outward", "resi 357 & chain F", merge=1)

cmd.color ("red", "resi 358 & chain F")

cmd.select ("Inward", "resi 358 & chain F", merge=1)

cmd.color ("blue", "resi 359 & chain F")

cmd.select ("Outward", "resi 359 & chain F", merge=1)

cmd.color ("red", "resi 360 & chain F")

cmd.select ("Inward", "resi 360 & chain F", merge=1)

cmd.color ("blue", "resi 361 & chain F")

cmd.select ("Outward", "resi 361 & chain F", merge=1)

cmd.color ("blue", "resi 362 & chain F")

cmd.select ("Outward", "resi 362 & chain F", merge=1)

cmd.color ("blue", "resi 336 & chain F")

cmd.select ("Outward", "resi 336 & chain F", merge=1)

cmd.color ("red", "resi 337 & chain F")

cmd.select ("Inward", "resi 337 & chain F", merge=1)

cmd.color ("blue", "resi 338 & chain F")

cmd.select ("Outward", "resi 338 & chain F", merge=1)

cmd.color ("red", "resi 339 & chain F")

cmd.select ("Inward", "resi 339 & chain F", merge=1)

cmd.color ("blue", "resi 340 & chain F")

cmd.select ("Outward", "resi 340 & chain F", merge=1)

cmd.color ("red", "resi 341 & chain F")

cmd.select ("Inward", "resi 341 & chain F", merge=1)

cmd.color ("blue", "resi 342 & chain F")

cmd.select ("Outward", "resi 342 & chain F", merge=1)

cmd.color ("red", "resi 343 & chain F")

cmd.select ("Inward", "resi 343 & chain F", merge=1)

cmd.color ("blue", "resi 344 & chain F")

cmd.select ("Outward", "resi 344 & chain F", merge=1)

cmd.color ("red", "resi 246 & chain F")

cmd.select ("Inward", "resi 246 & chain F", merge=1)

cmd.color ("blue", "resi 247 & chain F")

cmd.select ("Outward", "resi 247 & chain F", merge=1)

cmd.color ("red", "resi 248 & chain F")

cmd.select ("Inward", "resi 248 & chain F", merge=1)

cmd.color ("blue", "resi 249 & chain F")

cmd.select ("Outward", "resi 249 & chain F", merge=1)

cmd.color ("red", "resi 250 & chain F")

cmd.select ("Inward", "resi 250 & chain F", merge=1)

cmd.color ("blue", "resi 251 & chain F")

cmd.select ("Outward", "resi 251 & chain F", merge=1)

cmd.color ("red", "resi 252 & chain F")

cmd.select ("Inward", "resi 252 & chain F", merge=1)

cmd.color ("blue", "resi 253 & chain F")

cmd.select ("Outward", "resi 253 & chain F", merge=1)

cmd.color ("red", "resi 254 & chain F")

cmd.select ("Inward", "resi 254 & chain F", merge=1)

cmd.color ("red", "resi 323 & chain F")

cmd.select ("Inward", "resi 323 & chain F", merge=1)

cmd.color ("blue", "resi 324 & chain F")

cmd.select ("Outward", "resi 324 & chain F", merge=1)

cmd.color ("red", "resi 325 & chain F")

cmd.select ("Inward", "resi 325 & chain F", merge=1)

cmd.color ("blue", "resi 326 & chain F")

cmd.select ("Outward", "resi 326 & chain F", merge=1)

cmd.color ("red", "resi 327 & chain F")

cmd.select ("Inward", "resi 327 & chain F", merge=1)

cmd.color ("blue", "resi 328 & chain F")

cmd.select ("Outward", "resi 328 & chain F", merge=1)

cmd.color ("red", "resi 201 & chain F")

cmd.select ("Inward", "resi 201 & chain F", merge=1)

cmd.color ("blue", "resi 202 & chain F")

cmd.select ("Outward", "resi 202 & chain F", merge=1)

cmd.color ("red", "resi 203 & chain F")

cmd.select ("Inward", "resi 203 & chain F", merge=1)

cmd.color ("blue", "resi 204 & chain F")

cmd.select ("Outward", "resi 204 & chain F", merge=1)

cmd.color ("red", "resi 205 & chain F")

cmd.select ("Inward", "resi 205 & chain F", merge=1)

cmd.color ("blue", "resi 206 & chain F")

cmd.select ("Outward", "resi 206 & chain F", merge=1)

cmd.color ("red", "resi 207 & chain F")

cmd.select ("Inward", "resi 207 & chain F", merge=1)

cmd.color ("blue", "resi 208 & chain F")

cmd.select ("Outward", "resi 208 & chain F", merge=1)

cmd.color ("blue", "resi 231 & chain F")

cmd.select ("Outward", "resi 231 & chain F", merge=1)

cmd.color ("red", "resi 232 & chain F")

cmd.select ("Inward", "resi 232 & chain F", merge=1)

cmd.color ("blue", "resi 233 & chain F")

cmd.select ("Outward", "resi 233 & chain F", merge=1)

cmd.color ("red", "resi 234 & chain F")

cmd.select ("Inward", "resi 234 & chain F", merge=1)

cmd.color ("blue", "resi 235 & chain F")

cmd.select ("Outward", "resi 235 & chain F", merge=1)

cmd.color ("red", "resi 236 & chain F")

cmd.select ("Inward", "resi 236 & chain F", merge=1)

cmd.color ("blue", "resi 237 & chain F")

cmd.select ("Outward", "resi 237 & chain F", merge=1)

cmd.color ("red", "resi 238 & chain F")

cmd.select ("Inward", "resi 238 & chain F", merge=1)

cmd.color ("blue", "resi 239 & chain F")

cmd.select ("Outward", "resi 239 & chain F", merge=1)

cmd.color ("blue", "resi 240 & chain F")

cmd.select ("Outward", "resi 240 & chain F", merge=1)

cmd.color ("blue", "resi 178 & chain F")

cmd.select ("Outward", "resi 178 & chain F", merge=1)

cmd.color ("red", "resi 179 & chain F")

cmd.select ("Inward", "resi 179 & chain F", merge=1)

cmd.color ("blue", "resi 180 & chain F")

cmd.select ("Outward", "resi 180 & chain F", merge=1)

cmd.color ("red", "resi 181 & chain F")

cmd.select ("Inward", "resi 181 & chain F", merge=1)

cmd.color ("blue", "resi 182 & chain F")

cmd.select ("Outward", "resi 182 & chain F", merge=1)

cmd.color ("red", "resi 183 & chain F")

cmd.select ("Inward", "resi 183 & chain F", merge=1)

cmd.color ("blue", "resi 184 & chain F")

cmd.select ("Outward", "resi 184 & chain F", merge=1)

cmd.color ("red", "resi 185 & chain F")

cmd.select ("Inward", "resi 185 & chain F", merge=1)

cmd.color ("blue", "resi 186 & chain F")

cmd.select ("Outward", "resi 186 & chain F", merge=1)

cmd.color ("red", "resi 187 & chain F")

cmd.select ("Inward", "resi 187 & chain F", merge=1)

cmd.color ("blue", "resi 188 & chain F")

cmd.select ("Outward", "resi 188 & chain F", merge=1)

cmd.color ("blue", "resi 189 & chain F")

cmd.select ("Outward", "resi 189 & chain F", merge=1)

cmd.color ("blue", "resi 152 & chain F")

cmd.select ("Outward", "resi 152 & chain F", merge=1)

cmd.color ("red", "resi 153 & chain F")

cmd.select ("Inward", "resi 153 & chain F", merge=1)

cmd.color ("blue", "resi 154 & chain F")

cmd.select ("Outward", "resi 154 & chain F", merge=1)

cmd.color ("red", "resi 155 & chain F")

cmd.select ("Inward", "resi 155 & chain F", merge=1)

cmd.color ("blue", "resi 156 & chain F")

cmd.select ("Outward", "resi 156 & chain F", merge=1)

cmd.color ("red", "resi 157 & chain F")

cmd.select ("Inward", "resi 157 & chain F", merge=1)

cmd.color ("blue", "resi 158 & chain F")

cmd.select ("Outward", "resi 158 & chain F", merge=1)

cmd.color ("red", "resi 159 & chain F")

cmd.select ("Inward", "resi 159 & chain F", merge=1)

cmd.color ("blue", "resi 160 & chain F")

cmd.select ("Outward", "resi 160 & chain F", merge=1)

cmd.color ("red", "resi 161 & chain F")

cmd.select ("Inward", "resi 161 & chain F", merge=1)

cmd.color ("blue", "resi 162 & chain F")

cmd.select ("Outward", "resi 162 & chain F", merge=1)

cmd.color ("red", "resi 139 & chain F")

cmd.select ("Inward", "resi 139 & chain F", merge=1)

cmd.color ("blue", "resi 140 & chain F")

cmd.select ("Outward", "resi 140 & chain F", merge=1)

cmd.color ("red", "resi 141 & chain F")

cmd.select ("Inward", "resi 141 & chain F", merge=1)

cmd.color ("blue", "resi 142 & chain F")

cmd.select ("Outward", "resi 142 & chain F", merge=1)

cmd.color ("red", "resi 143 & chain F")

cmd.select ("Inward", "resi 143 & chain F", merge=1)

cmd.color ("blue", "resi 144 & chain F")

cmd.select ("Outward", "resi 144 & chain F", merge=1)

cmd.color ("red", "resi 145 & chain F")

cmd.select ("Inward", "resi 145 & chain F", merge=1)

cmd.color ("blue", "resi 146 & chain F")

cmd.select ("Outward", "resi 146 & chain F", merge=1)

cmd.color ("blue", "resi 104 & chain F")

cmd.select ("Outward", "resi 104 & chain F", merge=1)

cmd.color ("red", "resi 105 & chain F")

cmd.select ("Inward", "resi 105 & chain F", merge=1)

cmd.color ("blue", "resi 106 & chain F")

cmd.select ("Outward", "resi 106 & chain F", merge=1)

cmd.color ("red", "resi 107 & chain F")

cmd.select ("Inward", "resi 107 & chain F", merge=1)

cmd.color ("blue", "resi 108 & chain F")

cmd.select ("Outward", "resi 108 & chain F", merge=1)

cmd.color ("red", "resi 109 & chain F")

cmd.select ("Inward", "resi 109 & chain F", merge=1)

cmd.color ("blue", "resi 110 & chain F")

cmd.select ("Outward", "resi 110 & chain F", merge=1)

cmd.color ("red", "resi 111 & chain F")

cmd.select ("Inward", "resi 111 & chain F", merge=1)

cmd.color ("blue", "resi 112 & chain F")

cmd.select ("Outward", "resi 112 & chain F", merge=1)

cmd.color ("red", "resi 113 & chain F")

cmd.select ("Inward", "resi 113 & chain F", merge=1)

cmd.color ("red", "resi 114 & chain F")

cmd.select ("Inward", "resi 114 & chain F", merge=1)

cmd.color ("blue", "resi 115 & chain F")

cmd.select ("Outward", "resi 115 & chain F", merge=1)

cmd.color ("red", "resi 116 & chain F")

cmd.select ("Inward", "resi 116 & chain F", merge=1)

cmd.load_cgo( [9.0, 139.34293,150.16772,144.352, 139.34293, 150.16772, 144.352, 1, 1,1,0,0,0,1], "axis" )
