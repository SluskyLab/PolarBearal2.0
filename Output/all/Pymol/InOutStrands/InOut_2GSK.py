from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GSK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand8", "resi 137+138+139+140+141+142+143+144+145 & chain A ")


cmd.select("Astrand9", "resi 149+150+151+152+153+154+155+156+157+158+159+160+161 & chain A ")


cmd.select("Astrand10", "resi 164+165+166+167+168+169+170+171+172+173+174+175+176+177+178 & chain A ")


cmd.select("Astrand11", "resi 195+196+197+198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")


cmd.select("Astrand12", "resi 214+215+216+217+218+219+220+221+222+223+224+225+226+227+228 & chain A ")


cmd.select("Astrand13", "resi 242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257 & chain A ")


cmd.select("Astrand14", "resi 261+262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277 & chain A ")


cmd.select("Astrand15", "resi 289+290+291+292+293+294+295+296+297+298+299+300+301+302+303+304+305 & chain A ")


cmd.select("Astrand16", "resi 309+310+311+312+313+314+315+316+317+318+319+320+321+322 & chain A ")


cmd.select("Astrand17", "resi 333+334+335+336+337+338+339+340+341+342+343+344+345+346+347+348 & chain A ")


cmd.select("Astrand18", "resi 351+352+353+354+355+356+357+358+359+360+361+362 & chain A ")


cmd.select("Astrand19", "resi 366+367+368+369+370+371+372+373+374+375+376+377+378+379+380 & chain A ")


cmd.select("Astrand20", "resi 383+384+385+386+387+388+389+390+391+392+393+394 & chain A ")


cmd.select("Astrand21", "resi 413+414+415+416+417+418+419+420+421+422+423+424+425+426 & chain A ")


cmd.select("Astrand22", "resi 429+430+431+432+433+434+435+436+437+438+439+440+441 & chain A ")


cmd.select("Astrand25", "resi 459+460+461+462+463+464+465+466+467+468+469+470+471+472 & chain A ")


cmd.select("Astrand26", "resi 475+476+477+478+479+480+481+482+483+484+485+486+487+488 & chain A ")


cmd.select("Astrand28", "resi 501+502+503+504+505+506+507+508+509+510+511 & chain A ")


cmd.select("Astrand29", "resi 514+515+516+517+518+519+520+521+522+523 & chain A ")


cmd.select("Astrand32", "resi 544+545+546+547+548+549+550+551+552+553+554 & chain A ")


cmd.select("Astrand33", "resi 559+560+561+562+563+564+565+566 & chain A ")


