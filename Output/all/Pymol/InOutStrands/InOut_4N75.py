from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4N75.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 427+428+429+430+431+432+433 & chain A ")


cmd.select("Astrand16", "resi 799+800+801+802+803+804+805+806+807+808+809 & chain A ")


cmd.select("Astrand15", "resi 781+782+783+784+785+786+787+788+789+790+791+792 & chain A ")


cmd.select("Astrand14", "resi 767+768+769+770+771+772+773+774+775+776+777+778 & chain A ")


cmd.select("Astrand13", "resi 733+734+735+736+737+738+739+740+741+742+743+744+745 & chain A ")


cmd.select("Astrand12", "resi 710+711+712+713+714+715+716+717+718+719+720 & chain A ")


cmd.select("Astrand10", "resi 628+629+630+631+632+633+634+635+636+637+638+639+640 & chain A ")


cmd.select("Astrand9", "resi 608+609+610+611+612+613+614+615+616+617+618+619+620 & chain A ")


cmd.select("Astrand8", "resi 590+591+592+593+594+595+596+597+598+599+600 & chain A ")


cmd.select("Astrand7", "resi 564+565+566+567+568+569+570+571+572+573+574+575+576+577+578+579 & chain A ")


cmd.select("Astrand6", "resi 523+524+525+526+527+528+529+530+531+532+533+534+535+536+537 & chain A ")


cmd.select("Astrand5", "resi 505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520 & chain A ")


cmd.select("Astrand4", "resi 484+485+486+487+488+489+490+491+492+493+494+495 & chain A ")


cmd.select("Astrand3", "resi 466+467+468+469+470+471+472+473+474+475 & chain A ")


cmd.select("Astrand2", "resi 455+456+457+458+459+460+461+462 & chain A ")


cmd.select("Astrand1", "resi 437+438+439+440+441+442+443+444+445+446 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 799 & chain A")

cmd.select ("Outward", "resi 799 & chain A", merge=1)

cmd.color ("red", "resi 800 & chain A")

cmd.select ("Inward", "resi 800 & chain A", merge=1)

cmd.color ("blue", "resi 801 & chain A")

cmd.select ("Outward", "resi 801 & chain A", merge=1)

cmd.color ("blue", "resi 802 & chain A")

cmd.select ("Outward", "resi 802 & chain A", merge=1)

cmd.color ("red", "resi 803 & chain A")

cmd.select ("Inward", "resi 803 & chain A", merge=1)

cmd.color ("blue", "resi 804 & chain A")

cmd.select ("Outward", "resi 804 & chain A", merge=1)

cmd.color ("red", "resi 805 & chain A")

cmd.select ("Inward", "resi 805 & chain A", merge=1)

cmd.color ("blue", "resi 806 & chain A")

cmd.select ("Outward", "resi 806 & chain A", merge=1)

cmd.color ("red", "resi 807 & chain A")

cmd.select ("Inward", "resi 807 & chain A", merge=1)

cmd.color ("blue", "resi 808 & chain A")

cmd.select ("Outward", "resi 808 & chain A", merge=1)

cmd.color ("red", "resi 809 & chain A")

cmd.select ("Inward", "resi 809 & chain A", merge=1)

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

cmd.color ("red", "resi 786 & chain A")

cmd.select ("Inward", "resi 786 & chain A", merge=1)

cmd.color ("blue", "resi 787 & chain A")

cmd.select ("Outward", "resi 787 & chain A", merge=1)

cmd.color ("red", "resi 788 & chain A")

cmd.select ("Inward", "resi 788 & chain A", merge=1)

cmd.color ("blue", "resi 789 & chain A")

cmd.select ("Outward", "resi 789 & chain A", merge=1)

cmd.color ("red", "resi 790 & chain A")

cmd.select ("Inward", "resi 790 & chain A", merge=1)

cmd.color ("red", "resi 791 & chain A")

