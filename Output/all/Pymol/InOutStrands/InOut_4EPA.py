from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand5", "resi 140+141+142+143+144+145+146+147+148 & chain A ")


cmd.select("Astrand6", "resi 152+153+154+155+156+157+158+159+160+161+162+163+164 & chain A ")


cmd.select("Astrand7", "resi 168+169+170+171+172+173+174+175+176+177+178+179 & chain A ")


cmd.select("Astrand8", "resi 196+197+198+199+200+201+202+203+204+205+206+207 & chain A ")


cmd.select("Astrand9", "resi 214+215+216+217+218+219+220+221+222+223+224+225+226+227 & chain A ")


cmd.select("Astrand11", "resi 253+254+255+256+257+258+259+260+261+262+263 & chain A ")


cmd.select("Astrand13", "resi 273+274+275+276+277+278+279+280+281+282+283+284+285+286+287+288+289+290+291 & chain A ")


cmd.select("Astrand14", "resi 294+295+296+297+300+301+302+303+304+305+306+307+308+309+310+311+312 & chain A ")


cmd.select("Astrand16", "resi 320+321+322+323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340 & chain A ")


cmd.select("Astrand17", "resi 345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366+367 & chain A ")


cmd.select("Astrand18", "resi 372+373+374+375+376+377+378+379+380+381+382+383+384+385+386+387+388+389+390+391+392+393 & chain A ")


cmd.select("Astrand19", "resi 396+397+398+399+400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419+420 & chain A ")


cmd.select("Astrand22", "resi 454+455+456+457+458+459+460+461+462+463+464+465+466 & chain A ")


cmd.select("Astrand20", "resi 423+424+425+426+427+428+429+430 & chain A ")


cmd.select("Astrand23", "resi 470+471+472+473+474+475+476+477+478+479+480+481+482 & chain A ")


cmd.select("Astrand26", "resi 501+502+503+504+505+506+507+508+509+510+511+512+513 & chain A ")


cmd.select("Astrand27", "resi 520+521+522+523+524+525+526+527+528+529+530+531+532 & chain A ")


cmd.select("Astrand28", "resi 550+551+552+553+554+555+556+557 & chain A ")


cmd.select("Astrand29", "resi 567+568+569+570+571+572+573+574+575+576 & chain A ")


cmd.select("Astrand30", "resi 592+593+594+595+596+597+598+599+600+601 & chain A ")


cmd.select("Astrand31", "resi 607+608+609+610+611+612+613+614 & chain A ")


cmd.select("Astrand34", "resi 641+642+643+644+645+646+647+648 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 157 & chain A")

cmd.select ("Outward", "resi 157 & chain A", merge=1)

cmd.color ("red", "resi 158 & chain A")

