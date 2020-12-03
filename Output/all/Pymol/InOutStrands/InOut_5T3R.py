from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5T3R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Dstrand15", "resi 212+213+214+215+216+217+218+219+220+221+222+223+224 & chain D ")


cmd.select("Dstrand53", "resi 1006+1007+1008+1009+1010+1011+1012+1013+1014+1015 & chain D ")


cmd.select("Dstrand51", "resi 972+973+974+975+976+977+978+979+980 & chain D ")


cmd.select("Dstrand50", "resi 948+949+950+951+952+953+954+955+956+957+958+959 & chain D ")


cmd.select("Dstrand47", "resi 872+873+874+875+876+877+878+879+880+881+882 & chain D ")


cmd.select("Dstrand46", "resi 859+860+861+862+863+864+865+866+867+868+869 & chain D ")


cmd.select("Dstrand41", "resi 761+762+763+764+765+766+767+768+769+770+771+772+773+774+775+776+777 & chain D ")


cmd.select("Dstrand40", "resi 740+741+742+743+744+745+746+747+748+749+750+751+752+753+754 & chain D ")


cmd.select("Dstrand37", "resi 704+705+706+707+708+709+710+711+712+713+714+715+716 & chain D ")


cmd.select("Dstrand30", "resi 591+592+593+594+595+596+597+598+599 & chain D ")


cmd.select("Dstrand35", "resi 686+687+688+689+690+691+692+693 & chain D ")


cmd.select("Dstrand32", "resi 620+621+622+623+624+625+626+627 & chain D ")


cmd.select("Dstrand29", "resi 569+570+571+572+573+574+575+576+577+578+579+580 & chain D ")


cmd.select("Dstrand28", "resi 543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+561+562+563+564 & chain D ")


cmd.select("Dstrand27", "resi 502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520+521+522+523+524 & chain D ")


cmd.select("Dstrand26", "resi 475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494 & chain D ")


cmd.select("Dstrand23", "resi 441+442+443+444+445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460 & chain D ")


cmd.select("Dstrand22", "resi 421+422+423+424+425+426+427+428+429+430+431+432+433+434+435 & chain D ")


cmd.select("Dstrand21", "resi 357+358+359+360+361+362+363+364+365+366+367+368+369+370+371 & chain D ")


