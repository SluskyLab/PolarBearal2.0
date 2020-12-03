from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Q35.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand21", "resi 230+231+232+233+234+235+236 & chain A ")


cmd.select("Astrand62", "resi 726+727+728+729+730+731+732+733+734+735 & chain A ")


cmd.select("Astrand23", "resi 255+256+257+258+259+260+261+262+263+264 & chain A ")


cmd.select("Astrand22", "resi 242+243+244+245+246+247+248+249+250+251+252 & chain A ")


cmd.select("Astrand61", "resi 714+715+716+717+718+719+720+721+722+723 & chain A ")


cmd.select("Astrand24", "resi 269+270+271+272+273+274+275+276+277+278+279+280 & chain A ")


cmd.select("Astrand28", "resi 310+311+312+313+314+315+316+317+318+319+320+321 & chain A ")


cmd.select("Astrand29", "resi 326+327+328+329+330+331+332+333+334+335+336 & chain A ")


cmd.select("Astrand54", "resi 637+638+639+640+641+642+643+644+645+646+647 & chain A ")


cmd.select("Astrand32", "resi 354+355+356+357+358+359+360+361+362+363+364+365 & chain A ")


cmd.select("Astrand33", "resi 368+369+370+371+372+373+374+375+376+377+378+379 & chain A ")


cmd.select("Astrand35", "resi 387+388+389+390+391+392+393+394+395+396+397+398+399+400 & chain A ")


cmd.select("Astrand36", "resi 406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")


cmd.select("Astrand46", "resi 555+556+557+558+559+560+561+562+563+564+565+566+567+568 & chain A ")


cmd.select("Astrand37", "resi 424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442 & chain A ")


cmd.select("Astrand41", "resi 505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520 & chain A ")


cmd.select("Astrand39", "resi 470+471+472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495+496+497 & chain A ")


cmd.select("Astrand38", "resi 445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461 & chain A ")


cmd.select("Astrand48", "resi 575+576+577+578+579+580+581+582+583+584+585+586+587+588+589 & chain A ")


cmd.select("Astrand51", "resi 603+604+605+606+607+608+609+610+611+612+613+614+615+616+617 & chain A ")


cmd.select("Astrand52", "resi 620+621+622+623+624+625+626+627+628+629 & chain A ")


cmd.select("Astrand55", "resi 650+651+652+653+654+655+656+657+658+659 & chain A ")


cmd.select("Astrand58", "resi 682+683+684+685+686+687+688+689+690+691+692+693 & chain A ")


cmd.select("Astrand59", "resi 697+698+699+700+701+702+703+704+705+706 & chain A ")


cmd.select("Astrand25", "resi 284+285+286+287+288+289+290+291+292+293+294+295 & chain A ")


cmd.select("Astrand64", "resi 745+746+747+748+749+750+751+752+753+754+755+756+757+758+759 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 230 & chain A")

cmd.select ("Inward", "resi 230 & chain A", merge=1)

cmd.color ("blue", "resi 231 & chain A")

cmd.select ("Outward", "resi 231 & chain A", merge=1)

cmd.color ("red", "resi 232 & chain A")

cmd.select ("Inward", "resi 232 & chain A", merge=1)

cmd.color ("blue", "resi 233 & chain A")

cmd.select ("Outward", "resi 233 & chain A", merge=1)

cmd.color ("red", "resi 234 & chain A")

cmd.select ("Inward", "resi 234 & chain A", merge=1)

cmd.color ("blue", "resi 235 & chain A")

cmd.select ("Outward", "resi 235 & chain A", merge=1)

cmd.color ("red", "resi 236 & chain A")

cmd.select ("Inward", "resi 236 & chain A", merge=1)

cmd.color ("blue", "resi 726 & chain A")

cmd.select ("Outward", "resi 726 & chain A", merge=1)

cmd.color ("red", "resi 727 & chain A")

cmd.select ("Inward", "resi 727 & chain A", merge=1)

cmd.color ("blue", "resi 728 & chain A")

