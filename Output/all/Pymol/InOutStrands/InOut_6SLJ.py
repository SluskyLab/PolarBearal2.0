from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SLJ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand4", "resi 239+240+241+242+243+244+245+246+247+248+249+250 & chain A ")


cmd.select("Astrand5", "resi 329+330+331+332+333+334+335+336+337+338+339+340 & chain A ")


cmd.select("Astrand6", "resi 345+346+347+348+349+350+351+352+353+354+355+356+357 & chain A ")


cmd.select("Astrand7", "resi 365+366+367+368+369+370+371+372+373+374+375+376+377+378 & chain A ")


cmd.select("Astrand8", "resi 383+384+385+386+387+388+389+390+391+392+393+394+395+396+397 & chain A ")


cmd.select("Astrand9", "resi 455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470 & chain A ")


cmd.select("Astrand10", "resi 476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495 & chain A ")


cmd.select("Astrand11", "resi 507+508+509+510+511+512+513+514+515+516+517+520+521+522+523+524+525+526+527+528+529+530 & chain A ")


cmd.select("Astrand13", "resi 535+536+537+538+539+540+541+542+543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560 & chain A ")


cmd.select("Astrand14", "resi 581+582+583+584+585+586+587+588+589+590+591+592+593+594+595+596+597+598+599+600 & chain A ")


cmd.select("Astrand15", "resi 604+605+606+607+608+609+610+611+612+613+614+615 & chain A ")


cmd.select("Astrand16", "resi 624+625+626+627+628+629+630+631+632+633+634 & chain A ")


cmd.select("Astrand17", "resi 647+648+649+650+651+652+653+654+655+656+657+658+659+660+661 & chain A ")


cmd.select("Astrand20", "resi 698+699+700+701+702+703+704+705+706+707+708+709+710+711 & chain A ")


cmd.select("Astrand21", "resi 716+717+718+719+720+721+722+723+724+725+726+727+728 & chain A ")


cmd.select("Astrand24", "resi 751+752+753+754+755+756+757+758+759+760+761+762+763+764 & chain A ")


cmd.select("Astrand25", "resi 774+775+776+777+778+779+780+781+782+783+784+785+786+787+788 & chain A ")


cmd.select("Astrand30", "resi 864+865+866+867+868+869+870+871+872+873 & chain A ")


cmd.select("Astrand31", "resi 877+878+879+880+881+882+883+884+885+886+887 & chain A ")


cmd.select("Astrand32", "resi 946+947+948+949+950+951+952+953+954+955+956+957 & chain A ")


cmd.select("Astrand33", "resi 971+972+973+974+975+976+977+978+979 & chain A ")


cmd.select("Astrand35", "resi 1006+1007+1008+1009+1010+1011+1012+1013+1014+1015+1016 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 239 & chain A")

cmd.select ("Outward", "resi 239 & chain A", merge=1)

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

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

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

cmd.color ("blue", "resi 365 & chain A")

cmd.select ("Outward", "resi 365 & chain A", merge=1)

cmd.color ("red", "resi 366 & chain A")

cmd.select ("Inward", "resi 366 & chain A", merge=1)

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

cmd.color ("blue", "resi 378 & chain A")

cmd.select ("Outward", "resi 378 & chain A", merge=1)

cmd.color ("blue", "resi 383 & chain A")

cmd.select ("Outward", "resi 383 & chain A", merge=1)

cmd.color ("red", "resi 384 & chain A")

cmd.select ("Inward", "resi 384 & chain A", merge=1)

cmd.color ("blue", "resi 385 & chain A")

cmd.select ("Outward", "resi 385 & chain A", merge=1)

cmd.color ("red", "resi 386 & chain A")

cmd.select ("Inward", "resi 386 & chain A", merge=1)

cmd.color ("blue", "resi 387 & chain A")

cmd.select ("Outward", "resi 387 & chain A", merge=1)

cmd.color ("red", "resi 388 & chain A")

cmd.select ("Inward", "resi 388 & chain A", merge=1)

cmd.color ("blue", "resi 389 & chain A")

cmd.select ("Outward", "resi 389 & chain A", merge=1)

cmd.color ("red", "resi 390 & chain A")

cmd.select ("Inward", "resi 390 & chain A", merge=1)

cmd.color ("blue", "resi 391 & chain A")

cmd.select ("Outward", "resi 391 & chain A", merge=1)

cmd.color ("red", "resi 392 & chain A")

