from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2IAH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand15", "resi 278+279+280+281+282+283+284+285+286 & chain A ")


cmd.select("Astrand43", "resi 806+807+808+809+810+811+812 & chain A ")


cmd.select("Astrand40", "resi 776+777+778+779+780+781+782 & chain A ")


cmd.select("Astrand39", "resi 760+761+762+763+764+765+766+767+768+769+770 & chain A ")


cmd.select("Astrand36", "resi 728+729+730+731+732+733+734+735+736+737 & chain A ")


cmd.select("Astrand35", "resi 711+712+713+714+715+716+717+718+719+720 & chain A ")


cmd.select("Astrand33", "resi 685+686+687+688+689+690+691+692+693 & chain A ")


cmd.select("Astrand32", "resi 664+665+666+667+668+669+670+671+672+673+674+675+676+677+678+679+680+681+682 & chain A ")


cmd.select("Astrand30", "resi 611+612+613+614+615+616+617+618+619+620+621+622+623+624 & chain A ")


cmd.select("Astrand31", "resi 629+630+631+632+633+634+635+636+637+638+639+640+641+642+643+644+645 & chain A ")


cmd.select("Astrand29", "resi 583+584+585+586+587+588+589+590+591+592+593+594 & chain A ")


cmd.select("Astrand28", "resi 563+564+565+566+567+568+569+570+571+572+573+574+575+576+577+578 & chain A ")


cmd.select("Astrand27", "resi 543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558 & chain A ")


cmd.select("Astrand26", "resi 520+521+522+523+524+525+526+527+528+529+530+531+532+533+534+535+536+537 & chain A ")


cmd.select("Astrand24", "resi 471+472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490 & chain A ")


cmd.select("Astrand23", "resi 441+442+443+444+445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464+465+466 & chain A ")


cmd.select("Astrand22", "resi 411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+426+427+428+429+430 & chain A ")


cmd.select("Astrand21", "resi 392+393+394+395+396+397+398+399+400+401+402+403+404+405 & chain A ")


cmd.select("Astrand19", "resi 344+345+346+347+348+349+350+351+352+353+354+355+356+357+358 & chain A ")


