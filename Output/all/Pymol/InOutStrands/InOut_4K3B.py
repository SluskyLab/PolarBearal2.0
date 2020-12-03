from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand16", "resi 425+426+427+428+429+430+431+432+433 & chain A ")


cmd.select("Astrand17", "resi 437+438+439+440+441+442+443+444+445+446+447+448+449 & chain A ")


cmd.select("Astrand18", "resi 454+455+456+457+458+459+460+461+462 & chain A ")


cmd.select("Astrand19", "resi 466+467+468+469+470+471+472+473+474+475+476+477+478+479 & chain A ")


cmd.select("Astrand20", "resi 483+484+485+486+487+488+489+490+491+492+493+494 & chain A ")


cmd.select("Astrand21", "resi 507+508+509+510+511+512+513+514+515+516+517+518+519+520 & chain A ")


cmd.select("Astrand26", "resi 626+627+628+629+630+631+632+633+634+635 & chain A ")


cmd.select("Astrand25", "resi 609+610+611+612+613+614+615+616+617+618+619+620 & chain A ")


cmd.select("Astrand24", "resi 591+592+593+594+595+596+597+598+599+600 & chain A ")


cmd.select("Astrand23", "resi 564+565+566+567+568+569+570+571+572+573+574+575+576+577+578+579+580 & chain A ")


cmd.select("Astrand29", "resi 685+686+687+688+689+690+691+692+693+694+695 & chain A ")


cmd.select("Astrand22", "resi 526+527+528+529+530+531+532+533+534+535+536+537+538+539 & chain A ")


cmd.select("Astrand30", "resi 706+707+708+709+710+711+712+713+714+715+716+717+718 & chain A ")


cmd.select("Astrand31", "resi 749+750+751+752+753+754+755+756+757+758+759 & chain A ")


cmd.select("Astrand32", "resi 764+765+766+767+768+769+770+771+772+773 & chain A ")


cmd.select("Astrand33", "resi 784+785+786+787+788+789 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("red", "resi 447 & chain A")

cmd.select ("Inward", "resi 447 & chain A", merge=1)

cmd.color ("blue", "resi 448 & chain A")

cmd.select ("Outward", "resi 448 & chain A", merge=1)

cmd.color ("red", "resi 449 & chain A")

cmd.select ("Inward", "resi 449 & chain A", merge=1)

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

cmd.color ("red", "resi 479 & chain A")

cmd.select ("Inward", "resi 479 & chain A", merge=1)

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

cmd.color ("red", "resi 518 & chain A")

cmd.select ("Inward", "resi 518 & chain A", merge=1)

cmd.color ("blue", "resi 519 & chain A")

cmd.select ("Outward", "resi 519 & chain A", merge=1)

cmd.color ("blue", "resi 520 & chain A")

cmd.select ("Outward", "resi 520 & chain A", merge=1)

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

cmd.color ("red", "resi 634 & chain A")

cmd.select ("Inward", "resi 634 & chain A", merge=1)

cmd.color ("blue", "resi 635 & chain A")

cmd.select ("Outward", "resi 635 & chain A", merge=1)

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

cmd.color ("blue", "resi 580 & chain A")

cmd.select ("Outward", "resi 580 & chain A", merge=1)

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

cmd.color ("red", "resi 694 & chain A")

cmd.select ("Inward", "resi 694 & chain A", merge=1)

cmd.color ("blue", "resi 695 & chain A")

cmd.select ("Outward", "resi 695 & chain A", merge=1)

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

cmd.color ("red", "resi 538 & chain A")

cmd.select ("Inward", "resi 538 & chain A", merge=1)

cmd.color ("blue", "resi 539 & chain A")

cmd.select ("Outward", "resi 539 & chain A", merge=1)

cmd.color ("blue", "resi 706 & chain A")

cmd.select ("Outward", "resi 706 & chain A", merge=1)

cmd.color ("red", "resi 707 & chain A")

cmd.select ("Inward", "resi 707 & chain A", merge=1)

cmd.color ("blue", "resi 708 & chain A")

cmd.select ("Outward", "resi 708 & chain A", merge=1)

cmd.color ("red", "resi 709 & chain A")

cmd.select ("Inward", "resi 709 & chain A", merge=1)

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

cmd.color ("red", "resi 770 & chain A")

cmd.select ("Inward", "resi 770 & chain A", merge=1)

cmd.color ("blue", "resi 771 & chain A")

cmd.select ("Outward", "resi 771 & chain A", merge=1)

cmd.color ("red", "resi 772 & chain A")

cmd.select ("Inward", "resi 772 & chain A", merge=1)

cmd.color ("red", "resi 773 & chain A")

cmd.select ("Inward", "resi 773 & chain A", merge=1)

cmd.color ("blue", "resi 784 & chain A")

cmd.select ("Outward", "resi 784 & chain A", merge=1)

cmd.color ("red", "resi 785 & chain A")

cmd.select ("Inward", "resi 785 & chain A", merge=1)

cmd.color ("blue", "resi 786 & chain A")

cmd.select ("Outward", "resi 786 & chain A", merge=1)

cmd.color ("red", "resi 787 & chain A")

cmd.select ("Inward", "resi 787 & chain A", merge=1)

cmd.color ("blue", "resi 788 & chain A")

cmd.select ("Outward", "resi 788 & chain A", merge=1)

cmd.color ("blue", "resi 789 & chain A")

cmd.select ("Outward", "resi 789 & chain A", merge=1)

cmd.load_cgo( [9.0, -14.903438,19.222376,-22.904686, -14.903438, 19.222376, -22.904686, 1, 1,1,0,0,0,1], "axis" )
