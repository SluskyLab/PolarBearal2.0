from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6R2Q.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain B ")


cmd.select("Bstrand30", "resi 680+681+682+683+684+685+686+687+688+689+690+691+692+693+694 & chain B ")


cmd.select("Bstrand29", "resi 644+645+646+647+648+649+650+651+652+653+654+655+656+657+658+659 & chain B ")


cmd.select("Bstrand28", "resi 625+626+627+628+629+630+631+632+633+634+635+636+637+638 & chain B ")


cmd.select("Bstrand26", "resi 572+573+574+575+576+577+578+579+580+581+582+583+584+585+586+587+588+589+590 & chain B ")


cmd.select("Bstrand27", "resi 598+599+600+601+602+603+604+605+606+607+608+609+610+611+612+613+614+615+616+617+618+619+620+621 & chain B ")


cmd.select("Bstrand25", "resi 546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+561+562+563 & chain B ")


cmd.select("Bstrand23", "resi 506+507+508+509+510+511+512+513+514+515+516+517+518 & chain B ")


cmd.select("Bstrand24", "resi 525+526+527+528+529+530+531+532+533+534+535+536+537+538+539+540 & chain B ")


cmd.select("Bstrand22", "resi 489+490+491+492+493+494+495+496+497+498+499+500 & chain B ")


cmd.select("Bstrand21", "resi 452+453+454+455+456+457+458+459+460+461+462+463+464 & chain B ")


cmd.select("Bstrand18", "resi 396+397+398+399+400+401+402+403+404+405+406+407 & chain B ")


cmd.select("Bstrand19", "resi 413+414+415+416+417+418+419+420+421+422+423+424+425 & chain B ")


cmd.select("Bstrand20", "resi 433+434+435+436+437+438+439+440+441+442+443+444+445 & chain B ")


cmd.select("Bstrand15", "resi 356+357+358+359+360+361+362+363+364+365+366+367+368+369 & chain B ")


