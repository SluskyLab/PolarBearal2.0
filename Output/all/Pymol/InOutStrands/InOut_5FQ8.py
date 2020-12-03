from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FQ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand14", "resi 177+178+179+180+181+182+183+184+185+186+187+188 & chain B ")


cmd.select("Bstrand55", "resi 973+974+975+976+977+978+979+980+981+982+983 & chain B ")


cmd.select("Bstrand19", "resi 252+253+254+255+256+257+258+259+260+261+262+263+264 & chain B ")


cmd.select("Bstrand20", "resi 268+269+270+271+272+273+274+275+276+277+278+279+280 & chain B ")


cmd.select("Bstrand21", "resi 289+290+291+292+293+294+295+296+297+298+299+300+301+302+303 & chain B ")


cmd.select("Bstrand46", "resi 802+803+804+805+806+807+808+809+810+811+812 & chain B ")


cmd.select("Bstrand22", "resi 306+307+308+309+310+311+312+313+314+315+316+317+318+319+320 & chain B ")


cmd.select("Bstrand23", "resi 376+377+378+379+380+381+382+383+384+385+386+387+388+389+390+391+392+393+394 & chain B ")


cmd.select("Bstrand35", "resi 643+644+645+646+647+648+649+650+651+652+653+654+655+656 & chain B ")


cmd.select("Bstrand30", "resi 582+583+584+585+586+587+588+589+590+591+592+593+594+595+596 & chain B ")


cmd.select("Bstrand29", "resi 558+559+560+561+562+563+564+565+566+567+568+569 & chain B ")


cmd.select("Bstrand28", "resi 538+539+540+541+542+543+544+545+546+547+548+549 & chain B ")


cmd.select("Bstrand27", "resi 513+514+515+516+517+518+519+520+521+522+523+524+525+526+527+528+529+530+531+532+533+534 & chain B ")


cmd.select("Bstrand26", "resi 472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495 & chain B ")


cmd.select("Bstrand36", "resi 661+662+663+664+665+666+667+668+669+670+671+672+673 & chain B ")


cmd.select("Bstrand25", "resi 446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469 & chain B ")


cmd.select("Bstrand39", "resi 697+698+699+700+701+702+703+704+705+706+707+708+709+710+711+712 & chain B ")


cmd.select("Bstrand24", "resi 398+399+400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417 & chain B ")


cmd.select("Bstrand40", "resi 716+717+718+719+720+721+722+723+724+725+726+727+728+729+730+731 & chain B ")


cmd.select("Bstrand47", "resi 815+816+817+818+819+820+821+822+823+824+825 & chain B ")


cmd.select("Bstrand52", "resi 904+905+906+907+908+909+910+911+912+913+914+915 & chain B ")


cmd.select("Bstrand53", "resi 928+929+930+931+932+933+934+935+936+937+938+939+940+941 & chain B ")


cmd.select("barrel", "Bstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 177 & chain B")

cmd.select ("Outward", "resi 177 & chain B", merge=1)

cmd.color ("red", "resi 178 & chain B")

cmd.select ("Inward", "resi 178 & chain B", merge=1)

cmd.color ("blue", "resi 179 & chain B")

cmd.select ("Outward", "resi 179 & chain B", merge=1)

cmd.color ("red", "resi 180 & chain B")

cmd.select ("Inward", "resi 180 & chain B", merge=1)

cmd.color ("blue", "resi 181 & chain B")

cmd.select ("Outward", "resi 181 & chain B", merge=1)

cmd.color ("red", "resi 182 & chain B")

cmd.select ("Inward", "resi 182 & chain B", merge=1)

cmd.color ("blue", "resi 183 & chain B")

cmd.select ("Outward", "resi 183 & chain B", merge=1)

cmd.color ("red", "resi 184 & chain B")

cmd.select ("Inward", "resi 184 & chain B", merge=1)

cmd.color ("blue", "resi 185 & chain B")

cmd.select ("Outward", "resi 185 & chain B", merge=1)

cmd.color ("red", "resi 186 & chain B")

cmd.select ("Inward", "resi 186 & chain B", merge=1)

cmd.color ("blue", "resi 187 & chain B")

cmd.select ("Outward", "resi 187 & chain B", merge=1)

cmd.color ("blue", "resi 188 & chain B")

cmd.select ("Outward", "resi 188 & chain B", merge=1)

cmd.color ("red", "resi 973 & chain B")

cmd.select ("Inward", "resi 973 & chain B", merge=1)

cmd.color ("blue", "resi 974 & chain B")

cmd.select ("Outward", "resi 974 & chain B", merge=1)

cmd.color ("red", "resi 975 & chain B")

cmd.select ("Inward", "resi 975 & chain B", merge=1)

cmd.color ("blue", "resi 976 & chain B")

cmd.select ("Outward", "resi 976 & chain B", merge=1)

cmd.color ("red", "resi 977 & chain B")

cmd.select ("Inward", "resi 977 & chain B", merge=1)

cmd.color ("blue", "resi 978 & chain B")

cmd.select ("Outward", "resi 978 & chain B", merge=1)

cmd.color ("red", "resi 979 & chain B")

cmd.select ("Inward", "resi 979 & chain B", merge=1)

cmd.color ("blue", "resi 980 & chain B")

cmd.select ("Outward", "resi 980 & chain B", merge=1)

cmd.color ("red", "resi 981 & chain B")

cmd.select ("Inward", "resi 981 & chain B", merge=1)

cmd.color ("blue", "resi 982 & chain B")

cmd.select ("Outward", "resi 982 & chain B", merge=1)