cmd.select("Dstrand20", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352+353 & chain D ")


cmd.select("Dstrand19", "resi 319+320+321+322+323+324+325+326+327+328+329+330+331 & chain D ")


cmd.select("Dstrand18", "resi 303+304+305+306+307+308+309+310+311+312+313+314+315 & chain D ")


cmd.select("barrel", "Dstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 212 & chain D")

cmd.select ("Outward", "resi 212 & chain D", merge=1)

cmd.color ("red", "resi 213 & chain D")

cmd.select ("Inward", "resi 213 & chain D", merge=1)

cmd.color ("blue", "resi 214 & chain D")

cmd.select ("Outward", "resi 214 & chain D", merge=1)

cmd.color ("red", "resi 215 & chain D")

cmd.select ("Inward", "resi 215 & chain D", merge=1)

cmd.color ("blue", "resi 216 & chain D")

cmd.select ("Outward", "resi 216 & chain D", merge=1)

cmd.color ("red", "resi 217 & chain D")

cmd.select ("Inward", "resi 217 & chain D", merge=1)

cmd.color ("blue", "resi 218 & chain D")

cmd.select ("Outward", "resi 218 & chain D", merge=1)

cmd.color ("red", "resi 219 & chain D")

cmd.select ("Inward", "resi 219 & chain D", merge=1)

cmd.color ("blue", "resi 220 & chain D")

cmd.select ("Outward", "resi 220 & chain D", merge=1)

cmd.color ("red", "resi 221 & chain D")

cmd.select ("Inward", "resi 221 & chain D", merge=1)

cmd.color ("blue", "resi 222 & chain D")

cmd.select ("Outward", "resi 222 & chain D", merge=1)

cmd.color ("red", "resi 223 & chain D")

cmd.select ("Inward", "resi 223 & chain D", merge=1)

cmd.color ("blue", "resi 224 & chain D")

cmd.select ("Outward", "resi 224 & chain D", merge=1)

cmd.color ("blue", "resi 1006 & chain D")

cmd.select ("Outward", "resi 1006 & chain D", merge=1)

cmd.color ("red", "resi 1007 & chain D")

cmd.select ("Inward", "resi 1007 & chain D", merge=1)

cmd.color ("blue", "resi 1008 & chain D")

cmd.select ("Outward", "resi 1008 & chain D", merge=1)

cmd.color ("red", "resi 1009 & chain D")

cmd.select ("Inward", "resi 1009 & chain D", merge=1)

cmd.color ("blue", "resi 1010 & chain D")

cmd.select ("Outward", "resi 1010 & chain D", merge=1)

cmd.color ("red", "resi 1011 & chain D")

cmd.select ("Inward", "resi 1011 & chain D", merge=1)

cmd.color ("blue", "resi 1012 & chain D")

cmd.select ("Outward", "resi 1012 & chain D", merge=1)

cmd.color ("red", "resi 1013 & chain D")

cmd.select ("Inward", "resi 1013 & chain D", merge=1)

cmd.color ("blue", "resi 1014 & chain D")

cmd.select ("Outward", "resi 1014 & chain D", merge=1)

cmd.color ("red", "resi 1015 & chain D")

cmd.select ("Inward", "resi 1015 & chain D", merge=1)

cmd.color ("red", "resi 972 & chain D")

cmd.select ("Inward", "resi 972 & chain D", merge=1)

cmd.color ("blue", "resi 973 & chain D")

cmd.select ("Outward", "resi 973 & chain D", merge=1)

cmd.color ("red", "resi 974 & chain D")

cmd.select ("Inward", "resi 974 & chain D", merge=1)

cmd.color ("blue", "resi 975 & chain D")

cmd.select ("Outward", "resi 975 & chain D", merge=1)

cmd.color ("red", "resi 976 & chain D")

cmd.select ("Inward", "resi 976 & chain D", merge=1)

cmd.color ("blue", "resi 977 & chain D")

cmd.select ("Outward", "resi 977 & chain D", merge=1)

cmd.color ("red", "resi 978 & chain D")

cmd.select ("Inward", "resi 978 & chain D", merge=1)

cmd.color ("blue", "resi 979 & chain D")

cmd.select ("Outward", "resi 979 & chain D", merge=1)

cmd.color ("red", "resi 980 & chain D")

cmd.select ("Inward", "resi 980 & chain D", merge=1)

cmd.color ("red", "resi 948 & chain D")

cmd.select ("Inward", "resi 948 & chain D", merge=1)

cmd.color ("blue", "resi 949 & chain D")

cmd.select ("Outward", "resi 949 & chain D", merge=1)

cmd.color ("red", "resi 950 & chain D")

cmd.select ("Inward", "resi 950 & chain D", merge=1)

cmd.color ("blue", "resi 951 & chain D")

cmd.select ("Outward", "resi 951 & chain D", merge=1)

cmd.color ("red", "resi 952 & chain D")

cmd.select ("Inward", "resi 952 & chain D", merge=1)

cmd.color ("red", "resi 953 & chain D")

cmd.select ("Inward", "resi 953 & chain D", merge=1)

cmd.color ("blue", "resi 954 & chain D")

cmd.select ("Outward", "resi 954 & chain D", merge=1)

cmd.color ("red", "resi 955 & chain D")

cmd.select ("Inward", "resi 955 & chain D", merge=1)

cmd.color ("blue", "resi 956 & chain D")

cmd.select ("Outward", "resi 956 & chain D", merge=1)

cmd.color ("red", "resi 957 & chain D")

cmd.select ("Inward", "resi 957 & chain D", merge=1)

cmd.color ("blue", "resi 958 & chain D")

cmd.select ("Outward", "resi 958 & chain D", merge=1)

cmd.color ("red", "resi 959 & chain D")

cmd.select ("Inward", "resi 959 & chain D", merge=1)

cmd.color ("blue", "resi 872 & chain D")

cmd.select ("Outward", "resi 872 & chain D", merge=1)

cmd.color ("red", "resi 873 & chain D")

cmd.select ("Inward", "resi 873 & chain D", merge=1)

cmd.color ("blue", "resi 874 & chain D")

cmd.select ("Outward", "resi 874 & chain D", merge=1)

cmd.color ("red", "resi 875 & chain D")

cmd.select ("Inward", "resi 875 & chain D", merge=1)

cmd.color ("blue", "resi 876 & chain D")

cmd.select ("Outward", "resi 876 & chain D", merge=1)

cmd.color ("red", "resi 877 & chain D")

cmd.select ("Inward", "resi 877 & chain D", merge=1)

cmd.color ("blue", "resi 878 & chain D")

cmd.select ("Outward", "resi 878 & chain D", merge=1)

cmd.color ("red", "resi 879 & chain D")

cmd.select ("Inward", "resi 879 & chain D", merge=1)

cmd.color ("blue", "resi 880 & chain D")

cmd.select ("Outward", "resi 880 & chain D", merge=1)

cmd.color ("red", "resi 881 & chain D")

cmd.select ("Inward", "resi 881 & chain D", merge=1)

cmd.color ("red", "resi 882 & chain D")

cmd.select ("Inward", "resi 882 & chain D", merge=1)

cmd.color ("blue", "resi 859 & chain D")

cmd.select ("Outward", "resi 859 & chain D", merge=1)

cmd.color ("red", "resi 860 & chain D")

cmd.select ("Inward", "resi 860 & chain D", merge=1)

cmd.color ("blue", "resi 861 & chain D")

cmd.select ("Outward", "resi 861 & chain D", merge=1)

cmd.color ("red", "resi 862 & chain D")

cmd.select ("Inward", "resi 862 & chain D", merge=1)

cmd.color ("blue", "resi 863 & chain D")

cmd.select ("Outward", "resi 863 & chain D", merge=1)

cmd.color ("red", "resi 864 & chain D")

cmd.select ("Inward", "resi 864 & chain D", merge=1)

cmd.color ("blue", "resi 865 & chain D")

cmd.select ("Outward", "resi 865 & chain D", merge=1)

cmd.color ("red", "resi 866 & chain D")

cmd.select ("Inward", "resi 866 & chain D", merge=1)

cmd.color ("blue", "resi 867 & chain D")

cmd.select ("Outward", "resi 867 & chain D", merge=1)

cmd.color ("red", "resi 868 & chain D")

cmd.select ("Inward", "resi 868 & chain D", merge=1)

cmd.color ("blue", "resi 869 & chain D")

cmd.select ("Outward", "resi 869 & chain D", merge=1)

cmd.color ("red", "resi 761 & chain D")

cmd.select ("Inward", "resi 761 & chain D", merge=1)

cmd.color ("blue", "resi 762 & chain D")

cmd.select ("Outward", "resi 762 & chain D", merge=1)

cmd.color ("red", "resi 763 & chain D")

cmd.select ("Inward", "resi 763 & chain D", merge=1)

cmd.color ("blue", "resi 764 & chain D")

cmd.select ("Outward", "resi 764 & chain D", merge=1)

cmd.color ("red", "resi 765 & chain D")

cmd.select ("Inward", "resi 765 & chain D", merge=1)

cmd.color ("blue", "resi 766 & chain D")

cmd.select ("Outward", "resi 766 & chain D", merge=1)

cmd.color ("red", "resi 767 & chain D")

cmd.select ("Inward", "resi 767 & chain D", merge=1)

cmd.color ("blue", "resi 768 & chain D")

cmd.select ("Outward", "resi 768 & chain D", merge=1)

cmd.color ("red", "resi 769 & chain D")

cmd.select ("Inward", "resi 769 & chain D", merge=1)

cmd.color ("blue", "resi 770 & chain D")

cmd.select ("Outward", "resi 770 & chain D", merge=1)

cmd.color ("red", "resi 771 & chain D")

cmd.select ("Inward", "resi 771 & chain D", merge=1)

cmd.color ("blue", "resi 772 & chain D")

cmd.select ("Outward", "resi 772 & chain D", merge=1)

cmd.color ("red", "resi 773 & chain D")

cmd.select ("Inward", "resi 773 & chain D", merge=1)

cmd.color ("blue", "resi 774 & chain D")

cmd.select ("Outward", "resi 774 & chain D", merge=1)

cmd.color ("blue", "resi 775 & chain D")

cmd.select ("Outward", "resi 775 & chain D", merge=1)

cmd.color ("red", "resi 776 & chain D")

cmd.select ("Inward", "resi 776 & chain D", merge=1)

cmd.color ("blue", "resi 777 & chain D")

cmd.select ("Outward", "resi 777 & chain D", merge=1)

cmd.color ("blue", "resi 740 & chain D")

cmd.select ("Outward", "resi 740 & chain D", merge=1)

cmd.color ("red", "resi 741 & chain D")

cmd.select ("Inward", "resi 741 & chain D", merge=1)

cmd.color ("blue", "resi 742 & chain D")

cmd.select ("Outward", "resi 742 & chain D", merge=1)

cmd.color ("red", "resi 743 & chain D")

cmd.select ("Inward", "resi 743 & chain D", merge=1)

cmd.color ("blue", "resi 744 & chain D")

cmd.select ("Outward", "resi 744 & chain D", merge=1)

cmd.color ("red", "resi 745 & chain D")

cmd.select ("Inward", "resi 745 & chain D", merge=1)

cmd.color ("blue", "resi 746 & chain D")

cmd.select ("Outward", "resi 746 & chain D", merge=1)

cmd.color ("red", "resi 747 & chain D")

cmd.select ("Inward", "resi 747 & chain D", merge=1)

cmd.color ("blue", "resi 748 & chain D")

cmd.select ("Outward", "resi 748 & chain D", merge=1)

cmd.color ("red", "resi 749 & chain D")

cmd.select ("Inward", "resi 749 & chain D", merge=1)

cmd.color ("blue", "resi 750 & chain D")

cmd.select ("Outward", "resi 750 & chain D", merge=1)

cmd.color ("red", "resi 751 & chain D")

cmd.select ("Inward", "resi 751 & chain D", merge=1)

cmd.color ("blue", "resi 752 & chain D")

cmd.select ("Outward", "resi 752 & chain D", merge=1)

cmd.color ("red", "resi 753 & chain D")

cmd.select ("Inward", "resi 753 & chain D", merge=1)

cmd.color ("blue", "resi 754 & chain D")

cmd.select ("Outward", "resi 754 & chain D", merge=1)

cmd.color ("blue", "resi 704 & chain D")

cmd.select ("Outward", "resi 704 & chain D", merge=1)

cmd.color ("red", "resi 705 & chain D")

cmd.select ("Inward", "resi 705 & chain D", merge=1)

cmd.color ("blue", "resi 706 & chain D")

cmd.select ("Outward", "resi 706 & chain D", merge=1)

cmd.color ("red", "resi 707 & chain D")

cmd.select ("Inward", "resi 707 & chain D", merge=1)

cmd.color ("blue", "resi 708 & chain D")

cmd.select ("Outward", "resi 708 & chain D", merge=1)

cmd.color ("red", "resi 709 & chain D")

cmd.select ("Inward", "resi 709 & chain D", merge=1)

cmd.color ("blue", "resi 710 & chain D")

cmd.select ("Outward", "resi 710 & chain D", merge=1)

cmd.color ("red", "resi 711 & chain D")

cmd.select ("Inward", "resi 711 & chain D", merge=1)

cmd.color ("blue", "resi 712 & chain D")

cmd.select ("Outward", "resi 712 & chain D", merge=1)

cmd.color ("red", "resi 713 & chain D")

cmd.select ("Inward", "resi 713 & chain D", merge=1)

cmd.color ("blue", "resi 714 & chain D")

cmd.select ("Outward", "resi 714 & chain D", merge=1)

cmd.color ("red", "resi 715 & chain D")

cmd.select ("Inward", "resi 715 & chain D", merge=1)

cmd.color ("red", "resi 716 & chain D")

cmd.select ("Inward", "resi 716 & chain D", merge=1)

cmd.color ("blue", "resi 591 & chain D")

cmd.select ("Outward", "resi 591 & chain D", merge=1)

cmd.color ("red", "resi 592 & chain D")

cmd.select ("Inward", "resi 592 & chain D", merge=1)

cmd.color ("blue", "resi 593 & chain D")

cmd.select ("Outward", "resi 593 & chain D", merge=1)

cmd.color ("red", "resi 594 & chain D")

cmd.select ("Inward", "resi 594 & chain D", merge=1)

cmd.color ("blue", "resi 595 & chain D")

cmd.select ("Outward", "resi 595 & chain D", merge=1)

cmd.color ("red", "resi 596 & chain D")

cmd.select ("Inward", "resi 596 & chain D", merge=1)

cmd.color ("blue", "resi 597 & chain D")

cmd.select ("Outward", "resi 597 & chain D", merge=1)

cmd.color ("red", "resi 598 & chain D")

cmd.select ("Inward", "resi 598 & chain D", merge=1)

cmd.color ("blue", "resi 599 & chain D")

cmd.select ("Outward", "resi 599 & chain D", merge=1)

cmd.color ("red", "resi 686 & chain D")

cmd.select ("Inward", "resi 686 & chain D", merge=1)

cmd.color ("blue", "resi 687 & chain D")

cmd.select ("Outward", "resi 687 & chain D", merge=1)

cmd.color ("red", "resi 688 & chain D")

cmd.select ("Inward", "resi 688 & chain D", merge=1)

cmd.color ("blue", "resi 689 & chain D")

cmd.select ("Outward", "resi 689 & chain D", merge=1)

cmd.color ("red", "resi 690 & chain D")

cmd.select ("Inward", "resi 690 & chain D", merge=1)

cmd.color ("blue", "resi 691 & chain D")

cmd.select ("Outward", "resi 691 & chain D", merge=1)

cmd.color ("red", "resi 692 & chain D")

cmd.select ("Inward", "resi 692 & chain D", merge=1)

cmd.color ("blue", "resi 693 & chain D")

cmd.select ("Outward", "resi 693 & chain D", merge=1)

cmd.color ("blue", "resi 620 & chain D")

cmd.select ("Outward", "resi 620 & chain D", merge=1)

cmd.color ("red", "resi 621 & chain D")

cmd.select ("Inward", "resi 621 & chain D", merge=1)

cmd.color ("blue", "resi 622 & chain D")

cmd.select ("Outward", "resi 622 & chain D", merge=1)

cmd.color ("red", "resi 623 & chain D")

cmd.select ("Inward", "resi 623 & chain D", merge=1)

cmd.color ("blue", "resi 624 & chain D")

cmd.select ("Outward", "resi 624 & chain D", merge=1)

cmd.color ("red", "resi 625 & chain D")

cmd.select ("Inward", "resi 625 & chain D", merge=1)

cmd.color ("blue", "resi 626 & chain D")

cmd.select ("Outward", "resi 626 & chain D", merge=1)

cmd.color ("red", "resi 627 & chain D")

cmd.select ("Inward", "resi 627 & chain D", merge=1)

cmd.color ("blue", "resi 569 & chain D")

cmd.select ("Outward", "resi 569 & chain D", merge=1)

cmd.color ("red", "resi 570 & chain D")

cmd.select ("Inward", "resi 570 & chain D", merge=1)

cmd.color ("blue", "resi 571 & chain D")

cmd.select ("Outward", "resi 571 & chain D", merge=1)

cmd.color ("red", "resi 572 & chain D")

cmd.select ("Inward", "resi 572 & chain D", merge=1)

cmd.color ("blue", "resi 573 & chain D")

cmd.select ("Outward", "resi 573 & chain D", merge=1)

cmd.color ("red", "resi 574 & chain D")

cmd.select ("Inward", "resi 574 & chain D", merge=1)

cmd.color ("blue", "resi 575 & chain D")

cmd.select ("Outward", "resi 575 & chain D", merge=1)

cmd.color ("red", "resi 576 & chain D")

cmd.select ("Inward", "resi 576 & chain D", merge=1)

cmd.color ("blue", "resi 577 & chain D")

cmd.select ("Outward", "resi 577 & chain D", merge=1)

cmd.color ("red", "resi 578 & chain D")

cmd.select ("Inward", "resi 578 & chain D", merge=1)

cmd.color ("blue", "resi 579 & chain D")

cmd.select ("Outward", "resi 579 & chain D", merge=1)

cmd.color ("red", "resi 580 & chain D")

cmd.select ("Inward", "resi 580 & chain D", merge=1)

cmd.color ("blue", "resi 543 & chain D")

cmd.select ("Outward", "resi 543 & chain D", merge=1)

cmd.color ("red", "resi 544 & chain D")

cmd.select ("Inward", "resi 544 & chain D", merge=1)

cmd.color ("blue", "resi 545 & chain D")

cmd.select ("Outward", "resi 545 & chain D", merge=1)

cmd.color ("red", "resi 546 & chain D")

cmd.select ("Inward", "resi 546 & chain D", merge=1)

cmd.color ("blue", "resi 547 & chain D")

cmd.select ("Outward", "resi 547 & chain D", merge=1)

cmd.color ("red", "resi 548 & chain D")

cmd.select ("Inward", "resi 548 & chain D", merge=1)

cmd.color ("blue", "resi 549 & chain D")

cmd.select ("Outward", "resi 549 & chain D", merge=1)

cmd.color ("red", "resi 550 & chain D")

cmd.select ("Inward", "resi 550 & chain D", merge=1)

cmd.color ("blue", "resi 551 & chain D")

cmd.select ("Outward", "resi 551 & chain D", merge=1)

cmd.color ("red", "resi 552 & chain D")

cmd.select ("Inward", "resi 552 & chain D", merge=1)

cmd.color ("blue", "resi 553 & chain D")

cmd.select ("Outward", "resi 553 & chain D", merge=1)

cmd.color ("red", "resi 554 & chain D")

cmd.select ("Inward", "resi 554 & chain D", merge=1)

cmd.color ("blue", "resi 555 & chain D")

cmd.select ("Outward", "resi 555 & chain D", merge=1)

cmd.color ("red", "resi 556 & chain D")

cmd.select ("Inward", "resi 556 & chain D", merge=1)

cmd.color ("blue", "resi 557 & chain D")

cmd.select ("Outward", "resi 557 & chain D", merge=1)

cmd.color ("red", "resi 558 & chain D")

cmd.select ("Inward", "resi 558 & chain D", merge=1)

cmd.color ("blue", "resi 559 & chain D")

cmd.select ("Outward", "resi 559 & chain D", merge=1)

cmd.color ("red", "resi 560 & chain D")

cmd.select ("Inward", "resi 560 & chain D", merge=1)

cmd.color ("blue", "resi 561 & chain D")

cmd.select ("Outward", "resi 561 & chain D", merge=1)

cmd.color ("red", "resi 562 & chain D")

cmd.select ("Inward", "resi 562 & chain D", merge=1)

cmd.color ("blue", "resi 563 & chain D")

cmd.select ("Outward", "resi 563 & chain D", merge=1)

cmd.color ("red", "resi 564 & chain D")

cmd.select ("Inward", "resi 564 & chain D", merge=1)

cmd.color ("red", "resi 502 & chain D")

cmd.select ("Inward", "resi 502 & chain D", merge=1)

cmd.color ("blue", "resi 503 & chain D")

cmd.select ("Outward", "resi 503 & chain D", merge=1)

cmd.color ("red", "resi 504 & chain D")

cmd.select ("Inward", "resi 504 & chain D", merge=1)

cmd.color ("blue", "resi 505 & chain D")

cmd.select ("Outward", "resi 505 & chain D", merge=1)

cmd.color ("red", "resi 506 & chain D")

cmd.select ("Inward", "resi 506 & chain D", merge=1)

cmd.color ("blue", "resi 507 & chain D")

cmd.select ("Outward", "resi 507 & chain D", merge=1)

cmd.color ("red", "resi 508 & chain D")

cmd.select ("Inward", "resi 508 & chain D", merge=1)

cmd.color ("blue", "resi 509 & chain D")

cmd.select ("Outward", "resi 509 & chain D", merge=1)

cmd.color ("red", "resi 510 & chain D")

cmd.select ("Inward", "resi 510 & chain D", merge=1)

cmd.color ("blue", "resi 511 & chain D")

cmd.select ("Outward", "resi 511 & chain D", merge=1)

cmd.color ("red", "resi 512 & chain D")

cmd.select ("Inward", "resi 512 & chain D", merge=1)

cmd.color ("blue", "resi 513 & chain D")

cmd.select ("Outward", "resi 513 & chain D", merge=1)

cmd.color ("red", "resi 514 & chain D")

cmd.select ("Inward", "resi 514 & chain D", merge=1)

cmd.color ("blue", "resi 515 & chain D")

cmd.select ("Outward", "resi 515 & chain D", merge=1)

cmd.color ("red", "resi 516 & chain D")

cmd.select ("Inward", "resi 516 & chain D", merge=1)

cmd.color ("blue", "resi 517 & chain D")

cmd.select ("Outward", "resi 517 & chain D", merge=1)

cmd.color ("red", "resi 518 & chain D")

cmd.select ("Inward", "resi 518 & chain D", merge=1)

cmd.color ("blue", "resi 519 & chain D")

cmd.select ("Outward", "resi 519 & chain D", merge=1)

cmd.color ("red", "resi 520 & chain D")

cmd.select ("Inward", "resi 520 & chain D", merge=1)

cmd.color ("blue", "resi 521 & chain D")

cmd.select ("Outward", "resi 521 & chain D", merge=1)

cmd.color ("red", "resi 522 & chain D")

cmd.select ("Inward", "resi 522 & chain D", merge=1)

cmd.color ("blue", "resi 523 & chain D")

cmd.select ("Outward", "resi 523 & chain D", merge=1)

cmd.color ("blue", "resi 524 & chain D")

cmd.select ("Outward", "resi 524 & chain D", merge=1)

cmd.color ("red", "resi 475 & chain D")

cmd.select ("Inward", "resi 475 & chain D", merge=1)

cmd.color ("blue", "resi 476 & chain D")

cmd.select ("Outward", "resi 476 & chain D", merge=1)

cmd.color ("red", "resi 477 & chain D")

cmd.select ("Inward", "resi 477 & chain D", merge=1)

cmd.color ("blue", "resi 478 & chain D")

cmd.select ("Outward", "resi 478 & chain D", merge=1)

cmd.color ("red", "resi 479 & chain D")

cmd.select ("Inward", "resi 479 & chain D", merge=1)

cmd.color ("blue", "resi 480 & chain D")

cmd.select ("Outward", "resi 480 & chain D", merge=1)

cmd.color ("red", "resi 481 & chain D")

cmd.select ("Inward", "resi 481 & chain D", merge=1)

cmd.color ("blue", "resi 482 & chain D")

cmd.select ("Outward", "resi 482 & chain D", merge=1)

cmd.color ("red", "resi 483 & chain D")

cmd.select ("Inward", "resi 483 & chain D", merge=1)

cmd.color ("blue", "resi 484 & chain D")

cmd.select ("Outward", "resi 484 & chain D", merge=1)

cmd.color ("red", "resi 485 & chain D")

cmd.select ("Inward", "resi 485 & chain D", merge=1)

cmd.color ("blue", "resi 486 & chain D")

cmd.select ("Outward", "resi 486 & chain D", merge=1)

cmd.color ("red", "resi 487 & chain D")

cmd.select ("Inward", "resi 487 & chain D", merge=1)

cmd.color ("blue", "resi 488 & chain D")

cmd.select ("Outward", "resi 488 & chain D", merge=1)

cmd.color ("red", "resi 489 & chain D")

cmd.select ("Inward", "resi 489 & chain D", merge=1)

cmd.color ("blue", "resi 490 & chain D")

cmd.select ("Outward", "resi 490 & chain D", merge=1)

cmd.color ("red", "resi 491 & chain D")

cmd.select ("Inward", "resi 491 & chain D", merge=1)

cmd.color ("blue", "resi 492 & chain D")

cmd.select ("Outward", "resi 492 & chain D", merge=1)

cmd.color ("red", "resi 493 & chain D")

cmd.select ("Inward", "resi 493 & chain D", merge=1)

cmd.color ("blue", "resi 494 & chain D")

cmd.select ("Outward", "resi 494 & chain D", merge=1)

cmd.color ("blue", "resi 441 & chain D")

cmd.select ("Outward", "resi 441 & chain D", merge=1)

cmd.color ("red", "resi 442 & chain D")

cmd.select ("Inward", "resi 442 & chain D", merge=1)

cmd.color ("blue", "resi 443 & chain D")

cmd.select ("Outward", "resi 443 & chain D", merge=1)

cmd.color ("red", "resi 444 & chain D")

cmd.select ("Inward", "resi 444 & chain D", merge=1)

cmd.color ("blue", "resi 445 & chain D")

cmd.select ("Outward", "resi 445 & chain D", merge=1)

cmd.color ("red", "resi 446 & chain D")

cmd.select ("Inward", "resi 446 & chain D", merge=1)

cmd.color ("blue", "resi 447 & chain D")

cmd.select ("Outward", "resi 447 & chain D", merge=1)

cmd.color ("red", "resi 448 & chain D")

cmd.select ("Inward", "resi 448 & chain D", merge=1)

cmd.color ("blue", "resi 449 & chain D")

cmd.select ("Outward", "resi 449 & chain D", merge=1)

cmd.color ("red", "resi 450 & chain D")

cmd.select ("Inward", "resi 450 & chain D", merge=1)

cmd.color ("blue", "resi 451 & chain D")

cmd.select ("Outward", "resi 451 & chain D", merge=1)

cmd.color ("red", "resi 452 & chain D")

cmd.select ("Inward", "resi 452 & chain D", merge=1)

cmd.color ("blue", "resi 453 & chain D")

cmd.select ("Outward", "resi 453 & chain D", merge=1)

cmd.color ("red", "resi 454 & chain D")

cmd.select ("Inward", "resi 454 & chain D", merge=1)

cmd.color ("blue", "resi 455 & chain D")

cmd.select ("Outward", "resi 455 & chain D", merge=1)

cmd.color ("red", "resi 456 & chain D")

cmd.select ("Inward", "resi 456 & chain D", merge=1)

cmd.color ("blue", "resi 457 & chain D")

cmd.select ("Outward", "resi 457 & chain D", merge=1)

cmd.color ("red", "resi 458 & chain D")

cmd.select ("Inward", "resi 458 & chain D", merge=1)

cmd.color ("blue", "resi 459 & chain D")

cmd.select ("Outward", "resi 459 & chain D", merge=1)

cmd.color ("blue", "resi 460 & chain D")

cmd.select ("Outward", "resi 460 & chain D", merge=1)

cmd.color ("blue", "resi 421 & chain D")

cmd.select ("Outward", "resi 421 & chain D", merge=1)

cmd.color ("red", "resi 422 & chain D")

cmd.select ("Inward", "resi 422 & chain D", merge=1)

cmd.color ("blue", "resi 423 & chain D")

cmd.select ("Outward", "resi 423 & chain D", merge=1)

cmd.color ("red", "resi 424 & chain D")

cmd.select ("Inward", "resi 424 & chain D", merge=1)

cmd.color ("blue", "resi 425 & chain D")

cmd.select ("Outward", "resi 425 & chain D", merge=1)

cmd.color ("red", "resi 426 & chain D")

cmd.select ("Inward", "resi 426 & chain D", merge=1)

cmd.color ("blue", "resi 427 & chain D")

cmd.select ("Outward", "resi 427 & chain D", merge=1)

cmd.color ("red", "resi 428 & chain D")

cmd.select ("Inward", "resi 428 & chain D", merge=1)

cmd.color ("blue", "resi 429 & chain D")

cmd.select ("Outward", "resi 429 & chain D", merge=1)

cmd.color ("red", "resi 430 & chain D")

cmd.select ("Inward", "resi 430 & chain D", merge=1)

cmd.color ("blue", "resi 431 & chain D")

cmd.select ("Outward", "resi 431 & chain D", merge=1)

cmd.color ("red", "resi 432 & chain D")

cmd.select ("Inward", "resi 432 & chain D", merge=1)

cmd.color ("blue", "resi 433 & chain D")

cmd.select ("Outward", "resi 433 & chain D", merge=1)

cmd.color ("red", "resi 434 & chain D")

cmd.select ("Inward", "resi 434 & chain D", merge=1)

cmd.color ("blue", "resi 435 & chain D")

cmd.select ("Outward", "resi 435 & chain D", merge=1)

cmd.color ("blue", "resi 357 & chain D")

cmd.select ("Outward", "resi 357 & chain D", merge=1)

cmd.color ("red", "resi 358 & chain D")

cmd.select ("Inward", "resi 358 & chain D", merge=1)

cmd.color ("blue", "resi 359 & chain D")

cmd.select ("Outward", "resi 359 & chain D", merge=1)

cmd.color ("red", "resi 360 & chain D")

cmd.select ("Inward", "resi 360 & chain D", merge=1)

cmd.color ("blue", "resi 361 & chain D")

cmd.select ("Outward", "resi 361 & chain D", merge=1)

cmd.color ("red", "resi 362 & chain D")

cmd.select ("Inward", "resi 362 & chain D", merge=1)

cmd.color ("blue", "resi 363 & chain D")

cmd.select ("Outward", "resi 363 & chain D", merge=1)

cmd.color ("red", "resi 364 & chain D")

cmd.select ("Inward", "resi 364 & chain D", merge=1)

cmd.color ("blue", "resi 365 & chain D")

cmd.select ("Outward", "resi 365 & chain D", merge=1)

cmd.color ("red", "resi 366 & chain D")

cmd.select ("Inward", "resi 366 & chain D", merge=1)

cmd.color ("blue", "resi 367 & chain D")

cmd.select ("Outward", "resi 367 & chain D", merge=1)

cmd.color ("red", "resi 368 & chain D")

cmd.select ("Inward", "resi 368 & chain D", merge=1)

cmd.color ("blue", "resi 369 & chain D")

cmd.select ("Outward", "resi 369 & chain D", merge=1)

cmd.color ("red", "resi 370 & chain D")

cmd.select ("Inward", "resi 370 & chain D", merge=1)

cmd.color ("blue", "resi 371 & chain D")

cmd.select ("Outward", "resi 371 & chain D", merge=1)

cmd.color ("red", "resi 339 & chain D")

cmd.select ("Inward", "resi 339 & chain D", merge=1)

cmd.color ("blue", "resi 340 & chain D")

cmd.select ("Outward", "resi 340 & chain D", merge=1)

cmd.color ("red", "resi 341 & chain D")

cmd.select ("Inward", "resi 341 & chain D", merge=1)

cmd.color ("blue", "resi 342 & chain D")

cmd.select ("Outward", "resi 342 & chain D", merge=1)

cmd.color ("red", "resi 343 & chain D")

cmd.select ("Inward", "resi 343 & chain D", merge=1)

cmd.color ("blue", "resi 344 & chain D")

cmd.select ("Outward", "resi 344 & chain D", merge=1)

cmd.color ("red", "resi 345 & chain D")

cmd.select ("Inward", "resi 345 & chain D", merge=1)

cmd.color ("blue", "resi 346 & chain D")

cmd.select ("Outward", "resi 346 & chain D", merge=1)

cmd.color ("red", "resi 347 & chain D")

cmd.select ("Inward", "resi 347 & chain D", merge=1)

cmd.color ("blue", "resi 348 & chain D")

cmd.select ("Outward", "resi 348 & chain D", merge=1)

cmd.color ("red", "resi 349 & chain D")

cmd.select ("Inward", "resi 349 & chain D", merge=1)

cmd.color ("blue", "resi 350 & chain D")

cmd.select ("Outward", "resi 350 & chain D", merge=1)

cmd.color ("blue", "resi 351 & chain D")

cmd.select ("Outward", "resi 351 & chain D", merge=1)

cmd.color ("red", "resi 352 & chain D")

cmd.select ("Inward", "resi 352 & chain D", merge=1)

cmd.color ("blue", "resi 353 & chain D")

cmd.select ("Outward", "resi 353 & chain D", merge=1)

cmd.color ("blue", "resi 319 & chain D")

cmd.select ("Outward", "resi 319 & chain D", merge=1)

cmd.color ("red", "resi 320 & chain D")

cmd.select ("Inward", "resi 320 & chain D", merge=1)

cmd.color ("blue", "resi 321 & chain D")

cmd.select ("Outward", "resi 321 & chain D", merge=1)

cmd.color ("red", "resi 322 & chain D")

cmd.select ("Inward", "resi 322 & chain D", merge=1)

cmd.color ("blue", "resi 323 & chain D")

cmd.select ("Outward", "resi 323 & chain D", merge=1)

cmd.color ("red", "resi 324 & chain D")

cmd.select ("Inward", "resi 324 & chain D", merge=1)

cmd.color ("blue", "resi 325 & chain D")

cmd.select ("Outward", "resi 325 & chain D", merge=1)

cmd.color ("red", "resi 326 & chain D")

cmd.select ("Inward", "resi 326 & chain D", merge=1)

cmd.color ("blue", "resi 327 & chain D")

cmd.select ("Outward", "resi 327 & chain D", merge=1)

cmd.color ("red", "resi 328 & chain D")

cmd.select ("Inward", "resi 328 & chain D", merge=1)

cmd.color ("blue", "resi 329 & chain D")

cmd.select ("Outward", "resi 329 & chain D", merge=1)

cmd.color ("red", "resi 330 & chain D")

cmd.select ("Inward", "resi 330 & chain D", merge=1)

cmd.color ("blue", "resi 331 & chain D")

cmd.select ("Outward", "resi 331 & chain D", merge=1)

cmd.color ("red", "resi 303 & chain D")

cmd.select ("Inward", "resi 303 & chain D", merge=1)

cmd.color ("blue", "resi 304 & chain D")

cmd.select ("Outward", "resi 304 & chain D", merge=1)

cmd.color ("red", "resi 305 & chain D")

cmd.select ("Inward", "resi 305 & chain D", merge=1)

cmd.color ("blue", "resi 306 & chain D")

cmd.select ("Outward", "resi 306 & chain D", merge=1)

cmd.color ("red", "resi 307 & chain D")

cmd.select ("Inward", "resi 307 & chain D", merge=1)

cmd.color ("blue", "resi 308 & chain D")

cmd.select ("Outward", "resi 308 & chain D", merge=1)

cmd.color ("red", "resi 309 & chain D")

cmd.select ("Inward", "resi 309 & chain D", merge=1)

cmd.color ("blue", "resi 310 & chain D")

cmd.select ("Outward", "resi 310 & chain D", merge=1)

cmd.color ("red", "resi 311 & chain D")

cmd.select ("Inward", "resi 311 & chain D", merge=1)

cmd.color ("blue", "resi 312 & chain D")

cmd.select ("Outward", "resi 312 & chain D", merge=1)

cmd.color ("red", "resi 313 & chain D")

cmd.select ("Inward", "resi 313 & chain D", merge=1)

cmd.color ("blue", "resi 314 & chain D")

cmd.select ("Outward", "resi 314 & chain D", merge=1)

cmd.color ("red", "resi 315 & chain D")

cmd.select ("Inward", "resi 315 & chain D", merge=1)

cmd.load_cgo( [9.0, 15.421091,392.28958,137.63185, 15.421091, 392.28958, 137.63185, 1, 1,1,0,0,0,1], "axis" )