cmd.select ("Outward", "resi 728 & chain A", merge=1)

cmd.color ("red", "resi 729 & chain A")

cmd.select ("Inward", "resi 729 & chain A", merge=1)

cmd.color ("blue", "resi 730 & chain A")

cmd.select ("Outward", "resi 730 & chain A", merge=1)

cmd.color ("red", "resi 731 & chain A")

cmd.select ("Inward", "resi 731 & chain A", merge=1)

cmd.color ("blue", "resi 732 & chain A")

cmd.select ("Outward", "resi 732 & chain A", merge=1)

cmd.color ("red", "resi 733 & chain A")

cmd.select ("Inward", "resi 733 & chain A", merge=1)

cmd.color ("blue", "resi 734 & chain A")

cmd.select ("Outward", "resi 734 & chain A", merge=1)

cmd.color ("red", "resi 735 & chain A")

cmd.select ("Inward", "resi 735 & chain A", merge=1)

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

cmd.color ("red", "resi 264 & chain A")

cmd.select ("Inward", "resi 264 & chain A", merge=1)

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

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

cmd.color ("red", "resi 249 & chain A")

cmd.select ("Inward", "resi 249 & chain A", merge=1)

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

cmd.color ("red", "resi 251 & chain A")

cmd.select ("Inward", "resi 251 & chain A", merge=1)

cmd.color ("red", "resi 252 & chain A")

cmd.select ("Inward", "resi 252 & chain A", merge=1)

cmd.color ("red", "resi 714 & chain A")

cmd.select ("Inward", "resi 714 & chain A", merge=1)

cmd.color ("blue", "resi 715 & chain A")

cmd.select ("Outward", "resi 715 & chain A", merge=1)

cmd.color ("red", "resi 716 & chain A")

cmd.select ("Inward", "resi 716 & chain A", merge=1)

cmd.color ("blue", "resi 717 & chain A")

cmd.select ("Outward", "resi 717 & chain A", merge=1)

cmd.color ("red", "resi 718 & chain A")

cmd.select ("Inward", "resi 718 & chain A", merge=1)

cmd.color ("blue", "resi 719 & chain A")

cmd.select ("Outward", "resi 719 & chain A", merge=1)

cmd.color ("red", "resi 720 & chain A")

cmd.select ("Inward", "resi 720 & chain A", merge=1)

cmd.color ("blue", "resi 721 & chain A")

cmd.select ("Outward", "resi 721 & chain A", merge=1)

cmd.color ("red", "resi 722 & chain A")

cmd.select ("Inward", "resi 722 & chain A", merge=1)

cmd.color ("blue", "resi 723 & chain A")

cmd.select ("Outward", "resi 723 & chain A", merge=1)

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

cmd.color ("red", "resi 276 & chain A")

cmd.select ("Inward", "resi 276 & chain A", merge=1)

cmd.color ("blue", "resi 277 & chain A")

cmd.select ("Outward", "resi 277 & chain A", merge=1)

cmd.color ("blue", "resi 278 & chain A")

cmd.select ("Outward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 279 & chain A")

cmd.select ("Outward", "resi 279 & chain A", merge=1)

cmd.color ("red", "resi 280 & chain A")

cmd.select ("Inward", "resi 280 & chain A", merge=1)

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

cmd.color ("red", "resi 321 & chain A")

cmd.select ("Inward", "resi 321 & chain A", merge=1)

cmd.color ("red", "resi 326 & chain A")

cmd.select ("Inward", "resi 326 & chain A", merge=1)

cmd.color ("blue", "resi 327 & chain A")

cmd.select ("Outward", "resi 327 & chain A", merge=1)

cmd.color ("red", "resi 328 & chain A")

cmd.select ("Inward", "resi 328 & chain A", merge=1)

cmd.color ("blue", "resi 329 & chain A")

cmd.select ("Outward", "resi 329 & chain A", merge=1)

cmd.color ("red", "resi 330 & chain A")