cmd.color ("blue", "resi 983 & chain B")

cmd.select ("Outward", "resi 983 & chain B", merge=1)

cmd.color ("red", "resi 252 & chain B")

cmd.select ("Inward", "resi 252 & chain B", merge=1)

cmd.color ("blue", "resi 253 & chain B")

cmd.select ("Outward", "resi 253 & chain B", merge=1)

cmd.color ("red", "resi 254 & chain B")

cmd.select ("Inward", "resi 254 & chain B", merge=1)

cmd.color ("blue", "resi 255 & chain B")

cmd.select ("Outward", "resi 255 & chain B", merge=1)

cmd.color ("red", "resi 256 & chain B")

cmd.select ("Inward", "resi 256 & chain B", merge=1)

cmd.color ("blue", "resi 257 & chain B")

cmd.select ("Outward", "resi 257 & chain B", merge=1)

cmd.color ("red", "resi 258 & chain B")

cmd.select ("Inward", "resi 258 & chain B", merge=1)

cmd.color ("blue", "resi 259 & chain B")

cmd.select ("Outward", "resi 259 & chain B", merge=1)

cmd.color ("red", "resi 260 & chain B")

cmd.select ("Inward", "resi 260 & chain B", merge=1)

cmd.color ("blue", "resi 261 & chain B")

cmd.select ("Outward", "resi 261 & chain B", merge=1)

cmd.color ("red", "resi 262 & chain B")

cmd.select ("Inward", "resi 262 & chain B", merge=1)

cmd.color ("blue", "resi 263 & chain B")

cmd.select ("Outward", "resi 263 & chain B", merge=1)

cmd.color ("red", "resi 264 & chain B")

cmd.select ("Inward", "resi 264 & chain B", merge=1)

cmd.color ("blue", "resi 268 & chain B")

cmd.select ("Outward", "resi 268 & chain B", merge=1)

cmd.color ("red", "resi 269 & chain B")

cmd.select ("Inward", "resi 269 & chain B", merge=1)

cmd.color ("blue", "resi 270 & chain B")

cmd.select ("Outward", "resi 270 & chain B", merge=1)

cmd.color ("red", "resi 271 & chain B")

cmd.select ("Inward", "resi 271 & chain B", merge=1)

cmd.color ("blue", "resi 272 & chain B")

cmd.select ("Outward", "resi 272 & chain B", merge=1)

cmd.color ("red", "resi 273 & chain B")

cmd.select ("Inward", "resi 273 & chain B", merge=1)

cmd.color ("blue", "resi 274 & chain B")

cmd.select ("Outward", "resi 274 & chain B", merge=1)

cmd.color ("red", "resi 275 & chain B")

cmd.select ("Inward", "resi 275 & chain B", merge=1)

cmd.color ("blue", "resi 276 & chain B")

cmd.select ("Outward", "resi 276 & chain B", merge=1)

cmd.color ("red", "resi 277 & chain B")

cmd.select ("Inward", "resi 277 & chain B", merge=1)

cmd.color ("blue", "resi 278 & chain B")

cmd.select ("Outward", "resi 278 & chain B", merge=1)

cmd.color ("red", "resi 279 & chain B")

cmd.select ("Inward", "resi 279 & chain B", merge=1)

cmd.color ("blue", "resi 280 & chain B")

cmd.select ("Outward", "resi 280 & chain B", merge=1)

cmd.color ("blue", "resi 289 & chain B")

cmd.select ("Outward", "resi 289 & chain B", merge=1)

cmd.color ("red", "resi 290 & chain B")

cmd.select ("Inward", "resi 290 & chain B", merge=1)

cmd.color ("blue", "resi 291 & chain B")

cmd.select ("Outward", "resi 291 & chain B", merge=1)

cmd.color ("red", "resi 292 & chain B")

cmd.select ("Inward", "resi 292 & chain B", merge=1)

cmd.color ("blue", "resi 293 & chain B")

cmd.select ("Outward", "resi 293 & chain B", merge=1)

cmd.color ("red", "resi 294 & chain B")

cmd.select ("Inward", "resi 294 & chain B", merge=1)

cmd.color ("blue", "resi 295 & chain B")

cmd.select ("Outward", "resi 295 & chain B", merge=1)

cmd.color ("red", "resi 296 & chain B")

cmd.select ("Inward", "resi 296 & chain B", merge=1)

cmd.color ("blue", "resi 297 & chain B")

cmd.select ("Outward", "resi 297 & chain B", merge=1)

cmd.color ("red", "resi 298 & chain B")

cmd.select ("Inward", "resi 298 & chain B", merge=1)

cmd.color ("blue", "resi 299 & chain B")

cmd.select ("Outward", "resi 299 & chain B", merge=1)

cmd.color ("red", "resi 300 & chain B")

cmd.select ("Inward", "resi 300 & chain B", merge=1)

cmd.color ("blue", "resi 301 & chain B")

cmd.select ("Outward", "resi 301 & chain B", merge=1)

cmd.color ("blue", "resi 302 & chain B")

cmd.select ("Outward", "resi 302 & chain B", merge=1)

cmd.color ("blue", "resi 303 & chain B")

cmd.select ("Outward", "resi 303 & chain B", merge=1)

cmd.color ("blue", "resi 802 & chain B")

cmd.select ("Outward", "resi 802 & chain B", merge=1)

cmd.color ("red", "resi 803 & chain B")

cmd.select ("Inward", "resi 803 & chain B", merge=1)

cmd.color ("blue", "resi 804 & chain B")