cmd.select ("Inward", "resi 392 & chain A", merge=1)

cmd.color ("blue", "resi 393 & chain A")

cmd.select ("Outward", "resi 393 & chain A", merge=1)

cmd.color ("red", "resi 394 & chain A")

cmd.select ("Inward", "resi 394 & chain A", merge=1)

cmd.color ("blue", "resi 395 & chain A")

cmd.select ("Outward", "resi 395 & chain A", merge=1)

cmd.color ("red", "resi 396 & chain A")

cmd.select ("Inward", "resi 396 & chain A", merge=1)

cmd.color ("blue", "resi 397 & chain A")

cmd.select ("Outward", "resi 397 & chain A", merge=1)

cmd.color ("red", "resi 455 & chain A")

cmd.select ("Inward", "resi 455 & chain A", merge=1)

cmd.color ("blue", "resi 456 & chain A")

cmd.select ("Outward", "resi 456 & chain A", merge=1)

cmd.color ("red", "resi 457 & chain A")

cmd.select ("Inward", "resi 457 & chain A", merge=1)

cmd.color ("blue", "resi 458 & chain A")

cmd.select ("Outward", "resi 458 & chain A", merge=1)

cmd.color ("red", "resi 459 & chain A")

cmd.select ("Inward", "resi 459 & chain A", merge=1)

cmd.color ("blue", "resi 460 & chain A")

cmd.select ("Outward", "resi 460 & chain A", merge=1)

cmd.color ("red", "resi 461 & chain A")

cmd.select ("Inward", "resi 461 & chain A", merge=1)

cmd.color ("blue", "resi 462 & chain A")

cmd.select ("Outward", "resi 462 & chain A", merge=1)

cmd.color ("red", "resi 463 & chain A")

cmd.select ("Inward", "resi 463 & chain A", merge=1)

cmd.color ("blue", "resi 464 & chain A")

cmd.select ("Outward", "resi 464 & chain A", merge=1)

cmd.color ("red", "resi 465 & chain A")

cmd.select ("Inward", "resi 465 & chain A", merge=1)

cmd.color ("blue", "resi 466 & chain A")

cmd.select ("Outward", "resi 466 & chain A", merge=1)

cmd.color ("red", "resi 467 & chain A")

cmd.select ("Inward", "resi 467 & chain A", merge=1)

cmd.color ("blue", "resi 468 & chain A")

cmd.select ("Outward", "resi 468 & chain A", merge=1)

cmd.color ("red", "resi 469 & chain A")

cmd.select ("Inward", "resi 469 & chain A", merge=1)

cmd.color ("blue", "resi 470 & chain A")

cmd.select ("Outward", "resi 470 & chain A", merge=1)

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

cmd.color ("red", "resi 483 & chain A")

cmd.select ("Inward", "resi 483 & chain A", merge=1)

cmd.color ("blue", "resi 484 & chain A")

cmd.select ("Outward", "resi 484 & chain A", merge=1)

cmd.color ("red", "resi 485 & chain A")

cmd.select ("Inward", "resi 485 & chain A", merge=1)

cmd.color ("blue", "resi 486 & chain A")

cmd.select ("Outward", "resi 486 & chain A", merge=1)

cmd.color ("red", "resi 487 & chain A")

cmd.select ("Inward", "resi 487 & chain A", merge=1)

cmd.color ("blue", "resi 488 & chain A")

cmd.select ("Outward", "resi 488 & chain A", merge=1)

cmd.color ("red", "resi 489 & chain A")

cmd.select ("Inward", "resi 489 & chain A", merge=1)

cmd.color ("blue", "resi 490 & chain A")

cmd.select ("Outward", "resi 490 & chain A", merge=1)

cmd.color ("red", "resi 491 & chain A")

cmd.select ("Inward", "resi 491 & chain A", merge=1)

cmd.color ("blue", "resi 492 & chain A")

cmd.select ("Outward", "resi 492 & chain A", merge=1)

cmd.color ("red", "resi 493 & chain A")

cmd.select ("Inward", "resi 493 & chain A", merge=1)

cmd.color ("blue", "resi 494 & chain A")

cmd.select ("Outward", "resi 494 & chain A", merge=1)

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

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

cmd.color ("red", "resi 514 & chain A")

cmd.select ("Inward", "resi 514 & chain A", merge=1)

cmd.color ("blue", "resi 515 & chain A")

cmd.select ("Outward", "resi 515 & chain A", merge=1)

cmd.color ("red", "resi 516 & chain A")

