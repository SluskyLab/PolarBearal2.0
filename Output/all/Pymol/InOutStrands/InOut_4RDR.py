from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RDR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand7", "resi 148+149+150+151+152+153+154+155+156+157 & chain A ")


cmd.select("Astrand35", "resi 725+726+727+728+729+730+731+732+733 & chain A ")


cmd.select("Astrand34", "resi 694+695+696+697+698+699+700+701+702 & chain A ")


cmd.select("Astrand33", "resi 677+678+679+680+681+682+683+684+685+686+687+688+689 & chain A ")


cmd.select("Astrand32", "resi 653+654+655+656+657+658+659+660+661 & chain A ")


cmd.select("Astrand22", "resi 496+497+498+499+639+640+641+642+643+644+645+646+647 & chain A ")


cmd.select("Astrand19", "resi 593+594+595+596+531+532+597+533+598+534+599+535+475+600+476+536+477+601+537+478+602+538+479+418+480+603+419+539+420+481+604+540+421+482+422+605+423+541+483+484+542+424+606+425+486+545+485+543+607+547+546+548+426+544+427+504+549+506+550+428+429+505+507+430+431+432 & chain A ")


cmd.select("Astrand18", "resi 397+398+399+400+401+402+570+571+569+456+568+403+572+567+457+404+458+573+515+459+405+460+574+406+516+575+576+517+461+462+407+577+578+408+518+519+463+579+409+464+580+520+410+521+465+581+582+466+411+522+583+523+412+467+584+468+524+525+413+585+469+414+526+586+470+527+415+587+528+588+589+590 & chain A ")


cmd.select("Astrand17", "resi 369+370+371+372+373+374+375+376+377+378+379+380+381+382+383+384+385+386 & chain A ")


cmd.select("Astrand16", "resi 345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363 & chain A ")


cmd.select("Astrand15", "resi 324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")


cmd.select("Astrand14", "resi 302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317 & chain A ")


cmd.select("Astrand11", "resi 223+224+225+226+227+228+229+230+231+232+233+234+235+236+237 & chain A ")


cmd.select("Astrand10", "resi 207+208+209+210+211+212+213+214+215+216+217+218 & chain A ")


cmd.select("Astrand9", "resi 177+178+179+180+181+182+183+184+185+186+187+188 & chain A ")


cmd.select("Astrand8", "resi 163+164+165+166+167+168+169+170+171+172 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 148 & chain A")

cmd.select ("Outward", "resi 148 & chain A", merge=1)

cmd.color ("red", "resi 149 & chain A")