cmd.select ("Outward", "resi 804 & chain B", merge=1)

cmd.color ("red", "resi 805 & chain B")

cmd.select ("Inward", "resi 805 & chain B", merge=1)

cmd.color ("blue", "resi 806 & chain B")

cmd.select ("Outward", "resi 806 & chain B", merge=1)

cmd.color ("red", "resi 807 & chain B")

cmd.select ("Inward", "resi 807 & chain B", merge=1)

cmd.color ("blue", "resi 808 & chain B")

cmd.select ("Outward", "resi 808 & chain B", merge=1)

cmd.color ("red", "resi 809 & chain B")

cmd.select ("Inward", "resi 809 & chain B", merge=1)

cmd.color ("blue", "resi 810 & chain B")

cmd.select ("Outward", "resi 810 & chain B", merge=1)

cmd.color ("red", "resi 811 & chain B")

cmd.select ("Inward", "resi 811 & chain B", merge=1)

cmd.color ("blue", "resi 812 & chain B")

cmd.select ("Outward", "resi 812 & chain B", merge=1)

cmd.color ("blue", "resi 306 & chain B")

cmd.select ("Outward", "resi 306 & chain B", merge=1)

cmd.color ("red", "resi 307 & chain B")

cmd.select ("Inward", "resi 307 & chain B", merge=1)

cmd.color ("blue", "resi 308 & chain B")

cmd.select ("Outward", "resi 308 & chain B", merge=1)

cmd.color ("red", "resi 309 & chain B")

cmd.select ("Inward", "resi 309 & chain B", merge=1)

cmd.color ("blue", "resi 310 & chain B")

cmd.select ("Outward", "resi 310 & chain B", merge=1)

cmd.color ("red", "resi 311 & chain B")

cmd.select ("Inward", "resi 311 & chain B", merge=1)

cmd.color ("blue", "resi 312 & chain B")

cmd.select ("Outward", "resi 312 & chain B", merge=1)

cmd.color ("red", "resi 313 & chain B")

cmd.select ("Inward", "resi 313 & chain B", merge=1)

cmd.color ("blue", "resi 314 & chain B")

cmd.select ("Outward", "resi 314 & chain B", merge=1)

cmd.color ("red", "resi 315 & chain B")

cmd.select ("Inward", "resi 315 & chain B", merge=1)

cmd.color ("blue", "resi 316 & chain B")

cmd.select ("Outward", "resi 316 & chain B", merge=1)

cmd.color ("red", "resi 317 & chain B")

cmd.select ("Inward", "resi 317 & chain B", merge=1)

cmd.color ("blue", "resi 318 & chain B")

cmd.select ("Outward", "resi 318 & chain B", merge=1)

cmd.color ("red", "resi 319 & chain B")

cmd.select ("Inward", "resi 319 & chain B", merge=1)

cmd.color ("blue", "resi 320 & chain B")

cmd.select ("Outward", "resi 320 & chain B", merge=1)

cmd.color ("blue", "resi 376 & chain B")

cmd.select ("Outward", "resi 376 & chain B", merge=1)

cmd.color ("red", "resi 377 & chain B")

cmd.select ("Inward", "resi 377 & chain B", merge=1)

cmd.color ("blue", "resi 378 & chain B")

cmd.select ("Outward", "resi 378 & chain B", merge=1)

cmd.color ("red", "resi 379 & chain B")

cmd.select ("Inward", "resi 379 & chain B", merge=1)

cmd.color ("blue", "resi 380 & chain B")

cmd.select ("Outward", "resi 380 & chain B", merge=1)

cmd.color ("red", "resi 381 & chain B")

cmd.select ("Inward", "resi 381 & chain B", merge=1)

cmd.color ("blue", "resi 382 & chain B")

cmd.select ("Outward", "resi 382 & chain B", merge=1)

cmd.color ("red", "resi 383 & chain B")

cmd.select ("Inward", "resi 383 & chain B", merge=1)

cmd.color ("blue", "resi 384 & chain B")

cmd.select ("Outward", "resi 384 & chain B", merge=1)

cmd.color ("red", "resi 385 & chain B")

cmd.select ("Inward", "resi 385 & chain B", merge=1)

cmd.color ("blue", "resi 386 & chain B")

cmd.select ("Outward", "resi 386 & chain B", merge=1)

cmd.color ("red", "resi 387 & chain B")

cmd.select ("Inward", "resi 387 & chain B", merge=1)

cmd.color ("blue", "resi 388 & chain B")

cmd.select ("Outward", "resi 388 & chain B", merge=1)

cmd.color ("red", "resi 389 & chain B")

cmd.select ("Inward", "resi 389 & chain B", merge=1)

cmd.color ("blue", "resi 390 & chain B")

cmd.select ("Outward", "resi 390 & chain B", merge=1)

cmd.color ("red", "resi 391 & chain B")

cmd.select ("Inward", "resi 391 & chain B", merge=1)

cmd.color ("blue", "resi 392 & chain B")

cmd.select ("Outward", "resi 392 & chain B", merge=1)

cmd.color ("blue", "resi 393 & chain B")

cmd.select ("Outward", "resi 393 & chain B", merge=1)

cmd.color ("red", "resi 394 & chain B")

cmd.select ("Inward", "resi 394 & chain B", merge=1)

cmd.color ("red", "resi 643 & chain B")

cmd.select ("Inward", "resi 643 & chain B", merge=1)

cmd.color ("blue", "resi 644 & chain B")

cmd.select ("Outward", "resi 644 & chain B", merge=1)

cmd.color ("red", "resi 645 & chain B")

