from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Y25.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 518+519+520+521+522+523+524+525+526+527+528+529+530 & chain A ")


cmd.select("Astrand16", "resi 793+794+795+796+797+798+799+800+801+802+803+804+805+806+807 & chain A ")


cmd.select("Astrand15", "resi 776+777+778+779+780+781+782+783+784+785+786+787+788 & chain A ")


cmd.select("Astrand14", "resi 757+758+759+760+761+762+763+764+765+766+767+768+769+770+771+772 & chain A ")


cmd.select("Astrand13", "resi 738+739+740+741+742+743+744+745+746+747+748+749+750+751+752+753 & chain A ")


cmd.select("Astrand12", "resi 718+719+720+721+722+723+724+725+726+727+728+729+730+731+732+733+734+735 & chain A ")


cmd.select("Astrand10", "resi 693+694+695+696+697+700+701+702+703+704+705 & chain A ")


cmd.select("Astrand8", "resi 659+660+661+662+663+664+665+666+667+668+669+670 & chain A ")


cmd.select("Astrand9", "resi 675+676+677+678+679+680+681+682+683+684+685+686+687+688+689 & chain A ")


cmd.select("Astrand7", "resi 644+645+646+647+648+649+650+651+652+653+654 & chain A ")


cmd.select("Astrand6", "resi 620+621+622+623+624+625+626+627+628 & chain A ")


cmd.select("Astrand5", "resi 604+605+606+607+608+609+610+611+612+613+614+615 & chain A ")


cmd.select("Astrand4", "resi 589+590+591+592+593+594+595+596+597+598+599 & chain A ")


cmd.select("Astrand3", "resi 575+576+577+578+579+580+581+582+583+584+585+586 & chain A ")


cmd.select("Astrand2", "resi 555+556+557+558+559+560+561+562+563+564+565 & chain A ")


cmd.select("Astrand1", "resi 540+541+542+543+544+545+546+547 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 527 & chain A")

cmd.select ("Outward", "resi 527 & chain A", merge=1)

cmd.color ("red", "resi 528 & chain A")

cmd.select ("Inward", "resi 528 & chain A", merge=1)

cmd.color ("blue", "resi 529 & chain A")

cmd.select ("Outward", "resi 529 & chain A", merge=1)

cmd.color ("red", "resi 530 & chain A")

cmd.select ("Inward", "resi 530 & chain A", merge=1)

cmd.color ("blue", "resi 793 & chain A")

cmd.select ("Outward", "resi 793 & chain A", merge=1)

cmd.color ("red", "resi 794 & chain A")

cmd.select ("Inward", "resi 794 & chain A", merge=1)

cmd.color ("blue", "resi 795 & chain A")

cmd.select ("Outward", "resi 795 & chain A", merge=1)

cmd.color ("red", "resi 796 & chain A")

cmd.select ("Inward", "resi 796 & chain A", merge=1)

cmd.color ("blue", "resi 797 & chain A")

cmd.select ("Outward", "resi 797 & chain A", merge=1)

cmd.color ("red", "resi 798 & chain A")

cmd.select ("Inward", "resi 798 & chain A", merge=1)

cmd.color ("blue", "resi 799 & chain A")

cmd.select ("Outward", "resi 799 & chain A", merge=1)

cmd.color ("red", "resi 800 & chain A")

cmd.select ("Inward", "resi 800 & chain A", merge=1)

cmd.color ("blue", "resi 801 & chain A")

cmd.select ("Outward", "resi 801 & chain A", merge=1)

cmd.color ("red", "resi 802 & chain A")

cmd.select ("Inward", "resi 802 & chain A", merge=1)

cmd.color ("blue", "resi 803 & chain A")

cmd.select ("Outward", "resi 803 & chain A", merge=1)

cmd.color ("red", "resi 804 & chain A")

cmd.select ("Inward", "resi 804 & chain A", merge=1)

cmd.color ("blue", "resi 805 & chain A")

cmd.select ("Outward", "resi 805 & chain A", merge=1)

cmd.color ("blue", "resi 806 & chain A")

cmd.select ("Outward", "resi 806 & chain A", merge=1)

cmd.color ("red", "resi 807 & chain A")

cmd.select ("Inward", "resi 807 & chain A", merge=1)

cmd.color ("blue", "resi 776 & chain A")

cmd.select ("Outward", "resi 776 & chain A", merge=1)