cmd.select ("Inward", "resi 516 & chain A", merge=1)

cmd.color ("blue", "resi 517 & chain A")

cmd.select ("Outward", "resi 517 & chain A", merge=1)

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

cmd.color ("blue", "resi 530 & chain A")

cmd.select ("Outward", "resi 530 & chain A", merge=1)

cmd.color ("blue", "resi 535 & chain A")

cmd.select ("Outward", "resi 535 & chain A", merge=1)

cmd.color ("red", "resi 536 & chain A")

cmd.select ("Inward", "resi 536 & chain A", merge=1)

cmd.color ("blue", "resi 537 & chain A")

cmd.select ("Outward", "resi 537 & chain A", merge=1)

cmd.color ("red", "resi 538 & chain A")

cmd.select ("Inward", "resi 538 & chain A", merge=1)

cmd.color ("blue", "resi 539 & chain A")

cmd.select ("Outward", "resi 539 & chain A", merge=1)

cmd.color ("red", "resi 540 & chain A")

cmd.select ("Inward", "resi 540 & chain A", merge=1)

cmd.color ("blue", "resi 541 & chain A")

cmd.select ("Outward", "resi 541 & chain A", merge=1)

cmd.color ("red", "resi 542 & chain A")

cmd.select ("Inward", "resi 542 & chain A", merge=1)

cmd.color ("blue", "resi 543 & chain A")

cmd.select ("Outward", "resi 543 & chain A", merge=1)

cmd.color ("red", "resi 544 & chain A")

cmd.select ("Inward", "resi 544 & chain A", merge=1)

cmd.color ("blue", "resi 545 & chain A")

cmd.select ("Outward", "resi 545 & chain A", merge=1)

cmd.color ("red", "resi 546 & chain A")

cmd.select ("Inward", "resi 546 & chain A", merge=1)

cmd.color ("blue", "resi 547 & chain A")

cmd.select ("Outward", "resi 547 & chain A", merge=1)

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

cmd.color ("red", "resi 556 & chain A")

cmd.select ("Inward", "resi 556 & chain A", merge=1)

cmd.color ("blue", "resi 557 & chain A")

cmd.select ("Outward", "resi 557 & chain A", merge=1)

cmd.color ("red", "resi 558 & chain A")

cmd.select ("Inward", "resi 558 & chain A", merge=1)

cmd.color ("blue", "resi 559 & chain A")

cmd.select ("Outward", "resi 559 & chain A", merge=1)

cmd.color ("red", "resi 560 & chain A")

cmd.select ("Inward", "resi 560 & chain A", merge=1)

cmd.color ("red", "resi 581 & chain A")

cmd.select ("Inward", "resi 581 & chain A", merge=1)

cmd.color ("blue", "resi 582 & chain A")

cmd.select ("Outward", "resi 582 & chain A", merge=1)

cmd.color ("red", "resi 583 & chain A")

cmd.select ("Inward", "resi 583 & chain A", merge=1)

cmd.color ("blue", "resi 584 & chain A")

cmd.select ("Outward", "resi 584 & chain A", merge=1)

cmd.color ("red", "resi 585 & chain A")

cmd.select ("Inward", "resi 585 & chain A", merge=1)

cmd.color ("blue", "resi 586 & chain A")

cmd.select ("Outward", "resi 586 & chain A", merge=1)

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

cmd.color ("red", "resi 597 & chain A")

cmd.select ("Inward", "resi 597 & chain A", merge=1)

cmd.color ("blue", "resi 598 & chain A")

cmd.select ("Outward", "resi 598 & chain A", merge=1)

cmd.color ("red", "resi 599 & chain A")

cmd.select ("Inward", "resi 599 & chain A", merge=1)

cmd.color ("blue", "resi 600 & chain A")

cmd.select ("Outward", "resi 600 & chain A", merge=1)

cmd.color ("blue", "resi 604 & chain A")

cmd.select ("Outward", "resi 604 & chain A", merge=1)

cmd.color ("red", "resi 605 & chain A")

cmd.select ("Inward", "resi 605 & chain A", merge=1)

cmd.color ("blue", "resi 606 & chain A")

cmd.select ("Outward", "resi 606 & chain A", merge=1)

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

cmd.color ("red", "resi 615 & chain A")

cmd.select ("Inward", "resi 615 & chain A", merge=1)

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

cmd.color ("blue", "resi 647 & chain A")

cmd.select ("Outward", "resi 647 & chain A", merge=1)

