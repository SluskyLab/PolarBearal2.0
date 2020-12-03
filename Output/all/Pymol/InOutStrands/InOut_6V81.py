from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6V81.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand7", "resi 164+165+166+167+168+169+170+171+172 & chain A ")


cmd.select("Astrand36", "resi 688+689+690+691+692+693+694+695+696+697+698 & chain A ")


cmd.select("Astrand33", "resi 651+652+653+654+655+656+657+658+659+660 & chain A ")


cmd.select("Astrand32", "resi 635+636+637+638+639+640+641+642+643+644+645+646+647+648 & chain A ")


cmd.select("Astrand29", "resi 611+612+613+614+615+616+617+618+619 & chain A ")


cmd.select("Astrand28", "resi 596+597+598+599+600+601+602+603+604 & chain A ")


cmd.select("Astrand27", "resi 562+563+564+565+566+567+568+569+570+571+572+573+574+575 & chain A ")


cmd.select("Astrand26", "resi 545+546+547+548+549+550+551+552+553+554+555+556+557+558 & chain A ")


cmd.select("Astrand22", "resi 500+501+502+503+504+505+506+507+508+509 & chain A ")


cmd.select("Astrand23", "resi 512+513+514+515+516+517+518+519+520+521+522+523 & chain A ")


cmd.select("Astrand19", "resi 461+462+463+464+465+466+467+468 & chain A ")


cmd.select("Astrand18", "resi 440+441+442+443+444+445+446+447+448+449+450+451+452+453+454+455+456 & chain A ")


cmd.select("Astrand17", "resi 411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+426+427+428 & chain A ")


cmd.select("Astrand16", "resi 386+387+388+389+390+391+392+393+394+395+396+397+398+399+400+401+402+403+404+405+406+407+408 & chain A ")


cmd.select("Astrand15", "resi 350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366+367+368 & chain A ")