cmd.select ("Inward", "resi 645 & chain B", merge=1)

cmd.color ("blue", "resi 646 & chain B")

cmd.select ("Outward", "resi 646 & chain B", merge=1)

cmd.color ("red", "resi 647 & chain B")

cmd.select ("Inward", "resi 647 & chain B", merge=1)

cmd.color ("blue", "resi 648 & chain B")

cmd.select ("Outward", "resi 648 & chain B", merge=1)

cmd.color ("red", "resi 649 & chain B")

cmd.select ("Inward", "resi 649 & chain B", merge=1)

cmd.color ("blue", "resi 650 & chain B")

cmd.select ("Outward", "resi 650 & chain B", merge=1)

cmd.color ("red", "resi 651 & chain B")

cmd.select ("Inward", "resi 651 & chain B", merge=1)

cmd.color ("blue", "resi 652 & chain B")

cmd.select ("Outward", "resi 652 & chain B", merge=1)

cmd.color ("red", "resi 653 & chain B")

cmd.select ("Inward", "resi 653 & chain B", merge=1)

cmd.color ("blue", "resi 654 & chain B")

cmd.select ("Outward", "resi 654 & chain B", merge=1)

cmd.color ("red", "resi 655 & chain B")

cmd.select ("Inward", "resi 655 & chain B", merge=1)

cmd.color ("blue", "resi 656 & chain B")

cmd.select ("Outward", "resi 656 & chain B", merge=1)

cmd.color ("blue", "resi 582 & chain B")

cmd.select ("Outward", "resi 582 & chain B", merge=1)

cmd.color ("red", "resi 583 & chain B")

cmd.select ("Inward", "resi 583 & chain B", merge=1)

cmd.color ("red", "resi 584 & chain B")

cmd.select ("Inward", "resi 584 & chain B", merge=1)

cmd.color ("blue", "resi 585 & chain B")

cmd.select ("Outward", "resi 585 & chain B", merge=1)

cmd.color ("red", "resi 586 & chain B")

cmd.select ("Inward", "resi 586 & chain B", merge=1)

cmd.color ("blue", "resi 587 & chain B")

cmd.select ("Outward", "resi 587 & chain B", merge=1)

cmd.color ("red", "resi 588 & chain B")

cmd.select ("Inward", "resi 588 & chain B", merge=1)

cmd.color ("blue", "resi 589 & chain B")

cmd.select ("Outward", "resi 589 & chain B", merge=1)

cmd.color ("red", "resi 590 & chain B")

cmd.select ("Inward", "resi 590 & chain B", merge=1)

cmd.color ("blue", "resi 591 & chain B")

cmd.select ("Outward", "resi 591 & chain B", merge=1)

cmd.color ("red", "resi 592 & chain B")

cmd.select ("Inward", "resi 592 & chain B", merge=1)

cmd.color ("blue", "resi 593 & chain B")

cmd.select ("Outward", "resi 593 & chain B", merge=1)

cmd.color ("red", "resi 594 & chain B")

cmd.select ("Inward", "resi 594 & chain B", merge=1)

cmd.color ("blue", "resi 595 & chain B")

cmd.select ("Outward", "resi 595 & chain B", merge=1)

cmd.color ("red", "resi 596 & chain B")

cmd.select ("Inward", "resi 596 & chain B", merge=1)

cmd.color ("blue", "resi 558 & chain B")

cmd.select ("Outward", "resi 558 & chain B", merge=1)

cmd.color ("red", "resi 559 & chain B")

cmd.select ("Inward", "resi 559 & chain B", merge=1)

cmd.color ("blue", "resi 560 & chain B")

cmd.select ("Outward", "resi 560 & chain B", merge=1)

cmd.color ("red", "resi 561 & chain B")

cmd.select ("Inward", "resi 561 & chain B", merge=1)

cmd.color ("blue", "resi 562 & chain B")

cmd.select ("Outward", "resi 562 & chain B", merge=1)

cmd.color ("red", "resi 563 & chain B")

cmd.select ("Inward", "resi 563 & chain B", merge=1)

cmd.color ("blue", "resi 564 & chain B")

cmd.select ("Outward", "resi 564 & chain B", merge=1)

cmd.color ("red", "resi 565 & chain B")

cmd.select ("Inward", "resi 565 & chain B", merge=1)

cmd.color ("blue", "resi 566 & chain B")

cmd.select ("Outward", "resi 566 & chain B", merge=1)

cmd.color ("red", "resi 567 & chain B")

cmd.select ("Inward", "resi 567 & chain B", merge=1)

cmd.color ("blue", "resi 568 & chain B")

cmd.select ("Outward", "resi 568 & chain B", merge=1)

cmd.color ("red", "resi 569 & chain B")

cmd.select ("Inward", "resi 569 & chain B", merge=1)

cmd.color ("blue", "resi 538 & chain B")

cmd.select ("Outward", "resi 538 & chain B", merge=1)

cmd.color ("red", "resi 539 & chain B")

cmd.select ("Inward", "resi 539 & chain B", merge=1)

cmd.color ("blue", "resi 540 & chain B")

cmd.select ("Outward", "resi 540 & chain B", merge=1)

cmd.color ("red", "resi 541 & chain B")

cmd.select ("Inward", "resi 541 & chain B", merge=1)

cmd.color ("blue", "resi 542 & chain B")

cmd.select ("Outward", "resi 542 & chain B", merge=1)

cmd.color ("red", "resi 543 & chain B")

cmd.select ("Inward", "resi 543 & chain B", merge=1)