cmd.color ("red", "resi 648 & chain A")

cmd.select ("Inward", "resi 648 & chain A", merge=1)

cmd.color ("red", "resi 649 & chain A")

cmd.select ("Inward", "resi 649 & chain A", merge=1)

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

cmd.color ("blue", "resi 660 & chain A")

cmd.select ("Outward", "resi 660 & chain A", merge=1)

cmd.color ("red", "resi 661 & chain A")

cmd.select ("Inward", "resi 661 & chain A", merge=1)

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

cmd.color ("red", "resi 706 & chain A")

cmd.select ("Inward", "resi 706 & chain A", merge=1)

cmd.color ("blue", "resi 707 & chain A")

cmd.select ("Outward", "resi 707 & chain A", merge=1)

cmd.color ("red", "resi 708 & chain A")

cmd.select ("Inward", "resi 708 & chain A", merge=1)

cmd.color ("blue", "resi 709 & chain A")

cmd.select ("Outward", "resi 709 & chain A", merge=1)

cmd.color ("red", "resi 710 & chain A")

cmd.select ("Inward", "resi 710 & chain A", merge=1)

cmd.color ("red", "resi 711 & chain A")

cmd.select ("Inward", "resi 711 & chain A", merge=1)

cmd.color ("blue", "resi 716 & chain A")

cmd.select ("Outward", "resi 716 & chain A", merge=1)

cmd.color ("red", "resi 717 & chain A")

cmd.select ("Inward", "resi 717 & chain A", merge=1)

cmd.color ("blue", "resi 718 & chain A")

cmd.select ("Outward", "resi 718 & chain A", merge=1)

cmd.color ("red", "resi 719 & chain A")

cmd.select ("Inward", "resi 719 & chain A", merge=1)

cmd.color ("blue", "resi 720 & chain A")

cmd.select ("Outward", "resi 720 & chain A", merge=1)

cmd.color ("red", "resi 721 & chain A")

cmd.select ("Inward", "resi 721 & chain A", merge=1)

cmd.color ("blue", "resi 722 & chain A")

cmd.select ("Outward", "resi 722 & chain A", merge=1)

cmd.color ("red", "resi 723 & chain A")

cmd.select ("Inward", "resi 723 & chain A", merge=1)

cmd.color ("blue", "resi 724 & chain A")

cmd.select ("Outward", "resi 724 & chain A", merge=1)

cmd.color ("red", "resi 725 & chain A")

cmd.select ("Inward", "resi 725 & chain A", merge=1)

cmd.color ("blue", "resi 726 & chain A")

cmd.select ("Outward", "resi 726 & chain A", merge=1)

cmd.color ("red", "resi 727 & chain A")

cmd.select ("Inward", "resi 727 & chain A", merge=1)

cmd.color ("blue", "resi 728 & chain A")

cmd.select ("Outward", "resi 728 & chain A", merge=1)

cmd.color ("blue", "resi 751 & chain A")

cmd.select ("Outward", "resi 751 & chain A", merge=1)

cmd.color ("red", "resi 752 & chain A")

cmd.select ("Inward", "resi 752 & chain A", merge=1)

cmd.color ("blue", "resi 753 & chain A")

cmd.select ("Outward", "resi 753 & chain A", merge=1)

cmd.color ("red", "resi 754 & chain A")

cmd.select ("Inward", "resi 754 & chain A", merge=1)

cmd.color ("blue", "resi 755 & chain A")

cmd.select ("Outward", "resi 755 & chain A", merge=1)

cmd.color ("red", "resi 756 & chain A")

cmd.select ("Inward", "resi 756 & chain A", merge=1)

cmd.color ("blue", "resi 757 & chain A")

cmd.select ("Outward", "resi 757 & chain A", merge=1)

cmd.color ("red", "resi 758 & chain A")

cmd.select ("Inward", "resi 758 & chain A", merge=1)

cmd.color ("blue", "resi 759 & chain A")

cmd.select ("Outward", "resi 759 & chain A", merge=1)

cmd.color ("red", "resi 760 & chain A")

cmd.select ("Inward", "resi 760 & chain A", merge=1)

cmd.color ("blue", "resi 761 & chain A")

cmd.select ("Outward", "resi 761 & chain A", merge=1)

cmd.color ("red", "resi 762 & chain A")

cmd.select ("Inward", "resi 762 & chain A", merge=1)

cmd.color ("blue", "resi 763 & chain A")