cmd.select("Astrand14", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")


cmd.select("Astrand13", "resi 293+294+295+296+297+298+299+300+301+302+303+304+305+306+307+308+309 & chain A ")


cmd.select("Astrand12", "resi 273+274+275+276+277+278+279+280+281+282+283+284+285+286+287+288 & chain A ")


cmd.select("Astrand11", "resi 234+235+236+237+238+239+240+241+242+243+244+245+246+247 & chain A ")


cmd.select("Astrand10", "resi 216+217+218+219+220+221+222+223+224+225+226+227+228 & chain A ")


cmd.select("Astrand9", "resi 196+197+198+199+200+201+202+203+204+205+206+207 & chain A ")


cmd.select("Astrand8", "resi 176+177+178+179+180+181+182+183+184+185+186 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("red", "resi 170 & chain A")

cmd.select ("Inward", "resi 170 & chain A", merge=1)

cmd.color ("blue", "resi 171 & chain A")

cmd.select ("Outward", "resi 171 & chain A", merge=1)

cmd.color ("red", "resi 172 & chain A")

cmd.select ("Inward", "resi 172 & chain A", merge=1)

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

cmd.color ("blue", "resi 698 & chain A")

cmd.select ("Outward", "resi 698 & chain A", merge=1)

cmd.color ("blue", "resi 651 & chain A")

cmd.select ("Outward", "resi 651 & chain A", merge=1)

cmd.color ("red", "resi 652 & chain A")

cmd.select ("Inward", "resi 652 & chain A", merge=1)

cmd.color ("blue", "resi 653 & chain A")

cmd.select ("Outward", "resi 653 & chain A", merge=1)

cmd.color ("red", "resi 654 & chain A")

cmd.select ("Inward", "resi 654 & chain A", merge=1)

cmd.color ("blue", "resi 655 & chain A")

cmd.select ("Outward", "resi 655 & chain A", merge=1)

cmd.color ("red", "resi 656 & chain A")

cmd.select ("Inward", "resi 656 & chain A", merge=1)

cmd.color ("blue", "resi 657 & chain A")

cmd.select ("Outward", "resi 657 & chain A", merge=1)

cmd.color ("red", "resi 658 & chain A")

cmd.select ("Inward", "resi 658 & chain A", merge=1)

cmd.color ("blue", "resi 659 & chain A")

cmd.select ("Outward", "resi 659 & chain A", merge=1)

cmd.color ("red", "resi 660 & chain A")

cmd.select ("Inward", "resi 660 & chain A", merge=1)

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

cmd.color ("red", "resi 647 & chain A")

cmd.select ("Inward", "resi 647 & chain A", merge=1)

cmd.color ("blue", "resi 648 & chain A")

cmd.select ("Outward", "resi 648 & chain A", merge=1)

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

cmd.color ("blue", "resi 562 & chain A")

cmd.select ("Outward", "resi 562 & chain A", merge=1)

cmd.color ("red", "resi 563 & chain A")

cmd.select ("Inward", "resi 563 & chain A", merge=1)

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

cmd.color ("blue", "resi 575 & chain A")

cmd.select ("Outward", "resi 575 & chain A", merge=1)

cmd.color ("red", "resi 545 & chain A")

cmd.select ("Inward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 546 & chain A")

cmd.select ("Outward", "resi 546 & chain A", merge=1)

cmd.color ("red", "resi 547 & chain A")

cmd.select ("Inward", "resi 547 & chain A", merge=1)

cmd.color ("blue", "resi 548 & chain A")

cmd.select ("Outward", "resi 548 & chain A", merge=1)

cmd.color ("red", "resi 549 & chain A")

cmd.select ("Inward", "resi 549 & chain A", merge=1)

cmd.color ("blue", "resi 550 & chain A")

cmd.select ("Outward", "resi 550 & chain A", merge=1)

cmd.color ("red", "resi 551 & chain A")

cmd.select ("Inward", "resi 551 & chain A", merge=1)

cmd.color ("blue", "resi 552 & chain A")

cmd.select ("Outward", "resi 552 & chain A", merge=1)

cmd.color ("red", "resi 553 & chain A")

cmd.select ("Inward", "resi 553 & chain A", merge=1)

cmd.color ("blue", "resi 554 & chain A")

cmd.select ("Outward", "resi 554 & chain A", merge=1)

cmd.color ("red", "resi 555 & chain A")

cmd.select ("Inward", "resi 555 & chain A", merge=1)

cmd.color ("blue", "resi 556 & chain A")

cmd.select ("Outward", "resi 556 & chain A", merge=1)

cmd.color ("red", "resi 557 & chain A")

cmd.select ("Inward", "resi 557 & chain A", merge=1)

cmd.color ("blue", "resi 558 & chain A")

cmd.select ("Outward", "resi 558 & chain A", merge=1)

cmd.color ("red", "resi 500 & chain A")

cmd.select ("Inward", "resi 500 & chain A", merge=1)

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

cmd.color ("blue", "resi 508 & chain A")

cmd.select ("Outward", "resi 508 & chain A", merge=1)

cmd.color ("red", "resi 509 & chain A")

cmd.select ("Inward", "resi 509 & chain A", merge=1)

cmd.color ("blue", "resi 512 & chain A")

cmd.select ("Outward", "resi 512 & chain A", merge=1)

cmd.color ("red", "resi 513 & chain A")

cmd.select ("Inward", "resi 513 & chain A", merge=1)

cmd.color ("blue", "resi 514 & chain A")

cmd.select ("Outward", "resi 514 & chain A", merge=1)

cmd.color ("red", "resi 515 & chain A")

cmd.select ("Inward", "resi 515 & chain A", merge=1)

cmd.color ("blue", "resi 516 & chain A")

cmd.select ("Outward", "resi 516 & chain A", merge=1)

cmd.color ("red", "resi 517 & chain A")

cmd.select ("Inward", "resi 517 & chain A", merge=1)

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

cmd.color ("blue", "resi 461 & chain A")

cmd.select ("Outward", "resi 461 & chain A", merge=1)

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

cmd.color ("red", "resi 440 & chain A")

cmd.select ("Inward", "resi 440 & chain A", merge=1)

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

cmd.color ("blue", "resi 456 & chain A")

cmd.select ("Outward", "resi 456 & chain A", merge=1)

cmd.color ("blue", "resi 411 & chain A")

cmd.select ("Outward", "resi 411 & chain A", merge=1)

cmd.color ("red", "resi 412 & chain A")

cmd.select ("Inward", "resi 412 & chain A", merge=1)

cmd.color ("blue", "resi 413 & chain A")

cmd.select ("Outward", "resi 413 & chain A", merge=1)

cmd.color ("red", "resi 414 & chain A")

cmd.select ("Inward", "resi 414 & chain A", merge=1)

cmd.color ("blue", "resi 415 & chain A")

cmd.select ("Outward", "resi 415 & chain A", merge=1)

cmd.color ("red", "resi 416 & chain A")

cmd.select ("Inward", "resi 416 & chain A", merge=1)

cmd.color ("blue", "resi 417 & chain A")

cmd.select ("Outward", "resi 417 & chain A", merge=1)

cmd.color ("red", "resi 418 & chain A")

cmd.select ("Inward", "resi 418 & chain A", merge=1)

cmd.color ("blue", "resi 419 & chain A")

cmd.select ("Outward", "resi 419 & chain A", merge=1)

cmd.color ("red", "resi 420 & chain A")

cmd.select ("Inward", "resi 420 & chain A", merge=1)

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

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("red", "resi 387 & chain A")

cmd.select ("Inward", "resi 387 & chain A", merge=1)

cmd.color ("red", "resi 388 & chain A")

cmd.select ("Inward", "resi 388 & chain A", merge=1)

cmd.color ("blue", "resi 389 & chain A")

cmd.select ("Outward", "resi 389 & chain A", merge=1)

cmd.color ("red", "resi 390 & chain A")

cmd.select ("Inward", "resi 390 & chain A", merge=1)

cmd.color ("blue", "resi 391 & chain A")

cmd.select ("Outward", "resi 391 & chain A", merge=1)

cmd.color ("red", "resi 392 & chain A")

cmd.select ("Inward", "resi 392 & chain A", merge=1)

cmd.color ("blue", "resi 393 & chain A")

cmd.select ("Outward", "resi 393 & chain A", merge=1)

cmd.color ("red", "resi 394 & chain A")

cmd.select ("Inward", "resi 394 & chain A", merge=1)

cmd.color ("blue", "resi 395 & chain A")

cmd.select ("Outward", "resi 395 & chain A", merge=1)

cmd.color ("red", "resi 396 & chain A")

cmd.select ("Inward", "resi 396 & chain A", merge=1)

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

cmd.color ("blue", "resi 403 & chain A")

cmd.select ("Outward", "resi 403 & chain A", merge=1)

cmd.color ("red", "resi 404 & chain A")

cmd.select ("Inward", "resi 404 & chain A", merge=1)

cmd.color ("blue", "resi 405 & chain A")

cmd.select ("Outward", "resi 405 & chain A", merge=1)

cmd.color ("blue", "resi 406 & chain A")

cmd.select ("Outward", "resi 406 & chain A", merge=1)

cmd.color ("red", "resi 407 & chain A")

cmd.select ("Inward", "resi 407 & chain A", merge=1)

cmd.color ("blue", "resi 408 & chain A")

cmd.select ("Outward", "resi 408 & chain A", merge=1)

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

cmd.color ("red", "resi 359 & chain A")

cmd.select ("Inward", "resi 359 & chain A", merge=1)

cmd.color ("blue", "resi 360 & chain A")

cmd.select ("Outward", "resi 360 & chain A", merge=1)

cmd.color ("red", "resi 361 & chain A")

cmd.select ("Inward", "resi 361 & chain A", merge=1)

cmd.color ("blue", "resi 362 & chain A")

cmd.select ("Outward", "resi 362 & chain A", merge=1)

cmd.color ("red", "resi 363 & chain A")

cmd.select ("Inward", "resi 363 & chain A", merge=1)

cmd.color ("blue", "resi 364 & chain A")

cmd.select ("Outward", "resi 364 & chain A", merge=1)

cmd.color ("red", "resi 365 & chain A")

cmd.select ("Inward", "resi 365 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("red", "resi 367 & chain A")

cmd.select ("Inward", "resi 367 & chain A", merge=1)

cmd.color ("blue", "resi 368 & chain A")

cmd.select ("Outward", "resi 368 & chain A", merge=1)

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

cmd.color ("red", "resi 339 & chain A")

cmd.select ("Inward", "resi 339 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("red", "resi 341 & chain A")

cmd.select ("Inward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

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

cmd.color ("red", "resi 300 & chain A")

cmd.select ("Inward", "resi 300 & chain A", merge=1)

cmd.color ("blue", "resi 301 & chain A")

cmd.select ("Outward", "resi 301 & chain A", merge=1)

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

cmd.color ("blue", "resi 273 & chain A")

cmd.select ("Outward", "resi 273 & chain A", merge=1)

cmd.color ("red", "resi 274 & chain A")

cmd.select ("Inward", "resi 274 & chain A", merge=1)

cmd.color ("blue", "resi 275 & chain A")

cmd.select ("Outward", "resi 275 & chain A", merge=1)

cmd.color ("red", "resi 276 & chain A")

cmd.select ("Inward", "resi 276 & chain A", merge=1)

cmd.color ("blue", "resi 277 & chain A")

cmd.select ("Outward", "resi 277 & chain A", merge=1)

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

cmd.color ("blue", "resi 287 & chain A")

cmd.select ("Outward", "resi 287 & chain A", merge=1)

cmd.color ("blue", "resi 288 & chain A")

cmd.select ("Outward", "resi 288 & chain A", merge=1)

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

cmd.color ("blue", "resi 239 & chain A")

cmd.select ("Outward", "resi 239 & chain A", merge=1)

cmd.color ("red", "resi 240 & chain A")

cmd.select ("Inward", "resi 240 & chain A", merge=1)

cmd.color ("blue", "resi 241 & chain A")

cmd.select ("Outward", "resi 241 & chain A", merge=1)

cmd.color ("red", "resi 242 & chain A")

cmd.select ("Inward", "resi 242 & chain A", merge=1)

cmd.color ("blue", "resi 243 & chain A")

cmd.select ("Outward", "resi 243 & chain A", merge=1)

cmd.color ("red", "resi 244 & chain A")

cmd.select ("Inward", "resi 244 & chain A", merge=1)

cmd.color ("blue", "resi 245 & chain A")

cmd.select ("Outward", "resi 245 & chain A", merge=1)

cmd.color ("red", "resi 246 & chain A")

cmd.select ("Inward", "resi 246 & chain A", merge=1)

cmd.color ("blue", "resi 247 & chain A")

cmd.select ("Outward", "resi 247 & chain A", merge=1)

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

cmd.color ("red", "resi 224 & chain A")

cmd.select ("Inward", "resi 224 & chain A", merge=1)

cmd.color ("blue", "resi 225 & chain A")

cmd.select ("Outward", "resi 225 & chain A", merge=1)

cmd.color ("red", "resi 226 & chain A")

cmd.select ("Inward", "resi 226 & chain A", merge=1)

cmd.color ("blue", "resi 227 & chain A")

cmd.select ("Outward", "resi 227 & chain A", merge=1)

cmd.color ("blue", "resi 228 & chain A")

cmd.select ("Outward", "resi 228 & chain A", merge=1)

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

cmd.color ("red", "resi 203 & chain A")

cmd.select ("Inward", "resi 203 & chain A", merge=1)

cmd.color ("blue", "resi 204 & chain A")

cmd.select ("Outward", "resi 204 & chain A", merge=1)

cmd.color ("red", "resi 205 & chain A")

cmd.select ("Inward", "resi 205 & chain A", merge=1)

cmd.color ("blue", "resi 206 & chain A")

cmd.select ("Outward", "resi 206 & chain A", merge=1)

cmd.color ("red", "resi 207 & chain A")

cmd.select ("Inward", "resi 207 & chain A", merge=1)

cmd.color ("red", "resi 176 & chain A")

cmd.select ("Inward", "resi 176 & chain A", merge=1)

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

cmd.load_cgo( [9.0, 16.256865,12.5916815,13.066046, 16.256865, 12.5916815, 13.066046, 1, 1,1,0,0,0,1], "axis" )