cmd.color ("blue", "resi 544 & chain B")

cmd.select ("Outward", "resi 544 & chain B", merge=1)

cmd.color ("red", "resi 545 & chain B")

cmd.select ("Inward", "resi 545 & chain B", merge=1)

cmd.color ("blue", "resi 546 & chain B")

cmd.select ("Outward", "resi 546 & chain B", merge=1)

cmd.color ("red", "resi 547 & chain B")

cmd.select ("Inward", "resi 547 & chain B", merge=1)

cmd.color ("blue", "resi 548 & chain B")

cmd.select ("Outward", "resi 548 & chain B", merge=1)

cmd.color ("red", "resi 549 & chain B")

cmd.select ("Inward", "resi 549 & chain B", merge=1)

cmd.color ("red", "resi 513 & chain B")

cmd.select ("Inward", "resi 513 & chain B", merge=1)

cmd.color ("blue", "resi 514 & chain B")

cmd.select ("Outward", "resi 514 & chain B", merge=1)

cmd.color ("red", "resi 515 & chain B")

cmd.select ("Inward", "resi 515 & chain B", merge=1)

cmd.color ("blue", "resi 516 & chain B")

cmd.select ("Outward", "resi 516 & chain B", merge=1)

cmd.color ("red", "resi 517 & chain B")

cmd.select ("Inward", "resi 517 & chain B", merge=1)

cmd.color ("blue", "resi 518 & chain B")

cmd.select ("Outward", "resi 518 & chain B", merge=1)

cmd.color ("red", "resi 519 & chain B")

cmd.select ("Inward", "resi 519 & chain B", merge=1)

cmd.color ("blue", "resi 520 & chain B")

cmd.select ("Outward", "resi 520 & chain B", merge=1)

cmd.color ("red", "resi 521 & chain B")

cmd.select ("Inward", "resi 521 & chain B", merge=1)

cmd.color ("blue", "resi 522 & chain B")

cmd.select ("Outward", "resi 522 & chain B", merge=1)

cmd.color ("red", "resi 523 & chain B")

cmd.select ("Inward", "resi 523 & chain B", merge=1)

cmd.color ("blue", "resi 524 & chain B")

cmd.select ("Outward", "resi 524 & chain B", merge=1)

cmd.color ("red", "resi 525 & chain B")

cmd.select ("Inward", "resi 525 & chain B", merge=1)

cmd.color ("blue", "resi 526 & chain B")

cmd.select ("Outward", "resi 526 & chain B", merge=1)

cmd.color ("red", "resi 527 & chain B")

cmd.select ("Inward", "resi 527 & chain B", merge=1)

cmd.color ("blue", "resi 528 & chain B")

cmd.select ("Outward", "resi 528 & chain B", merge=1)

cmd.color ("red", "resi 529 & chain B")

cmd.select ("Inward", "resi 529 & chain B", merge=1)

cmd.color ("blue", "resi 530 & chain B")

cmd.select ("Outward", "resi 530 & chain B", merge=1)

cmd.color ("red", "resi 531 & chain B")

cmd.select ("Inward", "resi 531 & chain B", merge=1)

cmd.color ("blue", "resi 532 & chain B")

cmd.select ("Outward", "resi 532 & chain B", merge=1)

cmd.color ("red", "resi 533 & chain B")

cmd.select ("Inward", "resi 533 & chain B", merge=1)

cmd.color ("blue", "resi 534 & chain B")

cmd.select ("Outward", "resi 534 & chain B", merge=1)

cmd.color ("blue", "resi 472 & chain B")

cmd.select ("Outward", "resi 472 & chain B", merge=1)

cmd.color ("red", "resi 473 & chain B")

cmd.select ("Inward", "resi 473 & chain B", merge=1)

cmd.color ("blue", "resi 474 & chain B")

cmd.select ("Outward", "resi 474 & chain B", merge=1)

cmd.color ("red", "resi 475 & chain B")

cmd.select ("Inward", "resi 475 & chain B", merge=1)

cmd.color ("blue", "resi 476 & chain B")

cmd.select ("Outward", "resi 476 & chain B", merge=1)

cmd.color ("red", "resi 477 & chain B")

cmd.select ("Inward", "resi 477 & chain B", merge=1)

cmd.color ("blue", "resi 478 & chain B")

cmd.select ("Outward", "resi 478 & chain B", merge=1)

cmd.color ("red", "resi 479 & chain B")

cmd.select ("Inward", "resi 479 & chain B", merge=1)

cmd.color ("blue", "resi 480 & chain B")

cmd.select ("Outward", "resi 480 & chain B", merge=1)

cmd.color ("red", "resi 481 & chain B")

cmd.select ("Inward", "resi 481 & chain B", merge=1)

cmd.color ("blue", "resi 482 & chain B")

cmd.select ("Outward", "resi 482 & chain B", merge=1)

cmd.color ("red", "resi 483 & chain B")

cmd.select ("Inward", "resi 483 & chain B", merge=1)

cmd.color ("blue", "resi 484 & chain B")

cmd.select ("Outward", "resi 484 & chain B", merge=1)

cmd.color ("red", "resi 485 & chain B")

cmd.select ("Inward", "resi 485 & chain B", merge=1)

cmd.color ("blue", "resi 486 & chain B")

cmd.select ("Outward", "resi 486 & chain B", merge=1)

cmd.color ("red", "resi 487 & chain B")

cmd.select ("Inward", "resi 487 & chain B", merge=1)

cmd.color ("blue", "resi 488 & chain B")

cmd.select ("Outward", "resi 488 & chain B", merge=1)