cmd.select("Astrand34", "resi 585+586+587+588+589+590+591+592+593 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

cmd.color ("blue", "resi 138 & chain A")

cmd.select ("Outward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("blue", "resi 140 & chain A")

cmd.select ("Outward", "resi 140 & chain A", merge=1)

cmd.color ("blue", "resi 141 & chain A")

cmd.select ("Outward", "resi 141 & chain A", merge=1)

cmd.color ("blue", "resi 142 & chain A")

cmd.select ("Outward", "resi 142 & chain A", merge=1)

cmd.color ("blue", "resi 143 & chain A")

cmd.select ("Outward", "resi 143 & chain A", merge=1)

cmd.color ("blue", "resi 144 & chain A")

cmd.select ("Outward", "resi 144 & chain A", merge=1)

cmd.color ("blue", "resi 145 & chain A")

cmd.select ("Outward", "resi 145 & chain A", merge=1)

cmd.color ("blue", "resi 149 & chain A")

cmd.select ("Outward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("blue", "resi 151 & chain A")

cmd.select ("Outward", "resi 151 & chain A", merge=1)

cmd.color ("blue", "resi 152 & chain A")

cmd.select ("Outward", "resi 152 & chain A", merge=1)

cmd.color ("blue", "resi 153 & chain A")

cmd.select ("Outward", "resi 153 & chain A", merge=1)

cmd.color ("blue", "resi 154 & chain A")

cmd.select ("Outward", "resi 154 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 156 & chain A")

cmd.select ("Outward", "resi 156 & chain A", merge=1)

cmd.color ("blue", "resi 157 & chain A")

cmd.select ("Outward", "resi 157 & chain A", merge=1)

cmd.color ("blue", "resi 158 & chain A")

cmd.select ("Outward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("blue", "resi 160 & chain A")

cmd.select ("Outward", "resi 160 & chain A", merge=1)

cmd.color ("blue", "resi 161 & chain A")

cmd.select ("Outward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

cmd.color ("blue", "resi 165 & chain A")

cmd.select ("Outward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 166 & chain A")

cmd.select ("Outward", "resi 166 & chain A", merge=1)

cmd.color ("blue", "resi 167 & chain A")

cmd.select ("Outward", "resi 167 & chain A", merge=1)

cmd.color ("blue", "resi 168 & chain A")

cmd.select ("Outward", "resi 168 & chain A", merge=1)

cmd.color ("blue", "resi 169 & chain A")

cmd.select ("Outward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 170 & chain A")

cmd.select ("Outward", "resi 170 & chain A", merge=1)

cmd.color ("blue", "resi 171 & chain A")

cmd.select ("Outward", "resi 171 & chain A", merge=1)

cmd.color ("blue", "resi 172 & chain A")

cmd.select ("Outward", "resi 172 & chain A", merge=1)

cmd.color ("blue", "resi 173 & chain A")

cmd.select ("Outward", "resi 173 & chain A", merge=1)

cmd.color ("blue", "resi 174 & chain A")

cmd.select ("Outward", "resi 174 & chain A", merge=1)

cmd.color ("blue", "resi 175 & chain A")

cmd.select ("Outward", "resi 175 & chain A", merge=1)

cmd.color ("blue", "resi 176 & chain A")

cmd.select ("Outward", "resi 176 & chain A", merge=1)

cmd.color ("blue", "resi 177 & chain A")

cmd.select ("Outward", "resi 177 & chain A", merge=1)

cmd.color ("blue", "resi 178 & chain A")

cmd.select ("Outward", "resi 178 & chain A", merge=1)

cmd.color ("blue", "resi 195 & chain A")

cmd.select ("Outward", "resi 195 & chain A", merge=1)

cmd.color ("blue", "resi 196 & chain A")

cmd.select ("Outward", "resi 196 & chain A", merge=1)

cmd.color ("blue", "resi 197 & chain A")

cmd.select ("Outward", "resi 197 & chain A", merge=1)

cmd.color ("blue", "resi 198 & chain A")

cmd.select ("Outward", "resi 198 & chain A", merge=1)

cmd.color ("blue", "resi 199 & chain A")

cmd.select ("Outward", "resi 199 & chain A", merge=1)

cmd.color ("blue", "resi 200 & chain A")

cmd.select ("Outward", "resi 200 & chain A", merge=1)

cmd.color ("blue", "resi 201 & chain A")

cmd.select ("Outward", "resi 201 & chain A", merge=1)

cmd.color ("blue", "resi 202 & chain A")

cmd.select ("Outward", "resi 202 & chain A", merge=1)

cmd.color ("blue", "resi 203 & chain A")

cmd.select ("Outward", "resi 203 & chain A", merge=1)

cmd.color ("blue", "resi 204 & chain A")

cmd.select ("Outward", "resi 204 & chain A", merge=1)

cmd.color ("blue", "resi 205 & chain A")

cmd.select ("Outward", "resi 205 & chain A", merge=1)

cmd.color ("blue", "resi 206 & chain A")

cmd.select ("Outward", "resi 206 & chain A", merge=1)

cmd.color ("blue", "resi 207 & chain A")

cmd.select ("Outward", "resi 207 & chain A", merge=1)

cmd.color ("blue", "resi 208 & chain A")

cmd.select ("Outward", "resi 208 & chain A", merge=1)

cmd.color ("blue", "resi 209 & chain A")

cmd.select ("Outward", "resi 209 & chain A", merge=1)

cmd.color ("blue", "resi 214 & chain A")

cmd.select ("Outward", "resi 214 & chain A", merge=1)

cmd.color ("blue", "resi 215 & chain A")

cmd.select ("Outward", "resi 215 & chain A", merge=1)

cmd.color ("blue", "resi 216 & chain A")

cmd.select ("Outward", "resi 216 & chain A", merge=1)

cmd.color ("blue", "resi 217 & chain A")

cmd.select ("Outward", "resi 217 & chain A", merge=1)

cmd.color ("blue", "resi 218 & chain A")

cmd.select ("Outward", "resi 218 & chain A", merge=1)

cmd.color ("blue", "resi 219 & chain A")

cmd.select ("Outward", "resi 219 & chain A", merge=1)

cmd.color ("blue", "resi 220 & chain A")

cmd.select ("Outward", "resi 220 & chain A", merge=1)

cmd.color ("blue", "resi 221 & chain A")

cmd.select ("Outward", "resi 221 & chain A", merge=1)

cmd.color ("blue", "resi 222 & chain A")

cmd.select ("Outward", "resi 222 & chain A", merge=1)

cmd.color ("blue", "resi 223 & chain A")

cmd.select ("Outward", "resi 223 & chain A", merge=1)

cmd.color ("blue", "resi 224 & chain A")

cmd.select ("Outward", "resi 224 & chain A", merge=1)

cmd.color ("blue", "resi 225 & chain A")

cmd.select ("Outward", "resi 225 & chain A", merge=1)

cmd.color ("blue", "resi 226 & chain A")

cmd.select ("Outward", "resi 226 & chain A", merge=1)

cmd.color ("blue", "resi 227 & chain A")

cmd.select ("Outward", "resi 227 & chain A", merge=1)

cmd.color ("blue", "resi 228 & chain A")

cmd.select ("Outward", "resi 228 & chain A", merge=1)

cmd.color ("blue", "resi 242 & chain A")

cmd.select ("Outward", "resi 242 & chain A", merge=1)

cmd.color ("blue", "resi 243 & chain A")

cmd.select ("Outward", "resi 243 & chain A", merge=1)

cmd.color ("blue", "resi 244 & chain A")

cmd.select ("Outward", "resi 244 & chain A", merge=1)

cmd.color ("blue", "resi 245 & chain A")

cmd.select ("Outward", "resi 245 & chain A", merge=1)

cmd.color ("blue", "resi 246 & chain A")

cmd.select ("Outward", "resi 246 & chain A", merge=1)

cmd.color ("blue", "resi 247 & chain A")

cmd.select ("Outward", "resi 247 & chain A", merge=1)

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

cmd.color ("blue", "resi 249 & chain A")

cmd.select ("Outward", "resi 249 & chain A", merge=1)

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

cmd.color ("blue", "resi 251 & chain A")

cmd.select ("Outward", "resi 251 & chain A", merge=1)

cmd.color ("blue", "resi 252 & chain A")

cmd.select ("Outward", "resi 252 & chain A", merge=1)

cmd.color ("blue", "resi 253 & chain A")

cmd.select ("Outward", "resi 253 & chain A", merge=1)

cmd.color ("blue", "resi 254 & chain A")

cmd.select ("Outward", "resi 254 & chain A", merge=1)

cmd.color ("blue", "resi 255 & chain A")

cmd.select ("Outward", "resi 255 & chain A", merge=1)

cmd.color ("blue", "resi 256 & chain A")

cmd.select ("Outward", "resi 256 & chain A", merge=1)

cmd.color ("blue", "resi 257 & chain A")

cmd.select ("Outward", "resi 257 & chain A", merge=1)

cmd.color ("blue", "resi 261 & chain A")

cmd.select ("Outward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 262 & chain A")

cmd.select ("Outward", "resi 262 & chain A", merge=1)

cmd.color ("blue", "resi 263 & chain A")

cmd.select ("Outward", "resi 263 & chain A", merge=1)

cmd.color ("blue", "resi 264 & chain A")

cmd.select ("Outward", "resi 264 & chain A", merge=1)

cmd.color ("blue", "resi 265 & chain A")

cmd.select ("Outward", "resi 265 & chain A", merge=1)

cmd.color ("blue", "resi 266 & chain A")

cmd.select ("Outward", "resi 266 & chain A", merge=1)

cmd.color ("blue", "resi 267 & chain A")

cmd.select ("Outward", "resi 267 & chain A", merge=1)

cmd.color ("blue", "resi 268 & chain A")

cmd.select ("Outward", "resi 268 & chain A", merge=1)

cmd.color ("blue", "resi 269 & chain A")

cmd.select ("Outward", "resi 269 & chain A", merge=1)

cmd.color ("blue", "resi 270 & chain A")

cmd.select ("Outward", "resi 270 & chain A", merge=1)

cmd.color ("blue", "resi 271 & chain A")

cmd.select ("Outward", "resi 271 & chain A", merge=1)

cmd.color ("blue", "resi 272 & chain A")

cmd.select ("Outward", "resi 272 & chain A", merge=1)

cmd.color ("blue", "resi 273 & chain A")

cmd.select ("Outward", "resi 273 & chain A", merge=1)

cmd.color ("blue", "resi 274 & chain A")

cmd.select ("Outward", "resi 274 & chain A", merge=1)

cmd.color ("blue", "resi 275 & chain A")

cmd.select ("Outward", "resi 275 & chain A", merge=1)

cmd.color ("blue", "resi 276 & chain A")

cmd.select ("Outward", "resi 276 & chain A", merge=1)

cmd.color ("blue", "resi 277 & chain A")

cmd.select ("Outward", "resi 277 & chain A", merge=1)

cmd.color ("blue", "resi 289 & chain A")

cmd.select ("Outward", "resi 289 & chain A", merge=1)

cmd.color ("blue", "resi 290 & chain A")

cmd.select ("Outward", "resi 290 & chain A", merge=1)

cmd.color ("blue", "resi 291 & chain A")

cmd.select ("Outward", "resi 291 & chain A", merge=1)

cmd.color ("blue", "resi 292 & chain A")

cmd.select ("Outward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("blue", "resi 296 & chain A")

cmd.select ("Outward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("blue", "resi 298 & chain A")

cmd.select ("Outward", "resi 298 & chain A", merge=1)

cmd.color ("blue", "resi 299 & chain A")

cmd.select ("Outward", "resi 299 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.color ("blue", "resi 301 & chain A")

cmd.select ("Outward", "resi 301 & chain A", merge=1)

cmd.color ("blue", "resi 302 & chain A")

cmd.select ("Outward", "resi 302 & chain A", merge=1)

cmd.color ("blue", "resi 303 & chain A")

cmd.select ("Outward", "resi 303 & chain A", merge=1)

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

cmd.color ("blue", "resi 305 & chain A")

cmd.select ("Outward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 309 & chain A")

cmd.select ("Outward", "resi 309 & chain A", merge=1)

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

cmd.color ("blue", "resi 311 & chain A")

cmd.select ("Outward", "resi 311 & chain A", merge=1)

cmd.color ("blue", "resi 312 & chain A")

cmd.select ("Outward", "resi 312 & chain A", merge=1)

cmd.color ("blue", "resi 313 & chain A")

cmd.select ("Outward", "resi 313 & chain A", merge=1)

cmd.color ("blue", "resi 314 & chain A")

cmd.select ("Outward", "resi 314 & chain A", merge=1)

cmd.color ("blue", "resi 315 & chain A")

cmd.select ("Outward", "resi 315 & chain A", merge=1)

cmd.color ("blue", "resi 316 & chain A")

cmd.select ("Outward", "resi 316 & chain A", merge=1)

cmd.color ("blue", "resi 317 & chain A")

cmd.select ("Outward", "resi 317 & chain A", merge=1)

cmd.color ("blue", "resi 318 & chain A")

cmd.select ("Outward", "resi 318 & chain A", merge=1)

cmd.color ("blue", "resi 319 & chain A")

cmd.select ("Outward", "resi 319 & chain A", merge=1)

cmd.color ("blue", "resi 320 & chain A")

cmd.select ("Outward", "resi 320 & chain A", merge=1)

cmd.color ("blue", "resi 321 & chain A")

cmd.select ("Outward", "resi 321 & chain A", merge=1)

cmd.color ("blue", "resi 322 & chain A")

cmd.select ("Outward", "resi 322 & chain A", merge=1)

cmd.color ("blue", "resi 333 & chain A")

cmd.select ("Outward", "resi 333 & chain A", merge=1)

cmd.color ("blue", "resi 334 & chain A")

cmd.select ("Outward", "resi 334 & chain A", merge=1)

cmd.color ("blue", "resi 335 & chain A")

cmd.select ("Outward", "resi 335 & chain A", merge=1)

cmd.color ("blue", "resi 336 & chain A")

cmd.select ("Outward", "resi 336 & chain A", merge=1)

cmd.color ("blue", "resi 337 & chain A")

cmd.select ("Outward", "resi 337 & chain A", merge=1)

cmd.color ("blue", "resi 338 & chain A")

cmd.select ("Outward", "resi 338 & chain A", merge=1)

cmd.color ("blue", "resi 339 & chain A")

cmd.select ("Outward", "resi 339 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("blue", "resi 343 & chain A")

cmd.select ("Outward", "resi 343 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("blue", "resi 345 & chain A")

cmd.select ("Outward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("blue", "resi 347 & chain A")

cmd.select ("Outward", "resi 347 & chain A", merge=1)

cmd.color ("blue", "resi 348 & chain A")

cmd.select ("Outward", "resi 348 & chain A", merge=1)

cmd.color ("blue", "resi 351 & chain A")

cmd.select ("Outward", "resi 351 & chain A", merge=1)

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("blue", "resi 354 & chain A")

cmd.select ("Outward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 356 & chain A")

cmd.select ("Outward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("blue", "resi 358 & chain A")

cmd.select ("Outward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("blue", "resi 360 & chain A")

cmd.select ("Outward", "resi 360 & chain A", merge=1)

cmd.color ("blue", "resi 361 & chain A")

cmd.select ("Outward", "resi 361 & chain A", merge=1)

cmd.color ("blue", "resi 362 & chain A")

cmd.select ("Outward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("blue", "resi 367 & chain A")

cmd.select ("Outward", "resi 367 & chain A", merge=1)

cmd.color ("blue", "resi 368 & chain A")

cmd.select ("Outward", "resi 368 & chain A", merge=1)

cmd.color ("blue", "resi 369 & chain A")

cmd.select ("Outward", "resi 369 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("blue", "resi 371 & chain A")

cmd.select ("Outward", "resi 371 & chain A", merge=1)

cmd.color ("blue", "resi 372 & chain A")

cmd.select ("Outward", "resi 372 & chain A", merge=1)

cmd.color ("blue", "resi 373 & chain A")

cmd.select ("Outward", "resi 373 & chain A", merge=1)

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("blue", "resi 375 & chain A")

cmd.select ("Outward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 377 & chain A")

cmd.select ("Outward", "resi 377 & chain A", merge=1)

cmd.color ("blue", "resi 378 & chain A")

cmd.select ("Outward", "resi 378 & chain A", merge=1)

cmd.color ("blue", "resi 379 & chain A")

cmd.select ("Outward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("blue", "resi 383 & chain A")

cmd.select ("Outward", "resi 383 & chain A", merge=1)

cmd.color ("blue", "resi 384 & chain A")

cmd.select ("Outward", "resi 384 & chain A", merge=1)

cmd.color ("blue", "resi 385 & chain A")

cmd.select ("Outward", "resi 385 & chain A", merge=1)

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("blue", "resi 387 & chain A")

cmd.select ("Outward", "resi 387 & chain A", merge=1)

cmd.color ("blue", "resi 388 & chain A")

cmd.select ("Outward", "resi 388 & chain A", merge=1)

cmd.color ("blue", "resi 389 & chain A")

cmd.select ("Outward", "resi 389 & chain A", merge=1)

cmd.color ("blue", "resi 390 & chain A")

cmd.select ("Outward", "resi 390 & chain A", merge=1)

cmd.color ("blue", "resi 391 & chain A")

cmd.select ("Outward", "resi 391 & chain A", merge=1)

cmd.color ("blue", "resi 392 & chain A")

cmd.select ("Outward", "resi 392 & chain A", merge=1)

cmd.color ("blue", "resi 393 & chain A")

cmd.select ("Outward", "resi 393 & chain A", merge=1)

cmd.color ("blue", "resi 394 & chain A")

cmd.select ("Outward", "resi 394 & chain A", merge=1)

cmd.color ("blue", "resi 413 & chain A")

cmd.select ("Outward", "resi 413 & chain A", merge=1)

cmd.color ("blue", "resi 414 & chain A")

cmd.select ("Outward", "resi 414 & chain A", merge=1)

cmd.color ("blue", "resi 415 & chain A")

cmd.select ("Outward", "resi 415 & chain A", merge=1)

cmd.color ("blue", "resi 416 & chain A")

cmd.select ("Outward", "resi 416 & chain A", merge=1)

cmd.color ("blue", "resi 417 & chain A")

cmd.select ("Outward", "resi 417 & chain A", merge=1)

cmd.color ("blue", "resi 418 & chain A")

cmd.select ("Outward", "resi 418 & chain A", merge=1)

cmd.color ("blue", "resi 419 & chain A")

cmd.select ("Outward", "resi 419 & chain A", merge=1)

cmd.color ("blue", "resi 420 & chain A")

cmd.select ("Outward", "resi 420 & chain A", merge=1)

cmd.color ("blue", "resi 421 & chain A")

cmd.select ("Outward", "resi 421 & chain A", merge=1)

cmd.color ("blue", "resi 422 & chain A")

cmd.select ("Outward", "resi 422 & chain A", merge=1)

cmd.color ("blue", "resi 423 & chain A")

cmd.select ("Outward", "resi 423 & chain A", merge=1)

cmd.color ("blue", "resi 424 & chain A")

cmd.select ("Outward", "resi 424 & chain A", merge=1)

cmd.color ("blue", "resi 425 & chain A")

cmd.select ("Outward", "resi 425 & chain A", merge=1)

cmd.color ("blue", "resi 426 & chain A")

cmd.select ("Outward", "resi 426 & chain A", merge=1)

cmd.color ("blue", "resi 429 & chain A")

cmd.select ("Outward", "resi 429 & chain A", merge=1)

cmd.color ("blue", "resi 430 & chain A")

cmd.select ("Outward", "resi 430 & chain A", merge=1)

cmd.color ("blue", "resi 431 & chain A")

cmd.select ("Outward", "resi 431 & chain A", merge=1)

cmd.color ("blue", "resi 432 & chain A")

cmd.select ("Outward", "resi 432 & chain A", merge=1)

cmd.color ("blue", "resi 433 & chain A")

cmd.select ("Outward", "resi 433 & chain A", merge=1)

cmd.color ("blue", "resi 434 & chain A")

cmd.select ("Outward", "resi 434 & chain A", merge=1)

cmd.color ("blue", "resi 435 & chain A")

cmd.select ("Outward", "resi 435 & chain A", merge=1)

cmd.color ("blue", "resi 436 & chain A")

cmd.select ("Outward", "resi 436 & chain A", merge=1)

cmd.color ("blue", "resi 437 & chain A")

cmd.select ("Outward", "resi 437 & chain A", merge=1)

cmd.color ("blue", "resi 438 & chain A")

cmd.select ("Outward", "resi 438 & chain A", merge=1)

cmd.color ("blue", "resi 439 & chain A")

cmd.select ("Outward", "resi 439 & chain A", merge=1)

cmd.color ("blue", "resi 440 & chain A")

cmd.select ("Outward", "resi 440 & chain A", merge=1)

cmd.color ("blue", "resi 441 & chain A")

cmd.select ("Outward", "resi 441 & chain A", merge=1)

cmd.color ("blue", "resi 459 & chain A")

cmd.select ("Outward", "resi 459 & chain A", merge=1)

cmd.color ("blue", "resi 460 & chain A")

cmd.select ("Outward", "resi 460 & chain A", merge=1)

cmd.color ("blue", "resi 461 & chain A")

cmd.select ("Outward", "resi 461 & chain A", merge=1)

cmd.color ("blue", "resi 462 & chain A")

cmd.select ("Outward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("blue", "resi 464 & chain A")

cmd.select ("Outward", "resi 464 & chain A", merge=1)

cmd.color ("blue", "resi 465 & chain A")

cmd.select ("Outward", "resi 465 & chain A", merge=1)

cmd.color ("blue", "resi 466 & chain A")

cmd.select ("Outward", "resi 466 & chain A", merge=1)

cmd.color ("blue", "resi 467 & chain A")

cmd.select ("Outward", "resi 467 & chain A", merge=1)

cmd.color ("blue", "resi 468 & chain A")

cmd.select ("Outward", "resi 468 & chain A", merge=1)

cmd.color ("blue", "resi 469 & chain A")

cmd.select ("Outward", "resi 469 & chain A", merge=1)

cmd.color ("blue", "resi 470 & chain A")

cmd.select ("Outward", "resi 470 & chain A", merge=1)

cmd.color ("blue", "resi 471 & chain A")

cmd.select ("Outward", "resi 471 & chain A", merge=1)

cmd.color ("blue", "resi 472 & chain A")

cmd.select ("Outward", "resi 472 & chain A", merge=1)

cmd.color ("blue", "resi 475 & chain A")

cmd.select ("Outward", "resi 475 & chain A", merge=1)

cmd.color ("blue", "resi 476 & chain A")

cmd.select ("Outward", "resi 476 & chain A", merge=1)

cmd.color ("blue", "resi 477 & chain A")

cmd.select ("Outward", "resi 477 & chain A", merge=1)

cmd.color ("blue", "resi 478 & chain A")

cmd.select ("Outward", "resi 478 & chain A", merge=1)

cmd.color ("blue", "resi 479 & chain A")

cmd.select ("Outward", "resi 479 & chain A", merge=1)

cmd.color ("blue", "resi 480 & chain A")

cmd.select ("Outward", "resi 480 & chain A", merge=1)

cmd.color ("blue", "resi 481 & chain A")

cmd.select ("Outward", "resi 481 & chain A", merge=1)

cmd.color ("blue", "resi 482 & chain A")

cmd.select ("Outward", "resi 482 & chain A", merge=1)

cmd.color ("blue", "resi 483 & chain A")

cmd.select ("Outward", "resi 483 & chain A", merge=1)

cmd.color ("blue", "resi 484 & chain A")

cmd.select ("Outward", "resi 484 & chain A", merge=1)

cmd.color ("blue", "resi 485 & chain A")

cmd.select ("Outward", "resi 485 & chain A", merge=1)

cmd.color ("blue", "resi 486 & chain A")

cmd.select ("Outward", "resi 486 & chain A", merge=1)

cmd.color ("blue", "resi 487 & chain A")

cmd.select ("Outward", "resi 487 & chain A", merge=1)

cmd.color ("blue", "resi 488 & chain A")

cmd.select ("Outward", "resi 488 & chain A", merge=1)

cmd.color ("blue", "resi 501 & chain A")

cmd.select ("Outward", "resi 501 & chain A", merge=1)

cmd.color ("blue", "resi 502 & chain A")

cmd.select ("Outward", "resi 502 & chain A", merge=1)

cmd.color ("blue", "resi 503 & chain A")

cmd.select ("Outward", "resi 503 & chain A", merge=1)

cmd.color ("blue", "resi 504 & chain A")

cmd.select ("Outward", "resi 504 & chain A", merge=1)

cmd.color ("blue", "resi 505 & chain A")

cmd.select ("Outward", "resi 505 & chain A", merge=1)

cmd.color ("blue", "resi 506 & chain A")

cmd.select ("Outward", "resi 506 & chain A", merge=1)

cmd.color ("blue", "resi 507 & chain A")

cmd.select ("Outward", "resi 507 & chain A", merge=1)

cmd.color ("blue", "resi 508 & chain A")

cmd.select ("Outward", "resi 508 & chain A", merge=1)

cmd.color ("blue", "resi 509 & chain A")

cmd.select ("Outward", "resi 509 & chain A", merge=1)

cmd.color ("blue", "resi 510 & chain A")

cmd.select ("Outward", "resi 510 & chain A", merge=1)

cmd.color ("blue", "resi 511 & chain A")

cmd.select ("Outward", "resi 511 & chain A", merge=1)

cmd.color ("blue", "resi 514 & chain A")

cmd.select ("Outward", "resi 514 & chain A", merge=1)

cmd.color ("blue", "resi 515 & chain A")

cmd.select ("Outward", "resi 515 & chain A", merge=1)

cmd.color ("blue", "resi 516 & chain A")

cmd.select ("Outward", "resi 516 & chain A", merge=1)

cmd.color ("blue", "resi 517 & chain A")

cmd.select ("Outward", "resi 517 & chain A", merge=1)

cmd.color ("blue", "resi 518 & chain A")

cmd.select ("Outward", "resi 518 & chain A", merge=1)

cmd.color ("blue", "resi 519 & chain A")

cmd.select ("Outward", "resi 519 & chain A", merge=1)

cmd.color ("blue", "resi 520 & chain A")

cmd.select ("Outward", "resi 520 & chain A", merge=1)

cmd.color ("blue", "resi 521 & chain A")

cmd.select ("Outward", "resi 521 & chain A", merge=1)

cmd.color ("blue", "resi 522 & chain A")

cmd.select ("Outward", "resi 522 & chain A", merge=1)

cmd.color ("blue", "resi 523 & chain A")

cmd.select ("Outward", "resi 523 & chain A", merge=1)

cmd.color ("blue", "resi 544 & chain A")

cmd.select ("Outward", "resi 544 & chain A", merge=1)

cmd.color ("blue", "resi 545 & chain A")

cmd.select ("Outward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 546 & chain A")

cmd.select ("Outward", "resi 546 & chain A", merge=1)

cmd.color ("blue", "resi 547 & chain A")

cmd.select ("Outward", "resi 547 & chain A", merge=1)

cmd.color ("blue", "resi 548 & chain A")

cmd.select ("Outward", "resi 548 & chain A", merge=1)

cmd.color ("blue", "resi 549 & chain A")

cmd.select ("Outward", "resi 549 & chain A", merge=1)

cmd.color ("blue", "resi 550 & chain A")

cmd.select ("Outward", "resi 550 & chain A", merge=1)

cmd.color ("blue", "resi 551 & chain A")

cmd.select ("Outward", "resi 551 & chain A", merge=1)

cmd.color ("blue", "resi 552 & chain A")

cmd.select ("Outward", "resi 552 & chain A", merge=1)

cmd.color ("blue", "resi 553 & chain A")

cmd.select ("Outward", "resi 553 & chain A", merge=1)

cmd.color ("blue", "resi 554 & chain A")

cmd.select ("Outward", "resi 554 & chain A", merge=1)

cmd.color ("blue", "resi 559 & chain A")

cmd.select ("Outward", "resi 559 & chain A", merge=1)

cmd.color ("blue", "resi 560 & chain A")

cmd.select ("Outward", "resi 560 & chain A", merge=1)

cmd.color ("blue", "resi 561 & chain A")

cmd.select ("Outward", "resi 561 & chain A", merge=1)

cmd.color ("blue", "resi 562 & chain A")

cmd.select ("Outward", "resi 562 & chain A", merge=1)

cmd.color ("blue", "resi 563 & chain A")

cmd.select ("Outward", "resi 563 & chain A", merge=1)

cmd.color ("blue", "resi 564 & chain A")

cmd.select ("Outward", "resi 564 & chain A", merge=1)

cmd.color ("blue", "resi 565 & chain A")

cmd.select ("Outward", "resi 565 & chain A", merge=1)

cmd.color ("blue", "resi 566 & chain A")

cmd.select ("Outward", "resi 566 & chain A", merge=1)

cmd.color ("blue", "resi 585 & chain A")

cmd.select ("Outward", "resi 585 & chain A", merge=1)

cmd.color ("blue", "resi 586 & chain A")

cmd.select ("Outward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

cmd.color ("blue", "resi 588 & chain A")

cmd.select ("Outward", "resi 588 & chain A", merge=1)

cmd.color ("blue", "resi 589 & chain A")

cmd.select ("Outward", "resi 589 & chain A", merge=1)

cmd.color ("blue", "resi 590 & chain A")

cmd.select ("Outward", "resi 590 & chain A", merge=1)

cmd.color ("blue", "resi 591 & chain A")

cmd.select ("Outward", "resi 591 & chain A", merge=1)

cmd.color ("blue", "resi 592 & chain A")

cmd.select ("Outward", "resi 592 & chain A", merge=1)

cmd.color ("blue", "resi 593 & chain A")

cmd.select ("Outward", "resi 593 & chain A", merge=1)

cmd.load_cgo( [9.0, 30.03827,1.7635902,8.870045, 35.514954, 2.4528627, -21.849134, 1, 1,1,0,0,0,1], "axis" )
