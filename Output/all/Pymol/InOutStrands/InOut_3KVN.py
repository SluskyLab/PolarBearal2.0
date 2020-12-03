from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand6", "resi 347+348+349+350+351+352+353+354+355+356+357+358+359+360 & chain A ")


cmd.select("Astrand7", "resi 369+370+371+372+373+374+375+376+377+378+379+380+381+382+383 & chain A ")


cmd.select("Astrand8", "resi 388+389+390+391+392+393+394+395+396+397+398+399+400+401+402+403 & chain A ")


cmd.select("Astrand9", "resi 408+409+410+411+412+413+414+415+416+417+418+419+420+421+422+423+424+425 & chain A ")


cmd.select("Astrand10", "resi 428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+448+449+450 & chain A ")


cmd.select("Astrand11", "resi 453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472+473+474 & chain A ")


cmd.select("Astrand12", "resi 484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499 & chain A ")


cmd.select("Astrand14", "resi 517+518+519+520+521+522+523+524+525+526+527+528+529+530+531+532+533 & chain A ")


cmd.select("Astrand15", "resi 538+539+540+541+542+543+544+545+546+547+548+549 & chain A ")


cmd.select("Astrand18", "resi 579+580+581+582+583+584+585+586+587+588+589+590+591+592 & chain A ")


cmd.select("Astrand19", "resi 595+596+597+598+599+600+601+602+603+604+605+606 & chain A ")