cmd.select("Astrand18", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341 & chain A ")


cmd.select("Astrand17", "resi 307+308+309+310+311+312+313+314+315+316+317+318+319 & chain A ")


cmd.select("Astrand16", "resi 290+291+292+293+294+295+296+297+298+299+300 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 278 & chain A")

cmd.select ("Inward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 279 & chain A")

cmd.select ("Outward", "resi 279 & chain A", merge=1)

cmd.color ("red", "resi 280 & chain A")

cmd.select ("Inward", "resi 280 & chain A", merge=1)

cmd.color ("blue", "resi 281 & chain A")

cmd.select ("Outward", "resi 281 & chain A", merge=1)

cmd.color ("red", "resi 282 & chain A")

cmd.select ("Inward", "resi 282 & chain A", merge=1)

cmd.color ("blue", "resi 283 & chain A")

cmd.select ("Outward", "resi 283 & chain A", merge=1)

cmd.color ("red", "resi 284 & chain A")

cmd.select ("Inward", "resi 284 & chain A", merge=1)

cmd.color ("blue", "resi 285 & chain A")

cmd.select ("Outward", "resi 285 & chain A", merge=1)

cmd.color ("red", "resi 286 & chain A")

cmd.select ("Inward", "resi 286 & chain A", merge=1)

cmd.color ("red", "resi 806 & chain A")

cmd.select ("Inward", "resi 806 & chain A", merge=1)

cmd.color ("blue", "resi 807 & chain A")

cmd.select ("Outward", "resi 807 & chain A", merge=1)

cmd.color ("red", "resi 808 & chain A")

cmd.select ("Inward", "resi 808 & chain A", merge=1)

cmd.color ("blue", "resi 809 & chain A")

cmd.select ("Outward", "resi 809 & chain A", merge=1)

cmd.color ("red", "resi 810 & chain A")

cmd.select ("Inward", "resi 810 & chain A", merge=1)

cmd.color ("blue", "resi 811 & chain A")

cmd.select ("Outward", "resi 811 & chain A", merge=1)

cmd.color ("red", "resi 812 & chain A")

cmd.select ("Inward", "resi 812 & chain A", merge=1)

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

cmd.color ("red", "resi 760 & chain A")

cmd.select ("Inward", "resi 760 & chain A", merge=1)

cmd.color ("blue", "resi 761 & chain A")

cmd.select ("Outward", "resi 761 & chain A", merge=1)

cmd.color ("red", "resi 762 & chain A")

cmd.select ("Inward", "resi 762 & chain A", merge=1)

cmd.color ("blue", "resi 763 & chain A")

cmd.select ("Outward", "resi 763 & chain A", merge=1)

cmd.color ("red", "resi 764 & chain A")

cmd.select ("Inward", "resi 764 & chain A", merge=1)

cmd.color ("blue", "resi 765 & chain A")

cmd.select ("Outward", "resi 765 & chain A", merge=1)

cmd.color ("red", "resi 766 & chain A")

cmd.select ("Inward", "resi 766 & chain A", merge=1)

cmd.color ("blue", "resi 767 & chain A")

cmd.select ("Outward", "resi 767 & chain A", merge=1)

cmd.color ("red", "resi 768 & chain A")

cmd.select ("Inward", "resi 768 & chain A", merge=1)

cmd.color ("blue", "resi 769 & chain A")

cmd.select ("Outward", "resi 769 & chain A", merge=1)

cmd.color ("blue", "resi 770 & chain A")

cmd.select ("Outward", "resi 770 & chain A", merge=1)

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

cmd.color ("blue", "resi 736 & chain A")

cmd.select ("Outward", "resi 736 & chain A", merge=1)

cmd.color ("red", "resi 737 & chain A")

cmd.select ("Inward", "resi 737 & chain A", merge=1)

cmd.color ("blue", "resi 711 & chain A")

cmd.select ("Outward", "resi 711 & chain A", merge=1)

cmd.color ("red", "resi 712 & chain A")

cmd.select ("Inward", "resi 712 & chain A", merge=1)

cmd.color ("blue", "resi 713 & chain A")

cmd.select ("Outward", "resi 713 & chain A", merge=1)

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

cmd.color ("blue", "resi 720 & chain A")

cmd.select ("Outward", "resi 720 & chain A", merge=1)

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

cmd.color ("red", "resi 692 & chain A")

cmd.select ("Inward", "resi 692 & chain A", merge=1)

cmd.color ("blue", "resi 693 & chain A")

cmd.select ("Outward", "resi 693 & chain A", merge=1)

cmd.color ("red", "resi 664 & chain A")

cmd.select ("Inward", "resi 664 & chain A", merge=1)

cmd.color ("blue", "resi 665 & chain A")

cmd.select ("Outward", "resi 665 & chain A", merge=1)

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

cmd.color ("red", "resi 676 & chain A")

cmd.select ("Inward", "resi 676 & chain A", merge=1)

cmd.color ("blue", "resi 677 & chain A")

cmd.select ("Outward", "resi 677 & chain A", merge=1)

cmd.color ("red", "resi 678 & chain A")

cmd.select ("Inward", "resi 678 & chain A", merge=1)

cmd.color ("blue", "resi 679 & chain A")

cmd.select ("Outward", "resi 679 & chain A", merge=1)

cmd.color ("blue", "resi 680 & chain A")

cmd.select ("Outward", "resi 680 & chain A", merge=1)

cmd.color ("red", "resi 681 & chain A")

cmd.select ("Inward", "resi 681 & chain A", merge=1)

cmd.color ("blue", "resi 682 & chain A")

cmd.select ("Outward", "resi 682 & chain A", merge=1)

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

cmd.color ("red", "resi 621 & chain A")

cmd.select ("Inward", "resi 621 & chain A", merge=1)

cmd.color ("blue", "resi 622 & chain A")

cmd.select ("Outward", "resi 622 & chain A", merge=1)

cmd.color ("red", "resi 623 & chain A")

cmd.select ("Inward", "resi 623 & chain A", merge=1)

cmd.color ("blue", "resi 624 & chain A")

cmd.select ("Outward", "resi 624 & chain A", merge=1)

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

cmd.color ("red", "resi 634 & chain A")

cmd.select ("Inward", "resi 634 & chain A", merge=1)

cmd.color ("blue", "resi 635 & chain A")

cmd.select ("Outward", "resi 635 & chain A", merge=1)

cmd.color ("red", "resi 636 & chain A")

cmd.select ("Inward", "resi 636 & chain A", merge=1)

cmd.color ("blue", "resi 637 & chain A")

cmd.select ("Outward", "resi 637 & chain A", merge=1)

cmd.color ("red", "resi 638 & chain A")

cmd.select ("Inward", "resi 638 & chain A", merge=1)

cmd.color ("blue", "resi 639 & chain A")

cmd.select ("Outward", "resi 639 & chain A", merge=1)

cmd.color ("red", "resi 640 & chain A")

cmd.select ("Inward", "resi 640 & chain A", merge=1)

cmd.color ("blue", "resi 641 & chain A")

cmd.select ("Outward", "resi 641 & chain A", merge=1)

cmd.color ("blue", "resi 642 & chain A")

cmd.select ("Outward", "resi 642 & chain A", merge=1)

cmd.color ("red", "resi 643 & chain A")

cmd.select ("Inward", "resi 643 & chain A", merge=1)

cmd.color ("blue", "resi 644 & chain A")

cmd.select ("Outward", "resi 644 & chain A", merge=1)

cmd.color ("red", "resi 645 & chain A")

cmd.select ("Inward", "resi 645 & chain A", merge=1)

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

cmd.color ("red", "resi 588 & chain A")

cmd.select ("Inward", "resi 588 & chain A", merge=1)

cmd.color ("blue", "resi 589 & chain A")

cmd.select ("Outward", "resi 589 & chain A", merge=1)

cmd.color ("red", "resi 590 & chain A")

cmd.select ("Inward", "resi 590 & chain A", merge=1)

cmd.color ("blue", "resi 591 & chain A")

cmd.select ("Outward", "resi 591 & chain A", merge=1)

cmd.color ("red", "resi 592 & chain A")

cmd.select ("Inward", "resi 592 & chain A", merge=1)

cmd.color ("blue", "resi 593 & chain A")

cmd.select ("Outward", "resi 593 & chain A", merge=1)

cmd.color ("red", "resi 594 & chain A")

cmd.select ("Inward", "resi 594 & chain A", merge=1)

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

cmd.color ("blue", "resi 577 & chain A")

cmd.select ("Outward", "resi 577 & chain A", merge=1)

cmd.color ("blue", "resi 578 & chain A")

cmd.select ("Outward", "resi 578 & chain A", merge=1)

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

cmd.color ("red", "resi 532 & chain A")

cmd.select ("Inward", "resi 532 & chain A", merge=1)

cmd.color ("blue", "resi 533 & chain A")

cmd.select ("Outward", "resi 533 & chain A", merge=1)

cmd.color ("red", "resi 534 & chain A")

cmd.select ("Inward", "resi 534 & chain A", merge=1)

cmd.color ("blue", "resi 535 & chain A")

cmd.select ("Outward", "resi 535 & chain A", merge=1)

cmd.color ("red", "resi 536 & chain A")

cmd.select ("Inward", "resi 536 & chain A", merge=1)

cmd.color ("blue", "resi 537 & chain A")

cmd.select ("Outward", "resi 537 & chain A", merge=1)

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

cmd.color ("blue", "resi 441 & chain A")

cmd.select ("Outward", "resi 441 & chain A", merge=1)

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

cmd.color ("red", "resi 462 & chain A")

cmd.select ("Inward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("blue", "resi 464 & chain A")

cmd.select ("Outward", "resi 464 & chain A", merge=1)

cmd.color ("red", "resi 465 & chain A")

cmd.select ("Inward", "resi 465 & chain A", merge=1)

cmd.color ("blue", "resi 466 & chain A")

cmd.select ("Outward", "resi 466 & chain A", merge=1)

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

cmd.color ("blue", "resi 420 & chain A")

cmd.select ("Outward", "resi 420 & chain A", merge=1)

cmd.color ("red", "resi 421 & chain A")

cmd.select ("Inward", "resi 421 & chain A", merge=1)

cmd.color ("blue", "resi 422 & chain A")

cmd.select ("Outward", "resi 422 & chain A", merge=1)

cmd.color ("red", "resi 423 & chain A")

cmd.select ("Inward", "resi 423 & chain A", merge=1)

cmd.color ("blue", "resi 424 & chain A")

cmd.select ("Outward", "resi 424 & chain A", merge=1)

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

cmd.color ("blue", "resi 404 & chain A")

cmd.select ("Outward", "resi 404 & chain A", merge=1)

cmd.color ("blue", "resi 405 & chain A")

cmd.select ("Outward", "resi 405 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("red", "resi 345 & chain A")

cmd.select ("Inward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

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

cmd.color ("blue", "resi 339 & chain A")

cmd.select ("Outward", "resi 339 & chain A", merge=1)

cmd.color ("red", "resi 340 & chain A")

cmd.select ("Inward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

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

cmd.color ("red", "resi 290 & chain A")

cmd.select ("Inward", "resi 290 & chain A", merge=1)

cmd.color ("blue", "resi 291 & chain A")

cmd.select ("Outward", "resi 291 & chain A", merge=1)

cmd.color ("red", "resi 292 & chain A")

cmd.select ("Inward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("red", "resi 294 & chain A")

cmd.select ("Inward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("red", "resi 296 & chain A")

cmd.select ("Inward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("red", "resi 298 & chain A")

cmd.select ("Inward", "resi 298 & chain A", merge=1)

cmd.color ("blue", "resi 299 & chain A")

cmd.select ("Outward", "resi 299 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.load_cgo( [9.0, -3.917955,30.936817,120.56843, -3.917955, 30.936817, 120.56843, 1, 1,1,0,0,0,1], "axis" )