from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EFM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand8", "resi 162+163+164+165+166+167+168+169+170 & chain A ")


cmd.select("Astrand30", "resi 643+644+645+646+647+648+649+650+651 & chain A ")


cmd.select("Astrand10", "resi 191+192+193+194+195+196+197+198+199+200+201+202 & chain A ")


cmd.select("Astrand12", "resi 228+229+230+231+232+233+234+235+236+237+238+239+240+241 & chain A ")


cmd.select("Astrand13", "resi 261+262+263+264+265+266+267+268+269+270+271+272+273+274+275 & chain A ")


cmd.select("Astrand14", "resi 281+282+283+284+285+286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")


cmd.select("Astrand15", "resi 302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323 & chain A ")


cmd.select("Astrand16", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342+343+344+345+346+347 & chain A ")


cmd.select("Astrand17", "resi 410+411+412+413+369+368+370+371+414+372+373+415+510+374+416+375+511+417+460+512+376+418+513+419+461+377+462+420+421+378+463+517+379+422+518+464+423+380+519+465+381+520+424+559+466+560+522+425+521+382+561+562+467+523+383+524+426+468+563+564+384+427+526+525+469+470+527+385+565+428+471+386+472+566+429+528+387+473+529+567+568+530 & chain A ")


cmd.select("Astrand18", "resi 576+577+578+579+533+580+534+535+581+536+582+537+478+583+479+538+584+480+539+585+481+540+482+586+434+541+483+435+436+542+484+437+485+543+438+439+391+486+390+393+544+487+441+392+440+443+442+394+395+488+545+444+445+489+397+396+399+398+490+401+400+492+403+402+491+405+404+493+406+407+494+495 & chain A ")


cmd.select("Astrand11", "resi 211+212+213+214+215+216+217+218+219+220+221+222+223+224+225 & chain A ")


cmd.select("Astrand28", "resi 597+598+599+600+601+602+603+604+605+606+607+608+609 & chain A ")


cmd.select("Astrand29", "resi 612+613+614+615+616+617+618+619 & chain A ")


cmd.select("Astrand9", "resi 174+175+176+177+178+179+180+181+182+183+184 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 162 & chain A")

cmd.select ("Inward", "resi 162 & chain A", merge=1)

cmd.color ("blue", "resi 163 & chain A")

cmd.select ("Outward", "resi 163 & chain A", merge=1)

cmd.color ("red", "resi 164 & chain A")

cmd.select ("Inward", "resi 164 & chain A", merge=1)

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

cmd.color ("blue", "resi 649 & chain A")

cmd.select ("Outward", "resi 649 & chain A", merge=1)

cmd.color ("blue", "resi 650 & chain A")

cmd.select ("Outward", "resi 650 & chain A", merge=1)

cmd.color ("blue", "resi 651 & chain A")

cmd.select ("Outward", "resi 651 & chain A", merge=1)

cmd.color ("blue", "resi 191 & chain A")

cmd.select ("Outward", "resi 191 & chain A", merge=1)

cmd.color ("red", "resi 192 & chain A")

cmd.select ("Inward", "resi 192 & chain A", merge=1)

cmd.color ("blue", "resi 193 & chain A")

cmd.select ("Outward", "resi 193 & chain A", merge=1)

cmd.color ("red", "resi 194 & chain A")

cmd.select ("Inward", "resi 194 & chain A", merge=1)

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

cmd.color ("blue", "resi 236 & chain A")

cmd.select ("Outward", "resi 236 & chain A", merge=1)

cmd.color ("red", "resi 237 & chain A")

cmd.select ("Inward", "resi 237 & chain A", merge=1)

cmd.color ("blue", "resi 238 & chain A")

cmd.select ("Outward", "resi 238 & chain A", merge=1)

cmd.color ("red", "resi 239 & chain A")

cmd.select ("Inward", "resi 239 & chain A", merge=1)

cmd.color ("blue", "resi 240 & chain A")

cmd.select ("Outward", "resi 240 & chain A", merge=1)

cmd.color ("red", "resi 241 & chain A")

cmd.select ("Inward", "resi 241 & chain A", merge=1)

cmd.color ("red", "resi 261 & chain A")

cmd.select ("Inward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 262 & chain A")

cmd.select ("Outward", "resi 262 & chain A", merge=1)

cmd.color ("red", "resi 263 & chain A")

cmd.select ("Inward", "resi 263 & chain A", merge=1)

cmd.color ("blue", "resi 264 & chain A")

cmd.select ("Outward", "resi 264 & chain A", merge=1)

cmd.color ("red", "resi 265 & chain A")

cmd.select ("Inward", "resi 265 & chain A", merge=1)

cmd.color ("blue", "resi 266 & chain A")

cmd.select ("Outward", "resi 266 & chain A", merge=1)

cmd.color ("red", "resi 267 & chain A")

cmd.select ("Inward", "resi 267 & chain A", merge=1)

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

cmd.color ("blue", "resi 292 & chain A")

cmd.select ("Outward", "resi 292 & chain A", merge=1)

cmd.color ("red", "resi 293 & chain A")

cmd.select ("Inward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("red", "resi 295 & chain A")

cmd.select ("Inward", "resi 295 & chain A", merge=1)

cmd.color ("blue", "resi 296 & chain A")

cmd.select ("Outward", "resi 296 & chain A", merge=1)

cmd.color ("red", "resi 297 & chain A")

cmd.select ("Inward", "resi 297 & chain A", merge=1)

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

cmd.color ("blue", "resi 322 & chain A")

cmd.select ("Outward", "resi 322 & chain A", merge=1)

cmd.color ("red", "resi 323 & chain A")

cmd.select ("Inward", "resi 323 & chain A", merge=1)

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

cmd.color ("red", "resi 410 & chain A")

cmd.select ("Inward", "resi 410 & chain A", merge=1)

cmd.color ("blue", "resi 411 & chain A")

cmd.select ("Outward", "resi 411 & chain A", merge=1)

cmd.color ("red", "resi 412 & chain A")

cmd.select ("Inward", "resi 412 & chain A", merge=1)

cmd.color ("blue", "resi 413 & chain A")

cmd.select ("Outward", "resi 413 & chain A", merge=1)

cmd.color ("red", "resi 369 & chain A")

cmd.select ("Inward", "resi 369 & chain A", merge=1)

cmd.color ("blue", "resi 368 & chain A")

cmd.select ("Outward", "resi 368 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("red", "resi 371 & chain A")

cmd.select ("Inward", "resi 371 & chain A", merge=1)

cmd.color ("red", "resi 414 & chain A")

cmd.select ("Inward", "resi 414 & chain A", merge=1)

cmd.color ("blue", "resi 372 & chain A")

cmd.select ("Outward", "resi 372 & chain A", merge=1)

cmd.color ("red", "resi 373 & chain A")

cmd.select ("Inward", "resi 373 & chain A", merge=1)

cmd.color ("blue", "resi 415 & chain A")

cmd.select ("Outward", "resi 415 & chain A", merge=1)

cmd.color ("red", "resi 510 & chain A")

cmd.select ("Inward", "resi 510 & chain A", merge=1)

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("red", "resi 416 & chain A")

cmd.select ("Inward", "resi 416 & chain A", merge=1)

cmd.color ("red", "resi 375 & chain A")

cmd.select ("Inward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 511 & chain A")

cmd.select ("Outward", "resi 511 & chain A", merge=1)

cmd.color ("blue", "resi 417 & chain A")

cmd.select ("Outward", "resi 417 & chain A", merge=1)

cmd.color ("red", "resi 460 & chain A")

cmd.select ("Inward", "resi 460 & chain A", merge=1)

cmd.color ("blue", "resi 512 & chain A")

cmd.select ("Outward", "resi 512 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 418 & chain A")

cmd.select ("Outward", "resi 418 & chain A", merge=1)

cmd.color ("red", "resi 513 & chain A")

cmd.select ("Inward", "resi 513 & chain A", merge=1)

cmd.color ("red", "resi 419 & chain A")

cmd.select ("Inward", "resi 419 & chain A", merge=1)

cmd.color ("blue", "resi 461 & chain A")

cmd.select ("Outward", "resi 461 & chain A", merge=1)

cmd.color ("red", "resi 377 & chain A")

cmd.select ("Inward", "resi 377 & chain A", merge=1)

cmd.color ("red", "resi 462 & chain A")

cmd.select ("Inward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 420 & chain A")

cmd.select ("Outward", "resi 420 & chain A", merge=1)

cmd.color ("red", "resi 421 & chain A")

cmd.select ("Inward", "resi 421 & chain A", merge=1)

cmd.color ("blue", "resi 378 & chain A")

cmd.select ("Outward", "resi 378 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("blue", "resi 517 & chain A")

cmd.select ("Outward", "resi 517 & chain A", merge=1)

cmd.color ("red", "resi 379 & chain A")

cmd.select ("Inward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 422 & chain A")

cmd.select ("Outward", "resi 422 & chain A", merge=1)

cmd.color ("red", "resi 518 & chain A")

cmd.select ("Inward", "resi 518 & chain A", merge=1)

cmd.color ("red", "resi 464 & chain A")

cmd.select ("Inward", "resi 464 & chain A", merge=1)

cmd.color ("red", "resi 423 & chain A")

cmd.select ("Inward", "resi 423 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("blue", "resi 519 & chain A")

cmd.select ("Outward", "resi 519 & chain A", merge=1)

cmd.color ("blue", "resi 465 & chain A")

cmd.select ("Outward", "resi 465 & chain A", merge=1)

cmd.color ("red", "resi 381 & chain A")

cmd.select ("Inward", "resi 381 & chain A", merge=1)

cmd.color ("red", "resi 520 & chain A")

cmd.select ("Inward", "resi 520 & chain A", merge=1)

cmd.color ("blue", "resi 424 & chain A")

cmd.select ("Outward", "resi 424 & chain A", merge=1)

cmd.color ("blue", "resi 559 & chain A")

cmd.select ("Outward", "resi 559 & chain A", merge=1)

cmd.color ("red", "resi 466 & chain A")

cmd.select ("Inward", "resi 466 & chain A", merge=1)

cmd.color ("red", "resi 560 & chain A")

cmd.select ("Inward", "resi 560 & chain A", merge=1)

cmd.color ("red", "resi 522 & chain A")

cmd.select ("Inward", "resi 522 & chain A", merge=1)

cmd.color ("red", "resi 425 & chain A")

cmd.select ("Inward", "resi 425 & chain A", merge=1)

cmd.color ("blue", "resi 521 & chain A")

cmd.select ("Outward", "resi 521 & chain A", merge=1)

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("blue", "resi 561 & chain A")

cmd.select ("Outward", "resi 561 & chain A", merge=1)

cmd.color ("red", "resi 562 & chain A")

cmd.select ("Inward", "resi 562 & chain A", merge=1)

cmd.color ("blue", "resi 467 & chain A")

cmd.select ("Outward", "resi 467 & chain A", merge=1)

cmd.color ("blue", "resi 523 & chain A")

cmd.select ("Outward", "resi 523 & chain A", merge=1)

cmd.color ("red", "resi 383 & chain A")

cmd.select ("Inward", "resi 383 & chain A", merge=1)

cmd.color ("red", "resi 524 & chain A")

cmd.select ("Inward", "resi 524 & chain A", merge=1)

cmd.color ("blue", "resi 426 & chain A")

cmd.select ("Outward", "resi 426 & chain A", merge=1)

cmd.color ("red", "resi 468 & chain A")

cmd.select ("Inward", "resi 468 & chain A", merge=1)

cmd.color ("blue", "resi 563 & chain A")

cmd.select ("Outward", "resi 563 & chain A", merge=1)

cmd.color ("red", "resi 564 & chain A")

cmd.select ("Inward", "resi 564 & chain A", merge=1)

cmd.color ("blue", "resi 384 & chain A")

cmd.select ("Outward", "resi 384 & chain A", merge=1)

cmd.color ("red", "resi 427 & chain A")

cmd.select ("Inward", "resi 427 & chain A", merge=1)

cmd.color ("red", "resi 526 & chain A")

cmd.select ("Inward", "resi 526 & chain A", merge=1)

cmd.color ("blue", "resi 525 & chain A")

cmd.select ("Outward", "resi 525 & chain A", merge=1)

cmd.color ("blue", "resi 469 & chain A")

cmd.select ("Outward", "resi 469 & chain A", merge=1)

cmd.color ("red", "resi 470 & chain A")

cmd.select ("Inward", "resi 470 & chain A", merge=1)

cmd.color ("blue", "resi 527 & chain A")

cmd.select ("Outward", "resi 527 & chain A", merge=1)

cmd.color ("blue", "resi 385 & chain A")

cmd.select ("Outward", "resi 385 & chain A", merge=1)

cmd.color ("blue", "resi 565 & chain A")

cmd.select ("Outward", "resi 565 & chain A", merge=1)

cmd.color ("blue", "resi 428 & chain A")

cmd.select ("Outward", "resi 428 & chain A", merge=1)

cmd.color ("blue", "resi 471 & chain A")

cmd.select ("Outward", "resi 471 & chain A", merge=1)

cmd.color ("red", "resi 386 & chain A")

cmd.select ("Inward", "resi 386 & chain A", merge=1)

cmd.color ("red", "resi 472 & chain A")

cmd.select ("Inward", "resi 472 & chain A", merge=1)

cmd.color ("red", "resi 566 & chain A")

cmd.select ("Inward", "resi 566 & chain A", merge=1)

cmd.color ("blue", "resi 429 & chain A")

cmd.select ("Outward", "resi 429 & chain A", merge=1)

cmd.color ("blue", "resi 528 & chain A")

cmd.select ("Outward", "resi 528 & chain A", merge=1)

cmd.color ("blue", "resi 387 & chain A")

cmd.select ("Outward", "resi 387 & chain A", merge=1)

cmd.color ("red", "resi 473 & chain A")

cmd.select ("Inward", "resi 473 & chain A", merge=1)

cmd.color ("red", "resi 529 & chain A")

cmd.select ("Inward", "resi 529 & chain A", merge=1)

cmd.color ("blue", "resi 567 & chain A")

cmd.select ("Outward", "resi 567 & chain A", merge=1)

cmd.color ("blue", "resi 568 & chain A")

cmd.select ("Outward", "resi 568 & chain A", merge=1)

cmd.color ("blue", "resi 530 & chain A")

cmd.select ("Outward", "resi 530 & chain A", merge=1)

cmd.color ("blue", "resi 576 & chain A")

cmd.select ("Outward", "resi 576 & chain A", merge=1)

cmd.color ("red", "resi 577 & chain A")

cmd.select ("Inward", "resi 577 & chain A", merge=1)

cmd.color ("blue", "resi 578 & chain A")

cmd.select ("Outward", "resi 578 & chain A", merge=1)

cmd.color ("red", "resi 579 & chain A")

cmd.select ("Inward", "resi 579 & chain A", merge=1)

cmd.color ("blue", "resi 533 & chain A")

cmd.select ("Outward", "resi 533 & chain A", merge=1)

cmd.color ("blue", "resi 580 & chain A")

cmd.select ("Outward", "resi 580 & chain A", merge=1)

cmd.color ("red", "resi 534 & chain A")

cmd.select ("Inward", "resi 534 & chain A", merge=1)

cmd.color ("blue", "resi 535 & chain A")

cmd.select ("Outward", "resi 535 & chain A", merge=1)

cmd.color ("red", "resi 581 & chain A")

cmd.select ("Inward", "resi 581 & chain A", merge=1)

cmd.color ("red", "resi 536 & chain A")

cmd.select ("Inward", "resi 536 & chain A", merge=1)

cmd.color ("blue", "resi 582 & chain A")

cmd.select ("Outward", "resi 582 & chain A", merge=1)

cmd.color ("blue", "resi 537 & chain A")

cmd.select ("Outward", "resi 537 & chain A", merge=1)

cmd.color ("blue", "resi 478 & chain A")

cmd.select ("Outward", "resi 478 & chain A", merge=1)

cmd.color ("red", "resi 583 & chain A")

cmd.select ("Inward", "resi 583 & chain A", merge=1)

cmd.color ("red", "resi 479 & chain A")

cmd.select ("Inward", "resi 479 & chain A", merge=1)

cmd.color ("red", "resi 538 & chain A")

cmd.select ("Inward", "resi 538 & chain A", merge=1)

cmd.color ("blue", "resi 584 & chain A")

cmd.select ("Outward", "resi 584 & chain A", merge=1)

cmd.color ("blue", "resi 480 & chain A")

cmd.select ("Outward", "resi 480 & chain A", merge=1)

cmd.color ("blue", "resi 539 & chain A")

cmd.select ("Outward", "resi 539 & chain A", merge=1)

cmd.color ("red", "resi 585 & chain A")

cmd.select ("Inward", "resi 585 & chain A", merge=1)

cmd.color ("red", "resi 481 & chain A")

cmd.select ("Inward", "resi 481 & chain A", merge=1)

cmd.color ("red", "resi 540 & chain A")

cmd.select ("Inward", "resi 540 & chain A", merge=1)

cmd.color ("blue", "resi 482 & chain A")

cmd.select ("Outward", "resi 482 & chain A", merge=1)

cmd.color ("blue", "resi 586 & chain A")

cmd.select ("Outward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 434 & chain A")

cmd.select ("Outward", "resi 434 & chain A", merge=1)

cmd.color ("blue", "resi 541 & chain A")

cmd.select ("Outward", "resi 541 & chain A", merge=1)

cmd.color ("red", "resi 483 & chain A")

cmd.select ("Inward", "resi 483 & chain A", merge=1)

cmd.color ("red", "resi 435 & chain A")

cmd.select ("Inward", "resi 435 & chain A", merge=1)

cmd.color ("blue", "resi 436 & chain A")

cmd.select ("Outward", "resi 436 & chain A", merge=1)

cmd.color ("red", "resi 542 & chain A")

cmd.select ("Inward", "resi 542 & chain A", merge=1)

cmd.color ("blue", "resi 484 & chain A")

cmd.select ("Outward", "resi 484 & chain A", merge=1)

cmd.color ("red", "resi 437 & chain A")

cmd.select ("Inward", "resi 437 & chain A", merge=1)

cmd.color ("red", "resi 485 & chain A")

cmd.select ("Inward", "resi 485 & chain A", merge=1)

cmd.color ("blue", "resi 543 & chain A")

cmd.select ("Outward", "resi 543 & chain A", merge=1)

cmd.color ("blue", "resi 438 & chain A")

cmd.select ("Outward", "resi 438 & chain A", merge=1)

cmd.color ("red", "resi 439 & chain A")

cmd.select ("Inward", "resi 439 & chain A", merge=1)

cmd.color ("red", "resi 391 & chain A")

cmd.select ("Inward", "resi 391 & chain A", merge=1)

cmd.color ("blue", "resi 486 & chain A")

cmd.select ("Outward", "resi 486 & chain A", merge=1)

cmd.color ("blue", "resi 390 & chain A")

cmd.select ("Outward", "resi 390 & chain A", merge=1)

cmd.color ("red", "resi 393 & chain A")

cmd.select ("Inward", "resi 393 & chain A", merge=1)

cmd.color ("red", "resi 544 & chain A")

cmd.select ("Inward", "resi 544 & chain A", merge=1)

cmd.color ("red", "resi 487 & chain A")

cmd.select ("Inward", "resi 487 & chain A", merge=1)

cmd.color ("red", "resi 441 & chain A")

cmd.select ("Inward", "resi 441 & chain A", merge=1)

cmd.color ("blue", "resi 392 & chain A")

cmd.select ("Outward", "resi 392 & chain A", merge=1)

cmd.color ("blue", "resi 440 & chain A")

cmd.select ("Outward", "resi 440 & chain A", merge=1)

cmd.color ("red", "resi 443 & chain A")

cmd.select ("Inward", "resi 443 & chain A", merge=1)

cmd.color ("blue", "resi 442 & chain A")

cmd.select ("Outward", "resi 442 & chain A", merge=1)

cmd.color ("blue", "resi 394 & chain A")

cmd.select ("Outward", "resi 394 & chain A", merge=1)

cmd.color ("red", "resi 395 & chain A")

cmd.select ("Inward", "resi 395 & chain A", merge=1)

cmd.color ("blue", "resi 488 & chain A")

cmd.select ("Outward", "resi 488 & chain A", merge=1)

cmd.color ("blue", "resi 545 & chain A")

cmd.select ("Outward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 444 & chain A")

cmd.select ("Outward", "resi 444 & chain A", merge=1)

cmd.color ("red", "resi 445 & chain A")

cmd.select ("Inward", "resi 445 & chain A", merge=1)

cmd.color ("red", "resi 489 & chain A")

cmd.select ("Inward", "resi 489 & chain A", merge=1)

cmd.color ("red", "resi 397 & chain A")

cmd.select ("Inward", "resi 397 & chain A", merge=1)

cmd.color ("blue", "resi 396 & chain A")

cmd.select ("Outward", "resi 396 & chain A", merge=1)

cmd.color ("red", "resi 399 & chain A")

cmd.select ("Inward", "resi 399 & chain A", merge=1)

cmd.color ("blue", "resi 398 & chain A")

cmd.select ("Outward", "resi 398 & chain A", merge=1)

cmd.color ("red", "resi 490 & chain A")

cmd.select ("Inward", "resi 490 & chain A", merge=1)

cmd.color ("red", "resi 401 & chain A")

cmd.select ("Inward", "resi 401 & chain A", merge=1)

cmd.color ("blue", "resi 400 & chain A")

cmd.select ("Outward", "resi 400 & chain A", merge=1)

cmd.color ("red", "resi 492 & chain A")

cmd.select ("Inward", "resi 492 & chain A", merge=1)

cmd.color ("red", "resi 403 & chain A")

cmd.select ("Inward", "resi 403 & chain A", merge=1)

cmd.color ("blue", "resi 402 & chain A")

cmd.select ("Outward", "resi 402 & chain A", merge=1)

cmd.color ("red", "resi 491 & chain A")

cmd.select ("Inward", "resi 491 & chain A", merge=1)

cmd.color ("red", "resi 405 & chain A")

cmd.select ("Inward", "resi 405 & chain A", merge=1)

cmd.color ("blue", "resi 404 & chain A")

cmd.select ("Outward", "resi 404 & chain A", merge=1)

cmd.color ("red", "resi 493 & chain A")

cmd.select ("Inward", "resi 493 & chain A", merge=1)

cmd.color ("blue", "resi 406 & chain A")

cmd.select ("Outward", "resi 406 & chain A", merge=1)

cmd.color ("red", "resi 407 & chain A")

cmd.select ("Inward", "resi 407 & chain A", merge=1)

cmd.color ("blue", "resi 494 & chain A")

cmd.select ("Outward", "resi 494 & chain A", merge=1)

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

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

cmd.color ("red", "resi 224 & chain A")

cmd.select ("Inward", "resi 224 & chain A", merge=1)

cmd.color ("blue", "resi 225 & chain A")

cmd.select ("Outward", "resi 225 & chain A", merge=1)

cmd.color ("red", "resi 597 & chain A")

cmd.select ("Inward", "resi 597 & chain A", merge=1)

cmd.color ("blue", "resi 598 & chain A")

cmd.select ("Outward", "resi 598 & chain A", merge=1)

cmd.color ("red", "resi 599 & chain A")

cmd.select ("Inward", "resi 599 & chain A", merge=1)

cmd.color ("blue", "resi 600 & chain A")

cmd.select ("Outward", "resi 600 & chain A", merge=1)

cmd.color ("red", "resi 601 & chain A")

cmd.select ("Inward", "resi 601 & chain A", merge=1)

cmd.color ("blue", "resi 602 & chain A")

cmd.select ("Outward", "resi 602 & chain A", merge=1)

cmd.color ("red", "resi 603 & chain A")

cmd.select ("Inward", "resi 603 & chain A", merge=1)

cmd.color ("blue", "resi 604 & chain A")

cmd.select ("Outward", "resi 604 & chain A", merge=1)

cmd.color ("red", "resi 605 & chain A")

cmd.select ("Inward", "resi 605 & chain A", merge=1)

cmd.color ("blue", "resi 606 & chain A")

cmd.select ("Outward", "resi 606 & chain A", merge=1)

cmd.color ("blue", "resi 607 & chain A")

cmd.select ("Outward", "resi 607 & chain A", merge=1)

cmd.color ("red", "resi 608 & chain A")

cmd.select ("Inward", "resi 608 & chain A", merge=1)

cmd.color ("blue", "resi 609 & chain A")

cmd.select ("Outward", "resi 609 & chain A", merge=1)

cmd.color ("blue", "resi 612 & chain A")

cmd.select ("Outward", "resi 612 & chain A", merge=1)

cmd.color ("red", "resi 613 & chain A")

cmd.select ("Inward", "resi 613 & chain A", merge=1)

cmd.color ("blue", "resi 614 & chain A")

cmd.select ("Outward", "resi 614 & chain A", merge=1)

cmd.color ("red", "resi 615 & chain A")

cmd.select ("Inward", "resi 615 & chain A", merge=1)

cmd.color ("blue", "resi 616 & chain A")

cmd.select ("Outward", "resi 616 & chain A", merge=1)

cmd.color ("red", "resi 617 & chain A")

cmd.select ("Inward", "resi 617 & chain A", merge=1)

cmd.color ("blue", "resi 618 & chain A")

cmd.select ("Outward", "resi 618 & chain A", merge=1)

cmd.color ("red", "resi 619 & chain A")

cmd.select ("Inward", "resi 619 & chain A", merge=1)

cmd.color ("red", "resi 174 & chain A")

cmd.select ("Inward", "resi 174 & chain A", merge=1)

cmd.color ("blue", "resi 175 & chain A")

cmd.select ("Outward", "resi 175 & chain A", merge=1)

cmd.color ("red", "resi 176 & chain A")

cmd.select ("Inward", "resi 176 & chain A", merge=1)

cmd.color ("blue", "resi 177 & chain A")

cmd.select ("Outward", "resi 177 & chain A", merge=1)

cmd.color ("red", "resi 178 & chain A")

cmd.select ("Inward", "resi 178 & chain A", merge=1)

cmd.color ("blue", "resi 179 & chain A")

cmd.select ("Outward", "resi 179 & chain A", merge=1)

cmd.color ("red", "resi 180 & chain A")

cmd.select ("Inward", "resi 180 & chain A", merge=1)

cmd.color ("blue", "resi 181 & chain A")

cmd.select ("Outward", "resi 181 & chain A", merge=1)

cmd.color ("blue", "resi 182 & chain A")

cmd.select ("Outward", "resi 182 & chain A", merge=1)

cmd.color ("red", "resi 183 & chain A")

cmd.select ("Inward", "resi 183 & chain A", merge=1)

cmd.color ("blue", "resi 184 & chain A")

cmd.select ("Outward", "resi 184 & chain A", merge=1)

cmd.load_cgo( [9.0, 13.938785,14.559285,1.1394999, 13.938785, 14.559285, 1.1394999, 1, 1,1,0,0,0,1], "axis" )