cmd.select("Astrand20", "resi 609+610+611+612+613+614+615+616+617+618+619+620+621 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("red", "resi 358 & chain A")

cmd.select ("Inward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("red", "resi 360 & chain A")

cmd.select ("Inward", "resi 360 & chain A", merge=1)

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

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("red", "resi 381 & chain A")

cmd.select ("Inward", "resi 381 & chain A", merge=1)

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("blue", "resi 383 & chain A")

cmd.select ("Outward", "resi 383 & chain A", merge=1)

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

cmd.color ("red", "resi 399 & chain A")

cmd.select ("Inward", "resi 399 & chain A", merge=1)

cmd.color ("blue", "resi 400 & chain A")

cmd.select ("Outward", "resi 400 & chain A", merge=1)

cmd.color ("red", "resi 401 & chain A")

cmd.select ("Inward", "resi 401 & chain A", merge=1)

cmd.color ("blue", "resi 402 & chain A")

cmd.select ("Outward", "resi 402 & chain A", merge=1)

cmd.color ("red", "resi 403 & chain A")

cmd.select ("Inward", "resi 403 & chain A", merge=1)

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

cmd.color ("red", "resi 418 & chain A")

cmd.select ("Inward", "resi 418 & chain A", merge=1)

cmd.color ("blue", "resi 419 & chain A")

cmd.select ("Outward", "resi 419 & chain A", merge=1)

cmd.color ("red", "resi 420 & chain A")

cmd.select ("Inward", "resi 420 & chain A", merge=1)

cmd.color ("blue", "resi 421 & chain A")

cmd.select ("Outward", "resi 421 & chain A", merge=1)

cmd.color ("red", "resi 422 & chain A")

cmd.select ("Inward", "resi 422 & chain A", merge=1)

cmd.color ("blue", "resi 423 & chain A")

cmd.select ("Outward", "resi 423 & chain A", merge=1)

cmd.color ("red", "resi 424 & chain A")

cmd.select ("Inward", "resi 424 & chain A", merge=1)

cmd.color ("blue", "resi 425 & chain A")

cmd.select ("Outward", "resi 425 & chain A", merge=1)

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

cmd.color ("red", "resi 442 & chain A")

cmd.select ("Inward", "resi 442 & chain A", merge=1)

cmd.color ("blue", "resi 443 & chain A")

cmd.select ("Outward", "resi 443 & chain A", merge=1)

cmd.color ("red", "resi 444 & chain A")

cmd.select ("Inward", "resi 444 & chain A", merge=1)

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

cmd.color ("blue", "resi 450 & chain A")

cmd.select ("Outward", "resi 450 & chain A", merge=1)

cmd.color ("blue", "resi 453 & chain A")

cmd.select ("Outward", "resi 453 & chain A", merge=1)

cmd.color ("blue", "resi 454 & chain A")

cmd.select ("Outward", "resi 454 & chain A", merge=1)

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

cmd.color ("red", "resi 471 & chain A")

cmd.select ("Inward", "resi 471 & chain A", merge=1)

cmd.color ("blue", "resi 472 & chain A")

cmd.select ("Outward", "resi 472 & chain A", merge=1)

cmd.color ("red", "resi 473 & chain A")

cmd.select ("Inward", "resi 473 & chain A", merge=1)

cmd.color ("blue", "resi 474 & chain A")

cmd.select ("Outward", "resi 474 & chain A", merge=1)

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

cmd.color ("red", "resi 495 & chain A")

cmd.select ("Inward", "resi 495 & chain A", merge=1)

cmd.color ("blue", "resi 496 & chain A")

cmd.select ("Outward", "resi 496 & chain A", merge=1)

cmd.color ("red", "resi 497 & chain A")

cmd.select ("Inward", "resi 497 & chain A", merge=1)

cmd.color ("blue", "resi 498 & chain A")

cmd.select ("Outward", "resi 498 & chain A", merge=1)

cmd.color ("red", "resi 499 & chain A")

cmd.select ("Inward", "resi 499 & chain A", merge=1)

cmd.color ("red", "resi 517 & chain A")

cmd.select ("Inward", "resi 517 & chain A", merge=1)

cmd.color ("blue", "resi 518 & chain A")

cmd.select ("Outward", "resi 518 & chain A", merge=1)

cmd.color ("red", "resi 519 & chain A")

cmd.select ("Inward", "resi 519 & chain A", merge=1)

cmd.color ("blue", "resi 520 & chain A")

cmd.select ("Outward", "resi 520 & chain A", merge=1)

cmd.color ("red", "resi 521 & chain A")

cmd.select ("Inward", "resi 521 & chain A", merge=1)

cmd.color ("blue", "resi 522 & chain A")

cmd.select ("Outward", "resi 522 & chain A", merge=1)

cmd.color ("red", "resi 523 & chain A")

cmd.select ("Inward", "resi 523 & chain A", merge=1)

cmd.color ("blue", "resi 524 & chain A")

cmd.select ("Outward", "resi 524 & chain A", merge=1)

cmd.color ("red", "resi 525 & chain A")

cmd.select ("Inward", "resi 525 & chain A", merge=1)

cmd.color ("blue", "resi 526 & chain A")

cmd.select ("Outward", "resi 526 & chain A", merge=1)

cmd.color ("red", "resi 527 & chain A")

cmd.select ("Inward", "resi 527 & chain A", merge=1)

cmd.color ("blue", "resi 528 & chain A")

cmd.select ("Outward", "resi 528 & chain A", merge=1)

cmd.color ("red", "resi 529 & chain A")

cmd.select ("Inward", "resi 529 & chain A", merge=1)

cmd.color ("blue", "resi 530 & chain A")

cmd.select ("Outward", "resi 530 & chain A", merge=1)

cmd.color ("red", "resi 531 & chain A")

cmd.select ("Inward", "resi 531 & chain A", merge=1)

cmd.color ("blue", "resi 532 & chain A")

cmd.select ("Outward", "resi 532 & chain A", merge=1)

cmd.color ("blue", "resi 533 & chain A")

cmd.select ("Outward", "resi 533 & chain A", merge=1)

cmd.color ("blue", "resi 538 & chain A")

cmd.select ("Outward", "resi 538 & chain A", merge=1)

cmd.color ("red", "resi 539 & chain A")

cmd.select ("Inward", "resi 539 & chain A", merge=1)

cmd.color ("blue", "resi 540 & chain A")

cmd.select ("Outward", "resi 540 & chain A", merge=1)

cmd.color ("red", "resi 541 & chain A")

cmd.select ("Inward", "resi 541 & chain A", merge=1)

cmd.color ("blue", "resi 542 & chain A")

cmd.select ("Outward", "resi 542 & chain A", merge=1)

cmd.color ("red", "resi 543 & chain A")

cmd.select ("Inward", "resi 543 & chain A", merge=1)

cmd.color ("blue", "resi 544 & chain A")

cmd.select ("Outward", "resi 544 & chain A", merge=1)

cmd.color ("red", "resi 545 & chain A")

cmd.select ("Inward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 546 & chain A")

cmd.select ("Outward", "resi 546 & chain A", merge=1)

cmd.color ("red", "resi 547 & chain A")

cmd.select ("Inward", "resi 547 & chain A", merge=1)

cmd.color ("blue", "resi 548 & chain A")

cmd.select ("Outward", "resi 548 & chain A", merge=1)

cmd.color ("red", "resi 549 & chain A")

cmd.select ("Inward", "resi 549 & chain A", merge=1)

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

cmd.color ("blue", "resi 585 & chain A")

cmd.select ("Outward", "resi 585 & chain A", merge=1)

cmd.color ("red", "resi 586 & chain A")

cmd.select ("Inward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

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

cmd.color ("red", "resi 602 & chain A")

cmd.select ("Inward", "resi 602 & chain A", merge=1)

cmd.color ("blue", "resi 603 & chain A")

cmd.select ("Outward", "resi 603 & chain A", merge=1)

cmd.color ("red", "resi 604 & chain A")

cmd.select ("Inward", "resi 604 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("red", "resi 606 & chain A")

cmd.select ("Inward", "resi 606 & chain A", merge=1)

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

cmd.color ("blue", "resi 616 & chain A")

cmd.select ("Outward", "resi 616 & chain A", merge=1)

cmd.color ("red", "resi 617 & chain A")

cmd.select ("Inward", "resi 617 & chain A", merge=1)

cmd.color ("blue", "resi 618 & chain A")

cmd.select ("Outward", "resi 618 & chain A", merge=1)

cmd.color ("red", "resi 619 & chain A")

cmd.select ("Inward", "resi 619 & chain A", merge=1)

cmd.color ("blue", "resi 620 & chain A")

cmd.select ("Outward", "resi 620 & chain A", merge=1)

cmd.color ("blue", "resi 621 & chain A")

cmd.select ("Outward", "resi 621 & chain A", merge=1)

cmd.load_cgo( [9.0, -3.8732498,43.545,46.936417, -3.8732498, 43.545, 46.936417, 1, 1,1,0,0,0,1], "axis" )
