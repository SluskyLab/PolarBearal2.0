from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4CU4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand9", "resi 161+162+163+164+165+166+167+168+169 & chain A ")


cmd.select("Astrand34", "resi 716+717+718+719+720+721+722+723+724 & chain A ")


cmd.select("Astrand31", "resi 686+687+688+689+690+691+692 & chain A ")


cmd.select("Astrand30", "resi 666+667+668+669+670+671+672+673+674+675+676 & chain A ")


cmd.select("Astrand27", "resi 641+642+643+644+645+646+647+648+649+650 & chain A ")


cmd.select("Astrand26", "resi 623+624+625+626+627+628+629+630+631+632+633 & chain A ")


cmd.select("Astrand25", "resi 593+594+595+596+597+598+599+600+601+602+603+604+605+606+607+608 & chain A ")


cmd.select("Astrand24", "resi 570+571+572+573+574+575+576+577+578+579+580+581+582+583+584+585+586+587+588 & chain A ")


cmd.select("Astrand22", "resi 527+528+529+530+531+532+533+534+535+536+537+538 & chain A ")


cmd.select("Astrand21", "resi 501+502+503+504+505+506+507+508+509+510+511+512 & chain A ")


cmd.select("Astrand23", "resi 545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+561+562 & chain A ")


cmd.select("Astrand20", "resi 478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495 & chain A ")


cmd.select("Astrand15", "resi 456+457+458+370+459+371+372+460+373+374+461+375+462+376+294+463+295+377+296+297+464+378+379+298+465+299+380+466+300+381+467+301+382+468+302+383+469+303+384+304+305+470+385+471+306+307+386+387+472+308+473+309+388+389+315+313+314+311+316+310+391+312+390+317+392+393+394+396+397+400+395+399+401+398 & chain A ")


cmd.select("Astrand14", "resi 340+341+342+343+344+345+346+431+347+274+432+275+348+433+434+276+349+435+277+350+436+278+351+437+438+352+279+439+353+440+280+354+281+441+355+442+356+282+443+283+357+444+358+284+285+445+446+359+448+286+447+360+287+450+449+361+362+451+288+452+363+289+364+453+365+366+367 & chain A ")


cmd.select("Astrand13", "resi 227+228+229+230+231+232+233+234+235+236+237+238 & chain A ")


cmd.select("Astrand12", "resi 209+210+211+212+213+214+215+216+217+218+219+220+221+222+223+224 & chain A ")


cmd.select("Astrand11", "resi 190+191+192+193+194+195+196+197+198+199+200+201+202 & chain A ")


cmd.select("Astrand10", "resi 173+174+175+176+177+178+179+180+181+182+183 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 161 & chain A")

cmd.select ("Inward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 162 & chain A")

cmd.select ("Outward", "resi 162 & chain A", merge=1)

cmd.color ("red", "resi 163 & chain A")

