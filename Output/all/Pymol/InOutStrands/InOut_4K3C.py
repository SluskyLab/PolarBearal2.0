from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3C.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand6", "resi 421+422+423+424+425+426+427+428+429+430 & chain A ")


cmd.select("Astrand7", "resi 434+435+436+437+438+439+440+441+442+443+444+445+446 & chain A ")


cmd.select("Astrand8", "resi 451+452+453+454+455+456+457+458+459 & chain A ")


cmd.select("Astrand9", "resi 463+464+465+466+467+468+469+470+471+472+473+474+475 & chain A ")


cmd.select("Astrand10", "resi 481+482+483+484+485+486+487+488+489+490+491+492 & chain A ")


cmd.select("Astrand11", "resi 503+504+505+506+507+508+509+510+511+512+513+514+515 & chain A ")


cmd.select("Astrand12", "resi 521+522+523+524+525+526+527+528+529+530+531+532+533+534+535 & chain A ")


cmd.select("Astrand14", "resi 569+570+571+572+573+574+575+576+577+578 & chain A ")


cmd.select("Astrand15", "resi 589+590+591+592+593+594+595+596+597+598+599 & chain A ")


cmd.select("Astrand17", "resi 627+628+629+630+631+632+633+634+635+636+637+638+639 & chain A ")


cmd.select("Astrand16", "resi 607+608+609+610+611+612+613+614+615+616+617+618+619 & chain A ")


cmd.select("Astrand21", "resi 691+692+693+694+695+696+697+698+699+700+701 & chain A ")


cmd.select("Astrand22", "resi 714+715+716+717+718+719+720+721+722+723+724+725+726 & chain A ")


cmd.select("Astrand23", "resi 750+751+752+753+754+755+756+757+758+759+760+761 & chain A ")


cmd.select("Astrand24", "resi 764+765+766+767+768+769+770+771+772+773+774+775 & chain A ")