cmd.color ("red", "resi 777 & chain A")

cmd.select ("Inward", "resi 777 & chain A", merge=1)

cmd.color ("blue", "resi 778 & chain A")

cmd.select ("Outward", "resi 778 & chain A", merge=1)

cmd.color ("red", "resi 779 & chain A")

cmd.select ("Inward", "resi 779 & chain A", merge=1)

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

cmd.color ("blue", "resi 788 & chain A")

cmd.select ("Outward", "resi 788 & chain A", merge=1)

cmd.color ("red", "resi 757 & chain A")

cmd.select ("Inward", "resi 757 & chain A", merge=1)

cmd.color ("blue", "resi 758 & chain A")

cmd.select ("Outward", "resi 758 & chain A", merge=1)

cmd.color ("red", "resi 759 & chain A")

cmd.select ("Inward", "resi 759 & chain A", merge=1)

cmd.color ("blue", "resi 760 & chain A")

cmd.select ("Outward", "resi 760 & chain A", merge=1)

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

cmd.color ("red", "resi 771 & chain A")

cmd.select ("Inward", "resi 771 & chain A", merge=1)

cmd.color ("red", "resi 772 & chain A")

cmd.select ("Inward", "resi 772 & chain A", merge=1)

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

cmd.color ("red", "resi 729 & chain A")

cmd.select ("Inward", "resi 729 & chain A", merge=1)

cmd.color ("blue", "resi 730 & chain A")

cmd.select ("Outward", "resi 730 & chain A", merge=1)

cmd.color ("blue", "resi 731 & chain A")

cmd.select ("Outward", "resi 731 & chain A", merge=1)

cmd.color ("red", "resi 732 & chain A")

cmd.select ("Inward", "resi 732 & chain A", merge=1)

cmd.color ("blue", "resi 733 & chain A")

cmd.select ("Outward", "resi 733 & chain A", merge=1)

cmd.color ("red", "resi 734 & chain A")

cmd.select ("Inward", "resi 734 & chain A", merge=1)

cmd.color ("blue", "resi 735 & chain A")

cmd.select ("Outward", "resi 735 & chain A", merge=1)

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

cmd.color ("blue", "resi 659 & chain A")

cmd.select ("Outward", "resi 659 & chain A", merge=1)

cmd.color ("red", "resi 660 & chain A")

cmd.select ("Inward", "resi 660 & chain A", merge=1)

cmd.color ("blue", "resi 661 & chain A")

cmd.select ("Outward", "resi 661 & chain A", merge=1)

cmd.color ("red", "resi 662 & chain A")

cmd.select ("Inward", "resi 662 & chain A", merge=1)

cmd.color ("blue", "resi 663 & chain A")

cmd.select ("Outward", "resi 663 & chain A", merge=1)

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

cmd.color ("red", "resi 684 & chain A")

cmd.select ("Inward", "resi 684 & chain A", merge=1)

cmd.color ("blue", "resi 685 & chain A")

cmd.select ("Outward", "resi 685 & chain A", merge=1)

cmd.color ("blue", "resi 686 & chain A")

cmd.select ("Outward", "resi 686 & chain A", merge=1)

cmd.color ("red", "resi 687 & chain A")

cmd.select ("Inward", "resi 687 & chain A", merge=1)

cmd.color ("blue", "resi 688 & chain A")

cmd.select ("Outward", "resi 688 & chain A", merge=1)

cmd.color ("red", "resi 689 & chain A")

cmd.select ("Inward", "resi 689 & chain A", merge=1)

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

cmd.color ("blue", "resi 651 & chain A")

cmd.select ("Outward", "resi 651 & chain A", merge=1)

cmd.color ("red", "resi 652 & chain A")

cmd.select ("Inward", "resi 652 & chain A", merge=1)

cmd.color ("blue", "resi 653 & chain A")

cmd.select ("Outward", "resi 653 & chain A", merge=1)

cmd.color ("blue", "resi 654 & chain A")

cmd.select ("Outward", "resi 654 & chain A", merge=1)

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

cmd.color ("blue", "resi 615 & chain A")

cmd.select ("Outward", "resi 615 & chain A", merge=1)

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

cmd.load_cgo( [9.0, -194.41576,288.77075,179.75879, -194.41576, 288.77075, 179.75879, 1, 1,1,0,0,0,1], "axis" )