cmd.select ("Inward", "resi 163 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

cmd.color ("red", "resi 165 & chain A")

cmd.select ("Inward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 166 & chain A")

cmd.select ("Outward", "resi 166 & chain A", merge=1)

cmd.color ("red", "resi 167 & chain A")

cmd.select ("Inward", "resi 167 & chain A", merge=1)

cmd.color ("blue", "resi 168 & chain A")

cmd.select ("Outward", "resi 168 & chain A", merge=1)

cmd.color ("red", "resi 169 & chain A")

cmd.select ("Inward", "resi 169 & chain A", merge=1)

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

cmd.color ("blue", "resi 724 & chain A")

cmd.select ("Outward", "resi 724 & chain A", merge=1)

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

cmd.color ("red", "resi 692 & chain A")

cmd.select ("Inward", "resi 692 & chain A", merge=1)

cmd.color ("red", "resi 666 & chain A")

cmd.select ("Inward", "resi 666 & chain A", merge=1)

cmd.color ("blue", "resi 667 & chain A")

cmd.select ("Outward", "resi 667 & chain A", merge=1)

cmd.color ("red", "resi 668 & chain A")

cmd.select ("Inward", "resi 668 & chain A", merge=1)

cmd.color ("blue", "resi 669 & chain A")

cmd.select ("Outward", "resi 669 & chain A", merge=1)

cmd.color ("red", "resi 670 & chain A")

cmd.select ("Inward", "resi 670 & chain A", merge=1)

cmd.color ("blue", "resi 671 & chain A")

cmd.select ("Outward", "resi 671 & chain A", merge=1)

cmd.color ("red", "resi 672 & chain A")

cmd.select ("Inward", "resi 672 & chain A", merge=1)

cmd.color ("blue", "resi 673 & chain A")

cmd.select ("Outward", "resi 673 & chain A", merge=1)

cmd.color ("red", "resi 674 & chain A")

cmd.select ("Inward", "resi 674 & chain A", merge=1)

cmd.color ("blue", "resi 675 & chain A")

cmd.select ("Outward", "resi 675 & chain A", merge=1)

cmd.color ("blue", "resi 676 & chain A")

cmd.select ("Outward", "resi 676 & chain A", merge=1)

cmd.color ("blue", "resi 641 & chain A")

cmd.select ("Outward", "resi 641 & chain A", merge=1)

cmd.color ("red", "resi 642 & chain A")

cmd.select ("Inward", "resi 642 & chain A", merge=1)

cmd.color ("blue", "resi 643 & chain A")

cmd.select ("Outward", "resi 643 & chain A", merge=1)

cmd.color ("red", "resi 644 & chain A")

cmd.select ("Inward", "resi 644 & chain A", merge=1)

cmd.color ("blue", "resi 645 & chain A")

cmd.select ("Outward", "resi 645 & chain A", merge=1)

cmd.color ("red", "resi 646 & chain A")

cmd.select ("Inward", "resi 646 & chain A", merge=1)

cmd.color ("blue", "resi 647 & chain A")

cmd.select ("Outward", "resi 647 & chain A", merge=1)

cmd.color ("red", "resi 648 & chain A")

cmd.select ("Inward", "resi 648 & chain A", merge=1)

cmd.color ("blue", "resi 649 & chain A")

cmd.select ("Outward", "resi 649 & chain A", merge=1)

cmd.color ("red", "resi 650 & chain A")

cmd.select ("Inward", "resi 650 & chain A", merge=1)

cmd.color ("blue", "resi 623 & chain A")

cmd.select ("Outward", "resi 623 & chain A", merge=1)

cmd.color ("red", "resi 624 & chain A")

cmd.select ("Inward", "resi 624 & chain A", merge=1)

cmd.color ("blue", "resi 625 & chain A")

cmd.select ("Outward", "resi 625 & chain A", merge=1)

cmd.color ("red", "resi 626 & chain A")

cmd.select ("Inward", "resi 626 & chain A", merge=1)

cmd.color ("blue", "resi 627 & chain A")

cmd.select ("Outward", "resi 627 & chain A", merge=1)

cmd.color ("red", "resi 628 & chain A")

cmd.select ("Inward", "resi 628 & chain A", merge=1)

cmd.color ("blue", "resi 629 & chain A")

cmd.select ("Outward", "resi 629 & chain A", merge=1)

cmd.color ("red", "resi 630 & chain A")

cmd.select ("Inward", "resi 630 & chain A", merge=1)

cmd.color ("blue", "resi 631 & chain A")

cmd.select ("Outward", "resi 631 & chain A", merge=1)

cmd.color ("red", "resi 632 & chain A")

cmd.select ("Inward", "resi 632 & chain A", merge=1)

cmd.color ("blue", "resi 633 & chain A")

cmd.select ("Outward", "resi 633 & chain A", merge=1)

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

cmd.color ("red", "resi 602 & chain A")

cmd.select ("Inward", "resi 602 & chain A", merge=1)

cmd.color ("blue", "resi 603 & chain A")

cmd.select ("Outward", "resi 603 & chain A", merge=1)

cmd.color ("red", "resi 604 & chain A")

cmd.select ("Inward", "resi 604 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("blue", "resi 606 & chain A")

cmd.select ("Outward", "resi 606 & chain A", merge=1)

cmd.color ("red", "resi 607 & chain A")

cmd.select ("Inward", "resi 607 & chain A", merge=1)

cmd.color ("blue", "resi 608 & chain A")

cmd.select ("Outward", "resi 608 & chain A", merge=1)

cmd.color ("blue", "resi 570 & chain A")

cmd.select ("Outward", "resi 570 & chain A", merge=1)

cmd.color ("red", "resi 571 & chain A")

cmd.select ("Inward", "resi 571 & chain A", merge=1)

cmd.color ("blue", "resi 572 & chain A")

cmd.select ("Outward", "resi 572 & chain A", merge=1)

cmd.color ("red", "resi 573 & chain A")

cmd.select ("Inward", "resi 573 & chain A", merge=1)

cmd.color ("red", "resi 574 & chain A")

cmd.select ("Inward", "resi 574 & chain A", merge=1)

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

cmd.color ("blue", "resi 585 & chain A")

cmd.select ("Outward", "resi 585 & chain A", merge=1)

cmd.color ("red", "resi 586 & chain A")

cmd.select ("Inward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

cmd.color ("blue", "resi 588 & chain A")

cmd.select ("Outward", "resi 588 & chain A", merge=1)

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

cmd.color ("red", "resi 533 & chain A")

cmd.select ("Inward", "resi 533 & chain A", merge=1)

cmd.color ("blue", "resi 534 & chain A")

cmd.select ("Outward", "resi 534 & chain A", merge=1)

cmd.color ("red", "resi 535 & chain A")

cmd.select ("Inward", "resi 535 & chain A", merge=1)

cmd.color ("blue", "resi 536 & chain A")

cmd.select ("Outward", "resi 536 & chain A", merge=1)

cmd.color ("red", "resi 537 & chain A")

cmd.select ("Inward", "resi 537 & chain A", merge=1)

cmd.color ("blue", "resi 538 & chain A")

cmd.select ("Outward", "resi 538 & chain A", merge=1)

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

cmd.color ("red", "resi 494 & chain A")

cmd.select ("Inward", "resi 494 & chain A", merge=1)

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

cmd.color ("blue", "resi 456 & chain A")

cmd.select ("Outward", "resi 456 & chain A", merge=1)

cmd.color ("red", "resi 457 & chain A")

cmd.select ("Inward", "resi 457 & chain A", merge=1)

cmd.color ("blue", "resi 458 & chain A")

cmd.select ("Outward", "resi 458 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("red", "resi 459 & chain A")

cmd.select ("Inward", "resi 459 & chain A", merge=1)

cmd.color ("red", "resi 371 & chain A")

cmd.select ("Inward", "resi 371 & chain A", merge=1)

cmd.color ("blue", "resi 372 & chain A")

cmd.select ("Outward", "resi 372 & chain A", merge=1)

cmd.color ("blue", "resi 460 & chain A")

cmd.select ("Outward", "resi 460 & chain A", merge=1)

cmd.color ("red", "resi 373 & chain A")

cmd.select ("Inward", "resi 373 & chain A", merge=1)

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("red", "resi 461 & chain A")

cmd.select ("Inward", "resi 461 & chain A", merge=1)

cmd.color ("red", "resi 375 & chain A")

cmd.select ("Inward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 462 & chain A")

cmd.select ("Outward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("red", "resi 463 & chain A")

cmd.select ("Inward", "resi 463 & chain A", merge=1)

cmd.color ("red", "resi 295 & chain A")

cmd.select ("Inward", "resi 295 & chain A", merge=1)

cmd.color ("red", "resi 377 & chain A")

cmd.select ("Inward", "resi 377 & chain A", merge=1)

cmd.color ("blue", "resi 296 & chain A")

cmd.select ("Outward", "resi 296 & chain A", merge=1)

cmd.color ("red", "resi 297 & chain A")

cmd.select ("Inward", "resi 297 & chain A", merge=1)

cmd.color ("blue", "resi 464 & chain A")

cmd.select ("Outward", "resi 464 & chain A", merge=1)

cmd.color ("blue", "resi 378 & chain A")

cmd.select ("Outward", "resi 378 & chain A", merge=1)

cmd.color ("red", "resi 379 & chain A")

cmd.select ("Inward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 298 & chain A")

cmd.select ("Outward", "resi 298 & chain A", merge=1)

cmd.color ("red", "resi 465 & chain A")

cmd.select ("Inward", "resi 465 & chain A", merge=1)

cmd.color ("red", "resi 299 & chain A")

cmd.select ("Inward", "resi 299 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("blue", "resi 466 & chain A")

cmd.select ("Outward", "resi 466 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.color ("red", "resi 381 & chain A")

cmd.select ("Inward", "resi 381 & chain A", merge=1)

cmd.color ("red", "resi 467 & chain A")

cmd.select ("Inward", "resi 467 & chain A", merge=1)

cmd.color ("red", "resi 301 & chain A")

cmd.select ("Inward", "resi 301 & chain A", merge=1)

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("blue", "resi 468 & chain A")

cmd.select ("Outward", "resi 468 & chain A", merge=1)

cmd.color ("blue", "resi 302 & chain A")

cmd.select ("Outward", "resi 302 & chain A", merge=1)

cmd.color ("red", "resi 383 & chain A")

cmd.select ("Inward", "resi 383 & chain A", merge=1)

cmd.color ("red", "resi 469 & chain A")

cmd.select ("Inward", "resi 469 & chain A", merge=1)

cmd.color ("red", "resi 303 & chain A")

cmd.select ("Inward", "resi 303 & chain A", merge=1)

cmd.color ("blue", "resi 384 & chain A")

cmd.select ("Outward", "resi 384 & chain A", merge=1)

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

cmd.color ("red", "resi 305 & chain A")

cmd.select ("Inward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 470 & chain A")

cmd.select ("Outward", "resi 470 & chain A", merge=1)

cmd.color ("red", "resi 385 & chain A")

cmd.select ("Inward", "resi 385 & chain A", merge=1)

cmd.color ("red", "resi 471 & chain A")

cmd.select ("Inward", "resi 471 & chain A", merge=1)

cmd.color ("blue", "resi 306 & chain A")

cmd.select ("Outward", "resi 306 & chain A", merge=1)

cmd.color ("red", "resi 307 & chain A")

cmd.select ("Inward", "resi 307 & chain A", merge=1)

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("red", "resi 387 & chain A")

cmd.select ("Inward", "resi 387 & chain A", merge=1)

cmd.color ("blue", "resi 472 & chain A")

cmd.select ("Outward", "resi 472 & chain A", merge=1)

cmd.color ("blue", "resi 308 & chain A")

cmd.select ("Outward", "resi 308 & chain A", merge=1)

cmd.color ("blue", "resi 473 & chain A")

cmd.select ("Outward", "resi 473 & chain A", merge=1)

cmd.color ("red", "resi 309 & chain A")

cmd.select ("Inward", "resi 309 & chain A", merge=1)

cmd.color ("blue", "resi 388 & chain A")

cmd.select ("Outward", "resi 388 & chain A", merge=1)

cmd.color ("red", "resi 389 & chain A")

cmd.select ("Inward", "resi 389 & chain A", merge=1)

cmd.color ("red", "resi 315 & chain A")

cmd.select ("Inward", "resi 315 & chain A", merge=1)

cmd.color ("red", "resi 313 & chain A")

cmd.select ("Inward", "resi 313 & chain A", merge=1)

cmd.color ("blue", "resi 314 & chain A")

cmd.select ("Outward", "resi 314 & chain A", merge=1)

cmd.color ("red", "resi 311 & chain A")

cmd.select ("Inward", "resi 311 & chain A", merge=1)

cmd.color ("red", "resi 316 & chain A")

cmd.select ("Inward", "resi 316 & chain A", merge=1)

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

cmd.color ("red", "resi 391 & chain A")

cmd.select ("Inward", "resi 391 & chain A", merge=1)

cmd.color ("blue", "resi 312 & chain A")

cmd.select ("Outward", "resi 312 & chain A", merge=1)

cmd.color ("blue", "resi 390 & chain A")

cmd.select ("Outward", "resi 390 & chain A", merge=1)

cmd.color ("blue", "resi 317 & chain A")

cmd.select ("Outward", "resi 317 & chain A", merge=1)

cmd.color ("blue", "resi 392 & chain A")

cmd.select ("Outward", "resi 392 & chain A", merge=1)

cmd.color ("red", "resi 393 & chain A")

cmd.select ("Inward", "resi 393 & chain A", merge=1)

cmd.color ("blue", "resi 394 & chain A")

cmd.select ("Outward", "resi 394 & chain A", merge=1)

cmd.color ("red", "resi 396 & chain A")

cmd.select ("Inward", "resi 396 & chain A", merge=1)

cmd.color ("red", "resi 397 & chain A")

cmd.select ("Inward", "resi 397 & chain A", merge=1)

cmd.color ("red", "resi 400 & chain A")

cmd.select ("Inward", "resi 400 & chain A", merge=1)

cmd.color ("blue", "resi 395 & chain A")

cmd.select ("Outward", "resi 395 & chain A", merge=1)

cmd.color ("blue", "resi 399 & chain A")

cmd.select ("Outward", "resi 399 & chain A", merge=1)

cmd.color ("blue", "resi 401 & chain A")

cmd.select ("Outward", "resi 401 & chain A", merge=1)

cmd.color ("blue", "resi 398 & chain A")

cmd.select ("Outward", "resi 398 & chain A", merge=1)

cmd.color ("red", "resi 340 & chain A")

cmd.select ("Inward", "resi 340 & chain A", merge=1)

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

cmd.color ("blue", "resi 431 & chain A")

cmd.select ("Outward", "resi 431 & chain A", merge=1)

cmd.color ("blue", "resi 347 & chain A")

cmd.select ("Outward", "resi 347 & chain A", merge=1)

cmd.color ("blue", "resi 274 & chain A")

cmd.select ("Outward", "resi 274 & chain A", merge=1)

cmd.color ("red", "resi 432 & chain A")

cmd.select ("Inward", "resi 432 & chain A", merge=1)

cmd.color ("red", "resi 275 & chain A")

cmd.select ("Inward", "resi 275 & chain A", merge=1)

cmd.color ("red", "resi 348 & chain A")

cmd.select ("Inward", "resi 348 & chain A", merge=1)

cmd.color ("blue", "resi 433 & chain A")

cmd.select ("Outward", "resi 433 & chain A", merge=1)

cmd.color ("red", "resi 434 & chain A")

cmd.select ("Inward", "resi 434 & chain A", merge=1)

cmd.color ("blue", "resi 276 & chain A")

cmd.select ("Outward", "resi 276 & chain A", merge=1)

cmd.color ("blue", "resi 349 & chain A")

cmd.select ("Outward", "resi 349 & chain A", merge=1)

cmd.color ("blue", "resi 435 & chain A")

cmd.select ("Outward", "resi 435 & chain A", merge=1)

cmd.color ("red", "resi 277 & chain A")

cmd.select ("Inward", "resi 277 & chain A", merge=1)

cmd.color ("red", "resi 350 & chain A")

cmd.select ("Inward", "resi 350 & chain A", merge=1)

cmd.color ("red", "resi 436 & chain A")

cmd.select ("Inward", "resi 436 & chain A", merge=1)

cmd.color ("blue", "resi 278 & chain A")

cmd.select ("Outward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 351 & chain A")

cmd.select ("Outward", "resi 351 & chain A", merge=1)

cmd.color ("blue", "resi 437 & chain A")

cmd.select ("Outward", "resi 437 & chain A", merge=1)

cmd.color ("red", "resi 438 & chain A")

cmd.select ("Inward", "resi 438 & chain A", merge=1)

cmd.color ("red", "resi 352 & chain A")

cmd.select ("Inward", "resi 352 & chain A", merge=1)

cmd.color ("red", "resi 279 & chain A")

cmd.select ("Inward", "resi 279 & chain A", merge=1)

cmd.color ("blue", "resi 439 & chain A")

cmd.select ("Outward", "resi 439 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("red", "resi 440 & chain A")

cmd.select ("Inward", "resi 440 & chain A", merge=1)

cmd.color ("blue", "resi 280 & chain A")

cmd.select ("Outward", "resi 280 & chain A", merge=1)

cmd.color ("red", "resi 354 & chain A")

cmd.select ("Inward", "resi 354 & chain A", merge=1)

cmd.color ("red", "resi 281 & chain A")

cmd.select ("Inward", "resi 281 & chain A", merge=1)

cmd.color ("blue", "resi 441 & chain A")

cmd.select ("Outward", "resi 441 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("red", "resi 442 & chain A")

cmd.select ("Inward", "resi 442 & chain A", merge=1)

cmd.color ("red", "resi 356 & chain A")

cmd.select ("Inward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 282 & chain A")

cmd.select ("Outward", "resi 282 & chain A", merge=1)

cmd.color ("blue", "resi 443 & chain A")

cmd.select ("Outward", "resi 443 & chain A", merge=1)

cmd.color ("red", "resi 283 & chain A")

cmd.select ("Inward", "resi 283 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("red", "resi 444 & chain A")

cmd.select ("Inward", "resi 444 & chain A", merge=1)

cmd.color ("red", "resi 358 & chain A")

cmd.select ("Inward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 284 & chain A")

cmd.select ("Outward", "resi 284 & chain A", merge=1)

cmd.color ("red", "resi 285 & chain A")

cmd.select ("Inward", "resi 285 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("red", "resi 446 & chain A")

cmd.select ("Inward", "resi 446 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("red", "resi 448 & chain A")

cmd.select ("Inward", "resi 448 & chain A", merge=1)

cmd.color ("blue", "resi 286 & chain A")

cmd.select ("Outward", "resi 286 & chain A", merge=1)

cmd.color ("blue", "resi 447 & chain A")

cmd.select ("Outward", "resi 447 & chain A", merge=1)

cmd.color ("red", "resi 360 & chain A")

cmd.select ("Inward", "resi 360 & chain A", merge=1)

cmd.color ("red", "resi 287 & chain A")

cmd.select ("Inward", "resi 287 & chain A", merge=1)

cmd.color ("red", "resi 450 & chain A")

cmd.select ("Inward", "resi 450 & chain A", merge=1)

cmd.color ("blue", "resi 449 & chain A")

cmd.select ("Outward", "resi 449 & chain A", merge=1)

cmd.color ("blue", "resi 361 & chain A")

cmd.select ("Outward", "resi 361 & chain A", merge=1)

cmd.color ("red", "resi 362 & chain A")

cmd.select ("Inward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 451 & chain A")

cmd.select ("Outward", "resi 451 & chain A", merge=1)

cmd.color ("blue", "resi 288 & chain A")

cmd.select ("Outward", "resi 288 & chain A", merge=1)

cmd.color ("red", "resi 452 & chain A")

cmd.select ("Inward", "resi 452 & chain A", merge=1)

cmd.color ("blue", "resi 363 & chain A")

cmd.select ("Outward", "resi 363 & chain A", merge=1)

cmd.color ("red", "resi 289 & chain A")

cmd.select ("Inward", "resi 289 & chain A", merge=1)

cmd.color ("red", "resi 364 & chain A")

cmd.select ("Inward", "resi 364 & chain A", merge=1)

cmd.color ("blue", "resi 453 & chain A")

cmd.select ("Outward", "resi 453 & chain A", merge=1)

cmd.color ("blue", "resi 365 & chain A")

cmd.select ("Outward", "resi 365 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("red", "resi 367 & chain A")

cmd.select ("Inward", "resi 367 & chain A", merge=1)

cmd.color ("blue", "resi 227 & chain A")

cmd.select ("Outward", "resi 227 & chain A", merge=1)

cmd.color ("red", "resi 228 & chain A")

cmd.select ("Inward", "resi 228 & chain A", merge=1)

cmd.color ("blue", "resi 229 & chain A")

cmd.select ("Outward", "resi 229 & chain A", merge=1)

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

cmd.color ("blue", "resi 237 & chain A")

cmd.select ("Outward", "resi 237 & chain A", merge=1)

cmd.color ("red", "resi 238 & chain A")

cmd.select ("Inward", "resi 238 & chain A", merge=1)

cmd.color ("blue", "resi 209 & chain A")

cmd.select ("Outward", "resi 209 & chain A", merge=1)

cmd.color ("red", "resi 210 & chain A")

cmd.select ("Inward", "resi 210 & chain A", merge=1)

cmd.color ("blue", "resi 211 & chain A")

cmd.select ("Outward", "resi 211 & chain A", merge=1)

cmd.color ("red", "resi 212 & chain A")

cmd.select ("Inward", "resi 212 & chain A", merge=1)

cmd.color ("blue", "resi 213 & chain A")

cmd.select ("Outward", "resi 213 & chain A", merge=1)

cmd.color ("red", "resi 214 & chain A")

cmd.select ("Inward", "resi 214 & chain A", merge=1)

cmd.color ("blue", "resi 215 & chain A")

cmd.select ("Outward", "resi 215 & chain A", merge=1)

cmd.color ("red", "resi 216 & chain A")

cmd.select ("Inward", "resi 216 & chain A", merge=1)

cmd.color ("blue", "resi 217 & chain A")

cmd.select ("Outward", "resi 217 & chain A", merge=1)

cmd.color ("red", "resi 218 & chain A")

cmd.select ("Inward", "resi 218 & chain A", merge=1)

cmd.color ("blue", "resi 219 & chain A")

cmd.select ("Outward", "resi 219 & chain A", merge=1)

cmd.color ("red", "resi 220 & chain A")

cmd.select ("Inward", "resi 220 & chain A", merge=1)

cmd.color ("blue", "resi 221 & chain A")

cmd.select ("Outward", "resi 221 & chain A", merge=1)

cmd.color ("red", "resi 222 & chain A")

cmd.select ("Inward", "resi 222 & chain A", merge=1)

cmd.color ("blue", "resi 223 & chain A")

cmd.select ("Outward", "resi 223 & chain A", merge=1)

cmd.color ("blue", "resi 224 & chain A")

cmd.select ("Outward", "resi 224 & chain A", merge=1)

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

cmd.color ("blue", "resi 180 & chain A")

cmd.select ("Outward", "resi 180 & chain A", merge=1)

cmd.color ("red", "resi 181 & chain A")

cmd.select ("Inward", "resi 181 & chain A", merge=1)

cmd.color ("blue", "resi 182 & chain A")

cmd.select ("Outward", "resi 182 & chain A", merge=1)

cmd.color ("blue", "resi 183 & chain A")

cmd.select ("Outward", "resi 183 & chain A", merge=1)

cmd.load_cgo( [9.0, -19.222834,-27.79011,-4.270555, -19.222834, -27.79011, -4.270555, 1, 1,1,0,0,0,1], "axis" )
