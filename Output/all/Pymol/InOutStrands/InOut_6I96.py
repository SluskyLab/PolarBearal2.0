from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6I96.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand10", "resi 291+292+293+294+295+296+297+298+299 & chain A ")


cmd.select("Astrand36", "resi 811+812+813+814+815+816+817+818+819 & chain A ")


cmd.select("Astrand33", "resi 780+781+782+783+784+785+786+787 & chain A ")


cmd.select("Astrand32", "resi 761+762+763+764+765+766+767+768+769+770+771 & chain A ")


cmd.select("Astrand29", "resi 736+737+738+739+740+741+742+743+744+745 & chain A ")


cmd.select("Astrand28", "resi 718+719+720+721+722+723+724+725+726+727 & chain A ")


cmd.select("Astrand27", "resi 687+688+689+690+691+692+693+694+695+696+697+698+699+700+701+702 & chain A ")


cmd.select("Astrand26", "resi 665+666+667+668+669+670+671+672+673+674+675+676+677+678+679+680+681+682+683 & chain A ")


cmd.select("Astrand24", "resi 622+623+624+625+626+627+628+629+630+631+632+633 & chain A ")


cmd.select("Astrand23", "resi 596+597+598+599+600+601+602+603+604+605+606+607 & chain A ")


cmd.select("Astrand25", "resi 641+642+643+644+645+646+647+648+649+650+651+652+653+654+655+656 & chain A ")


cmd.select("Astrand22", "resi 574+575+576+577+578+579+580+581+582+583+584+585+586+587+588+589+590 & chain A ")


cmd.select("Astrand21", "resi 551+552+553+554+555+556+557+558+559+560+561+562+563+564+565+566+567+568 & chain A ")


cmd.select("Astrand20", "resi 529+530+531+532+533+534+535+536+537+538+539+540+541+542+543+544+545+546+547+548 & chain A ")


cmd.select("Astrand18", "resi 484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499+500+501+502+503+504+505+506+507+508+509+510+511+512 & chain A ")


cmd.select("Astrand17", "resi 454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472+473+474+475+476+477+478+479+480+481 & chain A ")


cmd.select("Astrand16", "resi 424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447 & chain A ")


cmd.select("Astrand15", "resi 404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")


cmd.select("Astrand14", "resi 357+358+359+360+361+362+363+364+365+366+367+368+369+370+371 & chain A ")