cmd.color ("red", "resi 489 & chain B")

cmd.select ("Inward", "resi 489 & chain B", merge=1)

cmd.color ("blue", "resi 490 & chain B")

cmd.select ("Outward", "resi 490 & chain B", merge=1)

cmd.color ("red", "resi 491 & chain B")

cmd.select ("Inward", "resi 491 & chain B", merge=1)

cmd.color ("blue", "resi 492 & chain B")

cmd.select ("Outward", "resi 492 & chain B", merge=1)

cmd.color ("red", "resi 493 & chain B")

cmd.select ("Inward", "resi 493 & chain B", merge=1)

cmd.color ("blue", "resi 494 & chain B")

cmd.select ("Outward", "resi 494 & chain B", merge=1)

cmd.color ("red", "resi 495 & chain B")

cmd.select ("Inward", "resi 495 & chain B", merge=1)

cmd.color ("blue", "resi 661 & chain B")

cmd.select ("Outward", "resi 661 & chain B", merge=1)

cmd.color ("red", "resi 662 & chain B")

cmd.select ("Inward", "resi 662 & chain B", merge=1)

cmd.color ("blue", "resi 663 & chain B")

cmd.select ("Outward", "resi 663 & chain B", merge=1)

cmd.color ("red", "resi 664 & chain B")

cmd.select ("Inward", "resi 664 & chain B", merge=1)

cmd.color ("blue", "resi 665 & chain B")

cmd.select ("Outward", "resi 665 & chain B", merge=1)

cmd.color ("red", "resi 666 & chain B")

cmd.select ("Inward", "resi 666 & chain B", merge=1)

cmd.color ("blue", "resi 667 & chain B")

cmd.select ("Outward", "resi 667 & chain B", merge=1)

cmd.color ("red", "resi 668 & chain B")

cmd.select ("Inward", "resi 668 & chain B", merge=1)

cmd.color ("blue", "resi 669 & chain B")

cmd.select ("Outward", "resi 669 & chain B", merge=1)

cmd.color ("red", "resi 670 & chain B")

cmd.select ("Inward", "resi 670 & chain B", merge=1)

cmd.color ("blue", "resi 671 & chain B")

cmd.select ("Outward", "resi 671 & chain B", merge=1)

cmd.color ("red", "resi 672 & chain B")

cmd.select ("Inward", "resi 672 & chain B", merge=1)

cmd.color ("blue", "resi 673 & chain B")

cmd.select ("Outward", "resi 673 & chain B", merge=1)

cmd.color ("red", "resi 446 & chain B")

cmd.select ("Inward", "resi 446 & chain B", merge=1)

cmd.color ("blue", "resi 447 & chain B")

cmd.select ("Outward", "resi 447 & chain B", merge=1)

cmd.color ("red", "resi 448 & chain B")

cmd.select ("Inward", "resi 448 & chain B", merge=1)

cmd.color ("blue", "resi 449 & chain B")

cmd.select ("Outward", "resi 449 & chain B", merge=1)

cmd.color ("red", "resi 450 & chain B")

cmd.select ("Inward", "resi 450 & chain B", merge=1)

cmd.color ("blue", "resi 451 & chain B")

cmd.select ("Outward", "resi 451 & chain B", merge=1)

cmd.color ("red", "resi 452 & chain B")

cmd.select ("Inward", "resi 452 & chain B", merge=1)

cmd.color ("blue", "resi 453 & chain B")

cmd.select ("Outward", "resi 453 & chain B", merge=1)

cmd.color ("red", "resi 454 & chain B")

cmd.select ("Inward", "resi 454 & chain B", merge=1)

cmd.color ("blue", "resi 455 & chain B")

cmd.select ("Outward", "resi 455 & chain B", merge=1)

cmd.color ("red", "resi 456 & chain B")

cmd.select ("Inward", "resi 456 & chain B", merge=1)

cmd.color ("blue", "resi 457 & chain B")

cmd.select ("Outward", "resi 457 & chain B", merge=1)

cmd.color ("red", "resi 458 & chain B")

cmd.select ("Inward", "resi 458 & chain B", merge=1)

cmd.color ("blue", "resi 459 & chain B")

cmd.select ("Outward", "resi 459 & chain B", merge=1)

cmd.color ("red", "resi 460 & chain B")

cmd.select ("Inward", "resi 460 & chain B", merge=1)

cmd.color ("blue", "resi 461 & chain B")

cmd.select ("Outward", "resi 461 & chain B", merge=1)

cmd.color ("red", "resi 462 & chain B")

cmd.select ("Inward", "resi 462 & chain B", merge=1)

cmd.color ("blue", "resi 463 & chain B")

cmd.select ("Outward", "resi 463 & chain B", merge=1)

cmd.color ("red", "resi 464 & chain B")

cmd.select ("Inward", "resi 464 & chain B", merge=1)

cmd.color ("blue", "resi 465 & chain B")

cmd.select ("Outward", "resi 465 & chain B", merge=1)

cmd.color ("red", "resi 466 & chain B")

cmd.select ("Inward", "resi 466 & chain B", merge=1)

cmd.color ("blue", "resi 467 & chain B")

cmd.select ("Outward", "resi 467 & chain B", merge=1)

cmd.color ("red", "resi 468 & chain B")

cmd.select ("Inward", "resi 468 & chain B", merge=1)

cmd.color ("blue", "resi 469 & chain B")

cmd.select ("Outward", "resi 469 & chain B", merge=1)

cmd.color ("red", "resi 697 & chain B")

cmd.select ("Inward", "resi 697 & chain B", merge=1)