cmd.select ("Inward", "resi 330 & chain A", merge=1)

cmd.color ("blue", "resi 331 & chain A")

cmd.select ("Outward", "resi 331 & chain A", merge=1)

cmd.color ("red", "resi 332 & chain A")

cmd.select ("Inward", "resi 332 & chain A", merge=1)

cmd.color ("blue", "resi 333 & chain A")

cmd.select ("Outward", "resi 333 & chain A", merge=1)

cmd.color ("red", "resi 334 & chain A")

cmd.select ("Inward", "resi 334 & chain A", merge=1)

cmd.color ("blue", "resi 335 & chain A")

cmd.select ("Outward", "resi 335 & chain A", merge=1)

cmd.color ("blue", "resi 336 & chain A")

cmd.select ("Outward", "resi 336 & chain A", merge=1)

cmd.color ("red", "resi 637 & chain A")

cmd.select ("Inward", "resi 637 & chain A", merge=1)

cmd.color ("blue", "resi 638 & chain A")

cmd.select ("Outward", "resi 638 & chain A", merge=1)

cmd.color ("red", "resi 639 & chain A")

cmd.select ("Inward", "resi 639 & chain A", merge=1)

cmd.color ("blue", "resi 640 & chain A")

cmd.select ("Outward", "resi 640 & chain A", merge=1)

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

cmd.color ("blue", "resi 647 & chain A")

cmd.select ("Outward", "resi 647 & chain A", merge=1)

cmd.color ("red", "resi 354 & chain A")

cmd.select ("Inward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 356 & chain A")

