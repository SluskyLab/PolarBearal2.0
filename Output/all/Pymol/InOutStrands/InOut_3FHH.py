from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FHH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand16", "resi 135+136+137+138+139+140+141+142+143+144+145+146 & chain A ")


cmd.select("Astrand17", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain A ")


cmd.select("Astrand18", "resi 165+166+167+168+169+170+171+172+173+174+175+176+177+178+179+180+181 & chain A ")


cmd.select("Astrand19", "resi 185+186+187+188+189+190+191+192+193+194+195+196+197+198+199+200+201+202 & chain A ")


cmd.select("Astrand21", "resi 208+209+210+211+212+213+214+215+216+217+218+219+220+221+222+223 & chain A ")


cmd.select("Astrand26", "resi 240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256 & chain A ")


cmd.select("Astrand28", "resi 263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278 & chain A ")


cmd.select("Astrand29", "resi 287+288+289+290+291+292+293+294+295+296+297+298+299+300+301+302+303 & chain A ")


cmd.select("Astrand30", "resi 307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326 & chain A ")


cmd.select("Astrand31", "resi 341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359 & chain A ")


cmd.select("Astrand42", "resi 432+431+430+429+496+497+498+499+500+501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518 & chain A ")


cmd.select("Astrand40", "resi 470+471+472+473+474+475+476+477+478+479+480+481+482+483+442+441+439+440+438+437+436+435 & chain A ")


cmd.select("Astrand34", "resi 385+386+387+388+389+390+391+392+393+394+395+396+397+398+399+400+401 & chain A ")


cmd.select("Astrand35", "resi 404+405+406+407+408+409+410+411+412+413+414+415 & chain A ")


cmd.select("Astrand32", "resi 362+363+364+365+366+367+368+369+370+371+372+373+374+375+376+377+378+379 & chain A ")


cmd.select("Astrand38", "resi 446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464 & chain A ")


cmd.select("Astrand41", "resi 521+522+523+524+525+526+527+528+529+530+531+532+533+487+488+489+490+491 & chain A ")


cmd.select("Astrand44", "resi 539+540+541+542+543+544+545+548+549+550+551+552+553+554+555+556+557 & chain A ")


cmd.select("Astrand46", "resi 562+563+564+565+566+567+568+569+570+571 & chain A ")


cmd.select("Astrand48", "resi 587+588+589+590+591+592+593+594+595+596+597+598+599 & chain A ")


cmd.select("Astrand49", "resi 605+606+607+608+609+610+611+612 & chain A ")


cmd.select("Astrand52", "resi 630+631+632+633+634+635+636+637+638+639 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 135 & chain A")

cmd.select ("Inward", "resi 135 & chain A", merge=1)

cmd.color ("red", "resi 136 & chain A")

cmd.select ("Inward", "resi 136 & chain A", merge=1)

cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

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

cmd.color ("red", "resi 159 & chain A")

cmd.select ("Inward", "resi 159 & chain A", merge=1)

cmd.color ("blue", "resi 160 & chain A")

cmd.select ("Outward", "resi 160 & chain A", merge=1)

cmd.color ("red", "resi 161 & chain A")

cmd.select ("Inward", "resi 161 & chain A", merge=1)

cmd.color ("red", "resi 162 & chain A")

cmd.select ("Inward", "resi 162 & chain A", merge=1)

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

cmd.color ("red", "resi 179 & chain A")

cmd.select ("Inward", "resi 179 & chain A", merge=1)

cmd.color ("blue", "resi 180 & chain A")

cmd.select ("Outward", "resi 180 & chain A", merge=1)

cmd.color ("red", "resi 181 & chain A")

cmd.select ("Inward", "resi 181 & chain A", merge=1)

cmd.color ("red", "resi 185 & chain A")

cmd.select ("Inward", "resi 185 & chain A", merge=1)

cmd.color ("blue", "resi 186 & chain A")

cmd.select ("Outward", "resi 186 & chain A", merge=1)

cmd.color ("red", "resi 187 & chain A")

cmd.select ("Inward", "resi 187 & chain A", merge=1)

cmd.color ("red", "resi 188 & chain A")

cmd.select ("Inward", "resi 188 & chain A", merge=1)

cmd.color ("blue", "resi 189 & chain A")

cmd.select ("Outward", "resi 189 & chain A", merge=1)

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

cmd.color ("red", "resi 201 & chain A")

cmd.select ("Inward", "resi 201 & chain A", merge=1)

cmd.color ("blue", "resi 202 & chain A")

cmd.select ("Outward", "resi 202 & chain A", merge=1)

cmd.color ("blue", "resi 208 & chain A")

cmd.select ("Outward", "resi 208 & chain A", merge=1)

cmd.color ("red", "resi 209 & chain A")

cmd.select ("Inward", "resi 209 & chain A", merge=1)

cmd.color ("blue", "resi 210 & chain A")

cmd.select ("Outward", "resi 210 & chain A", merge=1)

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

cmd.color ("red", "resi 223 & chain A")

cmd.select ("Inward", "resi 223 & chain A", merge=1)

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

cmd.color ("red", "resi 248 & chain A")

cmd.select ("Inward", "resi 248 & chain A", merge=1)

cmd.color ("blue", "resi 249 & chain A")

cmd.select ("Outward", "resi 249 & chain A", merge=1)

cmd.color ("red", "resi 250 & chain A")

cmd.select ("Inward", "resi 250 & chain A", merge=1)

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

cmd.color ("blue", "resi 287 & chain A")

cmd.select ("Outward", "resi 287 & chain A", merge=1)

cmd.color ("red", "resi 288 & chain A")

cmd.select ("Inward", "resi 288 & chain A", merge=1)

cmd.color ("blue", "resi 289 & chain A")

cmd.select ("Outward", "resi 289 & chain A", merge=1)

cmd.color ("red", "resi 290 & chain A")

cmd.select ("Inward", "resi 290 & chain A", merge=1)

cmd.color ("blue", "resi 291 & chain A")

cmd.select ("Outward", "resi 291 & chain A", merge=1)

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

cmd.color ("red", "resi 307 & chain A")

cmd.select ("Inward", "resi 307 & chain A", merge=1)

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

cmd.color ("red", "resi 318 & chain A")

cmd.select ("Inward", "resi 318 & chain A", merge=1)

cmd.color ("blue", "resi 319 & chain A")

cmd.select ("Outward", "resi 319 & chain A", merge=1)

cmd.color ("red", "resi 320 & chain A")

cmd.select ("Inward", "resi 320 & chain A", merge=1)

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

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

cmd.color ("red", "resi 342 & chain A")

cmd.select ("Inward", "resi 342 & chain A", merge=1)

cmd.color ("blue", "resi 343 & chain A")

cmd.select ("Outward", "resi 343 & chain A", merge=1)

cmd.color ("red", "resi 344 & chain A")

cmd.select ("Inward", "resi 344 & chain A", merge=1)

cmd.color ("blue", "resi 345 & chain A")

cmd.select ("Outward", "resi 345 & chain A", merge=1)

cmd.color ("red", "resi 346 & chain A")

cmd.select ("Inward", "resi 346 & chain A", merge=1)

cmd.color ("blue", "resi 347 & chain A")

cmd.select ("Outward", "resi 347 & chain A", merge=1)

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

cmd.color ("blue", "resi 358 & chain A")

cmd.select ("Outward", "resi 358 & chain A", merge=1)

cmd.color ("red", "resi 359 & chain A")

cmd.select ("Inward", "resi 359 & chain A", merge=1)

cmd.color ("red", "resi 432 & chain A")

cmd.select ("Inward", "resi 432 & chain A", merge=1)

cmd.color ("blue", "resi 431 & chain A")

cmd.select ("Outward", "resi 431 & chain A", merge=1)

cmd.color ("red", "resi 430 & chain A")

cmd.select ("Inward", "resi 430 & chain A", merge=1)

cmd.color ("blue", "resi 429 & chain A")

cmd.select ("Outward", "resi 429 & chain A", merge=1)

cmd.color ("blue", "resi 496 & chain A")

cmd.select ("Outward", "resi 496 & chain A", merge=1)

cmd.color ("red", "resi 497 & chain A")

cmd.select ("Inward", "resi 497 & chain A", merge=1)

cmd.color ("blue", "resi 498 & chain A")

cmd.select ("Outward", "resi 498 & chain A", merge=1)

cmd.color ("blue", "resi 499 & chain A")

cmd.select ("Outward", "resi 499 & chain A", merge=1)

cmd.color ("red", "resi 500 & chain A")

cmd.select ("Inward", "resi 500 & chain A", merge=1)

cmd.color ("blue", "resi 501 & chain A")

cmd.select ("Outward", "resi 501 & chain A", merge=1)

cmd.color ("red", "resi 502 & chain A")

cmd.select ("Inward", "resi 502 & chain A", merge=1)

cmd.color ("blue", "resi 503 & chain A")

cmd.select ("Outward", "resi 503 & chain A", merge=1)

cmd.color ("blue", "resi 504 & chain A")

cmd.select ("Outward", "resi 504 & chain A", merge=1)

cmd.color ("red", "resi 505 & chain A")

cmd.select ("Inward", "resi 505 & chain A", merge=1)

cmd.color ("blue", "resi 506 & chain A")

cmd.select ("Outward", "resi 506 & chain A", merge=1)

cmd.color ("red", "resi 507 & chain A")

cmd.select ("Inward", "resi 507 & chain A", merge=1)

cmd.color ("blue", "resi 508 & chain A")

cmd.select ("Outward", "resi 508 & chain A", merge=1)

cmd.color ("red", "resi 509 & chain A")

cmd.select ("Inward", "resi 509 & chain A", merge=1)

cmd.color ("blue", "resi 510 & chain A")

cmd.select ("Outward", "resi 510 & chain A", merge=1)

cmd.color ("red", "resi 511 & chain A")

cmd.select ("Inward", "resi 511 & chain A", merge=1)

cmd.color ("blue", "resi 512 & chain A")

cmd.select ("Outward", "resi 512 & chain A", merge=1)

cmd.color ("red", "resi 513 & chain A")

cmd.select ("Inward", "resi 513 & chain A", merge=1)

cmd.color ("blue", "resi 514 & chain A")

cmd.select ("Outward", "resi 514 & chain A", merge=1)

cmd.color ("red", "resi 515 & chain A")

cmd.select ("Inward", "resi 515 & chain A", merge=1)

cmd.color ("blue", "resi 516 & chain A")

cmd.select ("Outward", "resi 516 & chain A", merge=1)

cmd.color ("red", "resi 517 & chain A")

cmd.select ("Inward", "resi 517 & chain A", merge=1)

cmd.color ("blue", "resi 518 & chain A")

cmd.select ("Outward", "resi 518 & chain A", merge=1)

cmd.color ("red", "resi 470 & chain A")

cmd.select ("Inward", "resi 470 & chain A", merge=1)

cmd.color ("blue", "resi 471 & chain A")

cmd.select ("Outward", "resi 471 & chain A", merge=1)

cmd.color ("red", "resi 472 & chain A")

cmd.select ("Inward", "resi 472 & chain A", merge=1)

cmd.color ("blue", "resi 473 & chain A")

cmd.select ("Outward", "resi 473 & chain A", merge=1)

cmd.color ("red", "resi 474 & chain A")

cmd.select ("Inward", "resi 474 & chain A", merge=1)

cmd.color ("blue", "resi 475 & chain A")

cmd.select ("Outward", "resi 475 & chain A", merge=1)

cmd.color ("red", "resi 476 & chain A")

cmd.select ("Inward", "resi 476 & chain A", merge=1)

cmd.color ("blue", "resi 477 & chain A")

cmd.select ("Outward", "resi 477 & chain A", merge=1)

cmd.color ("red", "resi 478 & chain A")

cmd.select ("Inward", "resi 478 & chain A", merge=1)

cmd.color ("blue", "resi 479 & chain A")

cmd.select ("Outward", "resi 479 & chain A", merge=1)

cmd.color ("red", "resi 480 & chain A")

cmd.select ("Inward", "resi 480 & chain A", merge=1)

cmd.color ("blue", "resi 481 & chain A")

cmd.select ("Outward", "resi 481 & chain A", merge=1)

cmd.color ("red", "resi 482 & chain A")

cmd.select ("Inward", "resi 482 & chain A", merge=1)

cmd.color ("blue", "resi 483 & chain A")

cmd.select ("Outward", "resi 483 & chain A", merge=1)

cmd.color ("blue", "resi 442 & chain A")

cmd.select ("Outward", "resi 442 & chain A", merge=1)

cmd.color ("red", "resi 441 & chain A")

cmd.select ("Inward", "resi 441 & chain A", merge=1)

cmd.color ("red", "resi 439 & chain A")

cmd.select ("Inward", "resi 439 & chain A", merge=1)

cmd.color ("blue", "resi 440 & chain A")

cmd.select ("Outward", "resi 440 & chain A", merge=1)

cmd.color ("blue", "resi 438 & chain A")

cmd.select ("Outward", "resi 438 & chain A", merge=1)

cmd.color ("red", "resi 437 & chain A")

cmd.select ("Inward", "resi 437 & chain A", merge=1)

cmd.color ("red", "resi 436 & chain A")

cmd.select ("Inward", "resi 436 & chain A", merge=1)

cmd.color ("blue", "resi 435 & chain A")

cmd.select ("Outward", "resi 435 & chain A", merge=1)

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

cmd.color ("blue", "resi 399 & chain A")

cmd.select ("Outward", "resi 399 & chain A", merge=1)

cmd.color ("red", "resi 400 & chain A")

cmd.select ("Inward", "resi 400 & chain A", merge=1)

cmd.color ("blue", "resi 401 & chain A")

cmd.select ("Outward", "resi 401 & chain A", merge=1)

cmd.color ("blue", "resi 404 & chain A")

cmd.select ("Outward", "resi 404 & chain A", merge=1)

cmd.color ("red", "resi 405 & chain A")

cmd.select ("Inward", "resi 405 & chain A", merge=1)

cmd.color ("blue", "resi 406 & chain A")

cmd.select ("Outward", "resi 406 & chain A", merge=1)

cmd.color ("red", "resi 407 & chain A")

cmd.select ("Inward", "resi 407 & chain A", merge=1)

cmd.color ("blue", "resi 408 & chain A")

cmd.select ("Outward", "resi 408 & chain A", merge=1)

cmd.color ("red", "resi 409 & chain A")

cmd.select ("Inward", "resi 409 & chain A", merge=1)

cmd.color ("blue", "resi 410 & chain A")

cmd.select ("Outward", "resi 410 & chain A", merge=1)

cmd.color ("red", "resi 411 & chain A")

cmd.select ("Inward", "resi 411 & chain A", merge=1)

cmd.color ("blue", "resi 412 & chain A")

cmd.select ("Outward", "resi 412 & chain A", merge=1)

cmd.color ("red", "resi 413 & chain A")

cmd.select ("Inward", "resi 413 & chain A", merge=1)

cmd.color ("blue", "resi 414 & chain A")

cmd.select ("Outward", "resi 414 & chain A", merge=1)

cmd.color ("red", "resi 415 & chain A")

cmd.select ("Inward", "resi 415 & chain A", merge=1)

cmd.color ("red", "resi 362 & chain A")

cmd.select ("Inward", "resi 362 & chain A", merge=1)

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

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("red", "resi 375 & chain A")

cmd.select ("Inward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("red", "resi 377 & chain A")

cmd.select ("Inward", "resi 377 & chain A", merge=1)

cmd.color ("blue", "resi 378 & chain A")

cmd.select ("Outward", "resi 378 & chain A", merge=1)

cmd.color ("red", "resi 379 & chain A")

cmd.select ("Inward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 446 & chain A")

cmd.select ("Outward", "resi 446 & chain A", merge=1)

cmd.color ("blue", "resi 447 & chain A")

cmd.select ("Outward", "resi 447 & chain A", merge=1)

cmd.color ("red", "resi 448 & chain A")

cmd.select ("Inward", "resi 448 & chain A", merge=1)

cmd.color ("blue", "resi 449 & chain A")

cmd.select ("Outward", "resi 449 & chain A", merge=1)

cmd.color ("red", "resi 450 & chain A")

cmd.select ("Inward", "resi 450 & chain A", merge=1)

cmd.color ("blue", "resi 451 & chain A")

cmd.select ("Outward", "resi 451 & chain A", merge=1)

cmd.color ("red", "resi 452 & chain A")

cmd.select ("Inward", "resi 452 & chain A", merge=1)

cmd.color ("blue", "resi 453 & chain A")

cmd.select ("Outward", "resi 453 & chain A", merge=1)

cmd.color ("red", "resi 454 & chain A")

cmd.select ("Inward", "resi 454 & chain A", merge=1)

cmd.color ("blue", "resi 455 & chain A")

cmd.select ("Outward", "resi 455 & chain A", merge=1)

cmd.color ("red", "resi 456 & chain A")

cmd.select ("Inward", "resi 456 & chain A", merge=1)

cmd.color ("blue", "resi 457 & chain A")

cmd.select ("Outward", "resi 457 & chain A", merge=1)

cmd.color ("red", "resi 458 & chain A")

cmd.select ("Inward", "resi 458 & chain A", merge=1)

cmd.color ("blue", "resi 459 & chain A")

cmd.select ("Outward", "resi 459 & chain A", merge=1)

cmd.color ("red", "resi 460 & chain A")

cmd.select ("Inward", "resi 460 & chain A", merge=1)

cmd.color ("blue", "resi 461 & chain A")

cmd.select ("Outward", "resi 461 & chain A", merge=1)

cmd.color ("red", "resi 462 & chain A")

cmd.select ("Inward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("red", "resi 464 & chain A")

cmd.select ("Inward", "resi 464 & chain A", merge=1)

cmd.color ("blue", "resi 521 & chain A")

cmd.select ("Outward", "resi 521 & chain A", merge=1)

cmd.color ("red", "resi 522 & chain A")

cmd.select ("Inward", "resi 522 & chain A", merge=1)

cmd.color ("blue", "resi 523 & chain A")

cmd.select ("Outward", "resi 523 & chain A", merge=1)

cmd.color ("red", "resi 524 & chain A")

cmd.select ("Inward", "resi 524 & chain A", merge=1)

cmd.color ("blue", "resi 525 & chain A")

cmd.select ("Outward", "resi 525 & chain A", merge=1)

cmd.color ("red", "resi 526 & chain A")

cmd.select ("Inward", "resi 526 & chain A", merge=1)

cmd.color ("blue", "resi 527 & chain A")

cmd.select ("Outward", "resi 527 & chain A", merge=1)

cmd.color ("red", "resi 528 & chain A")

cmd.select ("Inward", "resi 528 & chain A", merge=1)

cmd.color ("blue", "resi 529 & chain A")

cmd.select ("Outward", "resi 529 & chain A", merge=1)

cmd.color ("red", "resi 530 & chain A")

cmd.select ("Inward", "resi 530 & chain A", merge=1)

cmd.color ("blue", "resi 531 & chain A")

cmd.select ("Outward", "resi 531 & chain A", merge=1)

cmd.color ("red", "resi 532 & chain A")

cmd.select ("Inward", "resi 532 & chain A", merge=1)

cmd.color ("blue", "resi 533 & chain A")

cmd.select ("Outward", "resi 533 & chain A", merge=1)

cmd.color ("red", "resi 487 & chain A")

cmd.select ("Inward", "resi 487 & chain A", merge=1)

cmd.color ("blue", "resi 488 & chain A")

cmd.select ("Outward", "resi 488 & chain A", merge=1)

cmd.color ("blue", "resi 489 & chain A")

cmd.select ("Outward", "resi 489 & chain A", merge=1)

cmd.color ("blue", "resi 490 & chain A")

cmd.select ("Outward", "resi 490 & chain A", merge=1)

cmd.color ("blue", "resi 491 & chain A")

cmd.select ("Outward", "resi 491 & chain A", merge=1)

cmd.color ("red", "resi 539 & chain A")

cmd.select ("Inward", "resi 539 & chain A", merge=1)

cmd.color ("blue", "resi 540 & chain A")

cmd.select ("Outward", "resi 540 & chain A", merge=1)

cmd.color ("blue", "resi 541 & chain A")

cmd.select ("Outward", "resi 541 & chain A", merge=1)

cmd.color ("red", "resi 542 & chain A")

cmd.select ("Inward", "resi 542 & chain A", merge=1)

cmd.color ("red", "resi 543 & chain A")

cmd.select ("Inward", "resi 543 & chain A", merge=1)

cmd.color ("blue", "resi 544 & chain A")

cmd.select ("Outward", "resi 544 & chain A", merge=1)

cmd.color ("blue", "resi 545 & chain A")

cmd.select ("Outward", "resi 545 & chain A", merge=1)

cmd.color ("red", "resi 548 & chain A")

cmd.select ("Inward", "resi 548 & chain A", merge=1)

cmd.color ("blue", "resi 549 & chain A")

cmd.select ("Outward", "resi 549 & chain A", merge=1)

cmd.color ("red", "resi 550 & chain A")

cmd.select ("Inward", "resi 550 & chain A", merge=1)

cmd.color ("blue", "resi 551 & chain A")

cmd.select ("Outward", "resi 551 & chain A", merge=1)

cmd.color ("red", "resi 552 & chain A")

cmd.select ("Inward", "resi 552 & chain A", merge=1)

cmd.color ("blue", "resi 553 & chain A")

cmd.select ("Outward", "resi 553 & chain A", merge=1)

cmd.color ("red", "resi 554 & chain A")

cmd.select ("Inward", "resi 554 & chain A", merge=1)

cmd.color ("blue", "resi 555 & chain A")

cmd.select ("Outward", "resi 555 & chain A", merge=1)

cmd.color ("blue", "resi 556 & chain A")

cmd.select ("Outward", "resi 556 & chain A", merge=1)

cmd.color ("red", "resi 557 & chain A")

cmd.select ("Inward", "resi 557 & chain A", merge=1)

cmd.color ("blue", "resi 562 & chain A")

cmd.select ("Outward", "resi 562 & chain A", merge=1)

cmd.color ("red", "resi 563 & chain A")

cmd.select ("Inward", "resi 563 & chain A", merge=1)

cmd.color ("blue", "resi 564 & chain A")

cmd.select ("Outward", "resi 564 & chain A", merge=1)

cmd.color ("red", "resi 565 & chain A")

cmd.select ("Inward", "resi 565 & chain A", merge=1)

cmd.color ("blue", "resi 566 & chain A")

cmd.select ("Outward", "resi 566 & chain A", merge=1)

cmd.color ("red", "resi 567 & chain A")

cmd.select ("Inward", "resi 567 & chain A", merge=1)

cmd.color ("blue", "resi 568 & chain A")

cmd.select ("Outward", "resi 568 & chain A", merge=1)

cmd.color ("red", "resi 569 & chain A")

cmd.select ("Inward", "resi 569 & chain A", merge=1)

cmd.color ("blue", "resi 570 & chain A")

cmd.select ("Outward", "resi 570 & chain A", merge=1)

cmd.color ("red", "resi 571 & chain A")

cmd.select ("Inward", "resi 571 & chain A", merge=1)

cmd.color ("red", "resi 587 & chain A")

cmd.select ("Inward", "resi 587 & chain A", merge=1)

cmd.color ("blue", "resi 588 & chain A")

cmd.select ("Outward", "resi 588 & chain A", merge=1)

cmd.color ("red", "resi 589 & chain A")

cmd.select ("Inward", "resi 589 & chain A", merge=1)

cmd.color ("blue", "resi 590 & chain A")

cmd.select ("Outward", "resi 590 & chain A", merge=1)

cmd.color ("red", "resi 591 & chain A")

cmd.select ("Inward", "resi 591 & chain A", merge=1)

cmd.color ("blue", "resi 592 & chain A")

cmd.select ("Outward", "resi 592 & chain A", merge=1)

cmd.color ("red", "resi 593 & chain A")

cmd.select ("Inward", "resi 593 & chain A", merge=1)

cmd.color ("blue", "resi 594 & chain A")

cmd.select ("Outward", "resi 594 & chain A", merge=1)

cmd.color ("red", "resi 595 & chain A")

cmd.select ("Inward", "resi 595 & chain A", merge=1)

cmd.color ("blue", "resi 596 & chain A")

cmd.select ("Outward", "resi 596 & chain A", merge=1)

cmd.color ("blue", "resi 597 & chain A")

cmd.select ("Outward", "resi 597 & chain A", merge=1)

cmd.color ("red", "resi 598 & chain A")

cmd.select ("Inward", "resi 598 & chain A", merge=1)

cmd.color ("blue", "resi 599 & chain A")

cmd.select ("Outward", "resi 599 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("red", "resi 606 & chain A")

cmd.select ("Inward", "resi 606 & chain A", merge=1)

cmd.color ("blue", "resi 607 & chain A")

cmd.select ("Outward", "resi 607 & chain A", merge=1)

cmd.color ("red", "resi 608 & chain A")

cmd.select ("Inward", "resi 608 & chain A", merge=1)

cmd.color ("blue", "resi 609 & chain A")

cmd.select ("Outward", "resi 609 & chain A", merge=1)

cmd.color ("red", "resi 610 & chain A")

cmd.select ("Inward", "resi 610 & chain A", merge=1)

cmd.color ("blue", "resi 611 & chain A")

cmd.select ("Outward", "resi 611 & chain A", merge=1)

cmd.color ("red", "resi 612 & chain A")

cmd.select ("Inward", "resi 612 & chain A", merge=1)

cmd.color ("blue", "resi 630 & chain A")

cmd.select ("Outward", "resi 630 & chain A", merge=1)

cmd.color ("red", "resi 631 & chain A")

cmd.select ("Inward", "resi 631 & chain A", merge=1)

cmd.color ("blue", "resi 632 & chain A")

cmd.select ("Outward", "resi 632 & chain A", merge=1)

cmd.color ("red", "resi 633 & chain A")

cmd.select ("Inward", "resi 633 & chain A", merge=1)

cmd.color ("blue", "resi 634 & chain A")

cmd.select ("Outward", "resi 634 & chain A", merge=1)

cmd.color ("red", "resi 635 & chain A")

cmd.select ("Inward", "resi 635 & chain A", merge=1)

cmd.color ("blue", "resi 636 & chain A")

cmd.select ("Outward", "resi 636 & chain A", merge=1)

cmd.color ("red", "resi 637 & chain A")

cmd.select ("Inward", "resi 637 & chain A", merge=1)

cmd.color ("blue", "resi 638 & chain A")

cmd.select ("Outward", "resi 638 & chain A", merge=1)

cmd.color ("red", "resi 639 & chain A")

cmd.select ("Inward", "resi 639 & chain A", merge=1)

cmd.load_cgo( [9.0, 1.7401366,22.589865,49.936584, 1.7401366, 22.589865, 49.936584, 1, 1,1,0,0,0,1], "axis" )