cmd.color ("blue", "resi 698 & chain B")

cmd.select ("Outward", "resi 698 & chain B", merge=1)

cmd.color ("red", "resi 699 & chain B")

cmd.select ("Inward", "resi 699 & chain B", merge=1)

cmd.color ("blue", "resi 700 & chain B")

cmd.select ("Outward", "resi 700 & chain B", merge=1)

cmd.color ("red", "resi 701 & chain B")

cmd.select ("Inward", "resi 701 & chain B", merge=1)

cmd.color ("blue", "resi 702 & chain B")

cmd.select ("Outward", "resi 702 & chain B", merge=1)

cmd.color ("red", "resi 703 & chain B")

cmd.select ("Inward", "resi 703 & chain B", merge=1)

cmd.color ("blue", "resi 704 & chain B")

cmd.select ("Outward", "resi 704 & chain B", merge=1)

cmd.color ("red", "resi 705 & chain B")

cmd.select ("Inward", "resi 705 & chain B", merge=1)

cmd.color ("blue", "resi 706 & chain B")

cmd.select ("Outward", "resi 706 & chain B", merge=1)

cmd.color ("red", "resi 707 & chain B")

cmd.select ("Inward", "resi 707 & chain B", merge=1)

cmd.color ("blue", "resi 708 & chain B")

cmd.select ("Outward", "resi 708 & chain B", merge=1)

cmd.color ("blue", "resi 709 & chain B")

cmd.select ("Outward", "resi 709 & chain B", merge=1)

cmd.color ("red", "resi 710 & chain B")

cmd.select ("Inward", "resi 710 & chain B", merge=1)

cmd.color ("blue", "resi 711 & chain B")

cmd.select ("Outward", "resi 711 & chain B", merge=1)

cmd.color ("red", "resi 712 & chain B")

cmd.select ("Inward", "resi 712 & chain B", merge=1)

cmd.color ("blue", "resi 398 & chain B")

cmd.select ("Outward", "resi 398 & chain B", merge=1)

cmd.color ("red", "resi 399 & chain B")

cmd.select ("Inward", "resi 399 & chain B", merge=1)

cmd.color ("blue", "resi 400 & chain B")

cmd.select ("Outward", "resi 400 & chain B", merge=1)

cmd.color ("red", "resi 401 & chain B")

cmd.select ("Inward", "resi 401 & chain B", merge=1)

cmd.color ("blue", "resi 402 & chain B")

cmd.select ("Outward", "resi 402 & chain B", merge=1)

cmd.color ("red", "resi 403 & chain B")

cmd.select ("Inward", "resi 403 & chain B", merge=1)

cmd.color ("blue", "resi 404 & chain B")

cmd.select ("Outward", "resi 404 & chain B", merge=1)

cmd.color ("red", "resi 405 & chain B")

cmd.select ("Inward", "resi 405 & chain B", merge=1)

cmd.color ("blue", "resi 406 & chain B")

cmd.select ("Outward", "resi 406 & chain B", merge=1)

cmd.color ("red", "resi 407 & chain B")

cmd.select ("Inward", "resi 407 & chain B", merge=1)

cmd.color ("blue", "resi 408 & chain B")

cmd.select ("Outward", "resi 408 & chain B", merge=1)

cmd.color ("red", "resi 409 & chain B")

cmd.select ("Inward", "resi 409 & chain B", merge=1)

cmd.color ("blue", "resi 410 & chain B")

cmd.select ("Outward", "resi 410 & chain B", merge=1)

cmd.color ("red", "resi 411 & chain B")

cmd.select ("Inward", "resi 411 & chain B", merge=1)

cmd.color ("blue", "resi 412 & chain B")

cmd.select ("Outward", "resi 412 & chain B", merge=1)

cmd.color ("red", "resi 413 & chain B")

cmd.select ("Inward", "resi 413 & chain B", merge=1)

cmd.color ("blue", "resi 414 & chain B")

cmd.select ("Outward", "resi 414 & chain B", merge=1)

cmd.color ("red", "resi 415 & chain B")

cmd.select ("Inward", "resi 415 & chain B", merge=1)

cmd.color ("blue", "resi 416 & chain B")

cmd.select ("Outward", "resi 416 & chain B", merge=1)

cmd.color ("red", "resi 417 & chain B")

cmd.select ("Inward", "resi 417 & chain B", merge=1)

cmd.color ("blue", "resi 716 & chain B")

cmd.select ("Outward", "resi 716 & chain B", merge=1)

cmd.color ("red", "resi 717 & chain B")

cmd.select ("Inward", "resi 717 & chain B", merge=1)

cmd.color ("blue", "resi 718 & chain B")

cmd.select ("Outward", "resi 718 & chain B", merge=1)

cmd.color ("red", "resi 719 & chain B")

cmd.select ("Inward", "resi 719 & chain B", merge=1)

cmd.color ("blue", "resi 720 & chain B")

cmd.select ("Outward", "resi 720 & chain B", merge=1)

cmd.color ("red", "resi 721 & chain B")

cmd.select ("Inward", "resi 721 & chain B", merge=1)

cmd.color ("blue", "resi 722 & chain B")

cmd.select ("Outward", "resi 722 & chain B", merge=1)

cmd.color ("red", "resi 723 & chain B")

cmd.select ("Inward", "resi 723 & chain B", merge=1)

cmd.color ("blue", "resi 724 & chain B")

cmd.select ("Outward", "resi 724 & chain B", merge=1)

cmd.color ("red", "resi 725 & chain B")