cmd.select ("Outward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("red", "resi 358 & chain A")

cmd.select ("Inward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("red", "resi 360 & chain A")

cmd.select ("Inward", "resi 360 & chain A", merge=1)

cmd.color ("blue", "resi 361 & chain A")

cmd.select ("Outward", "resi 361 & chain A", merge=1)

cmd.color ("red", "resi 362 & chain A")

cmd.select ("Inward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 363 & chain A")

cmd.select ("Outward", "resi 363 & chain A", merge=1)

cmd.color ("red", "resi 364 & chain A")

cmd.select ("Inward", "resi 364 & chain A", merge=1)

cmd.color ("blue", "resi 365 & chain A")

cmd.select ("Outward", "resi 365 & chain A", merge=1)

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

cmd.color ("blue", "resi 387 & chain A")

cmd.select ("Outward", "resi 387 & chain A", merge=1)

cmd.color ("red", "resi 388 & chain A")

cmd.select ("Inward", "resi 388 & chain A", merge=1)

cmd.color ("blue", "resi 389 & chain A")

cmd.select ("Outward", "resi 389 & chain A", merge=1)

cmd.color ("red", "resi 390 & chain A")

cmd.select ("Inward", "resi 390 & chain A", merge=1)

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

cmd.color ("red", "resi 399 & chain A")

cmd.select ("Inward", "resi 399 & chain A", merge=1)

cmd.color ("blue", "resi 400 & chain A")

cmd.select ("Outward", "resi 400 & chain A", merge=1)

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

cmd.color ("blue", "resi 416 & chain A")

cmd.select ("Outward", "resi 416 & chain A", merge=1)

cmd.color ("red", "resi 417 & chain A")

cmd.select ("Inward", "resi 417 & chain A", merge=1)

cmd.color ("blue", "resi 418 & chain A")

cmd.select ("Outward", "resi 418 & chain A", merge=1)

cmd.color ("red", "resi 419 & chain A")

cmd.select ("Inward", "resi 419 & chain A", merge=1)

cmd.color ("blue", "resi 555 & chain A")

cmd.select ("Outward", "resi 555 & chain A", merge=1)

cmd.color ("blue", "resi 556 & chain A")

cmd.select ("Outward", "resi 556 & chain A", merge=1)

cmd.color ("red", "resi 557 & chain A")

cmd.select ("Inward", "resi 557 & chain A", merge=1)

cmd.color ("blue", "resi 558 & chain A")

cmd.select ("Outward", "resi 558 & chain A", merge=1)

cmd.color ("red", "resi 559 & chain A")

cmd.select ("Inward", "resi 559 & chain A", merge=1)

cmd.color ("blue", "resi 560 & chain A")

cmd.select ("Outward", "resi 560 & chain A", merge=1)

cmd.color ("red", "resi 561 & chain A")

cmd.select ("Inward", "resi 561 & chain A", merge=1)

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

cmd.color ("blue", "resi 567 & chain A")

cmd.select ("Outward", "resi 567 & chain A", merge=1)

cmd.color ("red", "resi 568 & chain A")

cmd.select ("Inward", "resi 568 & chain A", merge=1)

cmd.color ("red", "resi 424 & chain A")

cmd.select ("Inward", "resi 424 & chain A", merge=1)

cmd.color ("red", "resi 425 & chain A")

cmd.select ("Inward", "resi 425 & chain A", merge=1)

cmd.color ("blue", "resi 426 & chain A")

cmd.select ("Outward", "resi 426 & chain A", merge=1)

cmd.color ("red", "resi 427 & chain A")

cmd.select ("Inward", "resi 427 & chain A", merge=1)

cmd.color ("blue", "resi 428 & chain A")

cmd.select ("Outward", "resi 428 & chain A", merge=1)

cmd.color ("red", "resi 429 & chain A")

cmd.select ("Inward", "resi 429 & chain A", merge=1)

cmd.color ("blue", "resi 430 & chain A")

cmd.select ("Outward", "resi 430 & chain A", merge=1)

cmd.color ("red", "resi 431 & chain A")

cmd.select ("Inward", "resi 431 & chain A", merge=1)

cmd.color ("blue", "resi 432 & chain A")

cmd.select ("Outward", "resi 432 & chain A", merge=1)

cmd.color ("red", "resi 433 & chain A")

cmd.select ("Inward", "resi 433 & chain A", merge=1)

cmd.color ("blue", "resi 434 & chain A")

cmd.select ("Outward", "resi 434 & chain A", merge=1)

cmd.color ("red", "resi 435 & chain A")

cmd.select ("Inward", "resi 435 & chain A", merge=1)

cmd.color ("blue", "resi 436 & chain A")

cmd.select ("Outward", "resi 436 & chain A", merge=1)

cmd.color ("red", "resi 437 & chain A")

cmd.select ("Inward", "resi 437 & chain A", merge=1)

cmd.color ("blue", "resi 438 & chain A")

cmd.select ("Outward", "resi 438 & chain A", merge=1)

cmd.color ("red", "resi 439 & chain A")

cmd.select ("Inward", "resi 439 & chain A", merge=1)

cmd.color ("blue", "resi 440 & chain A")

cmd.select ("Outward", "resi 440 & chain A", merge=1)

cmd.color ("red", "resi 441 & chain A")

cmd.select ("Inward", "resi 441 & chain A", merge=1)

cmd.color ("blue", "resi 442 & chain A")

cmd.select ("Outward", "resi 442 & chain A", merge=1)

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

cmd.color ("blue", "resi 519 & chain A")

cmd.select ("Outward", "resi 519 & chain A", merge=1)

cmd.color ("red", "resi 520 & chain A")

cmd.select ("Inward", "resi 520 & chain A", merge=1)

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

cmd.color ("red", "resi 484 & chain A")

cmd.select ("Inward", "resi 484 & chain A", merge=1)

cmd.color ("blue", "resi 485 & chain A")

cmd.select ("Outward", "resi 485 & chain A", merge=1)

cmd.color ("red", "resi 486 & chain A")

cmd.select ("Inward", "resi 486 & chain A", merge=1)

cmd.color ("blue", "resi 487 & chain A")

cmd.select ("Outward", "resi 487 & chain A", merge=1)

cmd.color ("red", "resi 488 & chain A")

cmd.select ("Inward", "resi 488 & chain A", merge=1)

cmd.color ("blue", "resi 489 & chain A")

cmd.select ("Outward", "resi 489 & chain A", merge=1)

cmd.color ("red", "resi 490 & chain A")

cmd.select ("Inward", "resi 490 & chain A", merge=1)

cmd.color ("blue", "resi 491 & chain A")

cmd.select ("Outward", "resi 491 & chain A", merge=1)

cmd.color ("red", "resi 492 & chain A")

cmd.select ("Inward", "resi 492 & chain A", merge=1)

cmd.color ("blue", "resi 493 & chain A")

cmd.select ("Outward", "resi 493 & chain A", merge=1)

cmd.color ("blue", "resi 494 & chain A")

cmd.select ("Outward", "resi 494 & chain A", merge=1)

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

cmd.color ("blue", "resi 496 & chain A")

cmd.select ("Outward", "resi 496 & chain A", merge=1)

cmd.color ("red", "resi 497 & chain A")

cmd.select ("Inward", "resi 497 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("red", "resi 446 & chain A")

cmd.select ("Inward", "resi 446 & chain A", merge=1)

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

cmd.color ("blue", "resi 575 & chain A")

cmd.select ("Outward", "resi 575 & chain A", merge=1)

cmd.color ("red", "resi 576 & chain A")

cmd.select ("Inward", "resi 576 & chain A", merge=1)

cmd.color ("blue", "resi 577 & chain A")

cmd.select ("Outward", "resi 577 & chain A", merge=1)

cmd.color ("red", "resi 578 & chain A")

cmd.select ("Inward", "resi 578 & chain A", merge=1)

cmd.color ("blue", "resi 579 & chain A")

cmd.select ("Outward", "resi 579 & chain A", merge=1)

cmd.color ("red", "resi 580 & chain A")

cmd.select ("Inward", "resi 580 & chain A", merge=1)

cmd.color ("blue", "resi 581 & chain A")

cmd.select ("Outward", "resi 581 & chain A", merge=1)

cmd.color ("red", "resi 582 & chain A")

cmd.select ("Inward", "resi 582 & chain A", merge=1)

cmd.color ("blue", "resi 583 & chain A")

cmd.select ("Outward", "resi 583 & chain A", merge=1)

cmd.color ("red", "resi 584 & chain A")

cmd.select ("Inward", "resi 584 & chain A", merge=1)

cmd.color ("red", "resi 585 & chain A")

cmd.select ("Inward", "resi 585 & chain A", merge=1)

cmd.color ("blue", "resi 586 & chain A")

cmd.select ("Outward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

cmd.color ("red", "resi 588 & chain A")

cmd.select ("Inward", "resi 588 & chain A", merge=1)

cmd.color ("blue", "resi 589 & chain A")

cmd.select ("Outward", "resi 589 & chain A", merge=1)

cmd.color ("blue", "resi 603 & chain A")

cmd.select ("Outward", "resi 603 & chain A", merge=1)

cmd.color ("red", "resi 604 & chain A")

cmd.select ("Inward", "resi 604 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("red", "resi 606 & chain A")

cmd.select ("Inward", "resi 606 & chain A", merge=1)

cmd.color ("red", "resi 607 & chain A")

cmd.select ("Inward", "resi 607 & chain A", merge=1)

cmd.color ("blue", "resi 608 & chain A")

cmd.select ("Outward", "resi 608 & chain A", merge=1)

cmd.color ("red", "resi 609 & chain A")

cmd.select ("Inward", "resi 609 & chain A", merge=1)

cmd.color ("blue", "resi 610 & chain A")

cmd.select ("Outward", "resi 610 & chain A", merge=1)

cmd.color ("red", "resi 611 & chain A")

cmd.select ("Inward", "resi 611 & chain A", merge=1)

cmd.color ("blue", "resi 612 & chain A")

cmd.select ("Outward", "resi 612 & chain A", merge=1)

cmd.color ("red", "resi 613 & chain A")

cmd.select ("Inward", "resi 613 & chain A", merge=1)

cmd.color ("blue", "resi 614 & chain A")

cmd.select ("Outward", "resi 614 & chain A", merge=1)

cmd.color ("blue", "resi 615 & chain A")

cmd.select ("Outward", "resi 615 & chain A", merge=1)

cmd.color ("red", "resi 616 & chain A")

cmd.select ("Inward", "resi 616 & chain A", merge=1)

cmd.color ("blue", "resi 617 & chain A")

cmd.select ("Outward", "resi 617 & chain A", merge=1)

cmd.color ("blue", "resi 620 & chain A")

cmd.select ("Outward", "resi 620 & chain A", merge=1)

cmd.color ("red", "resi 621 & chain A")

cmd.select ("Inward", "resi 621 & chain A", merge=1)

cmd.color ("blue", "resi 622 & chain A")

cmd.select ("Outward", "resi 622 & chain A", merge=1)

cmd.color ("red", "resi 623 & chain A")

cmd.select ("Inward", "resi 623 & chain A", merge=1)

cmd.color ("blue", "resi 624 & chain A")

cmd.select ("Outward", "resi 624 & chain A", merge=1)

cmd.color ("red", "resi 625 & chain A")

cmd.select ("Inward", "resi 625 & chain A", merge=1)

cmd.color ("blue", "resi 626 & chain A")

cmd.select ("Outward", "resi 626 & chain A", merge=1)

cmd.color ("red", "resi 627 & chain A")

cmd.select ("Inward", "resi 627 & chain A", merge=1)

cmd.color ("blue", "resi 628 & chain A")

cmd.select ("Outward", "resi 628 & chain A", merge=1)

cmd.color ("red", "resi 629 & chain A")

cmd.select ("Inward", "resi 629 & chain A", merge=1)

cmd.color ("blue", "resi 650 & chain A")

cmd.select ("Outward", "resi 650 & chain A", merge=1)

cmd.color ("red", "resi 651 & chain A")

cmd.select ("Inward", "resi 651 & chain A", merge=1)

cmd.color ("blue", "resi 652 & chain A")

cmd.select ("Outward", "resi 652 & chain A", merge=1)

cmd.color ("red", "resi 653 & chain A")

cmd.select ("Inward", "resi 653 & chain A", merge=1)

cmd.color ("blue", "resi 654 & chain A")

cmd.select ("Outward", "resi 654 & chain A", merge=1)

cmd.color ("red", "resi 655 & chain A")

cmd.select ("Inward", "resi 655 & chain A", merge=1)

cmd.color ("blue", "resi 656 & chain A")

cmd.select ("Outward", "resi 656 & chain A", merge=1)

cmd.color ("red", "resi 657 & chain A")

cmd.select ("Inward", "resi 657 & chain A", merge=1)

cmd.color ("blue", "resi 658 & chain A")

cmd.select ("Outward", "resi 658 & chain A", merge=1)

cmd.color ("red", "resi 659 & chain A")

cmd.select ("Inward", "resi 659 & chain A", merge=1)

cmd.color ("blue", "resi 682 & chain A")

cmd.select ("Outward", "resi 682 & chain A", merge=1)

cmd.color ("blue", "resi 683 & chain A")

cmd.select ("Outward", "resi 683 & chain A", merge=1)

cmd.color ("red", "resi 684 & chain A")

cmd.select ("Inward", "resi 684 & chain A", merge=1)

cmd.color ("blue", "resi 685 & chain A")

cmd.select ("Outward", "resi 685 & chain A", merge=1)

cmd.color ("red", "resi 686 & chain A")

cmd.select ("Inward", "resi 686 & chain A", merge=1)

cmd.color ("blue", "resi 687 & chain A")

cmd.select ("Outward", "resi 687 & chain A", merge=1)

cmd.color ("red", "resi 688 & chain A")

cmd.select ("Inward", "resi 688 & chain A", merge=1)

cmd.color ("blue", "resi 689 & chain A")

cmd.select ("Outward", "resi 689 & chain A", merge=1)

cmd.color ("red", "resi 690 & chain A")

cmd.select ("Inward", "resi 690 & chain A", merge=1)

cmd.color ("blue", "resi 691 & chain A")

cmd.select ("Outward", "resi 691 & chain A", merge=1)

cmd.color ("blue", "resi 692 & chain A")

cmd.select ("Outward", "resi 692 & chain A", merge=1)

cmd.color ("red", "resi 693 & chain A")

cmd.select ("Inward", "resi 693 & chain A", merge=1)

cmd.color ("blue", "resi 697 & chain A")

cmd.select ("Outward", "resi 697 & chain A", merge=1)

cmd.color ("red", "resi 698 & chain A")

cmd.select ("Inward", "resi 698 & chain A", merge=1)

cmd.color ("blue", "resi 699 & chain A")

cmd.select ("Outward", "resi 699 & chain A", merge=1)

cmd.color ("red", "resi 700 & chain A")

cmd.select ("Inward", "resi 700 & chain A", merge=1)

cmd.color ("blue", "resi 701 & chain A")

cmd.select ("Outward", "resi 701 & chain A", merge=1)

cmd.color ("red", "resi 702 & chain A")

cmd.select ("Inward", "resi 702 & chain A", merge=1)

cmd.color ("blue", "resi 703 & chain A")

cmd.select ("Outward", "resi 703 & chain A", merge=1)

cmd.color ("red", "resi 704 & chain A")

cmd.select ("Inward", "resi 704 & chain A", merge=1)

cmd.color ("blue", "resi 705 & chain A")

cmd.select ("Outward", "resi 705 & chain A", merge=1)

cmd.color ("blue", "resi 706 & chain A")

cmd.select ("Outward", "resi 706 & chain A", merge=1)

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

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("red", "resi 295 & chain A")

cmd.select ("Inward", "resi 295 & chain A", merge=1)

cmd.color ("blue", "resi 745 & chain A")

cmd.select ("Outward", "resi 745 & chain A", merge=1)

cmd.color ("blue", "resi 746 & chain A")

cmd.select ("Outward", "resi 746 & chain A", merge=1)

cmd.color ("red", "resi 747 & chain A")

cmd.select ("Inward", "resi 747 & chain A", merge=1)

cmd.color ("blue", "resi 748 & chain A")

cmd.select ("Outward", "resi 748 & chain A", merge=1)

cmd.color ("red", "resi 749 & chain A")

cmd.select ("Inward", "resi 749 & chain A", merge=1)

cmd.color ("blue", "resi 750 & chain A")

cmd.select ("Outward", "resi 750 & chain A", merge=1)

cmd.color ("red", "resi 751 & chain A")

cmd.select ("Inward", "resi 751 & chain A", merge=1)

cmd.color ("blue", "resi 752 & chain A")

cmd.select ("Outward", "resi 752 & chain A", merge=1)

cmd.color ("red", "resi 753 & chain A")

cmd.select ("Inward", "resi 753 & chain A", merge=1)

cmd.color ("blue", "resi 754 & chain A")

cmd.select ("Outward", "resi 754 & chain A", merge=1)

cmd.color ("red", "resi 755 & chain A")

cmd.select ("Inward", "resi 755 & chain A", merge=1)

cmd.color ("blue", "resi 756 & chain A")

cmd.select ("Outward", "resi 756 & chain A", merge=1)

cmd.color ("red", "resi 757 & chain A")

cmd.select ("Inward", "resi 757 & chain A", merge=1)

cmd.color ("blue", "resi 758 & chain A")

cmd.select ("Outward", "resi 758 & chain A", merge=1)

cmd.color ("blue", "resi 759 & chain A")

cmd.select ("Outward", "resi 759 & chain A", merge=1)

cmd.load_cgo( [9.0, 72.82627,26.068575,21.429996, 72.82627, 26.068575, 21.429996, 1, 1,1,0,0,0,1], "axis" )
