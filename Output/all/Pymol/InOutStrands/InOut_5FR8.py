from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FR8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand7", "resi 362+363+364+365+366+305+367+306+307+368+308+369+309+247+370+248+525+310+527+523+526+524+529+528+249+371+530+531+250+311+522+532+372+312+533+251+596+594+252+534+198+598+199+595+597+373+313+201+200+593+599+592+535+600+536+253+314+601+374+602+603+164+254+202+591+203+537+604+605+315+165+375+166+255+637+639+316+635+204+638+256+636+538+640+641+633+376+205+634+167+168+691+257+317+632+693+690+258+692+206+207+169+377+318+170+697+695+694+696+498+171+259+208+209+172+319+260+497+320+173+261+174+496+545+495+546+547+548+549+550 & chain A ")


cmd.select("Astrand8", "resi 561+562+563+564+565+481+566+482+480+479+567+568+569+570+340+571+572+342+341+343+573+287+344+506+574+288+345+575+289+507+346+290+576+508+291+347+229+230+577+292+348+509+231+293+232+510+578+349+233+294+234+579+350+511+618+295+182+619+235+675+512+236+580+351+183+296+676+184+581+677+620+721+352+297+237+621+513+185+186+238+582+678+723+722+298+353+514+679+187+583+622+239+188+299+724+725+354+623+240+515+680+189+584+300+726+516+681+355+241+190+727+624+585+301+242+728+356+243+625+517+191+682+683+302+193+357+586+192+244+518+358+684+626+587+194+627+588 & chain A ")


cmd.select("Astrand16", "resi 404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")


cmd.select("Astrand17", "resi 424+425+426+427+428+429+430+431+432+433+434+435 & chain A ")


cmd.select("Astrand18", "resi 439+440+441+442+443+444+445+446+447+448+449+450+451 & chain A ")


cmd.select("Astrand19", "resi 456+457+458+459+460+461+462+463+464+465+466+467 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 362 & chain A")

cmd.select ("Outward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 363 & chain A")

cmd.select ("Outward", "resi 363 & chain A", merge=1)

cmd.color ("blue", "resi 364 & chain A")

cmd.select ("Outward", "resi 364 & chain A", merge=1)

cmd.color ("blue", "resi 365 & chain A")