cmd.select("Astrand13", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354 & chain A ")


cmd.select("Astrand12", "resi 320+321+322+323+324+325+326+327+328+329+330+331+332 & chain A ")


cmd.select("Astrand11", "resi 304+305+306+307+308+309+310+311+312+313 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 298 & chain A")

cmd.select ("Outward", "resi 298 & chain A", merge=1)

cmd.color ("red", "resi 299 & chain A")

cmd.select ("Inward", "resi 299 & chain A", merge=1)

cmd.color ("red", "resi 811 & chain A")

cmd.select ("Inward", "resi 811 & chain A", merge=1)

cmd.color ("blue", "resi 812 & chain A")

cmd.select ("Outward", "resi 812 & chain A", merge=1)

cmd.color ("red", "resi 813 & chain A")

cmd.select ("Inward", "resi 813 & chain A", merge=1)

cmd.color ("blue", "resi 814 & chain A")

cmd.select ("Outward", "resi 814 & chain A", merge=1)

cmd.color ("red", "resi 815 & chain A")

cmd.select ("Inward", "resi 815 & chain A", merge=1)

cmd.color ("blue", "resi 816 & chain A")

cmd.select ("Outward", "resi 816 & chain A", merge=1)

cmd.color ("red", "resi 817 & chain A")

cmd.select ("Inward", "resi 817 & chain A", merge=1)

cmd.color ("blue", "resi 818 & chain A")

cmd.select ("Outward", "resi 818 & chain A", merge=1)

cmd.color ("blue", "resi 819 & chain A")

cmd.select ("Outward", "resi 819 & chain A", merge=1)

cmd.color ("blue", "resi 780 & chain A")

cmd.select ("Outward", "resi 780 & chain A", merge=1)

cmd.color ("red", "resi 781 & chain A")

cmd.select ("Inward", "resi 781 & chain A", merge=1)

cmd.color ("blue", "resi 782 & chain A")

cmd.select ("Outward", "resi 782 & chain A", merge=1)

cmd.color ("red", "resi 783 & chain A")

cmd.select ("Inward", "resi 783 & chain A", merge=1)

cmd.color ("blue", "resi 784 & chain A")

cmd.select ("Outward", "resi 784 & chain A", merge=1)

cmd.color ("red", "resi 785 & chain A")

cmd.select ("Inward", "resi 785 & chain A", merge=1)

cmd.color ("blue", "resi 786 & chain A")

cmd.select ("Outward", "resi 786 & chain A", merge=1)

cmd.color ("red", "resi 787 & chain A")

cmd.select ("Inward", "resi 787 & chain A", merge=1)

cmd.color ("red", "resi 761 & chain A")

cmd.select ("Inward", "resi 761 & chain A", merge=1)

cmd.color ("blue", "resi 762 & chain A")

cmd.select ("Outward", "resi 762 & chain A", merge=1)

cmd.color ("red", "resi 763 & chain A")

cmd.select ("Inward", "resi 763 & chain A", merge=1)

cmd.color ("blue", "resi 764 & chain A")

cmd.select ("Outward", "resi 764 & chain A", merge=1)

cmd.color ("red", "resi 765 & chain A")

cmd.select ("Inward", "resi 765 & chain A", merge=1)

cmd.color ("blue", "resi 766 & chain A")

cmd.select ("Outward", "resi 766 & chain A", merge=1)

cmd.color ("red", "resi 767 & chain A")

cmd.select ("Inward", "resi 767 & chain A", merge=1)

cmd.color ("blue", "resi 768 & chain A")

cmd.select ("Outward", "resi 768 & chain A", merge=1)

cmd.color ("red", "resi 769 & chain A")

cmd.select ("Inward", "resi 769 & chain A", merge=1)

cmd.color ("blue", "resi 770 & chain A")

cmd.select ("Outward", "resi 770 & chain A", merge=1)

cmd.color ("blue", "resi 771 & chain A")

cmd.select ("Outward", "resi 771 & chain A", merge=1)

cmd.color ("blue", "resi 736 & chain A")

cmd.select ("Outward", "resi 736 & chain A", merge=1)

cmd.color ("red", "resi 737 & chain A")

cmd.select ("Inward", "resi 737 & chain A", merge=1)

cmd.color ("blue", "resi 738 & chain A")

cmd.select ("Outward", "resi 738 & chain A", merge=1)

cmd.color ("red", "resi 739 & chain A")

cmd.select ("Inward", "resi 739 & chain A", merge=1)

cmd.color ("blue", "resi 740 & chain A")

cmd.select ("Outward", "resi 740 & chain A", merge=1)

cmd.color ("red", "resi 741 & chain A")

cmd.select ("Inward", "resi 741 & chain A", merge=1)

cmd.color ("blue", "resi 742 & chain A")

cmd.select ("Outward", "resi 742 & chain A", merge=1)

cmd.color ("red", "resi 743 & chain A")

cmd.select ("Inward", "resi 743 & chain A", merge=1)

cmd.color ("blue", "resi 744 & chain A")

cmd.select ("Outward", "resi 744 & chain A", merge=1)

cmd.color ("red", "resi 745 & chain A")

cmd.select ("Inward", "resi 745 & chain A", merge=1)

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

cmd.color ("red", "resi 694 & chain A")

cmd.select ("Inward", "resi 694 & chain A", merge=1)

cmd.color ("blue", "resi 695 & chain A")

cmd.select ("Outward", "resi 695 & chain A", merge=1)

cmd.color ("red", "resi 696 & chain A")

cmd.select ("Inward", "resi 696 & chain A", merge=1)

cmd.color ("blue", "resi 697 & chain A")

cmd.select ("Outward", "resi 697 & chain A", merge=1)

cmd.color ("red", "resi 698 & chain A")

cmd.select ("Inward", "resi 698 & chain A", merge=1)

cmd.color ("blue", "resi 699 & chain A")

cmd.select ("Outward", "resi 699 & chain A", merge=1)

cmd.color ("blue", "resi 700 & chain A")

cmd.select ("Outward", "resi 700 & chain A", merge=1)

cmd.color ("red", "resi 701 & chain A")

cmd.select ("Inward", "resi 701 & chain A", merge=1)

cmd.color ("blue", "resi 702 & chain A")

cmd.select ("Outward", "resi 702 & chain A", merge=1)

cmd.color ("red", "resi 665 & chain A")

cmd.select ("Inward", "resi 665 & chain A", merge=1)

cmd.color ("blue", "resi 666 & chain A")

cmd.select ("Outward", "resi 666 & chain A", merge=1)

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

cmd.color ("red", "resi 680 & chain A")

cmd.select ("Inward", "resi 680 & chain A", merge=1)

cmd.color ("blue", "resi 681 & chain A")

cmd.select ("Outward", "resi 681 & chain A", merge=1)

cmd.color ("red", "resi 682 & chain A")

cmd.select ("Inward", "resi 682 & chain A", merge=1)

cmd.color ("blue", "resi 683 & chain A")

cmd.select ("Outward", "resi 683 & chain A", merge=1)

cmd.color ("red", "resi 622 & chain A")

cmd.select ("Inward", "resi 622 & chain A", merge=1)

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

cmd.color ("red", "resi 607 & chain A")

cmd.select ("Inward", "resi 607 & chain A", merge=1)

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

cmd.color ("red", "resi 647 & chain A")

cmd.select ("Inward", "resi 647 & chain A", merge=1)

cmd.color ("blue", "resi 648 & chain A")

cmd.select ("Outward", "resi 648 & chain A", merge=1)

cmd.color ("red", "resi 649 & chain A")

cmd.select ("Inward", "resi 649 & chain A", merge=1)

cmd.color ("blue", "resi 650 & chain A")

cmd.select ("Outward", "resi 650 & chain A", merge=1)

cmd.color ("red", "resi 651 & chain A")

cmd.select ("Inward", "resi 651 & chain A", merge=1)

cmd.color ("blue", "resi 652 & chain A")

cmd.select ("Outward", "resi 652 & chain A", merge=1)

cmd.color ("blue", "resi 653 & chain A")

cmd.select ("Outward", "resi 653 & chain A", merge=1)

cmd.color ("red", "resi 654 & chain A")

cmd.select ("Inward", "resi 654 & chain A", merge=1)

cmd.color ("blue", "resi 655 & chain A")

cmd.select ("Outward", "resi 655 & chain A", merge=1)

cmd.color ("red", "resi 656 & chain A")

cmd.select ("Inward", "resi 656 & chain A", merge=1)

cmd.color ("blue", "resi 574 & chain A")

cmd.select ("Outward", "resi 574 & chain A", merge=1)

cmd.color ("red", "resi 575 & chain A")

cmd.select ("Inward", "resi 575 & chain A", merge=1)

cmd.color ("blue", "resi 576 & chain A")

cmd.select ("Outward", "resi 576 & chain A", merge=1)

cmd.color ("red", "resi 577 & chain A")

cmd.select ("Inward", "resi 577 & chain A", merge=1)

cmd.color ("blue", "resi 578 & chain A")

cmd.select ("Outward", "resi 578 & chain A", merge=1)

cmd.color ("red", "resi 579 & chain A")

cmd.select ("Inward", "resi 579 & chain A", merge=1)

cmd.color ("blue", "resi 580 & chain A")

cmd.select ("Outward", "resi 580 & chain A", merge=1)

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

cmd.color ("blue", "resi 561 & chain A")

cmd.select ("Outward", "resi 561 & chain A", merge=1)

cmd.color ("red", "resi 562 & chain A")

cmd.select ("Inward", "resi 562 & chain A", merge=1)

cmd.color ("blue", "resi 563 & chain A")

cmd.select ("Outward", "resi 563 & chain A", merge=1)

cmd.color ("red", "resi 564 & chain A")

cmd.select ("Inward", "resi 564 & chain A", merge=1)

cmd.color ("blue", "resi 565 & chain A")

cmd.select ("Outward", "resi 565 & chain A", merge=1)

cmd.color ("red", "resi 566 & chain A")

cmd.select ("Inward", "resi 566 & chain A", merge=1)

cmd.color ("blue", "resi 567 & chain A")

cmd.select ("Outward", "resi 567 & chain A", merge=1)

cmd.color ("blue", "resi 568 & chain A")

cmd.select ("Outward", "resi 568 & chain A", merge=1)

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

cmd.color ("blue", "resi 500 & chain A")

cmd.select ("Outward", "resi 500 & chain A", merge=1)

cmd.color ("red", "resi 501 & chain A")

cmd.select ("Inward", "resi 501 & chain A", merge=1)

cmd.color ("blue", "resi 502 & chain A")

cmd.select ("Outward", "resi 502 & chain A", merge=1)

cmd.color ("red", "resi 503 & chain A")

cmd.select ("Inward", "resi 503 & chain A", merge=1)

cmd.color ("blue", "resi 504 & chain A")

cmd.select ("Outward", "resi 504 & chain A", merge=1)

cmd.color ("red", "resi 505 & chain A")

cmd.select ("Inward", "resi 505 & chain A", merge=1)

cmd.color ("blue", "resi 506 & chain A")

cmd.select ("Outward", "resi 506 & chain A", merge=1)

cmd.color ("blue", "resi 507 & chain A")

cmd.select ("Outward", "resi 507 & chain A", merge=1)

cmd.color ("red", "resi 508 & chain A")

cmd.select ("Inward", "resi 508 & chain A", merge=1)

cmd.color ("blue", "resi 509 & chain A")

cmd.select ("Outward", "resi 509 & chain A", merge=1)

cmd.color ("blue", "resi 510 & chain A")

cmd.select ("Outward", "resi 510 & chain A", merge=1)

cmd.color ("red", "resi 511 & chain A")

cmd.select ("Inward", "resi 511 & chain A", merge=1)

cmd.color ("blue", "resi 512 & chain A")

cmd.select ("Outward", "resi 512 & chain A", merge=1)

cmd.color ("blue", "resi 454 & chain A")

cmd.select ("Outward", "resi 454 & chain A", merge=1)

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

cmd.color ("blue", "resi 460 & chain A")

cmd.select ("Outward", "resi 460 & chain A", merge=1)

cmd.color ("red", "resi 461 & chain A")

cmd.select ("Inward", "resi 461 & chain A", merge=1)

cmd.color ("red", "resi 462 & chain A")

cmd.select ("Inward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("red", "resi 464 & chain A")

cmd.select ("Inward", "resi 464 & chain A", merge=1)

cmd.color ("blue", "resi 465 & chain A")

cmd.select ("Outward", "resi 465 & chain A", merge=1)

cmd.color ("red", "resi 466 & chain A")

cmd.select ("Inward", "resi 466 & chain A", merge=1)

cmd.color ("blue", "resi 467 & chain A")

cmd.select ("Outward", "resi 467 & chain A", merge=1)

cmd.color ("red", "resi 468 & chain A")

cmd.select ("Inward", "resi 468 & chain A", merge=1)

cmd.color ("blue", "resi 469 & chain A")

cmd.select ("Outward", "resi 469 & chain A", merge=1)

cmd.color ("red", "resi 470 & chain A")

cmd.select ("Inward", "resi 470 & chain A", merge=1)

cmd.color ("blue", "resi 471 & chain A")

cmd.select ("Outward", "resi 471 & chain A", merge=1)

cmd.color ("red", "resi 472 & chain A")

cmd.select ("Inward", "resi 472 & chain A", merge=1)

cmd.color ("blue", "resi 473 & chain A")

cmd.select ("Outward", "resi 473 & chain A", merge=1)

cmd.color ("red", "resi 474 & chain A")

cmd.select ("Inward", "resi 474 & chain A", merge=1)

cmd.color ("blue", "resi 475 & chain A")

cmd.select ("Outward", "resi 475 & chain A", merge=1)

cmd.color ("red", "resi 476 & chain A")

cmd.select ("Inward", "resi 476 & chain A", merge=1)

cmd.color ("blue", "resi 477 & chain A")

cmd.select ("Outward", "resi 477 & chain A", merge=1)

cmd.color ("red", "resi 478 & chain A")

cmd.select ("Inward", "resi 478 & chain A", merge=1)

cmd.color ("blue", "resi 479 & chain A")

cmd.select ("Outward", "resi 479 & chain A", merge=1)

cmd.color ("blue", "resi 480 & chain A")

cmd.select ("Outward", "resi 480 & chain A", merge=1)

cmd.color ("red", "resi 481 & chain A")

cmd.select ("Inward", "resi 481 & chain A", merge=1)

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

cmd.color ("red", "resi 443 & chain A")

cmd.select ("Inward", "resi 443 & chain A", merge=1)

cmd.color ("blue", "resi 444 & chain A")

cmd.select ("Outward", "resi 444 & chain A", merge=1)

cmd.color ("red", "resi 445 & chain A")

cmd.select ("Inward", "resi 445 & chain A", merge=1)

cmd.color ("blue", "resi 446 & chain A")

cmd.select ("Outward", "resi 446 & chain A", merge=1)

cmd.color ("blue", "resi 447 & chain A")

cmd.select ("Outward", "resi 447 & chain A", merge=1)

cmd.color ("blue", "resi 404 & chain A")

cmd.select ("Outward", "resi 404 & chain A", merge=1)

cmd.color ("red", "resi 405 & chain A")

cmd.select ("Inward", "resi 405 & chain A", merge=1)

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

cmd.color ("blue", "resi 419 & chain A")

cmd.select ("Outward", "resi 419 & chain A", merge=1)

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

cmd.color ("red", "resi 366 & chain A")

cmd.select ("Inward", "resi 366 & chain A", merge=1)

cmd.color ("blue", "resi 367 & chain A")

cmd.select ("Outward", "resi 367 & chain A", merge=1)

cmd.color ("red", "resi 368 & chain A")

cmd.select ("Inward", "resi 368 & chain A", merge=1)

cmd.color ("blue", "resi 369 & chain A")

cmd.select ("Outward", "resi 369 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("red", "resi 371 & chain A")

cmd.select ("Inward", "resi 371 & chain A", merge=1)

cmd.color ("blue", "resi 339 & chain A")

cmd.select ("Outward", "resi 339 & chain A", merge=1)

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

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("red", "resi 353 & chain A")

cmd.select ("Inward", "resi 353 & chain A", merge=1)

cmd.color ("blue", "resi 354 & chain A")

cmd.select ("Outward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 320 & chain A")

cmd.select ("Outward", "resi 320 & chain A", merge=1)

cmd.color ("red", "resi 321 & chain A")

cmd.select ("Inward", "resi 321 & chain A", merge=1)

cmd.color ("blue", "resi 322 & chain A")

cmd.select ("Outward", "resi 322 & chain A", merge=1)

cmd.color ("red", "resi 323 & chain A")

cmd.select ("Inward", "resi 323 & chain A", merge=1)

cmd.color ("blue", "resi 324 & chain A")

cmd.select ("Outward", "resi 324 & chain A", merge=1)

cmd.color ("red", "resi 325 & chain A")

cmd.select ("Inward", "resi 325 & chain A", merge=1)

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

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

cmd.color ("red", "resi 305 & chain A")

cmd.select ("Inward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 306 & chain A")

cmd.select ("Outward", "resi 306 & chain A", merge=1)

cmd.color ("red", "resi 307 & chain A")

cmd.select ("Inward", "resi 307 & chain A", merge=1)

cmd.color ("blue", "resi 308 & chain A")

cmd.select ("Outward", "resi 308 & chain A", merge=1)

cmd.color ("red", "resi 309 & chain A")

cmd.select ("Inward", "resi 309 & chain A", merge=1)

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

cmd.color ("red", "resi 311 & chain A")

cmd.select ("Inward", "resi 311 & chain A", merge=1)

cmd.color ("blue", "resi 312 & chain A")

cmd.select ("Outward", "resi 312 & chain A", merge=1)

cmd.color ("blue", "resi 313 & chain A")

cmd.select ("Outward", "resi 313 & chain A", merge=1)

cmd.load_cgo( [9.0, -13.114409,29.713957,4.3695, -13.114409, 29.713957, 4.3695, 1, 1,1,0,0,0,1], "axis" )
