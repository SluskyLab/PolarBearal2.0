from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3CSL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand7", "resi 243+244+245+246+247+248+249+250+251+252 & chain A ")


cmd.select("Astrand8", "resi 258+259+260+261+262+263+264+265+266 & chain A ")


cmd.select("Astrand9", "resi 271+272+273+274+275+276+277+278+279+280+281+282 & chain A ")


cmd.select("Astrand10", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A ")


cmd.select("Astrand11", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355 & chain A ")


cmd.select("Astrand14", "resi 373+374+375+376+377+378+379+380+381+382+383+384+385+386+387+388+389+390 & chain A ")


cmd.select("Astrand15", "resi 400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415 & chain A ")


cmd.select("Astrand16", "resi 426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+448 & chain A ")


cmd.select("Astrand17", "resi 451+452+453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470 & chain A ")


cmd.select("Astrand18", "resi 482+483+484+485+486+487+488+489+490+491+492+493+494+495+496+497 & chain A ")


cmd.select("Astrand19", "resi 501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518 & chain A ")


cmd.select("Astrand22", "resi 554+555+556+557+558+559+560+561+562+563+564+565+566+567+568+569+570+571 & chain A ")


cmd.select("Astrand23", "resi 578+579+580+581+582+583+584+585+586+587+588+589 & chain A ")


cmd.select("Astrand25", "resi 617+618+619+620+621+622+623+624+625+626+627+628+629+630+631 & chain A ")


cmd.select("Astrand26", "resi 639+640+641+642+643+644+645+646+647+648+649+650+651+652 & chain A ")


cmd.select("Astrand29", "resi 682+683+684+685+686+687+688+689+690+691+692+693+694+695 & chain A ")


cmd.select("Astrand30", "resi 699+700+701+702+703+704+705+706+707+708+709 & chain A ")


cmd.select("Astrand35", "resi 766+767+768+769+770+771+772+773 & chain A ")


cmd.select("Astrand36", "resi 782+783+784+785+786+787+788+789 & chain A ")


cmd.select("Astrand39", "resi 810+811+812+813+814+815+816+817+818+819+820 & chain A ")


cmd.select("Astrand40", "resi 825+826+827+828+829+830+831 & chain A ")


cmd.select("Astrand41", "resi 857+858+859+860+861+862+863+864 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("red", "resi 248 & chain A")

cmd.select ("Inward", "resi 248 & chain A", merge=1)

cmd.color ("blue", "resi 249 & chain A")

cmd.select ("Outward", "resi 249 & chain A", merge=1)

cmd.color ("red", "resi 250 & chain A")

cmd.select ("Inward", "resi 250 & chain A", merge=1)

cmd.color ("blue", "resi 251 & chain A")

cmd.select ("Outward", "resi 251 & chain A", merge=1)

cmd.color ("red", "resi 252 & chain A")

cmd.select ("Inward", "resi 252 & chain A", merge=1)

cmd.color ("blue", "resi 258 & chain A")

cmd.select ("Outward", "resi 258 & chain A", merge=1)

cmd.color ("red", "resi 259 & chain A")

cmd.select ("Inward", "resi 259 & chain A", merge=1)

cmd.color ("blue", "resi 260 & chain A")

cmd.select ("Outward", "resi 260 & chain A", merge=1)

cmd.color ("red", "resi 261 & chain A")

cmd.select ("Inward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 262 & chain A")

cmd.select ("Outward", "resi 262 & chain A", merge=1)

cmd.color ("red", "resi 263 & chain A")

cmd.select ("Inward", "resi 263 & chain A", merge=1)

cmd.color ("blue", "resi 264 & chain A")

cmd.select ("Outward", "resi 264 & chain A", merge=1)

cmd.color ("red", "resi 265 & chain A")

cmd.select ("Inward", "resi 265 & chain A", merge=1)

cmd.color ("blue", "resi 266 & chain A")

cmd.select ("Outward", "resi 266 & chain A", merge=1)

cmd.color ("blue", "resi 271 & chain A")

cmd.select ("Outward", "resi 271 & chain A", merge=1)

cmd.color ("red", "resi 272 & chain A")

cmd.select ("Inward", "resi 272 & chain A", merge=1)

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

cmd.color ("red", "resi 322 & chain A")

cmd.select ("Inward", "resi 322 & chain A", merge=1)

cmd.color ("blue", "resi 323 & chain A")

cmd.select ("Outward", "resi 323 & chain A", merge=1)

cmd.color ("red", "resi 324 & chain A")

cmd.select ("Inward", "resi 324 & chain A", merge=1)

cmd.color ("blue", "resi 325 & chain A")

cmd.select ("Outward", "resi 325 & chain A", merge=1)

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

cmd.color ("blue", "resi 334 & chain A")

cmd.select ("Outward", "resi 334 & chain A", merge=1)

cmd.color ("red", "resi 335 & chain A")

cmd.select ("Inward", "resi 335 & chain A", merge=1)

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

cmd.color ("red", "resi 352 & chain A")

cmd.select ("Inward", "resi 352 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("red", "resi 354 & chain A")

cmd.select ("Inward", "resi 354 & chain A", merge=1)

cmd.color ("red", "resi 355 & chain A")

cmd.select ("Inward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 373 & chain A")

cmd.select ("Outward", "resi 373 & chain A", merge=1)

cmd.color ("red", "resi 374 & chain A")

cmd.select ("Inward", "resi 374 & chain A", merge=1)

cmd.color ("red", "resi 375 & chain A")

cmd.select ("Inward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("red", "resi 377 & chain A")

cmd.select ("Inward", "resi 377 & chain A", merge=1)

cmd.color ("blue", "resi 378 & chain A")

cmd.select ("Outward", "resi 378 & chain A", merge=1)

cmd.color ("red", "resi 379 & chain A")

cmd.select ("Inward", "resi 379 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("red", "resi 381 & chain A")

cmd.select ("Inward", "resi 381 & chain A", merge=1)

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("red", "resi 383 & chain A")

cmd.select ("Inward", "resi 383 & chain A", merge=1)

cmd.color ("blue", "resi 384 & chain A")

cmd.select ("Outward", "resi 384 & chain A", merge=1)

cmd.color ("red", "resi 385 & chain A")

cmd.select ("Inward", "resi 385 & chain A", merge=1)

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("red", "resi 387 & chain A")

cmd.select ("Inward", "resi 387 & chain A", merge=1)

cmd.color ("blue", "resi 388 & chain A")

cmd.select ("Outward", "resi 388 & chain A", merge=1)

cmd.color ("red", "resi 389 & chain A")

cmd.select ("Inward", "resi 389 & chain A", merge=1)

cmd.color ("blue", "resi 390 & chain A")

cmd.select ("Outward", "resi 390 & chain A", merge=1)

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

cmd.color ("blue", "resi 431 & chain A")

cmd.select ("Outward", "resi 431 & chain A", merge=1)

cmd.color ("red", "resi 432 & chain A")

cmd.select ("Inward", "resi 432 & chain A", merge=1)

cmd.color ("blue", "resi 433 & chain A")

cmd.select ("Outward", "resi 433 & chain A", merge=1)

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

cmd.color ("red", "resi 444 & chain A")

cmd.select ("Inward", "resi 444 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("blue", "resi 446 & chain A")

cmd.select ("Outward", "resi 446 & chain A", merge=1)

cmd.color ("red", "resi 447 & chain A")

cmd.select ("Inward", "resi 447 & chain A", merge=1)

cmd.color ("blue", "resi 448 & chain A")

cmd.select ("Outward", "resi 448 & chain A", merge=1)

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

cmd.color ("red", "resi 482 & chain A")

cmd.select ("Inward", "resi 482 & chain A", merge=1)

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

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

cmd.color ("red", "resi 496 & chain A")

cmd.select ("Inward", "resi 496 & chain A", merge=1)

cmd.color ("blue", "resi 497 & chain A")

cmd.select ("Outward", "resi 497 & chain A", merge=1)

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

cmd.color ("red", "resi 568 & chain A")

cmd.select ("Inward", "resi 568 & chain A", merge=1)

cmd.color ("blue", "resi 569 & chain A")

cmd.select ("Outward", "resi 569 & chain A", merge=1)

cmd.color ("red", "resi 570 & chain A")

cmd.select ("Inward", "resi 570 & chain A", merge=1)

cmd.color ("blue", "resi 571 & chain A")

cmd.select ("Outward", "resi 571 & chain A", merge=1)

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

cmd.color ("red", "resi 625 & chain A")

cmd.select ("Inward", "resi 625 & chain A", merge=1)

cmd.color ("blue", "resi 626 & chain A")

cmd.select ("Outward", "resi 626 & chain A", merge=1)

cmd.color ("red", "resi 627 & chain A")

cmd.select ("Inward", "resi 627 & chain A", merge=1)

cmd.color ("blue", "resi 628 & chain A")

cmd.select ("Outward", "resi 628 & chain A", merge=1)

cmd.color ("red", "resi 629 & chain A")

cmd.select ("Inward", "resi 629 & chain A", merge=1)

cmd.color ("blue", "resi 630 & chain A")

cmd.select ("Outward", "resi 630 & chain A", merge=1)

cmd.color ("blue", "resi 631 & chain A")

cmd.select ("Outward", "resi 631 & chain A", merge=1)

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

cmd.color ("red", "resi 649 & chain A")

cmd.select ("Inward", "resi 649 & chain A", merge=1)

cmd.color ("blue", "resi 650 & chain A")

cmd.select ("Outward", "resi 650 & chain A", merge=1)

cmd.color ("red", "resi 651 & chain A")

cmd.select ("Inward", "resi 651 & chain A", merge=1)

cmd.color ("blue", "resi 652 & chain A")

cmd.select ("Outward", "resi 652 & chain A", merge=1)

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

cmd.color ("red", "resi 687 & chain A")

cmd.select ("Inward", "resi 687 & chain A", merge=1)

cmd.color ("blue", "resi 688 & chain A")

cmd.select ("Outward", "resi 688 & chain A", merge=1)

cmd.color ("red", "resi 689 & chain A")

cmd.select ("Inward", "resi 689 & chain A", merge=1)

cmd.color ("blue", "resi 690 & chain A")

cmd.select ("Outward", "resi 690 & chain A", merge=1)

cmd.color ("red", "resi 691 & chain A")

cmd.select ("Inward", "resi 691 & chain A", merge=1)

cmd.color ("blue", "resi 692 & chain A")

cmd.select ("Outward", "resi 692 & chain A", merge=1)

cmd.color ("red", "resi 693 & chain A")

cmd.select ("Inward", "resi 693 & chain A", merge=1)

cmd.color ("blue", "resi 694 & chain A")

cmd.select ("Outward", "resi 694 & chain A", merge=1)

cmd.color ("red", "resi 695 & chain A")

cmd.select ("Inward", "resi 695 & chain A", merge=1)

cmd.color ("blue", "resi 699 & chain A")

cmd.select ("Outward", "resi 699 & chain A", merge=1)

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

cmd.color ("red", "resi 706 & chain A")

cmd.select ("Inward", "resi 706 & chain A", merge=1)

cmd.color ("blue", "resi 707 & chain A")

cmd.select ("Outward", "resi 707 & chain A", merge=1)

cmd.color ("red", "resi 708 & chain A")

cmd.select ("Inward", "resi 708 & chain A", merge=1)

cmd.color ("red", "resi 709 & chain A")

cmd.select ("Inward", "resi 709 & chain A", merge=1)

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

cmd.color ("blue", "resi 773 & chain A")

cmd.select ("Outward", "resi 773 & chain A", merge=1)

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

cmd.color ("red", "resi 789 & chain A")

cmd.select ("Inward", "resi 789 & chain A", merge=1)

cmd.color ("red", "resi 810 & chain A")

cmd.select ("Inward", "resi 810 & chain A", merge=1)

cmd.color ("blue", "resi 811 & chain A")

cmd.select ("Outward", "resi 811 & chain A", merge=1)

cmd.color ("red", "resi 812 & chain A")

cmd.select ("Inward", "resi 812 & chain A", merge=1)

cmd.color ("blue", "resi 813 & chain A")

cmd.select ("Outward", "resi 813 & chain A", merge=1)

cmd.color ("red", "resi 814 & chain A")

cmd.select ("Inward", "resi 814 & chain A", merge=1)

cmd.color ("blue", "resi 815 & chain A")

cmd.select ("Outward", "resi 815 & chain A", merge=1)

cmd.color ("red", "resi 816 & chain A")

cmd.select ("Inward", "resi 816 & chain A", merge=1)

cmd.color ("blue", "resi 817 & chain A")

cmd.select ("Outward", "resi 817 & chain A", merge=1)

cmd.color ("red", "resi 818 & chain A")

cmd.select ("Inward", "resi 818 & chain A", merge=1)

cmd.color ("blue", "resi 819 & chain A")

cmd.select ("Outward", "resi 819 & chain A", merge=1)

cmd.color ("blue", "resi 820 & chain A")

cmd.select ("Outward", "resi 820 & chain A", merge=1)

cmd.color ("blue", "resi 825 & chain A")

cmd.select ("Outward", "resi 825 & chain A", merge=1)

cmd.color ("red", "resi 826 & chain A")

cmd.select ("Inward", "resi 826 & chain A", merge=1)

cmd.color ("blue", "resi 827 & chain A")

cmd.select ("Outward", "resi 827 & chain A", merge=1)

cmd.color ("red", "resi 828 & chain A")

cmd.select ("Inward", "resi 828 & chain A", merge=1)

cmd.color ("blue", "resi 829 & chain A")

cmd.select ("Outward", "resi 829 & chain A", merge=1)

cmd.color ("red", "resi 830 & chain A")

cmd.select ("Inward", "resi 830 & chain A", merge=1)

cmd.color ("blue", "resi 831 & chain A")

cmd.select ("Outward", "resi 831 & chain A", merge=1)

cmd.color ("blue", "resi 857 & chain A")

cmd.select ("Outward", "resi 857 & chain A", merge=1)

cmd.color ("red", "resi 858 & chain A")

cmd.select ("Inward", "resi 858 & chain A", merge=1)

cmd.color ("blue", "resi 859 & chain A")

cmd.select ("Outward", "resi 859 & chain A", merge=1)

cmd.color ("red", "resi 860 & chain A")

cmd.select ("Inward", "resi 860 & chain A", merge=1)

cmd.color ("blue", "resi 861 & chain A")

cmd.select ("Outward", "resi 861 & chain A", merge=1)

cmd.color ("red", "resi 862 & chain A")

cmd.select ("Inward", "resi 862 & chain A", merge=1)

cmd.color ("blue", "resi 863 & chain A")

cmd.select ("Outward", "resi 863 & chain A", merge=1)

cmd.color ("red", "resi 864 & chain A")

cmd.select ("Inward", "resi 864 & chain A", merge=1)

cmd.load_cgo( [9.0, 51.73791,57.517227,247.69623, 51.73791, 57.517227, 247.69623, 1, 1,1,0,0,0,1], "axis" )