cmd.select ("Outward", "resi 365 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("blue", "resi 305 & chain A")

cmd.select ("Outward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 367 & chain A")

cmd.select ("Outward", "resi 367 & chain A", merge=1)

cmd.color ("blue", "resi 306 & chain A")

cmd.select ("Outward", "resi 306 & chain A", merge=1)

cmd.color ("blue", "resi 307 & chain A")

cmd.select ("Outward", "resi 307 & chain A", merge=1)

cmd.color ("blue", "resi 368 & chain A")

cmd.select ("Outward", "resi 368 & chain A", merge=1)

cmd.color ("blue", "resi 308 & chain A")

cmd.select ("Outward", "resi 308 & chain A", merge=1)

cmd.color ("blue", "resi 369 & chain A")

cmd.select ("Outward", "resi 369 & chain A", merge=1)

cmd.color ("blue", "resi 309 & chain A")

cmd.select ("Outward", "resi 309 & chain A", merge=1)

cmd.color ("blue", "resi 247 & chain A")

cmd.select ("Outward", "resi 247 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

cmd.color ("blue", "resi 525 & chain A")

cmd.select ("Outward", "resi 525 & chain A", merge=1)

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

cmd.color ("blue", "resi 527 & chain A")

cmd.select ("Outward", "resi 527 & chain A", merge=1)

cmd.color ("blue", "resi 523 & chain A")

cmd.select ("Outward", "resi 523 & chain A", merge=1)

cmd.color ("blue", "resi 526 & chain A")

cmd.select ("Outward", "resi 526 & chain A", merge=1)

cmd.color ("blue", "resi 524 & chain A")

cmd.select ("Outward", "resi 524 & chain A", merge=1)

cmd.color ("blue", "resi 529 & chain A")

cmd.select ("Outward", "resi 529 & chain A", merge=1)

cmd.color ("blue", "resi 528 & chain A")

cmd.select ("Outward", "resi 528 & chain A", merge=1)

cmd.color ("blue", "resi 249 & chain A")

cmd.select ("Outward", "resi 249 & chain A", merge=1)

cmd.color ("blue", "resi 371 & chain A")

cmd.select ("Outward", "resi 371 & chain A", merge=1)

cmd.color ("blue", "resi 530 & chain A")

cmd.select ("Outward", "resi 530 & chain A", merge=1)

cmd.color ("blue", "resi 531 & chain A")

cmd.select ("Outward", "resi 531 & chain A", merge=1)

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

cmd.color ("blue", "resi 311 & chain A")

cmd.select ("Outward", "resi 311 & chain A", merge=1)

cmd.color ("blue", "resi 522 & chain A")

cmd.select ("Outward", "resi 522 & chain A", merge=1)

cmd.color ("blue", "resi 532 & chain A")

cmd.select ("Outward", "resi 532 & chain A", merge=1)

cmd.color ("blue", "resi 372 & chain A")

cmd.select ("Outward", "resi 372 & chain A", merge=1)

cmd.color ("blue", "resi 312 & chain A")

cmd.select ("Outward", "resi 312 & chain A", merge=1)

cmd.color ("blue", "resi 533 & chain A")

cmd.select ("Outward", "resi 533 & chain A", merge=1)

cmd.color ("blue", "resi 251 & chain A")

cmd.select ("Outward", "resi 251 & chain A", merge=1)

cmd.color ("blue", "resi 596 & chain A")

cmd.select ("Outward", "resi 596 & chain A", merge=1)

cmd.color ("blue", "resi 594 & chain A")

cmd.select ("Outward", "resi 594 & chain A", merge=1)

cmd.color ("blue", "resi 252 & chain A")

cmd.select ("Outward", "resi 252 & chain A", merge=1)

cmd.color ("blue", "resi 534 & chain A")

cmd.select ("Outward", "resi 534 & chain A", merge=1)

cmd.color ("blue", "resi 198 & chain A")

cmd.select ("Outward", "resi 198 & chain A", merge=1)

cmd.color ("blue", "resi 598 & chain A")

cmd.select ("Outward", "resi 598 & chain A", merge=1)

cmd.color ("blue", "resi 199 & chain A")

cmd.select ("Outward", "resi 199 & chain A", merge=1)

cmd.color ("blue", "resi 595 & chain A")

cmd.select ("Outward", "resi 595 & chain A", merge=1)

cmd.color ("blue", "resi 597 & chain A")

cmd.select ("Outward", "resi 597 & chain A", merge=1)

cmd.color ("blue", "resi 373 & chain A")

cmd.select ("Outward", "resi 373 & chain A", merge=1)

cmd.color ("blue", "resi 313 & chain A")

cmd.select ("Outward", "resi 313 & chain A", merge=1)

cmd.color ("blue", "resi 201 & chain A")

cmd.select ("Outward", "resi 201 & chain A", merge=1)

cmd.color ("blue", "resi 200 & chain A")

cmd.select ("Outward", "resi 200 & chain A", merge=1)

cmd.color ("blue", "resi 593 & chain A")

cmd.select ("Outward", "resi 593 & chain A", merge=1)

cmd.color ("blue", "resi 599 & chain A")

cmd.select ("Outward", "resi 599 & chain A", merge=1)

cmd.color ("blue", "resi 592 & chain A")

cmd.select ("Outward", "resi 592 & chain A", merge=1)

cmd.color ("blue", "resi 535 & chain A")

cmd.select ("Outward", "resi 535 & chain A", merge=1)

cmd.color ("blue", "resi 600 & chain A")

cmd.select ("Outward", "resi 600 & chain A", merge=1)

cmd.color ("blue", "resi 536 & chain A")

cmd.select ("Outward", "resi 536 & chain A", merge=1)

cmd.color ("blue", "resi 253 & chain A")

cmd.select ("Outward", "resi 253 & chain A", merge=1)

cmd.color ("blue", "resi 314 & chain A")

cmd.select ("Outward", "resi 314 & chain A", merge=1)

cmd.color ("blue", "resi 601 & chain A")

cmd.select ("Outward", "resi 601 & chain A", merge=1)

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("blue", "resi 602 & chain A")

cmd.select ("Outward", "resi 602 & chain A", merge=1)

cmd.color ("blue", "resi 603 & chain A")

cmd.select ("Outward", "resi 603 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

cmd.color ("blue", "resi 254 & chain A")

cmd.select ("Outward", "resi 254 & chain A", merge=1)

cmd.color ("blue", "resi 202 & chain A")

cmd.select ("Outward", "resi 202 & chain A", merge=1)

cmd.color ("blue", "resi 591 & chain A")

cmd.select ("Outward", "resi 591 & chain A", merge=1)

cmd.color ("blue", "resi 203 & chain A")

cmd.select ("Outward", "resi 203 & chain A", merge=1)

cmd.color ("blue", "resi 537 & chain A")

cmd.select ("Outward", "resi 537 & chain A", merge=1)

cmd.color ("blue", "resi 604 & chain A")

cmd.select ("Outward", "resi 604 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("blue", "resi 315 & chain A")

cmd.select ("Outward", "resi 315 & chain A", merge=1)

cmd.color ("blue", "resi 165 & chain A")

cmd.select ("Outward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 375 & chain A")

cmd.select ("Outward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 166 & chain A")

cmd.select ("Outward", "resi 166 & chain A", merge=1)

cmd.color ("blue", "resi 255 & chain A")

cmd.select ("Outward", "resi 255 & chain A", merge=1)

cmd.color ("blue", "resi 637 & chain A")

cmd.select ("Outward", "resi 637 & chain A", merge=1)

cmd.color ("blue", "resi 639 & chain A")

cmd.select ("Outward", "resi 639 & chain A", merge=1)

cmd.color ("blue", "resi 316 & chain A")

cmd.select ("Outward", "resi 316 & chain A", merge=1)

cmd.color ("blue", "resi 635 & chain A")

cmd.select ("Outward", "resi 635 & chain A", merge=1)

cmd.color ("blue", "resi 204 & chain A")

cmd.select ("Outward", "resi 204 & chain A", merge=1)

cmd.color ("blue", "resi 638 & chain A")

cmd.select ("Outward", "resi 638 & chain A", merge=1)

cmd.color ("blue", "resi 256 & chain A")

cmd.select ("Outward", "resi 256 & chain A", merge=1)

cmd.color ("blue", "resi 636 & chain A")

cmd.select ("Outward", "resi 636 & chain A", merge=1)

cmd.color ("blue", "resi 538 & chain A")

cmd.select ("Outward", "resi 538 & chain A", merge=1)

cmd.color ("blue", "resi 640 & chain A")

cmd.select ("Outward", "resi 640 & chain A", merge=1)

cmd.color ("blue", "resi 641 & chain A")

cmd.select ("Outward", "resi 641 & chain A", merge=1)

cmd.color ("blue", "resi 633 & chain A")

cmd.select ("Outward", "resi 633 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 205 & chain A")

cmd.select ("Outward", "resi 205 & chain A", merge=1)

cmd.color ("blue", "resi 634 & chain A")

cmd.select ("Outward", "resi 634 & chain A", merge=1)

cmd.color ("blue", "resi 167 & chain A")

cmd.select ("Outward", "resi 167 & chain A", merge=1)

cmd.color ("blue", "resi 168 & chain A")

cmd.select ("Outward", "resi 168 & chain A", merge=1)

cmd.color ("blue", "resi 691 & chain A")

cmd.select ("Outward", "resi 691 & chain A", merge=1)

cmd.color ("blue", "resi 257 & chain A")

cmd.select ("Outward", "resi 257 & chain A", merge=1)

cmd.color ("blue", "resi 317 & chain A")

cmd.select ("Outward", "resi 317 & chain A", merge=1)

cmd.color ("blue", "resi 632 & chain A")

cmd.select ("Outward", "resi 632 & chain A", merge=1)

cmd.color ("blue", "resi 693 & chain A")

cmd.select ("Outward", "resi 693 & chain A", merge=1)

cmd.color ("blue", "resi 690 & chain A")

cmd.select ("Outward", "resi 690 & chain A", merge=1)

cmd.color ("blue", "resi 258 & chain A")

cmd.select ("Outward", "resi 258 & chain A", merge=1)

cmd.color ("blue", "resi 692 & chain A")

cmd.select ("Outward", "resi 692 & chain A", merge=1)

cmd.color ("blue", "resi 206 & chain A")

cmd.select ("Outward", "resi 206 & chain A", merge=1)

cmd.color ("blue", "resi 207 & chain A")

cmd.select ("Outward", "resi 207 & chain A", merge=1)

cmd.color ("blue", "resi 169 & chain A")

cmd.select ("Outward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 377 & chain A")

cmd.select ("Outward", "resi 377 & chain A", merge=1)

cmd.color ("blue", "resi 318 & chain A")

cmd.select ("Outward", "resi 318 & chain A", merge=1)

cmd.color ("blue", "resi 170 & chain A")

cmd.select ("Outward", "resi 170 & chain A", merge=1)

cmd.color ("blue", "resi 697 & chain A")

cmd.select ("Outward", "resi 697 & chain A", merge=1)

cmd.color ("blue", "resi 695 & chain A")

cmd.select ("Outward", "resi 695 & chain A", merge=1)

cmd.color ("blue", "resi 694 & chain A")

cmd.select ("Outward", "resi 694 & chain A", merge=1)

cmd.color ("blue", "resi 696 & chain A")

cmd.select ("Outward", "resi 696 & chain A", merge=1)

cmd.color ("blue", "resi 498 & chain A")

cmd.select ("Outward", "resi 498 & chain A", merge=1)

cmd.color ("blue", "resi 171 & chain A")

cmd.select ("Outward", "resi 171 & chain A", merge=1)

cmd.color ("blue", "resi 259 & chain A")

cmd.select ("Outward", "resi 259 & chain A", merge=1)

cmd.color ("blue", "resi 208 & chain A")

cmd.select ("Outward", "resi 208 & chain A", merge=1)

cmd.color ("blue", "resi 209 & chain A")

cmd.select ("Outward", "resi 209 & chain A", merge=1)

cmd.color ("blue", "resi 172 & chain A")

cmd.select ("Outward", "resi 172 & chain A", merge=1)

cmd.color ("blue", "resi 319 & chain A")

cmd.select ("Outward", "resi 319 & chain A", merge=1)

cmd.color ("blue", "resi 260 & chain A")

cmd.select ("Outward", "resi 260 & chain A", merge=1)

cmd.color ("blue", "resi 497 & chain A")

cmd.select ("Outward", "resi 497 & chain A", merge=1)

cmd.color ("blue", "resi 320 & chain A")

cmd.select ("Outward", "resi 320 & chain A", merge=1)

cmd.color ("blue", "resi 173 & chain A")

cmd.select ("Outward", "resi 173 & chain A", merge=1)

cmd.color ("blue", "resi 261 & chain A")

cmd.select ("Outward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 174 & chain A")

cmd.select ("Outward", "resi 174 & chain A", merge=1)

cmd.color ("blue", "resi 496 & chain A")

cmd.select ("Outward", "resi 496 & chain A", merge=1)

cmd.color ("blue", "resi 545 & chain A")

cmd.select ("Outward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

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

cmd.color ("blue", "resi 481 & chain A")

cmd.select ("Outward", "resi 481 & chain A", merge=1)

cmd.color ("blue", "resi 566 & chain A")

cmd.select ("Outward", "resi 566 & chain A", merge=1)

cmd.color ("blue", "resi 482 & chain A")

cmd.select ("Outward", "resi 482 & chain A", merge=1)

cmd.color ("blue", "resi 480 & chain A")

cmd.select ("Outward", "resi 480 & chain A", merge=1)

cmd.color ("blue", "resi 479 & chain A")

cmd.select ("Outward", "resi 479 & chain A", merge=1)

cmd.color ("blue", "resi 567 & chain A")

cmd.select ("Outward", "resi 567 & chain A", merge=1)

cmd.color ("blue", "resi 568 & chain A")

cmd.select ("Outward", "resi 568 & chain A", merge=1)

cmd.color ("blue", "resi 569 & chain A")

cmd.select ("Outward", "resi 569 & chain A", merge=1)

cmd.color ("blue", "resi 570 & chain A")

cmd.select ("Outward", "resi 570 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 571 & chain A")

cmd.select ("Outward", "resi 571 & chain A", merge=1)

cmd.color ("blue", "resi 572 & chain A")

cmd.select ("Outward", "resi 572 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 343 & chain A")

cmd.select ("Outward", "resi 343 & chain A", merge=1)

cmd.color ("blue", "resi 573 & chain A")

cmd.select ("Outward", "resi 573 & chain A", merge=1)

cmd.color ("blue", "resi 287 & chain A")

cmd.select ("Outward", "resi 287 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("blue", "resi 506 & chain A")

cmd.select ("Outward", "resi 506 & chain A", merge=1)

cmd.color ("blue", "resi 574 & chain A")

cmd.select ("Outward", "resi 574 & chain A", merge=1)

cmd.color ("blue", "resi 288 & chain A")

cmd.select ("Outward", "resi 288 & chain A", merge=1)

cmd.color ("blue", "resi 345 & chain A")

cmd.select ("Outward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 575 & chain A")

cmd.select ("Outward", "resi 575 & chain A", merge=1)

cmd.color ("blue", "resi 289 & chain A")

cmd.select ("Outward", "resi 289 & chain A", merge=1)

cmd.color ("blue", "resi 507 & chain A")

cmd.select ("Outward", "resi 507 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("blue", "resi 290 & chain A")

cmd.select ("Outward", "resi 290 & chain A", merge=1)

cmd.color ("blue", "resi 576 & chain A")

cmd.select ("Outward", "resi 576 & chain A", merge=1)

cmd.color ("blue", "resi 508 & chain A")

cmd.select ("Outward", "resi 508 & chain A", merge=1)

cmd.color ("blue", "resi 291 & chain A")

cmd.select ("Outward", "resi 291 & chain A", merge=1)

cmd.color ("blue", "resi 347 & chain A")

cmd.select ("Outward", "resi 347 & chain A", merge=1)

cmd.color ("blue", "resi 229 & chain A")

cmd.select ("Outward", "resi 229 & chain A", merge=1)

cmd.color ("blue", "resi 230 & chain A")

cmd.select ("Outward", "resi 230 & chain A", merge=1)

cmd.color ("blue", "resi 577 & chain A")

cmd.select ("Outward", "resi 577 & chain A", merge=1)

cmd.color ("blue", "resi 292 & chain A")

cmd.select ("Outward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 348 & chain A")

cmd.select ("Outward", "resi 348 & chain A", merge=1)

cmd.color ("blue", "resi 509 & chain A")

cmd.select ("Outward", "resi 509 & chain A", merge=1)

cmd.color ("blue", "resi 231 & chain A")

cmd.select ("Outward", "resi 231 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 232 & chain A")

cmd.select ("Outward", "resi 232 & chain A", merge=1)

cmd.color ("blue", "resi 510 & chain A")

cmd.select ("Outward", "resi 510 & chain A", merge=1)

cmd.color ("blue", "resi 578 & chain A")

cmd.select ("Outward", "resi 578 & chain A", merge=1)

cmd.color ("blue", "resi 349 & chain A")

cmd.select ("Outward", "resi 349 & chain A", merge=1)

cmd.color ("blue", "resi 233 & chain A")

cmd.select ("Outward", "resi 233 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 234 & chain A")

cmd.select ("Outward", "resi 234 & chain A", merge=1)

cmd.color ("blue", "resi 579 & chain A")

cmd.select ("Outward", "resi 579 & chain A", merge=1)

cmd.color ("blue", "resi 350 & chain A")

cmd.select ("Outward", "resi 350 & chain A", merge=1)

cmd.color ("blue", "resi 511 & chain A")

cmd.select ("Outward", "resi 511 & chain A", merge=1)

cmd.color ("blue", "resi 618 & chain A")

cmd.select ("Outward", "resi 618 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("blue", "resi 182 & chain A")

cmd.select ("Outward", "resi 182 & chain A", merge=1)

cmd.color ("blue", "resi 619 & chain A")

cmd.select ("Outward", "resi 619 & chain A", merge=1)

cmd.color ("blue", "resi 235 & chain A")

cmd.select ("Outward", "resi 235 & chain A", merge=1)

cmd.color ("blue", "resi 675 & chain A")

cmd.select ("Outward", "resi 675 & chain A", merge=1)

cmd.color ("blue", "resi 512 & chain A")

cmd.select ("Outward", "resi 512 & chain A", merge=1)

cmd.color ("blue", "resi 236 & chain A")

cmd.select ("Outward", "resi 236 & chain A", merge=1)

cmd.color ("blue", "resi 580 & chain A")

cmd.select ("Outward", "resi 580 & chain A", merge=1)

cmd.color ("blue", "resi 351 & chain A")

cmd.select ("Outward", "resi 351 & chain A", merge=1)

cmd.color ("blue", "resi 183 & chain A")

cmd.select ("Outward", "resi 183 & chain A", merge=1)

cmd.color ("blue", "resi 296 & chain A")

cmd.select ("Outward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 676 & chain A")

cmd.select ("Outward", "resi 676 & chain A", merge=1)

cmd.color ("blue", "resi 184 & chain A")

cmd.select ("Outward", "resi 184 & chain A", merge=1)

cmd.color ("blue", "resi 581 & chain A")

cmd.select ("Outward", "resi 581 & chain A", merge=1)

cmd.color ("blue", "resi 677 & chain A")

cmd.select ("Outward", "resi 677 & chain A", merge=1)

cmd.color ("blue", "resi 620 & chain A")

cmd.select ("Outward", "resi 620 & chain A", merge=1)

cmd.color ("blue", "resi 721 & chain A")

cmd.select ("Outward", "resi 721 & chain A", merge=1)

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("blue", "resi 237 & chain A")

cmd.select ("Outward", "resi 237 & chain A", merge=1)

cmd.color ("blue", "resi 621 & chain A")

cmd.select ("Outward", "resi 621 & chain A", merge=1)

cmd.color ("blue", "resi 513 & chain A")

cmd.select ("Outward", "resi 513 & chain A", merge=1)

cmd.color ("blue", "resi 185 & chain A")

cmd.select ("Outward", "resi 185 & chain A", merge=1)

cmd.color ("blue", "resi 186 & chain A")

cmd.select ("Outward", "resi 186 & chain A", merge=1)

cmd.color ("blue", "resi 238 & chain A")

cmd.select ("Outward", "resi 238 & chain A", merge=1)

cmd.color ("blue", "resi 582 & chain A")

cmd.select ("Outward", "resi 582 & chain A", merge=1)

cmd.color ("blue", "resi 678 & chain A")

cmd.select ("Outward", "resi 678 & chain A", merge=1)

cmd.color ("blue", "resi 723 & chain A")

cmd.select ("Outward", "resi 723 & chain A", merge=1)

cmd.color ("blue", "resi 722 & chain A")

cmd.select ("Outward", "resi 722 & chain A", merge=1)

cmd.color ("blue", "resi 298 & chain A")

cmd.select ("Outward", "resi 298 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("blue", "resi 514 & chain A")

cmd.select ("Outward", "resi 514 & chain A", merge=1)

cmd.color ("blue", "resi 679 & chain A")

cmd.select ("Outward", "resi 679 & chain A", merge=1)

cmd.color ("blue", "resi 187 & chain A")

cmd.select ("Outward", "resi 187 & chain A", merge=1)

cmd.color ("blue", "resi 583 & chain A")

cmd.select ("Outward", "resi 583 & chain A", merge=1)

cmd.color ("blue", "resi 622 & chain A")

cmd.select ("Outward", "resi 622 & chain A", merge=1)

cmd.color ("blue", "resi 239 & chain A")

cmd.select ("Outward", "resi 239 & chain A", merge=1)

cmd.color ("blue", "resi 188 & chain A")

cmd.select ("Outward", "resi 188 & chain A", merge=1)

cmd.color ("blue", "resi 299 & chain A")

cmd.select ("Outward", "resi 299 & chain A", merge=1)

cmd.color ("blue", "resi 724 & chain A")

cmd.select ("Outward", "resi 724 & chain A", merge=1)

cmd.color ("blue", "resi 725 & chain A")

cmd.select ("Outward", "resi 725 & chain A", merge=1)

cmd.color ("blue", "resi 354 & chain A")

cmd.select ("Outward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 623 & chain A")

cmd.select ("Outward", "resi 623 & chain A", merge=1)

cmd.color ("blue", "resi 240 & chain A")

cmd.select ("Outward", "resi 240 & chain A", merge=1)

cmd.color ("blue", "resi 515 & chain A")

cmd.select ("Outward", "resi 515 & chain A", merge=1)

cmd.color ("blue", "resi 680 & chain A")

cmd.select ("Outward", "resi 680 & chain A", merge=1)

cmd.color ("blue", "resi 189 & chain A")

cmd.select ("Outward", "resi 189 & chain A", merge=1)

cmd.color ("blue", "resi 584 & chain A")

cmd.select ("Outward", "resi 584 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.color ("blue", "resi 726 & chain A")

cmd.select ("Outward", "resi 726 & chain A", merge=1)

cmd.color ("blue", "resi 516 & chain A")

cmd.select ("Outward", "resi 516 & chain A", merge=1)

cmd.color ("blue", "resi 681 & chain A")

cmd.select ("Outward", "resi 681 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 241 & chain A")

cmd.select ("Outward", "resi 241 & chain A", merge=1)

cmd.color ("blue", "resi 190 & chain A")

cmd.select ("Outward", "resi 190 & chain A", merge=1)

cmd.color ("blue", "resi 727 & chain A")

cmd.select ("Outward", "resi 727 & chain A", merge=1)

cmd.color ("blue", "resi 624 & chain A")

cmd.select ("Outward", "resi 624 & chain A", merge=1)

cmd.color ("blue", "resi 585 & chain A")

cmd.select ("Outward", "resi 585 & chain A", merge=1)

cmd.color ("blue", "resi 301 & chain A")

cmd.select ("Outward", "resi 301 & chain A", merge=1)

cmd.color ("blue", "resi 242 & chain A")

cmd.select ("Outward", "resi 242 & chain A", merge=1)

cmd.color ("blue", "resi 728 & chain A")

cmd.select ("Outward", "resi 728 & chain A", merge=1)

cmd.color ("blue", "resi 356 & chain A")

cmd.select ("Outward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 243 & chain A")

cmd.select ("Outward", "resi 243 & chain A", merge=1)

cmd.color ("blue", "resi 625 & chain A")

cmd.select ("Outward", "resi 625 & chain A", merge=1)

cmd.color ("blue", "resi 517 & chain A")

cmd.select ("Outward", "resi 517 & chain A", merge=1)

cmd.color ("blue", "resi 191 & chain A")

cmd.select ("Outward", "resi 191 & chain A", merge=1)

cmd.color ("blue", "resi 682 & chain A")

cmd.select ("Outward", "resi 682 & chain A", merge=1)

cmd.color ("blue", "resi 683 & chain A")

cmd.select ("Outward", "resi 683 & chain A", merge=1)

cmd.color ("blue", "resi 302 & chain A")

cmd.select ("Outward", "resi 302 & chain A", merge=1)

cmd.color ("blue", "resi 193 & chain A")

cmd.select ("Outward", "resi 193 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("blue", "resi 586 & chain A")

cmd.select ("Outward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 192 & chain A")

cmd.select ("Outward", "resi 192 & chain A", merge=1)

cmd.color ("blue", "resi 244 & chain A")

cmd.select ("Outward", "resi 244 & chain A", merge=1)

cmd.color ("blue", "resi 518 & chain A")

cmd.select ("Outward", "resi 518 & chain A", merge=1)

cmd.color ("blue", "resi 358 & chain A")

cmd.select ("Outward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 684 & chain A")

cmd.select ("Outward", "resi 684 & chain A", merge=1)

cmd.color ("blue", "resi 626 & chain A")

cmd.select ("Outward", "resi 626 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

cmd.color ("blue", "resi 194 & chain A")

cmd.select ("Outward", "resi 194 & chain A", merge=1)

cmd.color ("blue", "resi 627 & chain A")

cmd.select ("Outward", "resi 627 & chain A", merge=1)

cmd.color ("blue", "resi 588 & chain A")

cmd.select ("Outward", "resi 588 & chain A", merge=1)

cmd.color ("blue", "resi 404 & chain A")

cmd.select ("Outward", "resi 404 & chain A", merge=1)

cmd.color ("blue", "resi 405 & chain A")

cmd.select ("Outward", "resi 405 & chain A", merge=1)

cmd.color ("blue", "resi 406 & chain A")

cmd.select ("Outward", "resi 406 & chain A", merge=1)

cmd.color ("blue", "resi 407 & chain A")

cmd.select ("Outward", "resi 407 & chain A", merge=1)

cmd.color ("blue", "resi 408 & chain A")

cmd.select ("Outward", "resi 408 & chain A", merge=1)

cmd.color ("blue", "resi 409 & chain A")

cmd.select ("Outward", "resi 409 & chain A", merge=1)

cmd.color ("blue", "resi 410 & chain A")

cmd.select ("Outward", "resi 410 & chain A", merge=1)

cmd.color ("blue", "resi 411 & chain A")

cmd.select ("Outward", "resi 411 & chain A", merge=1)

cmd.color ("blue", "resi 412 & chain A")

cmd.select ("Outward", "resi 412 & chain A", merge=1)

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

cmd.color ("blue", "resi 424 & chain A")

cmd.select ("Outward", "resi 424 & chain A", merge=1)

cmd.color ("blue", "resi 425 & chain A")

cmd.select ("Outward", "resi 425 & chain A", merge=1)

cmd.color ("blue", "resi 426 & chain A")

cmd.select ("Outward", "resi 426 & chain A", merge=1)

cmd.color ("blue", "resi 427 & chain A")

cmd.select ("Outward", "resi 427 & chain A", merge=1)

cmd.color ("blue", "resi 428 & chain A")

cmd.select ("Outward", "resi 428 & chain A", merge=1)

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

cmd.color ("blue", "resi 439 & chain A")

cmd.select ("Outward", "resi 439 & chain A", merge=1)

cmd.color ("blue", "resi 440 & chain A")

cmd.select ("Outward", "resi 440 & chain A", merge=1)

cmd.color ("blue", "resi 441 & chain A")

cmd.select ("Outward", "resi 441 & chain A", merge=1)

cmd.color ("blue", "resi 442 & chain A")

cmd.select ("Outward", "resi 442 & chain A", merge=1)

cmd.color ("blue", "resi 443 & chain A")

cmd.select ("Outward", "resi 443 & chain A", merge=1)

cmd.color ("blue", "resi 444 & chain A")

cmd.select ("Outward", "resi 444 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("blue", "resi 446 & chain A")

cmd.select ("Outward", "resi 446 & chain A", merge=1)

cmd.color ("blue", "resi 447 & chain A")

cmd.select ("Outward", "resi 447 & chain A", merge=1)

cmd.color ("blue", "resi 448 & chain A")

cmd.select ("Outward", "resi 448 & chain A", merge=1)

cmd.color ("blue", "resi 449 & chain A")

cmd.select ("Outward", "resi 449 & chain A", merge=1)

cmd.color ("blue", "resi 450 & chain A")

cmd.select ("Outward", "resi 450 & chain A", merge=1)

cmd.color ("blue", "resi 451 & chain A")

cmd.select ("Outward", "resi 451 & chain A", merge=1)

cmd.color ("blue", "resi 456 & chain A")

cmd.select ("Outward", "resi 456 & chain A", merge=1)

cmd.color ("blue", "resi 457 & chain A")

cmd.select ("Outward", "resi 457 & chain A", merge=1)

cmd.color ("blue", "resi 458 & chain A")

cmd.select ("Outward", "resi 458 & chain A", merge=1)

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

cmd.load_cgo( [9.0, -5.295667,-63.8515,71.80817, -24.40233, -27.156836, 51.556, 1, 1,1,0,0,0,1], "axis" )