cmd.select ("Inward", "resi 725 & chain B", merge=1)

cmd.color ("blue", "resi 726 & chain B")

cmd.select ("Outward", "resi 726 & chain B", merge=1)

cmd.color ("red", "resi 727 & chain B")

cmd.select ("Inward", "resi 727 & chain B", merge=1)

cmd.color ("blue", "resi 728 & chain B")

cmd.select ("Outward", "resi 728 & chain B", merge=1)

cmd.color ("red", "resi 729 & chain B")

cmd.select ("Inward", "resi 729 & chain B", merge=1)

cmd.color ("blue", "resi 730 & chain B")

cmd.select ("Outward", "resi 730 & chain B", merge=1)

cmd.color ("blue", "resi 731 & chain B")

cmd.select ("Outward", "resi 731 & chain B", merge=1)

cmd.color ("blue", "resi 815 & chain B")

cmd.select ("Outward", "resi 815 & chain B", merge=1)

cmd.color ("red", "resi 816 & chain B")

cmd.select ("Inward", "resi 816 & chain B", merge=1)

cmd.color ("blue", "resi 817 & chain B")

cmd.select ("Outward", "resi 817 & chain B", merge=1)

cmd.color ("red", "resi 818 & chain B")

cmd.select ("Inward", "resi 818 & chain B", merge=1)

cmd.color ("blue", "resi 819 & chain B")

cmd.select ("Outward", "resi 819 & chain B", merge=1)

cmd.color ("red", "resi 820 & chain B")

cmd.select ("Inward", "resi 820 & chain B", merge=1)

cmd.color ("blue", "resi 821 & chain B")

cmd.select ("Outward", "resi 821 & chain B", merge=1)

cmd.color ("red", "resi 822 & chain B")

cmd.select ("Inward", "resi 822 & chain B", merge=1)

cmd.color ("blue", "resi 823 & chain B")

cmd.select ("Outward", "resi 823 & chain B", merge=1)

cmd.color ("red", "resi 824 & chain B")

cmd.select ("Inward", "resi 824 & chain B", merge=1)

cmd.color ("blue", "resi 825 & chain B")

cmd.select ("Outward", "resi 825 & chain B", merge=1)

cmd.color ("red", "resi 904 & chain B")

cmd.select ("Inward", "resi 904 & chain B", merge=1)

cmd.color ("blue", "resi 905 & chain B")

cmd.select ("Outward", "resi 905 & chain B", merge=1)

cmd.color ("red", "resi 906 & chain B")

cmd.select ("Inward", "resi 906 & chain B", merge=1)

cmd.color ("blue", "resi 907 & chain B")

cmd.select ("Outward", "resi 907 & chain B", merge=1)

cmd.color ("red", "resi 908 & chain B")

cmd.select ("Inward", "resi 908 & chain B", merge=1)

cmd.color ("red", "resi 909 & chain B")

cmd.select ("Inward", "resi 909 & chain B", merge=1)

cmd.color ("blue", "resi 910 & chain B")

cmd.select ("Outward", "resi 910 & chain B", merge=1)

cmd.color ("red", "resi 911 & chain B")

cmd.select ("Inward", "resi 911 & chain B", merge=1)

cmd.color ("blue", "resi 912 & chain B")

cmd.select ("Outward", "resi 912 & chain B", merge=1)

cmd.color ("red", "resi 913 & chain B")

cmd.select ("Inward", "resi 913 & chain B", merge=1)

cmd.color ("blue", "resi 914 & chain B")

cmd.select ("Outward", "resi 914 & chain B", merge=1)

cmd.color ("red", "resi 915 & chain B")

cmd.select ("Inward", "resi 915 & chain B", merge=1)

cmd.color ("red", "resi 928 & chain B")

cmd.select ("Inward", "resi 928 & chain B", merge=1)

cmd.color ("blue", "resi 929 & chain B")

cmd.select ("Outward", "resi 929 & chain B", merge=1)

cmd.color ("red", "resi 930 & chain B")

cmd.select ("Inward", "resi 930 & chain B", merge=1)

cmd.color ("blue", "resi 931 & chain B")

cmd.select ("Outward", "resi 931 & chain B", merge=1)

cmd.color ("red", "resi 932 & chain B")

cmd.select ("Inward", "resi 932 & chain B", merge=1)

cmd.color ("blue", "resi 933 & chain B")

cmd.select ("Outward", "resi 933 & chain B", merge=1)

cmd.color ("red", "resi 934 & chain B")

cmd.select ("Inward", "resi 934 & chain B", merge=1)

cmd.color ("blue", "resi 935 & chain B")

cmd.select ("Outward", "resi 935 & chain B", merge=1)

cmd.color ("red", "resi 936 & chain B")

cmd.select ("Inward", "resi 936 & chain B", merge=1)

cmd.color ("blue", "resi 937 & chain B")

cmd.select ("Outward", "resi 937 & chain B", merge=1)

cmd.color ("red", "resi 938 & chain B")

cmd.select ("Inward", "resi 938 & chain B", merge=1)

cmd.color ("blue", "resi 939 & chain B")

cmd.select ("Outward", "resi 939 & chain B", merge=1)

cmd.color ("red", "resi 940 & chain B")

cmd.select ("Inward", "resi 940 & chain B", merge=1)

cmd.color ("blue", "resi 941 & chain B")

cmd.select ("Outward", "resi 941 & chain B", merge=1)

cmd.load_cgo( [9.0, 53.22014,66.86913,9.619, 53.22014, 66.86913, 9.619, 1, 1,1,0,0,0,1], "axis" )