cmd.select ("Inward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("red", "resi 151 & chain A")

cmd.select ("Inward", "resi 151 & chain A", merge=1)

cmd.color ("blue", "resi 152 & chain A")

cmd.select ("Outward", "resi 152 & chain A", merge=1)

cmd.color ("red", "resi 153 & chain A")

cmd.select ("Inward", "resi 153 & chain A", merge=1)

cmd.color ("blue", "resi 154 & chain A")

cmd.select ("Outward", "resi 154 & chain A", merge=1)

cmd.color ("red", "resi 155 & chain A")

cmd.select ("Inward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 156 & chain A")

cmd.select ("Outward", "resi 156 & chain A", merge=1)

cmd.color ("red", "resi 157 & chain A")

cmd.select ("Inward", "resi 157 & chain A", merge=1)

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

cmd.color ("red", "resi 731 & chain A")

cmd.select ("Inward", "resi 731 & chain A", merge=1)

cmd.color ("blue", "resi 732 & chain A")

cmd.select ("Outward", "resi 732 & chain A", merge=1)

cmd.color ("blue", "resi 733 & chain A")

cmd.select ("Outward", "resi 733 & chain A", merge=1)

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

cmd.color ("red", "resi 702 & chain A")

cmd.select ("Inward", "resi 702 & chain A", merge=1)

cmd.color ("red", "resi 677 & chain A")

cmd.select ("Inward", "resi 677 & chain A", merge=1)

cmd.color ("blue", "resi 678 & chain A")

cmd.select ("Outward", "resi 678 & chain A", merge=1)

cmd.color ("red", "resi 679 & chain A")

cmd.select ("Inward", "resi 679 & chain A", merge=1)

cmd.color ("blue", "resi 680 & chain A")

cmd.select ("Outward", "resi 680 & chain A", merge=1)

cmd.color ("red", "resi 681 & chain A")

cmd.select ("Inward", "resi 681 & chain A", merge=1)

cmd.color ("blue", "resi 682 & chain A")

cmd.select ("Outward", "resi 682 & chain A", merge=1)

cmd.color ("red", "resi 683 & chain A")

cmd.select ("Inward", "resi 683 & chain A", merge=1)

cmd.color ("blue", "resi 684 & chain A")

cmd.select ("Outward", "resi 684 & chain A", merge=1)

cmd.color ("red", "resi 685 & chain A")

cmd.select ("Inward", "resi 685 & chain A", merge=1)

cmd.color ("blue", "resi 686 & chain A")

cmd.select ("Outward", "resi 686 & chain A", merge=1)

cmd.color ("blue", "resi 687 & chain A")

cmd.select ("Outward", "resi 687 & chain A", merge=1)

cmd.color ("red", "resi 688 & chain A")

cmd.select ("Inward", "resi 688 & chain A", merge=1)

cmd.color ("blue", "resi 689 & chain A")

cmd.select ("Outward", "resi 689 & chain A", merge=1)

cmd.color ("red", "resi 653 & chain A")

cmd.select ("Inward", "resi 653 & chain A", merge=1)

cmd.color ("blue", "resi 654 & chain A")

cmd.select ("Outward", "resi 654 & chain A", merge=1)

cmd.color ("red", "resi 655 & chain A")

cmd.select ("Inward", "resi 655 & chain A", merge=1)

cmd.color ("blue", "resi 656 & chain A")

cmd.select ("Outward", "resi 656 & chain A", merge=1)

cmd.color ("red", "resi 657 & chain A")

cmd.select ("Inward", "resi 657 & chain A", merge=1)

cmd.color ("blue", "resi 658 & chain A")

cmd.select ("Outward", "resi 658 & chain A", merge=1)

cmd.color ("red", "resi 659 & chain A")

cmd.select ("Inward", "resi 659 & chain A", merge=1)

cmd.color ("blue", "resi 660 & chain A")

cmd.select ("Outward", "resi 660 & chain A", merge=1)

cmd.color ("red", "resi 661 & chain A")

cmd.select ("Inward", "resi 661 & chain A", merge=1)

cmd.color ("red", "resi 496 & chain A")

cmd.select ("Inward", "resi 496 & chain A", merge=1)

cmd.color ("red", "resi 497 & chain A")

cmd.select ("Inward", "resi 497 & chain A", merge=1)

cmd.color ("red", "resi 498 & chain A")

cmd.select ("Inward", "resi 498 & chain A", merge=1)

cmd.color ("blue", "resi 499 & chain A")

cmd.select ("Outward", "resi 499 & chain A", merge=1)

cmd.color ("red", "resi 639 & chain A")

cmd.select ("Inward", "resi 639 & chain A", merge=1)

cmd.color ("blue", "resi 640 & chain A")

cmd.select ("Outward", "resi 640 & chain A", merge=1)

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

cmd.color ("blue", "resi 647 & chain A")

cmd.select ("Outward", "resi 647 & chain A", merge=1)

cmd.color ("blue", "resi 593 & chain A")

cmd.select ("Outward", "resi 593 & chain A", merge=1)

cmd.color ("red", "resi 594 & chain A")

cmd.select ("Inward", "resi 594 & chain A", merge=1)

cmd.color ("blue", "resi 595 & chain A")

cmd.select ("Outward", "resi 595 & chain A", merge=1)

cmd.color ("red", "resi 596 & chain A")

cmd.select ("Inward", "resi 596 & chain A", merge=1)

cmd.color ("blue", "resi 531 & chain A")

cmd.select ("Outward", "resi 531 & chain A", merge=1)

cmd.color ("red", "resi 532 & chain A")

cmd.select ("Inward", "resi 532 & chain A", merge=1)

cmd.color ("blue", "resi 597 & chain A")

cmd.select ("Outward", "resi 597 & chain A", merge=1)

cmd.color ("blue", "resi 533 & chain A")

cmd.select ("Outward", "resi 533 & chain A", merge=1)

cmd.color ("red", "resi 598 & chain A")

cmd.select ("Inward", "resi 598 & chain A", merge=1)

cmd.color ("red", "resi 534 & chain A")

cmd.select ("Inward", "resi 534 & chain A", merge=1)

cmd.color ("blue", "resi 599 & chain A")

cmd.select ("Outward", "resi 599 & chain A", merge=1)

cmd.color ("blue", "resi 535 & chain A")

cmd.select ("Outward", "resi 535 & chain A", merge=1)

cmd.color ("blue", "resi 475 & chain A")

cmd.select ("Outward", "resi 475 & chain A", merge=1)

cmd.color ("red", "resi 600 & chain A")

cmd.select ("Inward", "resi 600 & chain A", merge=1)

cmd.color ("red", "resi 476 & chain A")

cmd.select ("Inward", "resi 476 & chain A", merge=1)

cmd.color ("red", "resi 536 & chain A")

cmd.select ("Inward", "resi 536 & chain A", merge=1)

cmd.color ("blue", "resi 477 & chain A")

cmd.select ("Outward", "resi 477 & chain A", merge=1)

cmd.color ("blue", "resi 601 & chain A")

cmd.select ("Outward", "resi 601 & chain A", merge=1)

cmd.color ("blue", "resi 537 & chain A")

cmd.select ("Outward", "resi 537 & chain A", merge=1)

cmd.color ("red", "resi 478 & chain A")

cmd.select ("Inward", "resi 478 & chain A", merge=1)

cmd.color ("red", "resi 602 & chain A")

cmd.select ("Inward", "resi 602 & chain A", merge=1)

cmd.color ("red", "resi 538 & chain A")

cmd.select ("Inward", "resi 538 & chain A", merge=1)

cmd.color ("blue", "resi 479 & chain A")

cmd.select ("Outward", "resi 479 & chain A", merge=1)

cmd.color ("blue", "resi 418 & chain A")

cmd.select ("Outward", "resi 418 & chain A", merge=1)

cmd.color ("red", "resi 480 & chain A")

cmd.select ("Inward", "resi 480 & chain A", merge=1)

cmd.color ("blue", "resi 603 & chain A")

cmd.select ("Outward", "resi 603 & chain A", merge=1)

cmd.color ("red", "resi 419 & chain A")

cmd.select ("Inward", "resi 419 & chain A", merge=1)

cmd.color ("blue", "resi 539 & chain A")

cmd.select ("Outward", "resi 539 & chain A", merge=1)

cmd.color ("blue", "resi 420 & chain A")

cmd.select ("Outward", "resi 420 & chain A", merge=1)

cmd.color ("blue", "resi 481 & chain A")

cmd.select ("Outward", "resi 481 & chain A", merge=1)

cmd.color ("red", "resi 604 & chain A")

cmd.select ("Inward", "resi 604 & chain A", merge=1)

cmd.color ("red", "resi 540 & chain A")

cmd.select ("Inward", "resi 540 & chain A", merge=1)

cmd.color ("red", "resi 421 & chain A")

cmd.select ("Inward", "resi 421 & chain A", merge=1)

cmd.color ("red", "resi 482 & chain A")

cmd.select ("Inward", "resi 482 & chain A", merge=1)

cmd.color ("blue", "resi 422 & chain A")

cmd.select ("Outward", "resi 422 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("red", "resi 423 & chain A")

cmd.select ("Inward", "resi 423 & chain A", merge=1)

cmd.color ("blue", "resi 541 & chain A")

cmd.select ("Outward", "resi 541 & chain A", merge=1)

cmd.color ("blue", "resi 483 & chain A")

cmd.select ("Outward", "resi 483 & chain A", merge=1)

cmd.color ("red", "resi 484 & chain A")

cmd.select ("Inward", "resi 484 & chain A", merge=1)

cmd.color ("red", "resi 542 & chain A")

cmd.select ("Inward", "resi 542 & chain A", merge=1)

cmd.color ("blue", "resi 424 & chain A")

cmd.select ("Outward", "resi 424 & chain A", merge=1)

cmd.color ("red", "resi 606 & chain A")

cmd.select ("Inward", "resi 606 & chain A", merge=1)

cmd.color ("red", "resi 425 & chain A")

cmd.select ("Inward", "resi 425 & chain A", merge=1)

cmd.color ("red", "resi 486 & chain A")

cmd.select ("Inward", "resi 486 & chain A", merge=1)

cmd.color ("red", "resi 545 & chain A")

cmd.select ("Inward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 485 & chain A")

cmd.select ("Outward", "resi 485 & chain A", merge=1)

cmd.color ("red", "resi 543 & chain A")

cmd.select ("Inward", "resi 543 & chain A", merge=1)

cmd.color ("blue", "resi 607 & chain A")

cmd.select ("Outward", "resi 607 & chain A", merge=1)

cmd.color ("red", "resi 547 & chain A")

cmd.select ("Inward", "resi 547 & chain A", merge=1)

cmd.color ("blue", "resi 546 & chain A")

cmd.select ("Outward", "resi 546 & chain A", merge=1)

cmd.color ("red", "resi 548 & chain A")

cmd.select ("Inward", "resi 548 & chain A", merge=1)

cmd.color ("blue", "resi 426 & chain A")

cmd.select ("Outward", "resi 426 & chain A", merge=1)

cmd.color ("blue", "resi 544 & chain A")

cmd.select ("Outward", "resi 544 & chain A", merge=1)

cmd.color ("red", "resi 427 & chain A")

cmd.select ("Inward", "resi 427 & chain A", merge=1)

cmd.color ("red", "resi 504 & chain A")

cmd.select ("Inward", "resi 504 & chain A", merge=1)

cmd.color ("blue", "resi 549 & chain A")

cmd.select ("Outward", "resi 549 & chain A", merge=1)

cmd.color ("red", "resi 506 & chain A")

cmd.select ("Inward", "resi 506 & chain A", merge=1)

cmd.color ("red", "resi 550 & chain A")

cmd.select ("Inward", "resi 550 & chain A", merge=1)

cmd.color ("blue", "resi 428 & chain A")

cmd.select ("Outward", "resi 428 & chain A", merge=1)

cmd.color ("red", "resi 429 & chain A")

cmd.select ("Inward", "resi 429 & chain A", merge=1)

cmd.color ("blue", "resi 505 & chain A")

cmd.select ("Outward", "resi 505 & chain A", merge=1)

cmd.color ("blue", "resi 507 & chain A")

cmd.select ("Outward", "resi 507 & chain A", merge=1)

cmd.color ("blue", "resi 430 & chain A")

cmd.select ("Outward", "resi 430 & chain A", merge=1)

cmd.color ("red", "resi 431 & chain A")

cmd.select ("Inward", "resi 431 & chain A", merge=1)

cmd.color ("red", "resi 432 & chain A")

cmd.select ("Inward", "resi 432 & chain A", merge=1)

cmd.color ("blue", "resi 397 & chain A")

cmd.select ("Outward", "resi 397 & chain A", merge=1)

cmd.color ("red", "resi 398 & chain A")

cmd.select ("Inward", "resi 398 & chain A", merge=1)

cmd.color ("blue", "resi 399 & chain A")

cmd.select ("Outward", "resi 399 & chain A", merge=1)

cmd.color ("red", "resi 400 & chain A")

cmd.select ("Inward", "resi 400 & chain A", merge=1)

cmd.color ("blue", "resi 401 & chain A")

cmd.select ("Outward", "resi 401 & chain A", merge=1)

cmd.color ("red", "resi 402 & chain A")

cmd.select ("Inward", "resi 402 & chain A", merge=1)

cmd.color ("red", "resi 570 & chain A")

cmd.select ("Inward", "resi 570 & chain A", merge=1)

cmd.color ("blue", "resi 571 & chain A")

cmd.select ("Outward", "resi 571 & chain A", merge=1)

cmd.color ("blue", "resi 569 & chain A")

cmd.select ("Outward", "resi 569 & chain A", merge=1)

cmd.color ("red", "resi 456 & chain A")

cmd.select ("Inward", "resi 456 & chain A", merge=1)

cmd.color ("red", "resi 568 & chain A")

cmd.select ("Inward", "resi 568 & chain A", merge=1)

cmd.color ("blue", "resi 403 & chain A")

cmd.select ("Outward", "resi 403 & chain A", merge=1)

cmd.color ("red", "resi 572 & chain A")

cmd.select ("Inward", "resi 572 & chain A", merge=1)

cmd.color ("red", "resi 567 & chain A")

cmd.select ("Inward", "resi 567 & chain A", merge=1)

cmd.color ("blue", "resi 457 & chain A")

cmd.select ("Outward", "resi 457 & chain A", merge=1)

cmd.color ("red", "resi 404 & chain A")

cmd.select ("Inward", "resi 404 & chain A", merge=1)

cmd.color ("red", "resi 458 & chain A")

cmd.select ("Inward", "resi 458 & chain A", merge=1)

cmd.color ("blue", "resi 573 & chain A")

cmd.select ("Outward", "resi 573 & chain A", merge=1)

cmd.color ("red", "resi 515 & chain A")

cmd.select ("Inward", "resi 515 & chain A", merge=1)

cmd.color ("blue", "resi 459 & chain A")

cmd.select ("Outward", "resi 459 & chain A", merge=1)

cmd.color ("blue", "resi 405 & chain A")

cmd.select ("Outward", "resi 405 & chain A", merge=1)

cmd.color ("red", "resi 460 & chain A")

cmd.select ("Inward", "resi 460 & chain A", merge=1)

cmd.color ("red", "resi 574 & chain A")

cmd.select ("Inward", "resi 574 & chain A", merge=1)

cmd.color ("red", "resi 406 & chain A")

cmd.select ("Inward", "resi 406 & chain A", merge=1)

cmd.color ("blue", "resi 516 & chain A")

cmd.select ("Outward", "resi 516 & chain A", merge=1)

cmd.color ("blue", "resi 575 & chain A")

cmd.select ("Outward", "resi 575 & chain A", merge=1)

cmd.color ("red", "resi 576 & chain A")

cmd.select ("Inward", "resi 576 & chain A", merge=1)

cmd.color ("red", "resi 517 & chain A")

cmd.select ("Inward", "resi 517 & chain A", merge=1)

cmd.color ("blue", "resi 461 & chain A")

cmd.select ("Outward", "resi 461 & chain A", merge=1)

cmd.color ("red", "resi 462 & chain A")

cmd.select ("Inward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 407 & chain A")

cmd.select ("Outward", "resi 407 & chain A", merge=1)

cmd.color ("blue", "resi 577 & chain A")

cmd.select ("Outward", "resi 577 & chain A", merge=1)

cmd.color ("red", "resi 578 & chain A")

cmd.select ("Inward", "resi 578 & chain A", merge=1)

cmd.color ("red", "resi 408 & chain A")

cmd.select ("Inward", "resi 408 & chain A", merge=1)

cmd.color ("blue", "resi 518 & chain A")

cmd.select ("Outward", "resi 518 & chain A", merge=1)

cmd.color ("red", "resi 519 & chain A")

cmd.select ("Inward", "resi 519 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("blue", "resi 579 & chain A")

cmd.select ("Outward", "resi 579 & chain A", merge=1)

cmd.color ("blue", "resi 409 & chain A")

cmd.select ("Outward", "resi 409 & chain A", merge=1)

cmd.color ("red", "resi 464 & chain A")

cmd.select ("Inward", "resi 464 & chain A", merge=1)

cmd.color ("red", "resi 580 & chain A")

cmd.select ("Inward", "resi 580 & chain A", merge=1)

cmd.color ("blue", "resi 520 & chain A")

cmd.select ("Outward", "resi 520 & chain A", merge=1)

cmd.color ("red", "resi 410 & chain A")

cmd.select ("Inward", "resi 410 & chain A", merge=1)

cmd.color ("red", "resi 521 & chain A")

cmd.select ("Inward", "resi 521 & chain A", merge=1)

cmd.color ("blue", "resi 465 & chain A")

cmd.select ("Outward", "resi 465 & chain A", merge=1)

cmd.color ("blue", "resi 581 & chain A")

cmd.select ("Outward", "resi 581 & chain A", merge=1)

cmd.color ("red", "resi 582 & chain A")

cmd.select ("Inward", "resi 582 & chain A", merge=1)

cmd.color ("red", "resi 466 & chain A")

cmd.select ("Inward", "resi 466 & chain A", merge=1)

cmd.color ("blue", "resi 411 & chain A")

cmd.select ("Outward", "resi 411 & chain A", merge=1)

cmd.color ("blue", "resi 522 & chain A")

cmd.select ("Outward", "resi 522 & chain A", merge=1)

cmd.color ("blue", "resi 583 & chain A")

cmd.select ("Outward", "resi 583 & chain A", merge=1)

cmd.color ("red", "resi 523 & chain A")

cmd.select ("Inward", "resi 523 & chain A", merge=1)

cmd.color ("red", "resi 412 & chain A")

cmd.select ("Inward", "resi 412 & chain A", merge=1)

cmd.color ("blue", "resi 467 & chain A")

cmd.select ("Outward", "resi 467 & chain A", merge=1)

cmd.color ("red", "resi 584 & chain A")

cmd.select ("Inward", "resi 584 & chain A", merge=1)

cmd.color ("red", "resi 468 & chain A")

cmd.select ("Inward", "resi 468 & chain A", merge=1)

cmd.color ("blue", "resi 524 & chain A")

cmd.select ("Outward", "resi 524 & chain A", merge=1)

cmd.color ("red", "resi 525 & chain A")

cmd.select ("Inward", "resi 525 & chain A", merge=1)

cmd.color ("blue", "resi 413 & chain A")

cmd.select ("Outward", "resi 413 & chain A", merge=1)

cmd.color ("blue", "resi 585 & chain A")

cmd.select ("Outward", "resi 585 & chain A", merge=1)

cmd.color ("blue", "resi 469 & chain A")

cmd.select ("Outward", "resi 469 & chain A", merge=1)

cmd.color ("red", "resi 414 & chain A")

cmd.select ("Inward", "resi 414 & chain A", merge=1)

cmd.color ("blue", "resi 526 & chain A")

cmd.select ("Outward", "resi 526 & chain A", merge=1)

cmd.color ("red", "resi 586 & chain A")

cmd.select ("Inward", "resi 586 & chain A", merge=1)

cmd.color ("red", "resi 470 & chain A")

cmd.select ("Inward", "resi 470 & chain A", merge=1)

cmd.color ("red", "resi 527 & chain A")

cmd.select ("Inward", "resi 527 & chain A", merge=1)

cmd.color ("blue", "resi 415 & chain A")

cmd.select ("Outward", "resi 415 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

cmd.color ("blue", "resi 528 & chain A")

cmd.select ("Outward", "resi 528 & chain A", merge=1)

cmd.color ("red", "resi 588 & chain A")

cmd.select ("Inward", "resi 588 & chain A", merge=1)

cmd.color ("red", "resi 589 & chain A")

cmd.select ("Inward", "resi 589 & chain A", merge=1)

cmd.color ("blue", "resi 590 & chain A")

cmd.select ("Outward", "resi 590 & chain A", merge=1)

cmd.color ("blue", "resi 369 & chain A")

cmd.select ("Outward", "resi 369 & chain A", merge=1)

cmd.color ("red", "resi 370 & chain A")

cmd.select ("Inward", "resi 370 & chain A", merge=1)

cmd.color ("blue", "resi 371 & chain A")

cmd.select ("Outward", "resi 371 & chain A", merge=1)

cmd.color ("red", "resi 372 & chain A")

cmd.select ("Inward", "resi 372 & chain A", merge=1)

cmd.color ("blue", "resi 373 & chain A")

cmd.select ("Outward", "resi 373 & chain A", merge=1)

cmd.color ("red", "resi 374 & chain A")

cmd.select ("Inward", "resi 374 & chain A", merge=1)

cmd.color ("blue", "resi 375 & chain A")

cmd.select ("Outward", "resi 375 & chain A", merge=1)

cmd.color ("red", "resi 376 & chain A")

cmd.select ("Inward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 377 & chain A")

cmd.select ("Outward", "resi 377 & chain A", merge=1)

cmd.color ("red", "resi 378 & chain A")

cmd.select ("Inward", "resi 378 & chain A", merge=1)

cmd.color ("blue", "resi 379 & chain A")

cmd.select ("Outward", "resi 379 & chain A", merge=1)

cmd.color ("red", "resi 380 & chain A")

cmd.select ("Inward", "resi 380 & chain A", merge=1)

cmd.color ("blue", "resi 381 & chain A")

cmd.select ("Outward", "resi 381 & chain A", merge=1)

cmd.color ("red", "resi 382 & chain A")

cmd.select ("Inward", "resi 382 & chain A", merge=1)

cmd.color ("blue", "resi 383 & chain A")

cmd.select ("Outward", "resi 383 & chain A", merge=1)

cmd.color ("red", "resi 384 & chain A")

cmd.select ("Inward", "resi 384 & chain A", merge=1)

cmd.color ("blue", "resi 385 & chain A")

cmd.select ("Outward", "resi 385 & chain A", merge=1)

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("red", "resi 345 & chain A")

cmd.select ("Inward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("red", "resi 347 & chain A")

cmd.select ("Inward", "resi 347 & chain A", merge=1)

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

cmd.color ("blue", "resi 361 & chain A")

cmd.select ("Outward", "resi 361 & chain A", merge=1)

cmd.color ("red", "resi 362 & chain A")

cmd.select ("Inward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 363 & chain A")

cmd.select ("Outward", "resi 363 & chain A", merge=1)

cmd.color ("blue", "resi 324 & chain A")

cmd.select ("Outward", "resi 324 & chain A", merge=1)

cmd.color ("red", "resi 325 & chain A")

cmd.select ("Inward", "resi 325 & chain A", merge=1)

cmd.color ("red", "resi 326 & chain A")

cmd.select ("Inward", "resi 326 & chain A", merge=1)

cmd.color ("blue", "resi 327 & chain A")

cmd.select ("Outward", "resi 327 & chain A", merge=1)

cmd.color ("red", "resi 328 & chain A")

cmd.select ("Inward", "resi 328 & chain A", merge=1)

cmd.color ("blue", "resi 329 & chain A")

cmd.select ("Outward", "resi 329 & chain A", merge=1)

cmd.color ("red", "resi 330 & chain A")

cmd.select ("Inward", "resi 330 & chain A", merge=1)

cmd.color ("blue", "resi 331 & chain A")

cmd.select ("Outward", "resi 331 & chain A", merge=1)

cmd.color ("red", "resi 332 & chain A")

cmd.select ("Inward", "resi 332 & chain A", merge=1)

cmd.color ("blue", "resi 333 & chain A")

cmd.select ("Outward", "resi 333 & chain A", merge=1)

cmd.color ("red", "resi 334 & chain A")

cmd.select ("Inward", "resi 334 & chain A", merge=1)

cmd.color ("blue", "resi 335 & chain A")

cmd.select ("Outward", "resi 335 & chain A", merge=1)

cmd.color ("red", "resi 336 & chain A")

cmd.select ("Inward", "resi 336 & chain A", merge=1)

cmd.color ("blue", "resi 337 & chain A")

cmd.select ("Outward", "resi 337 & chain A", merge=1)

cmd.color ("red", "resi 338 & chain A")

cmd.select ("Inward", "resi 338 & chain A", merge=1)

cmd.color ("blue", "resi 339 & chain A")

cmd.select ("Outward", "resi 339 & chain A", merge=1)

cmd.color ("red", "resi 340 & chain A")

cmd.select ("Inward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("red", "resi 302 & chain A")

cmd.select ("Inward", "resi 302 & chain A", merge=1)

cmd.color ("blue", "resi 303 & chain A")

cmd.select ("Outward", "resi 303 & chain A", merge=1)

cmd.color ("red", "resi 304 & chain A")

cmd.select ("Inward", "resi 304 & chain A", merge=1)

cmd.color ("blue", "resi 305 & chain A")

cmd.select ("Outward", "resi 305 & chain A", merge=1)

cmd.color ("red", "resi 306 & chain A")

cmd.select ("Inward", "resi 306 & chain A", merge=1)

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

cmd.color ("blue", "resi 223 & chain A")

cmd.select ("Outward", "resi 223 & chain A", merge=1)

cmd.color ("red", "resi 224 & chain A")

cmd.select ("Inward", "resi 224 & chain A", merge=1)

cmd.color ("blue", "resi 225 & chain A")

cmd.select ("Outward", "resi 225 & chain A", merge=1)

cmd.color ("red", "resi 226 & chain A")

cmd.select ("Inward", "resi 226 & chain A", merge=1)

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

cmd.color ("red", "resi 207 & chain A")

cmd.select ("Inward", "resi 207 & chain A", merge=1)

cmd.color ("blue", "resi 208 & chain A")

cmd.select ("Outward", "resi 208 & chain A", merge=1)

cmd.color ("red", "resi 209 & chain A")

cmd.select ("Inward", "resi 209 & chain A", merge=1)

cmd.color ("blue", "resi 210 & chain A")

cmd.select ("Outward", "resi 210 & chain A", merge=1)

cmd.color ("red", "resi 211 & chain A")

cmd.select ("Inward", "resi 211 & chain A", merge=1)

cmd.color ("blue", "resi 212 & chain A")

cmd.select ("Outward", "resi 212 & chain A", merge=1)

cmd.color ("red", "resi 213 & chain A")

cmd.select ("Inward", "resi 213 & chain A", merge=1)

cmd.color ("blue", "resi 214 & chain A")

cmd.select ("Outward", "resi 214 & chain A", merge=1)

cmd.color ("red", "resi 215 & chain A")

cmd.select ("Inward", "resi 215 & chain A", merge=1)

cmd.color ("blue", "resi 216 & chain A")

cmd.select ("Outward", "resi 216 & chain A", merge=1)

cmd.color ("red", "resi 217 & chain A")

cmd.select ("Inward", "resi 217 & chain A", merge=1)

cmd.color ("blue", "resi 218 & chain A")

cmd.select ("Outward", "resi 218 & chain A", merge=1)

cmd.color ("blue", "resi 177 & chain A")

cmd.select ("Outward", "resi 177 & chain A", merge=1)

cmd.color ("red", "resi 178 & chain A")

cmd.select ("Inward", "resi 178 & chain A", merge=1)

cmd.color ("blue", "resi 179 & chain A")

cmd.select ("Outward", "resi 179 & chain A", merge=1)

cmd.color ("red", "resi 180 & chain A")

cmd.select ("Inward", "resi 180 & chain A", merge=1)

cmd.color ("blue", "resi 181 & chain A")

cmd.select ("Outward", "resi 181 & chain A", merge=1)

cmd.color ("red", "resi 182 & chain A")

cmd.select ("Inward", "resi 182 & chain A", merge=1)

cmd.color ("blue", "resi 183 & chain A")

cmd.select ("Outward", "resi 183 & chain A", merge=1)

cmd.color ("red", "resi 184 & chain A")

cmd.select ("Inward", "resi 184 & chain A", merge=1)

cmd.color ("blue", "resi 185 & chain A")

cmd.select ("Outward", "resi 185 & chain A", merge=1)

cmd.color ("red", "resi 186 & chain A")

cmd.select ("Inward", "resi 186 & chain A", merge=1)

cmd.color ("blue", "resi 187 & chain A")

cmd.select ("Outward", "resi 187 & chain A", merge=1)

cmd.color ("red", "resi 188 & chain A")

cmd.select ("Inward", "resi 188 & chain A", merge=1)

cmd.color ("blue", "resi 163 & chain A")

cmd.select ("Outward", "resi 163 & chain A", merge=1)

cmd.color ("red", "resi 164 & chain A")

cmd.select ("Inward", "resi 164 & chain A", merge=1)

cmd.color ("blue", "resi 165 & chain A")

cmd.select ("Outward", "resi 165 & chain A", merge=1)

cmd.color ("red", "resi 166 & chain A")

cmd.select ("Inward", "resi 166 & chain A", merge=1)

cmd.color ("blue", "resi 167 & chain A")

cmd.select ("Outward", "resi 167 & chain A", merge=1)

cmd.color ("red", "resi 168 & chain A")

cmd.select ("Inward", "resi 168 & chain A", merge=1)

cmd.color ("blue", "resi 169 & chain A")

cmd.select ("Outward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 170 & chain A")

cmd.select ("Outward", "resi 170 & chain A", merge=1)

cmd.color ("red", "resi 171 & chain A")

cmd.select ("Inward", "resi 171 & chain A", merge=1)

cmd.color ("blue", "resi 172 & chain A")

cmd.select ("Outward", "resi 172 & chain A", merge=1)

cmd.load_cgo( [9.0, -45.693874,29.757,17.055, -45.693874, 29.757, 17.055, 1, 1,1,0,0,0,1], "axis" )