cmd.select("Bstrand14", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350 & chain B ")


cmd.select("Bstrand13", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317 & chain B ")


cmd.select("Bstrand12", "resi 288+289+290+291+292+293+294+295+296+297+298+299 & chain B ")


cmd.select("Bstrand9", "resi 246+247+248+249+250+251+252+253+254+255+256+257+258+259 & chain B ")


cmd.select("Bstrand8", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+242 & chain B ")


cmd.select("Bstrand7", "resi 196+197+198+199+200+201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216 & chain B ")


cmd.select("Bstrand6", "resi 173+174+175+176+177+178+179+180+181+182+183+184+185+186+187+188+189+190+191 & chain B ")


cmd.select("Bstrand4", "resi 121+122+123+124+125+126+127+128+129+130+131+132+133+134+135 & chain B ")


cmd.select("Bstrand3", "resi 110+111+112+113 & chain B ")


cmd.select("Bstrand1", "resi 85+86+87+88 & chain B ")


cmd.select("Bstrand2", "resi 99+100+101+102 & chain B ")


cmd.select("barrel", "Bstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 52 & chain B")

cmd.select ("Inward", "resi 52 & chain B", merge=1)

cmd.color ("blue", "resi 53 & chain B")

cmd.select ("Outward", "resi 53 & chain B", merge=1)

cmd.color ("red", "resi 54 & chain B")

cmd.select ("Inward", "resi 54 & chain B", merge=1)

cmd.color ("blue", "resi 55 & chain B")

cmd.select ("Outward", "resi 55 & chain B", merge=1)

cmd.color ("red", "resi 56 & chain B")

cmd.select ("Inward", "resi 56 & chain B", merge=1)

cmd.color ("blue", "resi 57 & chain B")

cmd.select ("Outward", "resi 57 & chain B", merge=1)

cmd.color ("red", "resi 58 & chain B")

cmd.select ("Inward", "resi 58 & chain B", merge=1)

cmd.color ("blue", "resi 59 & chain B")

cmd.select ("Outward", "resi 59 & chain B", merge=1)

cmd.color ("red", "resi 60 & chain B")

cmd.select ("Inward", "resi 60 & chain B", merge=1)

cmd.color ("blue", "resi 61 & chain B")

cmd.select ("Outward", "resi 61 & chain B", merge=1)

cmd.color ("red", "resi 62 & chain B")

cmd.select ("Inward", "resi 62 & chain B", merge=1)

cmd.color ("blue", "resi 63 & chain B")

cmd.select ("Outward", "resi 63 & chain B", merge=1)

cmd.color ("blue", "resi 680 & chain B")

cmd.select ("Outward", "resi 680 & chain B", merge=1)

cmd.color ("blue", "resi 681 & chain B")

cmd.select ("Outward", "resi 681 & chain B", merge=1)

cmd.color ("red", "resi 682 & chain B")

cmd.select ("Inward", "resi 682 & chain B", merge=1)

cmd.color ("blue", "resi 683 & chain B")

cmd.select ("Outward", "resi 683 & chain B", merge=1)

cmd.color ("red", "resi 684 & chain B")

cmd.select ("Inward", "resi 684 & chain B", merge=1)

cmd.color ("blue", "resi 685 & chain B")

cmd.select ("Outward", "resi 685 & chain B", merge=1)

cmd.color ("red", "resi 686 & chain B")

cmd.select ("Inward", "resi 686 & chain B", merge=1)

cmd.color ("blue", "resi 687 & chain B")

cmd.select ("Outward", "resi 687 & chain B", merge=1)

cmd.color ("red", "resi 688 & chain B")

cmd.select ("Inward", "resi 688 & chain B", merge=1)

cmd.color ("blue", "resi 689 & chain B")

cmd.select ("Outward", "resi 689 & chain B", merge=1)

cmd.color ("red", "resi 690 & chain B")

cmd.select ("Inward", "resi 690 & chain B", merge=1)

cmd.color ("blue", "resi 691 & chain B")

cmd.select ("Outward", "resi 691 & chain B", merge=1)

cmd.color ("red", "resi 692 & chain B")

cmd.select ("Inward", "resi 692 & chain B", merge=1)

cmd.color ("blue", "resi 693 & chain B")

cmd.select ("Outward", "resi 693 & chain B", merge=1)

cmd.color ("blue", "resi 694 & chain B")

cmd.select ("Outward", "resi 694 & chain B", merge=1)

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

cmd.color ("red", "resi 657 & chain B")

cmd.select ("Inward", "resi 657 & chain B", merge=1)

cmd.color ("blue", "resi 658 & chain B")

cmd.select ("Outward", "resi 658 & chain B", merge=1)

cmd.color ("red", "resi 659 & chain B")

cmd.select ("Inward", "resi 659 & chain B", merge=1)

cmd.color ("red", "resi 625 & chain B")

cmd.select ("Inward", "resi 625 & chain B", merge=1)

cmd.color ("blue", "resi 626 & chain B")

cmd.select ("Outward", "resi 626 & chain B", merge=1)

cmd.color ("red", "resi 627 & chain B")

cmd.select ("Inward", "resi 627 & chain B", merge=1)

cmd.color ("blue", "resi 628 & chain B")

cmd.select ("Outward", "resi 628 & chain B", merge=1)

cmd.color ("red", "resi 629 & chain B")

cmd.select ("Inward", "resi 629 & chain B", merge=1)

cmd.color ("blue", "resi 630 & chain B")

cmd.select ("Outward", "resi 630 & chain B", merge=1)

cmd.color ("red", "resi 631 & chain B")

cmd.select ("Inward", "resi 631 & chain B", merge=1)

cmd.color ("blue", "resi 632 & chain B")

cmd.select ("Outward", "resi 632 & chain B", merge=1)

cmd.color ("red", "resi 633 & chain B")

cmd.select ("Inward", "resi 633 & chain B", merge=1)

cmd.color ("blue", "resi 634 & chain B")

cmd.select ("Outward", "resi 634 & chain B", merge=1)

cmd.color ("red", "resi 635 & chain B")

cmd.select ("Inward", "resi 635 & chain B", merge=1)

cmd.color ("blue", "resi 636 & chain B")

cmd.select ("Outward", "resi 636 & chain B", merge=1)

cmd.color ("red", "resi 637 & chain B")

cmd.select ("Inward", "resi 637 & chain B", merge=1)

cmd.color ("blue", "resi 638 & chain B")

cmd.select ("Outward", "resi 638 & chain B", merge=1)

cmd.color ("red", "resi 572 & chain B")

cmd.select ("Inward", "resi 572 & chain B", merge=1)

cmd.color ("blue", "resi 573 & chain B")

cmd.select ("Outward", "resi 573 & chain B", merge=1)

cmd.color ("red", "resi 574 & chain B")

cmd.select ("Inward", "resi 574 & chain B", merge=1)

cmd.color ("blue", "resi 575 & chain B")

cmd.select ("Outward", "resi 575 & chain B", merge=1)

cmd.color ("red", "resi 576 & chain B")

cmd.select ("Inward", "resi 576 & chain B", merge=1)

cmd.color ("blue", "resi 577 & chain B")

cmd.select ("Outward", "resi 577 & chain B", merge=1)

cmd.color ("red", "resi 578 & chain B")

cmd.select ("Inward", "resi 578 & chain B", merge=1)

cmd.color ("blue", "resi 579 & chain B")

cmd.select ("Outward", "resi 579 & chain B", merge=1)

cmd.color ("red", "resi 580 & chain B")

cmd.select ("Inward", "resi 580 & chain B", merge=1)

cmd.color ("blue", "resi 581 & chain B")

cmd.select ("Outward", "resi 581 & chain B", merge=1)

cmd.color ("red", "resi 582 & chain B")

cmd.select ("Inward", "resi 582 & chain B", merge=1)

cmd.color ("blue", "resi 583 & chain B")

cmd.select ("Outward", "resi 583 & chain B", merge=1)

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

cmd.color ("red", "resi 598 & chain B")

cmd.select ("Inward", "resi 598 & chain B", merge=1)

cmd.color ("blue", "resi 599 & chain B")

cmd.select ("Outward", "resi 599 & chain B", merge=1)

cmd.color ("red", "resi 600 & chain B")

cmd.select ("Inward", "resi 600 & chain B", merge=1)

cmd.color ("blue", "resi 601 & chain B")

cmd.select ("Outward", "resi 601 & chain B", merge=1)

cmd.color ("red", "resi 602 & chain B")

cmd.select ("Inward", "resi 602 & chain B", merge=1)

cmd.color ("blue", "resi 603 & chain B")

cmd.select ("Outward", "resi 603 & chain B", merge=1)

cmd.color ("red", "resi 604 & chain B")

cmd.select ("Inward", "resi 604 & chain B", merge=1)

cmd.color ("blue", "resi 605 & chain B")

cmd.select ("Outward", "resi 605 & chain B", merge=1)

cmd.color ("red", "resi 606 & chain B")

cmd.select ("Inward", "resi 606 & chain B", merge=1)

cmd.color ("blue", "resi 607 & chain B")

cmd.select ("Outward", "resi 607 & chain B", merge=1)

cmd.color ("red", "resi 608 & chain B")

cmd.select ("Inward", "resi 608 & chain B", merge=1)

cmd.color ("blue", "resi 609 & chain B")

cmd.select ("Outward", "resi 609 & chain B", merge=1)

cmd.color ("red", "resi 610 & chain B")

cmd.select ("Inward", "resi 610 & chain B", merge=1)

cmd.color ("blue", "resi 611 & chain B")

cmd.select ("Outward", "resi 611 & chain B", merge=1)

cmd.color ("red", "resi 612 & chain B")

cmd.select ("Inward", "resi 612 & chain B", merge=1)

cmd.color ("blue", "resi 613 & chain B")

cmd.select ("Outward", "resi 613 & chain B", merge=1)

cmd.color ("red", "resi 614 & chain B")

cmd.select ("Inward", "resi 614 & chain B", merge=1)

cmd.color ("red", "resi 615 & chain B")

cmd.select ("Inward", "resi 615 & chain B", merge=1)

cmd.color ("red", "resi 616 & chain B")

cmd.select ("Inward", "resi 616 & chain B", merge=1)

cmd.color ("blue", "resi 617 & chain B")

cmd.select ("Outward", "resi 617 & chain B", merge=1)

cmd.color ("blue", "resi 618 & chain B")

cmd.select ("Outward", "resi 618 & chain B", merge=1)

cmd.color ("red", "resi 619 & chain B")

cmd.select ("Inward", "resi 619 & chain B", merge=1)

cmd.color ("blue", "resi 620 & chain B")

cmd.select ("Outward", "resi 620 & chain B", merge=1)

cmd.color ("red", "resi 621 & chain B")

cmd.select ("Inward", "resi 621 & chain B", merge=1)

cmd.color ("blue", "resi 546 & chain B")

cmd.select ("Outward", "resi 546 & chain B", merge=1)

cmd.color ("red", "resi 547 & chain B")

cmd.select ("Inward", "resi 547 & chain B", merge=1)

cmd.color ("blue", "resi 548 & chain B")

cmd.select ("Outward", "resi 548 & chain B", merge=1)

cmd.color ("red", "resi 549 & chain B")

cmd.select ("Inward", "resi 549 & chain B", merge=1)

cmd.color ("blue", "resi 550 & chain B")

cmd.select ("Outward", "resi 550 & chain B", merge=1)

cmd.color ("red", "resi 551 & chain B")

cmd.select ("Inward", "resi 551 & chain B", merge=1)

cmd.color ("blue", "resi 552 & chain B")

cmd.select ("Outward", "resi 552 & chain B", merge=1)

cmd.color ("red", "resi 553 & chain B")

cmd.select ("Inward", "resi 553 & chain B", merge=1)

cmd.color ("blue", "resi 554 & chain B")

cmd.select ("Outward", "resi 554 & chain B", merge=1)

cmd.color ("red", "resi 555 & chain B")

cmd.select ("Inward", "resi 555 & chain B", merge=1)

cmd.color ("blue", "resi 556 & chain B")

cmd.select ("Outward", "resi 556 & chain B", merge=1)

cmd.color ("red", "resi 557 & chain B")

cmd.select ("Inward", "resi 557 & chain B", merge=1)

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

cmd.color ("blue", "resi 506 & chain B")

cmd.select ("Outward", "resi 506 & chain B", merge=1)

cmd.color ("red", "resi 507 & chain B")

cmd.select ("Inward", "resi 507 & chain B", merge=1)

cmd.color ("blue", "resi 508 & chain B")

cmd.select ("Outward", "resi 508 & chain B", merge=1)

cmd.color ("red", "resi 509 & chain B")

cmd.select ("Inward", "resi 509 & chain B", merge=1)

cmd.color ("blue", "resi 510 & chain B")

cmd.select ("Outward", "resi 510 & chain B", merge=1)

cmd.color ("red", "resi 511 & chain B")

cmd.select ("Inward", "resi 511 & chain B", merge=1)

cmd.color ("blue", "resi 512 & chain B")

cmd.select ("Outward", "resi 512 & chain B", merge=1)

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

cmd.color ("red", "resi 535 & chain B")

cmd.select ("Inward", "resi 535 & chain B", merge=1)

cmd.color ("blue", "resi 536 & chain B")

cmd.select ("Outward", "resi 536 & chain B", merge=1)

cmd.color ("red", "resi 537 & chain B")

cmd.select ("Inward", "resi 537 & chain B", merge=1)

cmd.color ("blue", "resi 538 & chain B")

cmd.select ("Outward", "resi 538 & chain B", merge=1)

cmd.color ("red", "resi 539 & chain B")

cmd.select ("Inward", "resi 539 & chain B", merge=1)

cmd.color ("blue", "resi 540 & chain B")

cmd.select ("Outward", "resi 540 & chain B", merge=1)

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

cmd.color ("blue", "resi 496 & chain B")

cmd.select ("Outward", "resi 496 & chain B", merge=1)

cmd.color ("red", "resi 497 & chain B")

cmd.select ("Inward", "resi 497 & chain B", merge=1)

cmd.color ("blue", "resi 498 & chain B")

cmd.select ("Outward", "resi 498 & chain B", merge=1)

cmd.color ("red", "resi 499 & chain B")

cmd.select ("Inward", "resi 499 & chain B", merge=1)

cmd.color ("blue", "resi 500 & chain B")

cmd.select ("Outward", "resi 500 & chain B", merge=1)

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

cmd.color ("red", "resi 396 & chain B")

cmd.select ("Inward", "resi 396 & chain B", merge=1)

cmd.color ("blue", "resi 397 & chain B")

cmd.select ("Outward", "resi 397 & chain B", merge=1)

cmd.color ("red", "resi 398 & chain B")

cmd.select ("Inward", "resi 398 & chain B", merge=1)

cmd.color ("blue", "resi 399 & chain B")

cmd.select ("Outward", "resi 399 & chain B", merge=1)

cmd.color ("red", "resi 400 & chain B")

cmd.select ("Inward", "resi 400 & chain B", merge=1)

cmd.color ("blue", "resi 401 & chain B")

cmd.select ("Outward", "resi 401 & chain B", merge=1)

cmd.color ("red", "resi 402 & chain B")

cmd.select ("Inward", "resi 402 & chain B", merge=1)

cmd.color ("blue", "resi 403 & chain B")

cmd.select ("Outward", "resi 403 & chain B", merge=1)

cmd.color ("red", "resi 404 & chain B")

cmd.select ("Inward", "resi 404 & chain B", merge=1)

cmd.color ("blue", "resi 405 & chain B")

cmd.select ("Outward", "resi 405 & chain B", merge=1)

cmd.color ("red", "resi 406 & chain B")

cmd.select ("Inward", "resi 406 & chain B", merge=1)

cmd.color ("blue", "resi 407 & chain B")

cmd.select ("Outward", "resi 407 & chain B", merge=1)

cmd.color ("blue", "resi 413 & chain B")

cmd.select ("Outward", "resi 413 & chain B", merge=1)

cmd.color ("red", "resi 414 & chain B")

cmd.select ("Inward", "resi 414 & chain B", merge=1)

cmd.color ("blue", "resi 415 & chain B")

cmd.select ("Outward", "resi 415 & chain B", merge=1)

cmd.color ("red", "resi 416 & chain B")

cmd.select ("Inward", "resi 416 & chain B", merge=1)

cmd.color ("blue", "resi 417 & chain B")

cmd.select ("Outward", "resi 417 & chain B", merge=1)

cmd.color ("red", "resi 418 & chain B")

cmd.select ("Inward", "resi 418 & chain B", merge=1)

cmd.color ("blue", "resi 419 & chain B")

cmd.select ("Outward", "resi 419 & chain B", merge=1)

cmd.color ("red", "resi 420 & chain B")

cmd.select ("Inward", "resi 420 & chain B", merge=1)

cmd.color ("blue", "resi 421 & chain B")

cmd.select ("Outward", "resi 421 & chain B", merge=1)

cmd.color ("red", "resi 422 & chain B")

cmd.select ("Inward", "resi 422 & chain B", merge=1)

cmd.color ("blue", "resi 423 & chain B")

cmd.select ("Outward", "resi 423 & chain B", merge=1)

cmd.color ("red", "resi 424 & chain B")

cmd.select ("Inward", "resi 424 & chain B", merge=1)

cmd.color ("blue", "resi 425 & chain B")

cmd.select ("Outward", "resi 425 & chain B", merge=1)

cmd.color ("blue", "resi 433 & chain B")

cmd.select ("Outward", "resi 433 & chain B", merge=1)

cmd.color ("red", "resi 434 & chain B")

cmd.select ("Inward", "resi 434 & chain B", merge=1)

cmd.color ("blue", "resi 435 & chain B")

cmd.select ("Outward", "resi 435 & chain B", merge=1)

cmd.color ("red", "resi 436 & chain B")

cmd.select ("Inward", "resi 436 & chain B", merge=1)

cmd.color ("blue", "resi 437 & chain B")

cmd.select ("Outward", "resi 437 & chain B", merge=1)

cmd.color ("red", "resi 438 & chain B")

cmd.select ("Inward", "resi 438 & chain B", merge=1)

cmd.color ("blue", "resi 439 & chain B")

cmd.select ("Outward", "resi 439 & chain B", merge=1)

cmd.color ("red", "resi 440 & chain B")

cmd.select ("Inward", "resi 440 & chain B", merge=1)

cmd.color ("blue", "resi 441 & chain B")

cmd.select ("Outward", "resi 441 & chain B", merge=1)

cmd.color ("red", "resi 442 & chain B")

cmd.select ("Inward", "resi 442 & chain B", merge=1)

cmd.color ("blue", "resi 443 & chain B")

cmd.select ("Outward", "resi 443 & chain B", merge=1)

cmd.color ("red", "resi 444 & chain B")

cmd.select ("Inward", "resi 444 & chain B", merge=1)

cmd.color ("blue", "resi 445 & chain B")

cmd.select ("Outward", "resi 445 & chain B", merge=1)

cmd.color ("blue", "resi 356 & chain B")

cmd.select ("Outward", "resi 356 & chain B", merge=1)

cmd.color ("red", "resi 357 & chain B")

cmd.select ("Inward", "resi 357 & chain B", merge=1)

cmd.color ("blue", "resi 358 & chain B")

cmd.select ("Outward", "resi 358 & chain B", merge=1)

cmd.color ("red", "resi 359 & chain B")

cmd.select ("Inward", "resi 359 & chain B", merge=1)

cmd.color ("blue", "resi 360 & chain B")

cmd.select ("Outward", "resi 360 & chain B", merge=1)

cmd.color ("red", "resi 361 & chain B")

cmd.select ("Inward", "resi 361 & chain B", merge=1)

cmd.color ("blue", "resi 362 & chain B")

cmd.select ("Outward", "resi 362 & chain B", merge=1)

cmd.color ("red", "resi 363 & chain B")

cmd.select ("Inward", "resi 363 & chain B", merge=1)

cmd.color ("blue", "resi 364 & chain B")

cmd.select ("Outward", "resi 364 & chain B", merge=1)

cmd.color ("red", "resi 365 & chain B")

cmd.select ("Inward", "resi 365 & chain B", merge=1)

cmd.color ("blue", "resi 366 & chain B")

cmd.select ("Outward", "resi 366 & chain B", merge=1)

cmd.color ("red", "resi 367 & chain B")

cmd.select ("Inward", "resi 367 & chain B", merge=1)

cmd.color ("blue", "resi 368 & chain B")

cmd.select ("Outward", "resi 368 & chain B", merge=1)

cmd.color ("red", "resi 369 & chain B")

cmd.select ("Inward", "resi 369 & chain B", merge=1)

cmd.color ("red", "resi 337 & chain B")

cmd.select ("Inward", "resi 337 & chain B", merge=1)

cmd.color ("blue", "resi 338 & chain B")

cmd.select ("Outward", "resi 338 & chain B", merge=1)

cmd.color ("red", "resi 339 & chain B")

cmd.select ("Inward", "resi 339 & chain B", merge=1)

cmd.color ("blue", "resi 340 & chain B")

cmd.select ("Outward", "resi 340 & chain B", merge=1)

cmd.color ("red", "resi 341 & chain B")

cmd.select ("Inward", "resi 341 & chain B", merge=1)

cmd.color ("blue", "resi 342 & chain B")

cmd.select ("Outward", "resi 342 & chain B", merge=1)

cmd.color ("red", "resi 343 & chain B")

cmd.select ("Inward", "resi 343 & chain B", merge=1)

cmd.color ("blue", "resi 344 & chain B")

cmd.select ("Outward", "resi 344 & chain B", merge=1)

cmd.color ("red", "resi 345 & chain B")

cmd.select ("Inward", "resi 345 & chain B", merge=1)

cmd.color ("blue", "resi 346 & chain B")

cmd.select ("Outward", "resi 346 & chain B", merge=1)

cmd.color ("red", "resi 347 & chain B")

cmd.select ("Inward", "resi 347 & chain B", merge=1)

cmd.color ("blue", "resi 348 & chain B")

cmd.select ("Outward", "resi 348 & chain B", merge=1)

cmd.color ("red", "resi 349 & chain B")

cmd.select ("Inward", "resi 349 & chain B", merge=1)

cmd.color ("blue", "resi 350 & chain B")

cmd.select ("Outward", "resi 350 & chain B", merge=1)

cmd.color ("blue", "resi 304 & chain B")

cmd.select ("Outward", "resi 304 & chain B", merge=1)

cmd.color ("red", "resi 305 & chain B")

cmd.select ("Inward", "resi 305 & chain B", merge=1)

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

cmd.color ("red", "resi 288 & chain B")

cmd.select ("Inward", "resi 288 & chain B", merge=1)

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

cmd.color ("blue", "resi 246 & chain B")

cmd.select ("Outward", "resi 246 & chain B", merge=1)

cmd.color ("red", "resi 247 & chain B")

cmd.select ("Inward", "resi 247 & chain B", merge=1)

cmd.color ("blue", "resi 248 & chain B")

cmd.select ("Outward", "resi 248 & chain B", merge=1)

cmd.color ("red", "resi 249 & chain B")

cmd.select ("Inward", "resi 249 & chain B", merge=1)

cmd.color ("blue", "resi 250 & chain B")

cmd.select ("Outward", "resi 250 & chain B", merge=1)

cmd.color ("red", "resi 251 & chain B")

cmd.select ("Inward", "resi 251 & chain B", merge=1)

cmd.color ("blue", "resi 252 & chain B")

cmd.select ("Outward", "resi 252 & chain B", merge=1)

cmd.color ("red", "resi 253 & chain B")

cmd.select ("Inward", "resi 253 & chain B", merge=1)

cmd.color ("blue", "resi 254 & chain B")

cmd.select ("Outward", "resi 254 & chain B", merge=1)

cmd.color ("red", "resi 255 & chain B")

cmd.select ("Inward", "resi 255 & chain B", merge=1)

cmd.color ("blue", "resi 256 & chain B")

cmd.select ("Outward", "resi 256 & chain B", merge=1)

cmd.color ("red", "resi 257 & chain B")

cmd.select ("Inward", "resi 257 & chain B", merge=1)

cmd.color ("blue", "resi 258 & chain B")

cmd.select ("Outward", "resi 258 & chain B", merge=1)

cmd.color ("red", "resi 259 & chain B")

cmd.select ("Inward", "resi 259 & chain B", merge=1)

cmd.color ("blue", "resi 221 & chain B")

cmd.select ("Outward", "resi 221 & chain B", merge=1)

cmd.color ("red", "resi 222 & chain B")

cmd.select ("Inward", "resi 222 & chain B", merge=1)

cmd.color ("blue", "resi 223 & chain B")

cmd.select ("Outward", "resi 223 & chain B", merge=1)

cmd.color ("red", "resi 224 & chain B")

cmd.select ("Inward", "resi 224 & chain B", merge=1)

cmd.color ("blue", "resi 225 & chain B")

cmd.select ("Outward", "resi 225 & chain B", merge=1)

cmd.color ("red", "resi 226 & chain B")

cmd.select ("Inward", "resi 226 & chain B", merge=1)

cmd.color ("blue", "resi 227 & chain B")

cmd.select ("Outward", "resi 227 & chain B", merge=1)

cmd.color ("red", "resi 228 & chain B")

cmd.select ("Inward", "resi 228 & chain B", merge=1)

cmd.color ("blue", "resi 229 & chain B")

cmd.select ("Outward", "resi 229 & chain B", merge=1)

cmd.color ("red", "resi 230 & chain B")

cmd.select ("Inward", "resi 230 & chain B", merge=1)

cmd.color ("blue", "resi 231 & chain B")

cmd.select ("Outward", "resi 231 & chain B", merge=1)

cmd.color ("red", "resi 232 & chain B")

cmd.select ("Inward", "resi 232 & chain B", merge=1)

cmd.color ("blue", "resi 233 & chain B")

cmd.select ("Outward", "resi 233 & chain B", merge=1)

cmd.color ("red", "resi 234 & chain B")

cmd.select ("Inward", "resi 234 & chain B", merge=1)

cmd.color ("blue", "resi 235 & chain B")

cmd.select ("Outward", "resi 235 & chain B", merge=1)

cmd.color ("red", "resi 236 & chain B")

cmd.select ("Inward", "resi 236 & chain B", merge=1)

cmd.color ("blue", "resi 237 & chain B")

cmd.select ("Outward", "resi 237 & chain B", merge=1)

cmd.color ("red", "resi 238 & chain B")

cmd.select ("Inward", "resi 238 & chain B", merge=1)

cmd.color ("blue", "resi 239 & chain B")

cmd.select ("Outward", "resi 239 & chain B", merge=1)

cmd.color ("red", "resi 240 & chain B")

cmd.select ("Inward", "resi 240 & chain B", merge=1)

cmd.color ("blue", "resi 241 & chain B")

cmd.select ("Outward", "resi 241 & chain B", merge=1)

cmd.color ("red", "resi 242 & chain B")

cmd.select ("Inward", "resi 242 & chain B", merge=1)

cmd.color ("blue", "resi 196 & chain B")

cmd.select ("Outward", "resi 196 & chain B", merge=1)

cmd.color ("red", "resi 197 & chain B")

cmd.select ("Inward", "resi 197 & chain B", merge=1)

cmd.color ("blue", "resi 198 & chain B")

cmd.select ("Outward", "resi 198 & chain B", merge=1)

cmd.color ("red", "resi 199 & chain B")

cmd.select ("Inward", "resi 199 & chain B", merge=1)

cmd.color ("blue", "resi 200 & chain B")

cmd.select ("Outward", "resi 200 & chain B", merge=1)

cmd.color ("red", "resi 201 & chain B")

cmd.select ("Inward", "resi 201 & chain B", merge=1)

cmd.color ("blue", "resi 202 & chain B")

cmd.select ("Outward", "resi 202 & chain B", merge=1)

cmd.color ("red", "resi 203 & chain B")

cmd.select ("Inward", "resi 203 & chain B", merge=1)

cmd.color ("blue", "resi 204 & chain B")

cmd.select ("Outward", "resi 204 & chain B", merge=1)

cmd.color ("red", "resi 205 & chain B")

cmd.select ("Inward", "resi 205 & chain B", merge=1)

cmd.color ("blue", "resi 206 & chain B")

cmd.select ("Outward", "resi 206 & chain B", merge=1)

cmd.color ("red", "resi 207 & chain B")

cmd.select ("Inward", "resi 207 & chain B", merge=1)

cmd.color ("blue", "resi 208 & chain B")

cmd.select ("Outward", "resi 208 & chain B", merge=1)

cmd.color ("red", "resi 209 & chain B")

cmd.select ("Inward", "resi 209 & chain B", merge=1)

cmd.color ("blue", "resi 210 & chain B")

cmd.select ("Outward", "resi 210 & chain B", merge=1)

cmd.color ("red", "resi 211 & chain B")

cmd.select ("Inward", "resi 211 & chain B", merge=1)

cmd.color ("blue", "resi 212 & chain B")

cmd.select ("Outward", "resi 212 & chain B", merge=1)

cmd.color ("red", "resi 213 & chain B")

cmd.select ("Inward", "resi 213 & chain B", merge=1)

cmd.color ("blue", "resi 214 & chain B")

cmd.select ("Outward", "resi 214 & chain B", merge=1)

cmd.color ("red", "resi 215 & chain B")

cmd.select ("Inward", "resi 215 & chain B", merge=1)

cmd.color ("blue", "resi 216 & chain B")

cmd.select ("Outward", "resi 216 & chain B", merge=1)

cmd.color ("blue", "resi 173 & chain B")

cmd.select ("Outward", "resi 173 & chain B", merge=1)

cmd.color ("blue", "resi 174 & chain B")

cmd.select ("Outward", "resi 174 & chain B", merge=1)

cmd.color ("red", "resi 175 & chain B")

cmd.select ("Inward", "resi 175 & chain B", merge=1)

cmd.color ("blue", "resi 176 & chain B")

cmd.select ("Outward", "resi 176 & chain B", merge=1)

cmd.color ("red", "resi 177 & chain B")

cmd.select ("Inward", "resi 177 & chain B", merge=1)

cmd.color ("blue", "resi 178 & chain B")

cmd.select ("Outward", "resi 178 & chain B", merge=1)

cmd.color ("red", "resi 179 & chain B")

cmd.select ("Inward", "resi 179 & chain B", merge=1)

cmd.color ("blue", "resi 180 & chain B")

cmd.select ("Outward", "resi 180 & chain B", merge=1)

cmd.color ("red", "resi 181 & chain B")

cmd.select ("Inward", "resi 181 & chain B", merge=1)

cmd.color ("blue", "resi 182 & chain B")

cmd.select ("Outward", "resi 182 & chain B", merge=1)

cmd.color ("red", "resi 183 & chain B")

cmd.select ("Inward", "resi 183 & chain B", merge=1)

cmd.color ("blue", "resi 184 & chain B")

cmd.select ("Outward", "resi 184 & chain B", merge=1)

cmd.color ("red", "resi 185 & chain B")

cmd.select ("Inward", "resi 185 & chain B", merge=1)

cmd.color ("blue", "resi 186 & chain B")

cmd.select ("Outward", "resi 186 & chain B", merge=1)

cmd.color ("red", "resi 187 & chain B")

cmd.select ("Inward", "resi 187 & chain B", merge=1)

cmd.color ("blue", "resi 188 & chain B")

cmd.select ("Outward", "resi 188 & chain B", merge=1)

cmd.color ("red", "resi 189 & chain B")

cmd.select ("Inward", "resi 189 & chain B", merge=1)

cmd.color ("blue", "resi 190 & chain B")

cmd.select ("Outward", "resi 190 & chain B", merge=1)

cmd.color ("blue", "resi 191 & chain B")

cmd.select ("Outward", "resi 191 & chain B", merge=1)

cmd.color ("blue", "resi 121 & chain B")

cmd.select ("Outward", "resi 121 & chain B", merge=1)

cmd.color ("red", "resi 122 & chain B")

cmd.select ("Inward", "resi 122 & chain B", merge=1)

cmd.color ("blue", "resi 123 & chain B")

cmd.select ("Outward", "resi 123 & chain B", merge=1)

cmd.color ("red", "resi 124 & chain B")

cmd.select ("Inward", "resi 124 & chain B", merge=1)

cmd.color ("blue", "resi 125 & chain B")

cmd.select ("Outward", "resi 125 & chain B", merge=1)

cmd.color ("red", "resi 126 & chain B")

cmd.select ("Inward", "resi 126 & chain B", merge=1)

cmd.color ("blue", "resi 127 & chain B")

cmd.select ("Outward", "resi 127 & chain B", merge=1)

cmd.color ("red", "resi 128 & chain B")

cmd.select ("Inward", "resi 128 & chain B", merge=1)

cmd.color ("blue", "resi 129 & chain B")

cmd.select ("Outward", "resi 129 & chain B", merge=1)

cmd.color ("red", "resi 130 & chain B")

cmd.select ("Inward", "resi 130 & chain B", merge=1)

cmd.color ("blue", "resi 131 & chain B")

cmd.select ("Outward", "resi 131 & chain B", merge=1)

cmd.color ("red", "resi 132 & chain B")

cmd.select ("Inward", "resi 132 & chain B", merge=1)

cmd.color ("blue", "resi 133 & chain B")

cmd.select ("Outward", "resi 133 & chain B", merge=1)

cmd.color ("red", "resi 134 & chain B")

cmd.select ("Inward", "resi 134 & chain B", merge=1)

cmd.color ("blue", "resi 135 & chain B")

cmd.select ("Outward", "resi 135 & chain B", merge=1)

cmd.color ("red", "resi 110 & chain B")

cmd.select ("Inward", "resi 110 & chain B", merge=1)

cmd.color ("blue", "resi 111 & chain B")

cmd.select ("Outward", "resi 111 & chain B", merge=1)

cmd.color ("red", "resi 112 & chain B")

cmd.select ("Inward", "resi 112 & chain B", merge=1)

cmd.color ("blue", "resi 113 & chain B")

cmd.select ("Outward", "resi 113 & chain B", merge=1)

cmd.color ("blue", "resi 85 & chain B")

cmd.select ("Outward", "resi 85 & chain B", merge=1)

cmd.color ("red", "resi 86 & chain B")

cmd.select ("Inward", "resi 86 & chain B", merge=1)

cmd.color ("blue", "resi 87 & chain B")

cmd.select ("Outward", "resi 87 & chain B", merge=1)

cmd.color ("red", "resi 88 & chain B")

cmd.select ("Inward", "resi 88 & chain B", merge=1)

cmd.color ("blue", "resi 99 & chain B")

cmd.select ("Outward", "resi 99 & chain B", merge=1)

cmd.color ("red", "resi 100 & chain B")

cmd.select ("Inward", "resi 100 & chain B", merge=1)

cmd.color ("blue", "resi 101 & chain B")

cmd.select ("Outward", "resi 101 & chain B", merge=1)

cmd.color ("red", "resi 102 & chain B")

cmd.select ("Inward", "resi 102 & chain B", merge=1)

cmd.load_cgo( [9.0, 19.916616,50.489433,4.4791536, 19.916616, 50.489433, 4.4791536, 1, 1,1,0,0,0,1], "axis" )