cmd.select("Astrand25", "resi 782+783+784+785+786+787+788+789+790+791+792 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("red", "resi 426 & chain A")

cmd.select ("Inward", "resi 426 & chain A", merge=1)

cmd.color ("blue", "resi 427 & chain A")

cmd.select ("Outward", "resi 427 & chain A", merge=1)

cmd.color ("red", "resi 428 & chain A")

cmd.select ("Inward", "resi 428 & chain A", merge=1)

cmd.color ("blue", "resi 429 & chain A")

cmd.select ("Outward", "resi 429 & chain A", merge=1)

cmd.color ("red", "resi 430 & chain A")

cmd.select ("Inward", "resi 430 & chain A", merge=1)

cmd.color ("red", "resi 434 & chain A")

cmd.select ("Inward", "resi 434 & chain A", merge=1)

cmd.color ("blue", "resi 435 & chain A")

cmd.select ("Outward", "resi 435 & chain A", merge=1)

cmd.color ("red", "resi 436 & chain A")

cmd.select ("Inward", "resi 436 & chain A", merge=1)

cmd.color ("blue", "resi 437 & chain A")

cmd.select ("Outward", "resi 437 & chain A", merge=1)

cmd.color ("red", "resi 438 & chain A")

cmd.select ("Inward", "resi 438 & chain A", merge=1)

cmd.color ("blue", "resi 439 & chain A")

cmd.select ("Outward", "resi 439 & chain A", merge=1)

cmd.color ("red", "resi 440 & chain A")

cmd.select ("Inward", "resi 440 & chain A", merge=1)

cmd.color ("blue", "resi 441 & chain A")

cmd.select ("Outward", "resi 441 & chain A", merge=1)

cmd.color ("red", "resi 442 & chain A")

cmd.select ("Inward", "resi 442 & chain A", merge=1)

cmd.color ("blue", "resi 443 & chain A")

cmd.select ("Outward", "resi 443 & chain A", merge=1)

cmd.color ("blue", "resi 444 & chain A")

cmd.select ("Outward", "resi 444 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("red", "resi 446 & chain A")

cmd.select ("Inward", "resi 446 & chain A", merge=1)

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

cmd.color ("blue", "resi 473 & chain A")

cmd.select ("Outward", "resi 473 & chain A", merge=1)

cmd.color ("blue", "resi 474 & chain A")

cmd.select ("Outward", "resi 474 & chain A", merge=1)

cmd.color ("red", "resi 475 & chain A")

cmd.select ("Inward", "resi 475 & chain A", merge=1)

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

cmd.color ("blue", "resi 513 & chain A")

cmd.select ("Outward", "resi 513 & chain A", merge=1)

cmd.color ("red", "resi 514 & chain A")

cmd.select ("Inward", "resi 514 & chain A", merge=1)

cmd.color ("blue", "resi 515 & chain A")

cmd.select ("Outward", "resi 515 & chain A", merge=1)

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

cmd.color ("red", "resi 578 & chain A")

cmd.select ("Inward", "resi 578 & chain A", merge=1)

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

cmd.color ("blue", "resi 599 & chain A")

cmd.select ("Outward", "resi 599 & chain A", merge=1)

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

cmd.color ("red", "resi 635 & chain A")

cmd.select ("Inward", "resi 635 & chain A", merge=1)

cmd.color ("blue", "resi 636 & chain A")

cmd.select ("Outward", "resi 636 & chain A", merge=1)

cmd.color ("red", "resi 637 & chain A")

cmd.select ("Inward", "resi 637 & chain A", merge=1)

cmd.color ("blue", "resi 638 & chain A")

cmd.select ("Outward", "resi 638 & chain A", merge=1)

cmd.color ("red", "resi 639 & chain A")

cmd.select ("Inward", "resi 639 & chain A", merge=1)

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

cmd.color ("blue", "resi 616 & chain A")

cmd.select ("Outward", "resi 616 & chain A", merge=1)

cmd.color ("red", "resi 617 & chain A")

cmd.select ("Inward", "resi 617 & chain A", merge=1)

cmd.color ("blue", "resi 618 & chain A")

cmd.select ("Outward", "resi 618 & chain A", merge=1)

cmd.color ("blue", "resi 619 & chain A")

cmd.select ("Outward", "resi 619 & chain A", merge=1)

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

cmd.color ("red", "resi 700 & chain A")

cmd.select ("Inward", "resi 700 & chain A", merge=1)

cmd.color ("blue", "resi 701 & chain A")

cmd.select ("Outward", "resi 701 & chain A", merge=1)

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

cmd.color ("red", "resi 750 & chain A")

cmd.select ("Inward", "resi 750 & chain A", merge=1)

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

cmd.color ("blue", "resi 760 & chain A")

cmd.select ("Outward", "resi 760 & chain A", merge=1)

cmd.color ("red", "resi 761 & chain A")

cmd.select ("Inward", "resi 761 & chain A", merge=1)

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

cmd.color ("red", "resi 771 & chain A")

cmd.select ("Inward", "resi 771 & chain A", merge=1)

cmd.color ("blue", "resi 772 & chain A")

cmd.select ("Outward", "resi 772 & chain A", merge=1)

cmd.color ("blue", "resi 773 & chain A")

cmd.select ("Outward", "resi 773 & chain A", merge=1)

cmd.color ("red", "resi 774 & chain A")

cmd.select ("Inward", "resi 774 & chain A", merge=1)

cmd.color ("blue", "resi 775 & chain A")

cmd.select ("Outward", "resi 775 & chain A", merge=1)

cmd.color ("blue", "resi 782 & chain A")

cmd.select ("Outward", "resi 782 & chain A", merge=1)

cmd.color ("red", "resi 783 & chain A")

cmd.select ("Inward", "resi 783 & chain A", merge=1)

cmd.color ("blue", "resi 784 & chain A")

cmd.select ("Outward", "resi 784 & chain A", merge=1)

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

cmd.color ("blue", "resi 791 & chain A")

cmd.select ("Outward", "resi 791 & chain A", merge=1)

cmd.color ("red", "resi 792 & chain A")

cmd.select ("Inward", "resi 792 & chain A", merge=1)

cmd.load_cgo( [9.0, -0.90393734,14.320874,-46.817436, -0.90393734, 14.320874, -46.817436, 1, 1,1,0,0,0,1], "axis" )