cmd.select ("Inward", "resi 791 & chain A", merge=1)

cmd.color ("blue", "resi 792 & chain A")

cmd.select ("Outward", "resi 792 & chain A", merge=1)

cmd.color ("red", "resi 767 & chain A")

cmd.select ("Inward", "resi 767 & chain A", merge=1)

cmd.color ("blue", "resi 768 & chain A")

cmd.select ("Outward", "resi 768 & chain A", merge=1)

cmd.color ("red", "resi 769 & chain A")

cmd.select ("Inward", "resi 769 & chain A", merge=1)

cmd.color ("blue", "resi 770 & chain A")

cmd.select ("Outward", "resi 770 & chain A", merge=1)

cmd.color ("red", "resi 771 & chain A")

cmd.select ("Inward", "resi 771 & chain A", merge=1)

cmd.color ("blue", "resi 772 & chain A")

cmd.select ("Outward", "resi 772 & chain A", merge=1)

cmd.color ("red", "resi 773 & chain A")

cmd.select ("Inward", "resi 773 & chain A", merge=1)

cmd.color ("blue", "resi 774 & chain A")

cmd.select ("Outward", "resi 774 & chain A", merge=1)

cmd.color ("red", "resi 775 & chain A")

cmd.select ("Inward", "resi 775 & chain A", merge=1)

cmd.color ("blue", "resi 776 & chain A")

cmd.select ("Outward", "resi 776 & chain A", merge=1)

cmd.color ("blue", "resi 777 & chain A")

cmd.select ("Outward", "resi 777 & chain A", merge=1)

cmd.color ("red", "resi 778 & chain A")

cmd.select ("Inward", "resi 778 & chain A", merge=1)

cmd.color ("blue", "resi 733 & chain A")

cmd.select ("Outward", "resi 733 & chain A", merge=1)

cmd.color ("red", "resi 734 & chain A")

cmd.select ("Inward", "resi 734 & chain A", merge=1)

cmd.color ("blue", "resi 735 & chain A")

cmd.select ("Outward", "resi 735 & chain A", merge=1)

cmd.color ("red", "resi 736 & chain A")

cmd.select ("Inward", "resi 736 & chain A", merge=1)

cmd.color ("blue", "resi 737 & chain A")

cmd.select ("Outward", "resi 737 & chain A", merge=1)

cmd.color ("red", "resi 738 & chain A")

cmd.select ("Inward", "resi 738 & chain A", merge=1)

cmd.color ("blue", "resi 739 & chain A")

cmd.select ("Outward", "resi 739 & chain A", merge=1)

cmd.color ("red", "resi 740 & chain A")

cmd.select ("Inward", "resi 740 & chain A", merge=1)

cmd.color ("blue", "resi 741 & chain A")

cmd.select ("Outward", "resi 741 & chain A", merge=1)

cmd.color ("red", "resi 742 & chain A")

cmd.select ("Inward", "resi 742 & chain A", merge=1)

cmd.color ("blue", "resi 743 & chain A")

cmd.select ("Outward", "resi 743 & chain A", merge=1)

cmd.color ("red", "resi 744 & chain A")

cmd.select ("Inward", "resi 744 & chain A", merge=1)

cmd.color ("blue", "resi 745 & chain A")

cmd.select ("Outward", "resi 745 & chain A", merge=1)

cmd.color ("blue", "resi 710 & chain A")

cmd.select ("Outward", "resi 710 & chain A", merge=1)

cmd.color ("red", "resi 711 & chain A")

cmd.select ("Inward", "resi 711 & chain A", merge=1)

cmd.color ("blue", "resi 712 & chain A")

cmd.select ("Outward", "resi 712 & chain A", merge=1)

cmd.color ("red", "resi 713 & chain A")

cmd.select ("Inward", "resi 713 & chain A", merge=1)

cmd.color ("blue", "resi 714 & chain A")