cmd.select ("Outward", "resi 763 & chain A", merge=1)

cmd.color ("blue", "resi 764 & chain A")

cmd.select ("Outward", "resi 764 & chain A", merge=1)

cmd.color ("red", "resi 774 & chain A")

cmd.select ("Inward", "resi 774 & chain A", merge=1)

cmd.color ("blue", "resi 775 & chain A")

cmd.select ("Outward", "resi 775 & chain A", merge=1)

cmd.color ("red", "resi 776 & chain A")

cmd.select ("Inward", "resi 776 & chain A", merge=1)

cmd.color ("blue", "resi 777 & chain A")

cmd.select ("Outward", "resi 777 & chain A", merge=1)

cmd.color ("red", "resi 778 & chain A")

cmd.select ("Inward", "resi 778 & chain A", merge=1)

cmd.color ("blue", "resi 779 & chain A")

cmd.select ("Outward", "resi 779 & chain A", merge=1)

cmd.color ("red", "resi 780 & chain A")

cmd.select ("Inward", "resi 780 & chain A", merge=1)

cmd.color ("blue", "resi 781 & chain A")

cmd.select ("Outward", "resi 781 & chain A", merge=1)

cmd.color ("red", "resi 782 & chain A")

cmd.select ("Inward", "resi 782 & chain A", merge=1)

cmd.color ("blue", "resi 783 & chain A")

cmd.select ("Outward", "resi 783 & chain A", merge=1)

cmd.color ("red", "resi 784 & chain A")

cmd.select ("Inward", "resi 784 & chain A", merge=1)

cmd.color ("blue", "resi 785 & chain A")

cmd.select ("Outward", "resi 785 & chain A", merge=1)

cmd.color ("blue", "resi 786 & chain A")

cmd.select ("Outward", "resi 786 & chain A", merge=1)

cmd.color ("red", "resi 787 & chain A")

cmd.select ("Inward", "resi 787 & chain A", merge=1)

cmd.color ("blue", "resi 788 & chain A")

cmd.select ("Outward", "resi 788 & chain A", merge=1)

cmd.color ("blue", "resi 864 & chain A")

cmd.select ("Outward", "resi 864 & chain A", merge=1)

cmd.color ("red", "resi 865 & chain A")

cmd.select ("Inward", "resi 865 & chain A", merge=1)

cmd.color ("blue", "resi 866 & chain A")

cmd.select ("Outward", "resi 866 & chain A", merge=1)

cmd.color ("red", "resi 867 & chain A")

cmd.select ("Inward", "resi 867 & chain A", merge=1)

cmd.color ("blue", "resi 868 & chain A")

cmd.select ("Outward", "resi 868 & chain A", merge=1)

cmd.color ("red", "resi 869 & chain A")

cmd.select ("Inward", "resi 869 & chain A", merge=1)

cmd.color ("blue", "resi 870 & chain A")

cmd.select ("Outward", "resi 870 & chain A", merge=1)

cmd.color ("red", "resi 871 & chain A")

cmd.select ("Inward", "resi 871 & chain A", merge=1)

cmd.color ("blue", "resi 872 & chain A")

cmd.select ("Outward", "resi 872 & chain A", merge=1)

cmd.color ("red", "resi 873 & chain A")

cmd.select ("Inward", "resi 873 & chain A", merge=1)

cmd.color ("blue", "resi 877 & chain A")

cmd.select ("Outward", "resi 877 & chain A", merge=1)

cmd.color ("red", "resi 878 & chain A")

cmd.select ("Inward", "resi 878 & chain A", merge=1)

cmd.color ("blue", "resi 879 & chain A")

cmd.select ("Outward", "resi 879 & chain A", merge=1)

cmd.color ("red", "resi 880 & chain A")

cmd.select ("Inward", "resi 880 & chain A", merge=1)

cmd.color ("blue", "resi 881 & chain A")

cmd.select ("Outward", "resi 881 & chain A", merge=1)

cmd.color ("red", "resi 882 & chain A")

cmd.select ("Inward", "resi 882 & chain A", merge=1)

cmd.color ("blue", "resi 883 & chain A")

cmd.select ("Outward", "resi 883 & chain A", merge=1)

cmd.color ("red", "resi 884 & chain A")

cmd.select ("Inward", "resi 884 & chain A", merge=1)

cmd.color ("blue", "resi 885 & chain A")

cmd.select ("Outward", "resi 885 & chain A", merge=1)