cmd.select ("Inward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("red", "resi 160 & chain A")

cmd.select ("Inward", "resi 160 & chain A", merge=1)

cmd.color ("blue", "resi 161 & chain A")

cmd.select ("Outward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 162 & chain A")

cmd.select ("Outward", "resi 162 & chain A", merge=1)

cmd.color ("red", "resi 163 & chain A")

cmd.select ("Inward", "resi 163 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

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

cmd.color ("blue", "resi 174 & chain A")

cmd.select ("Outward", "resi 174 & chain A", merge=1)

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

cmd.color ("blue", "resi 205 & chain A")

cmd.select ("Outward", "resi 205 & chain A", merge=1)

cmd.color ("red", "resi 206 & chain A")

cmd.select ("Inward", "resi 206 & chain A", merge=1)

cmd.color ("blue", "resi 207 & chain A")

cmd.select ("Outward", "resi 207 & chain A", merge=1)

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

cmd.color ("blue", "resi 224 & chain A")

cmd.select ("Outward", "resi 224 & chain A", merge=1)

cmd.color ("red", "resi 225 & chain A")

cmd.select ("Inward", "resi 225 & chain A", merge=1)

cmd.color ("blue", "resi 226 & chain A")

cmd.select ("Outward", "resi 226 & chain A", merge=1)

cmd.color ("red", "resi 227 & chain A")

cmd.select ("Inward", "resi 227 & chain A", merge=1)

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

cmd.color ("blue", "resi 278 & chain A")

cmd.select ("Outward", "resi 278 & chain A", merge=1)

cmd.color ("red", "resi 279 & chain A")

cmd.select ("Inward", "resi 279 & chain A", merge=1)

cmd.color ("blue", "resi 280 & chain A")

cmd.select ("Outward", "resi 280 & chain A", merge=1)

cmd.color ("red", "resi 281 & chain A")

cmd.select ("Inward", "resi 281 & chain A", merge=1)

cmd.color ("blue", "resi 282 & chain A")

cmd.select ("Outward", "resi 282 & chain A", merge=1)

cmd.color ("red", "resi 283 & chain A")

cmd.select ("Inward", "resi 283 & chain A", merge=1)

cmd.color ("blue", "resi 284 & chain A")

cmd.select ("Outward", "resi 284 & chain A", merge=1)

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

cmd.color ("red", "resi 294 & chain A")

cmd.select ("Inward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("red", "resi 296 & chain A")

cmd.select ("Inward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("red", "resi 300 & chain A")

cmd.select ("Inward", "resi 300 & chain A", merge=1)

cmd.color ("blue", "resi 301 & chain A")

cmd.select ("Outward", "resi 301 & chain A", merge=1)

cmd.color ("red", "resi 302 & chain A")

cmd.select ("Inward", "resi 302 & chain A", merge=1)

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

cmd.color ("red", "resi 325 & chain A")

cmd.select ("Inward", "resi 325 & chain A", merge=1)

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

cmd.color ("red", "resi 337 & chain A")

cmd.select ("Inward", "resi 337 & chain A", merge=1)

cmd.color ("blue", "resi 338 & chain A")

cmd.select ("Outward", "resi 338 & chain A", merge=1)

cmd.color ("red", "resi 339 & chain A")

cmd.select ("Inward", "resi 339 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 345 & chain A")

cmd.select ("Outward", "resi 345 & chain A", merge=1)

cmd.color ("red", "resi 346 & chain A")

cmd.select ("Inward", "resi 346 & chain A", merge=1)

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

cmd.color ("blue", "resi 354 & chain A")

cmd.select ("Outward", "resi 354 & chain A", merge=1)

cmd.color ("red", "resi 355 & chain A")

cmd.select ("Inward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 356 & chain A")

cmd.select ("Outward", "resi 356 & chain A", merge=1)

cmd.color ("red", "resi 357 & chain A")

cmd.select ("Inward", "resi 357 & chain A", merge=1)

cmd.color ("blue", "resi 358 & chain A")

cmd.select ("Outward", "resi 358 & chain A", merge=1)

cmd.color ("red", "resi 359 & chain A")

cmd.select ("Inward", "resi 359 & chain A", merge=1)

cmd.color ("blue", "resi 360 & chain A")

cmd.select ("Outward", "resi 360 & chain A", merge=1)

cmd.color ("red", "resi 361 & chain A")

cmd.select ("Inward", "resi 361 & chain A", merge=1)

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

cmd.color ("blue", "resi 367 & chain A")

cmd.select ("Outward", "resi 367 & chain A", merge=1)

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

cmd.color ("blue", "resi 392 & chain A")

cmd.select ("Outward", "resi 392 & chain A", merge=1)

cmd.color ("red", "resi 393 & chain A")

cmd.select ("Inward", "resi 393 & chain A", merge=1)

cmd.color ("red", "resi 396 & chain A")

cmd.select ("Inward", "resi 396 & chain A", merge=1)

cmd.color ("blue", "resi 397 & chain A")

cmd.select ("Outward", "resi 397 & chain A", merge=1)

cmd.color ("red", "resi 398 & chain A")

cmd.select ("Inward", "resi 398 & chain A", merge=1)

cmd.color ("blue", "resi 399 & chain A")

cmd.select ("Outward", "resi 399 & chain A", merge=1)

cmd.color ("red", "resi 400 & chain A")

cmd.select ("Inward", "resi 400 & chain A", merge=1)

cmd.color ("blue", "resi 401 & chain A")

cmd.select ("Outward", "resi 401 & chain A", merge=1)

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

cmd.color ("blue", "resi 417 & chain A")

cmd.select ("Outward", "resi 417 & chain A", merge=1)

cmd.color ("blue", "resi 418 & chain A")

cmd.select ("Outward", "resi 418 & chain A", merge=1)

cmd.color ("red", "resi 419 & chain A")

cmd.select ("Inward", "resi 419 & chain A", merge=1)

cmd.color ("blue", "resi 420 & chain A")

cmd.select ("Outward", "resi 420 & chain A", merge=1)

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

cmd.color ("blue", "resi 465 & chain A")

cmd.select ("Outward", "resi 465 & chain A", merge=1)

cmd.color ("red", "resi 466 & chain A")

cmd.select ("Inward", "resi 466 & chain A", merge=1)

cmd.color ("blue", "resi 423 & chain A")

cmd.select ("Outward", "resi 423 & chain A", merge=1)

cmd.color ("red", "resi 424 & chain A")

cmd.select ("Inward", "resi 424 & chain A", merge=1)

cmd.color ("blue", "resi 425 & chain A")

cmd.select ("Outward", "resi 425 & chain A", merge=1)

cmd.color ("red", "resi 426 & chain A")

cmd.select ("Inward", "resi 426 & chain A", merge=1)

cmd.color ("blue", "resi 427 & chain A")

cmd.select ("Outward", "resi 427 & chain A", merge=1)

cmd.color ("red", "resi 428 & chain A")

cmd.select ("Inward", "resi 428 & chain A", merge=1)

cmd.color ("blue", "resi 429 & chain A")

cmd.select ("Outward", "resi 429 & chain A", merge=1)

cmd.color ("red", "resi 430 & chain A")

cmd.select ("Inward", "resi 430 & chain A", merge=1)

cmd.color ("blue", "resi 470 & chain A")

cmd.select ("Outward", "resi 470 & chain A", merge=1)

cmd.color ("red", "resi 471 & chain A")

cmd.select ("Inward", "resi 471 & chain A", merge=1)

cmd.color ("blue", "resi 472 & chain A")

cmd.select ("Outward", "resi 472 & chain A", merge=1)

cmd.color ("red", "resi 473 & chain A")

cmd.select ("Inward", "resi 473 & chain A", merge=1)

cmd.color ("blue", "resi 474 & chain A")

cmd.select ("Outward", "resi 474 & chain A", merge=1)

cmd.color ("red", "resi 475 & chain A")

cmd.select ("Inward", "resi 475 & chain A", merge=1)

cmd.color ("blue", "resi 476 & chain A")

cmd.select ("Outward", "resi 476 & chain A", merge=1)

cmd.color ("red", "resi 477 & chain A")

cmd.select ("Inward", "resi 477 & chain A", merge=1)

cmd.color ("blue", "resi 478 & chain A")

cmd.select ("Outward", "resi 478 & chain A", merge=1)

cmd.color ("red", "resi 479 & chain A")

cmd.select ("Inward", "resi 479 & chain A", merge=1)

cmd.color ("blue", "resi 480 & chain A")

cmd.select ("Outward", "resi 480 & chain A", merge=1)

cmd.color ("red", "resi 481 & chain A")

cmd.select ("Inward", "resi 481 & chain A", merge=1)

cmd.color ("blue", "resi 482 & chain A")

cmd.select ("Outward", "resi 482 & chain A", merge=1)

cmd.color ("blue", "resi 501 & chain A")

cmd.select ("Outward", "resi 501 & chain A", merge=1)

cmd.color ("red", "resi 502 & chain A")

cmd.select ("Inward", "resi 502 & chain A", merge=1)

cmd.color ("blue", "resi 503 & chain A")

cmd.select ("Outward", "resi 503 & chain A", merge=1)

cmd.color ("red", "resi 504 & chain A")

cmd.select ("Inward", "resi 504 & chain A", merge=1)

cmd.color ("blue", "resi 505 & chain A")

cmd.select ("Outward", "resi 505 & chain A", merge=1)

cmd.color ("red", "resi 506 & chain A")

cmd.select ("Inward", "resi 506 & chain A", merge=1)

cmd.color ("blue", "resi 507 & chain A")

cmd.select ("Outward", "resi 507 & chain A", merge=1)

cmd.color ("red", "resi 508 & chain A")

cmd.select ("Inward", "resi 508 & chain A", merge=1)

cmd.color ("blue", "resi 509 & chain A")

cmd.select ("Outward", "resi 509 & chain A", merge=1)

cmd.color ("red", "resi 510 & chain A")

cmd.select ("Inward", "resi 510 & chain A", merge=1)

cmd.color ("blue", "resi 511 & chain A")

cmd.select ("Outward", "resi 511 & chain A", merge=1)

cmd.color ("red", "resi 512 & chain A")

cmd.select ("Inward", "resi 512 & chain A", merge=1)

cmd.color ("blue", "resi 513 & chain A")

cmd.select ("Outward", "resi 513 & chain A", merge=1)

cmd.color ("red", "resi 520 & chain A")

cmd.select ("Inward", "resi 520 & chain A", merge=1)

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

cmd.color ("blue", "resi 532 & chain A")

cmd.select ("Outward", "resi 532 & chain A", merge=1)

cmd.color ("blue", "resi 550 & chain A")

cmd.select ("Outward", "resi 550 & chain A", merge=1)

cmd.color ("red", "resi 551 & chain A")

cmd.select ("Inward", "resi 551 & chain A", merge=1)

cmd.color ("blue", "resi 552 & chain A")

cmd.select ("Outward", "resi 552 & chain A", merge=1)

cmd.color ("red", "resi 553 & chain A")

cmd.select ("Inward", "resi 553 & chain A", merge=1)

cmd.color ("blue", "resi 554 & chain A")

cmd.select ("Outward", "resi 554 & chain A", merge=1)

cmd.color ("red", "resi 555 & chain A")

cmd.select ("Inward", "resi 555 & chain A", merge=1)

cmd.color ("blue", "resi 556 & chain A")

cmd.select ("Outward", "resi 556 & chain A", merge=1)

cmd.color ("red", "resi 557 & chain A")

cmd.select ("Inward", "resi 557 & chain A", merge=1)

cmd.color ("blue", "resi 567 & chain A")

cmd.select ("Outward", "resi 567 & chain A", merge=1)

cmd.color ("red", "resi 568 & chain A")

cmd.select ("Inward", "resi 568 & chain A", merge=1)

cmd.color ("blue", "resi 569 & chain A")

cmd.select ("Outward", "resi 569 & chain A", merge=1)

cmd.color ("red", "resi 570 & chain A")

cmd.select ("Inward", "resi 570 & chain A", merge=1)

cmd.color ("blue", "resi 571 & chain A")

cmd.select ("Outward", "resi 571 & chain A", merge=1)

cmd.color ("red", "resi 572 & chain A")

cmd.select ("Inward", "resi 572 & chain A", merge=1)

cmd.color ("blue", "resi 573 & chain A")

cmd.select ("Outward", "resi 573 & chain A", merge=1)

cmd.color ("red", "resi 574 & chain A")

cmd.select ("Inward", "resi 574 & chain A", merge=1)

cmd.color ("blue", "resi 575 & chain A")

cmd.select ("Outward", "resi 575 & chain A", merge=1)

cmd.color ("red", "resi 576 & chain A")

cmd.select ("Inward", "resi 576 & chain A", merge=1)

cmd.color ("red", "resi 592 & chain A")

cmd.select ("Inward", "resi 592 & chain A", merge=1)

cmd.color ("blue", "resi 593 & chain A")

cmd.select ("Outward", "resi 593 & chain A", merge=1)

cmd.color ("red", "resi 594 & chain A")

cmd.select ("Inward", "resi 594 & chain A", merge=1)

cmd.color ("blue", "resi 595 & chain A")

cmd.select ("Outward", "resi 595 & chain A", merge=1)

cmd.color ("red", "resi 596 & chain A")

cmd.select ("Inward", "resi 596 & chain A", merge=1)

cmd.color ("blue", "resi 597 & chain A")

cmd.select ("Outward", "resi 597 & chain A", merge=1)

cmd.color ("red", "resi 598 & chain A")

cmd.select ("Inward", "resi 598 & chain A", merge=1)

cmd.color ("blue", "resi 599 & chain A")

cmd.select ("Outward", "resi 599 & chain A", merge=1)

cmd.color ("red", "resi 600 & chain A")

cmd.select ("Inward", "resi 600 & chain A", merge=1)

cmd.color ("blue", "resi 601 & chain A")

cmd.select ("Outward", "resi 601 & chain A", merge=1)

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

cmd.color ("blue", "resi 613 & chain A")

cmd.select ("Outward", "resi 613 & chain A", merge=1)

cmd.color ("red", "resi 614 & chain A")

cmd.select ("Inward", "resi 614 & chain A", merge=1)

cmd.color ("red", "resi 641 & chain A")

cmd.select ("Inward", "resi 641 & chain A", merge=1)

cmd.color ("blue", "resi 642 & chain A")

cmd.select ("Outward", "resi 642 & chain A", merge=1)

cmd.color ("red", "resi 643 & chain A")

cmd.select ("Inward", "resi 643 & chain A", merge=1)

cmd.color ("blue", "resi 644 & chain A")

cmd.select ("Outward", "resi 644 & chain A", merge=1)

cmd.color ("red", "resi 645 & chain A")

cmd.select ("Inward", "resi 645 & chain A", merge=1)

cmd.color ("blue", "resi 646 & chain A")

cmd.select ("Outward", "resi 646 & chain A", merge=1)

cmd.color ("red", "resi 647 & chain A")

cmd.select ("Inward", "resi 647 & chain A", merge=1)

cmd.color ("blue", "resi 648 & chain A")

cmd.select ("Outward", "resi 648 & chain A", merge=1)

cmd.load_cgo( [9.0, 68.01028,71.484276,142.21346, 68.01028, 71.484276, 142.21346, 1, 1,1,0,0,0,1], "axis" )