cmd.select ("Outward", "resi 714 & chain A", merge=1)

cmd.color ("red", "resi 715 & chain A")

cmd.select ("Inward", "resi 715 & chain A", merge=1)

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

cmd.color ("blue", "resi 640 & chain A")

cmd.select ("Outward", "resi 640 & chain A", merge=1)

cmd.color ("red", "resi 608 & chain A")

cmd.select ("Inward", "resi 608 & chain A", merge=1)

cmd.color ("blue", "resi 609 & chain A")

cmd.select ("Outward", "resi 609 & chain A", merge=1)

cmd.color ("red", "resi 610 & chain A")

cmd.select ("Inward", "resi 610 & chain A", merge=1)

cmd.color ("blue", "resi 611 & chain A")

cmd.select ("Outward", "resi 611 & chain A", merge=1)

cmd.color ("red", "resi 612 & chain A")

cmd.select ("Inward", "resi 612 & chain A", merge=1)

cmd.color ("blue", "resi 613 & chain A")

cmd.select ("Outward", "resi 613 & chain A", merge=1)

cmd.color ("red", "resi 614 & chain A")

cmd.select ("Inward", "resi 614 & chain A", merge=1)

cmd.color ("blue", "resi 615 & chain A")

cmd.select ("Outward", "resi 615 & chain A", merge=1)

cmd.color ("red", "resi 616 & chain A")

cmd.select ("Inward", "resi 616 & chain A", merge=1)

cmd.color ("blue", "resi 617 & chain A")

cmd.select ("Outward", "resi 617 & chain A", merge=1)

cmd.color ("red", "resi 618 & chain A")

cmd.select ("Inward", "resi 618 & chain A", merge=1)

cmd.color ("blue", "resi 619 & chain A")

cmd.select ("Outward", "resi 619 & chain A", merge=1)

cmd.color ("blue", "resi 620 & chain A")

cmd.select ("Outward", "resi 620 & chain A", merge=1)

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

cmd.color ("blue", "resi 600 & chain A")

cmd.select ("Outward", "resi 600 & chain A", merge=1)

cmd.color ("blue", "resi 564 & chain A")

cmd.select ("Outward", "resi 564 & chain A", merge=1)

cmd.color ("red", "resi 565 & chain A")

cmd.select ("Inward", "resi 565 & chain A", merge=1)

cmd.color ("blue", "resi 566 & chain A")

cmd.select ("Outward", "resi 566 & chain A", merge=1)

cmd.color ("red", "resi 567 & chain A")

cmd.select ("Inward", "resi 567 & chain A", merge=1)

cmd.color ("blue", "resi 568 & chain A")

cmd.select ("Outward", "resi 568 & chain A", merge=1)

cmd.color ("red", "resi 569 & chain A")

cmd.select ("Inward", "resi 569 & chain A", merge=1)

cmd.color ("blue", "resi 570 & chain A")

cmd.select ("Outward", "resi 570 & chain A", merge=1)

cmd.color ("red", "resi 571 & chain A")

cmd.select ("Inward", "resi 571 & chain A", merge=1)

cmd.color ("blue", "resi 572 & chain A")

cmd.select ("Outward", "resi 572 & chain A", merge=1)

cmd.color ("red", "resi 573 & chain A")

cmd.select ("Inward", "resi 573 & chain A", merge=1)

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

cmd.color ("blue", "resi 518 & chain A")

cmd.select ("Outward", "resi 518 & chain A", merge=1)

cmd.color ("red", "resi 519 & chain A")

cmd.select ("Inward", "resi 519 & chain A", merge=1)

cmd.color ("blue", "resi 520 & chain A")

cmd.select ("Outward", "resi 520 & chain A", merge=1)

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

cmd.load_cgo( [9.0, 35.92719,61.040627,11.111688, 35.92719, 61.040627, 11.111688, 1, 1,1,0,0,0,1], "axis" )