cmd.color ("red", "resi 886 & chain A")

cmd.select ("Inward", "resi 886 & chain A", merge=1)

cmd.color ("blue", "resi 887 & chain A")

cmd.select ("Outward", "resi 887 & chain A", merge=1)

cmd.color ("red", "resi 946 & chain A")

cmd.select ("Inward", "resi 946 & chain A", merge=1)

cmd.color ("blue", "resi 947 & chain A")

cmd.select ("Outward", "resi 947 & chain A", merge=1)

cmd.color ("red", "resi 948 & chain A")

cmd.select ("Inward", "resi 948 & chain A", merge=1)

cmd.color ("blue", "resi 949 & chain A")

cmd.select ("Outward", "resi 949 & chain A", merge=1)

cmd.color ("red", "resi 950 & chain A")

cmd.select ("Inward", "resi 950 & chain A", merge=1)

cmd.color ("red", "resi 951 & chain A")

cmd.select ("Inward", "resi 951 & chain A", merge=1)

cmd.color ("blue", "resi 952 & chain A")

cmd.select ("Outward", "resi 952 & chain A", merge=1)

cmd.color ("red", "resi 953 & chain A")

cmd.select ("Inward", "resi 953 & chain A", merge=1)

cmd.color ("blue", "resi 954 & chain A")

cmd.select ("Outward", "resi 954 & chain A", merge=1)

cmd.color ("red", "resi 955 & chain A")

cmd.select ("Inward", "resi 955 & chain A", merge=1)

cmd.color ("blue", "resi 956 & chain A")

cmd.select ("Outward", "resi 956 & chain A", merge=1)

cmd.color ("red", "resi 957 & chain A")

cmd.select ("Inward", "resi 957 & chain A", merge=1)

cmd.color ("red", "resi 971 & chain A")

cmd.select ("Inward", "resi 971 & chain A", merge=1)

cmd.color ("blue", "resi 972 & chain A")

cmd.select ("Outward", "resi 972 & chain A", merge=1)

cmd.color ("red", "resi 973 & chain A")

cmd.select ("Inward", "resi 973 & chain A", merge=1)

cmd.color ("blue", "resi 974 & chain A")

cmd.select ("Outward", "resi 974 & chain A", merge=1)

cmd.color ("red", "resi 975 & chain A")

cmd.select ("Inward", "resi 975 & chain A", merge=1)

cmd.color ("blue", "resi 976 & chain A")

cmd.select ("Outward", "resi 976 & chain A", merge=1)

cmd.color ("red", "resi 977 & chain A")

cmd.select ("Inward", "resi 977 & chain A", merge=1)

cmd.color ("blue", "resi 978 & chain A")

cmd.select ("Outward", "resi 978 & chain A", merge=1)

cmd.color ("red", "resi 979 & chain A")

cmd.select ("Inward", "resi 979 & chain A", merge=1)

cmd.color ("red", "resi 1006 & chain A")

cmd.select ("Inward", "resi 1006 & chain A", merge=1)

cmd.color ("blue", "resi 1007 & chain A")

cmd.select ("Outward", "resi 1007 & chain A", merge=1)

cmd.color ("red", "resi 1008 & chain A")

cmd.select ("Inward", "resi 1008 & chain A", merge=1)

cmd.color ("blue", "resi 1009 & chain A")

cmd.select ("Outward", "resi 1009 & chain A", merge=1)

cmd.color ("red", "resi 1010 & chain A")

cmd.select ("Inward", "resi 1010 & chain A", merge=1)

cmd.color ("blue", "resi 1011 & chain A")

cmd.select ("Outward", "resi 1011 & chain A", merge=1)

cmd.color ("red", "resi 1012 & chain A")

cmd.select ("Inward", "resi 1012 & chain A", merge=1)

cmd.color ("blue", "resi 1013 & chain A")

cmd.select ("Outward", "resi 1013 & chain A", merge=1)

cmd.color ("red", "resi 1014 & chain A")

cmd.select ("Inward", "resi 1014 & chain A", merge=1)

cmd.color ("blue", "resi 1015 & chain A")

cmd.select ("Outward", "resi 1015 & chain A", merge=1)

cmd.color ("blue", "resi 1016 & chain A")

cmd.select ("Outward", "resi 1016 & chain A", merge=1)

cmd.load_cgo( [9.0, 32.278824,83.77068,42.327682, 32.278824, 83.77068, 42.327682, 1, 1,1,0,0,0,1], "axis" )
