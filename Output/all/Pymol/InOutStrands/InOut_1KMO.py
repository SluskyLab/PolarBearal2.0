from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1KMO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand7", "resi 224+225+226+227+228+229+230+231+232+233 & chain A ")


cmd.select("Astrand8", "resi 243+244+245+246+247+248+249+250+251+252+253 & chain A ")


cmd.select("Astrand9", "resi 258+259+260+261+262+263+264+265+266+267+268+269 & chain A ")


cmd.select("Astrand10", "resi 278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")


cmd.select("Astrand11", "resi 295+296+297+298+299+300+301+302+303+304+305+306+307+308+309 & chain A ")


cmd.select("Astrand12", "resi 332+333+334+377+376+335+375+336+374+380+381+337+436+438+437+382+439+338+440+383+441+339+442+384+443+340+385+444+341+386+483+484+445+535+485+446+486+342+387+536+537+487+388+447+343+488+448+490+489+539+538+389+344+492+449+491+450+540+541+390+345+494+493+543+542+545+451+391+496+544+452+495+346+546+392+547+497+498+454+453+393+499+455+500+394+456+501+502+395+457+396+397 & chain A ")


cmd.select("Astrand13", "resi 551+552+553+554+505+555+506+507+556+508+557+509+558+460+461+510+462+559+463+511+560+512+401+403+464+400+402+465+514+513+561+405+404+353+562+466+352+515+467+406+355+407+354+516+357+563+356+408+468+409+565+359+358+469+564+361+411+360+410+363+470+362+365+471+413+412+364+366+367+472+414+473+415+369+368+417+416+474+370+475+371+418+419+476+420+477+421+422+423 & chain A ")


cmd.select("Astrand23", "resi 579+580+581+582+583+584+585+586+587+588+589+590+591+592+593 & chain A ")


cmd.select("Astrand24", "resi 604+605+606+607+608+609+610+611+612+613+614+615+616+617 & chain A ")


cmd.select("Astrand25", "resi 634+635+636+637+638+639+640+641+642 & chain A ")


cmd.select("Astrand26", "resi 647+648+649+650+651+652+653+654+655+656 & chain A ")


cmd.select("Astrand27", "resi 681+682+683+684+685+686+687+688+689+690+691 & chain A ")


cmd.select("Astrand28", "resi 700+701+702+703+704+705+706 & chain A ")


cmd.select("Astrand31", "resi 732+733+734+735+736+737+738+739+740 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 224 & chain A")

cmd.select ("Outward", "resi 224 & chain A", merge=1)

cmd.color ("blue", "resi 225 & chain A")

cmd.select ("Outward", "resi 225 & chain A", merge=1)

cmd.color ("blue", "resi 226 & chain A")

cmd.select ("Outward", "resi 226 & chain A", merge=1)

cmd.color ("blue", "resi 227 & chain A")

cmd.select ("Outward", "resi 227 & chain A", merge=1)

cmd.color ("blue", "resi 228 & chain A")

cmd.select ("Outward", "resi 228 & chain A", merge=1)

cmd.color ("blue", "resi 229 & chain A")

cmd.select ("Outward", "resi 229 & chain A", merge=1)

cmd.color ("blue", "resi 230 & chain A")

cmd.select ("Outward", "resi 230 & chain A", merge=1)

cmd.color ("blue", "resi 231 & chain A")

cmd.select ("Outward", "resi 231 & chain A", merge=1)

cmd.color ("blue", "resi 232 & chain A")

cmd.select ("Outward", "resi 232 & chain A", merge=1)

cmd.color ("blue", "resi 233 & chain A")

cmd.select ("Outward", "resi 233 & chain A", merge=1)

cmd.color ("blue", "resi 243 & chain A")

cmd.select ("Outward", "resi 243 & chain A", merge=1)

cmd.color ("blue", "resi 244 & chain A")

cmd.select ("Outward", "resi 244 & chain A", merge=1)

cmd.color ("blue", "resi 245 & chain A")

cmd.select ("Outward", "resi 245 & chain A", merge=1)

cmd.color ("blue", "resi 246 & chain A")

cmd.select ("Outward", "resi 246 & chain A", merge=1)

cmd.color ("blue", "resi 247 & chain A")

cmd.select ("Outward", "resi 247 & chain A", merge=1)

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

cmd.color ("blue", "resi 249 & chain A")

cmd.select ("Outward", "resi 249 & chain A", merge=1)

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

cmd.color ("blue", "resi 251 & chain A")

cmd.select ("Outward", "resi 251 & chain A", merge=1)

cmd.color ("blue", "resi 252 & chain A")

cmd.select ("Outward", "resi 252 & chain A", merge=1)

cmd.color ("blue", "resi 253 & chain A")

cmd.select ("Outward", "resi 253 & chain A", merge=1)

cmd.color ("blue", "resi 258 & chain A")

cmd.select ("Outward", "resi 258 & chain A", merge=1)

cmd.color ("blue", "resi 259 & chain A")

cmd.select ("Outward", "resi 259 & chain A", merge=1)

cmd.color ("blue", "resi 260 & chain A")

cmd.select ("Outward", "resi 260 & chain A", merge=1)

cmd.color ("blue", "resi 261 & chain A")

cmd.select ("Outward", "resi 261 & chain A", merge=1)

cmd.color ("blue", "resi 262 & chain A")

cmd.select ("Outward", "resi 262 & chain A", merge=1)

cmd.color ("blue", "resi 263 & chain A")

cmd.select ("Outward", "resi 263 & chain A", merge=1)

cmd.color ("blue", "resi 264 & chain A")

cmd.select ("Outward", "resi 264 & chain A", merge=1)

cmd.color ("blue", "resi 265 & chain A")

cmd.select ("Outward", "resi 265 & chain A", merge=1)

cmd.color ("blue", "resi 266 & chain A")

cmd.select ("Outward", "resi 266 & chain A", merge=1)

cmd.color ("blue", "resi 267 & chain A")

cmd.select ("Outward", "resi 267 & chain A", merge=1)

cmd.color ("blue", "resi 268 & chain A")

cmd.select ("Outward", "resi 268 & chain A", merge=1)

cmd.color ("blue", "resi 269 & chain A")

cmd.select ("Outward", "resi 269 & chain A", merge=1)

cmd.color ("blue", "resi 278 & chain A")

cmd.select ("Outward", "resi 278 & chain A", merge=1)

cmd.color ("blue", "resi 279 & chain A")

cmd.select ("Outward", "resi 279 & chain A", merge=1)

cmd.color ("blue", "resi 280 & chain A")

cmd.select ("Outward", "resi 280 & chain A", merge=1)

cmd.color ("blue", "resi 281 & chain A")

cmd.select ("Outward", "resi 281 & chain A", merge=1)

cmd.color ("blue", "resi 282 & chain A")

cmd.select ("Outward", "resi 282 & chain A", merge=1)

cmd.color ("blue", "resi 283 & chain A")

cmd.select ("Outward", "resi 283 & chain A", merge=1)

cmd.color ("blue", "resi 284 & chain A")

cmd.select ("Outward", "resi 284 & chain A", merge=1)

cmd.color ("blue", "resi 285 & chain A")

cmd.select ("Outward", "resi 285 & chain A", merge=1)

cmd.color ("blue", "resi 286 & chain A")

cmd.select ("Outward", "resi 286 & chain A", merge=1)

cmd.color ("blue", "resi 287 & chain A")

cmd.select ("Outward", "resi 287 & chain A", merge=1)

cmd.color ("blue", "resi 288 & chain A")

cmd.select ("Outward", "resi 288 & chain A", merge=1)

cmd.color ("blue", "resi 289 & chain A")

cmd.select ("Outward", "resi 289 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("blue", "resi 296 & chain A")

cmd.select ("Outward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("blue", "resi 298 & chain A")

cmd.select ("Outward", "resi 298 & chain A", merge=1)

cmd.color ("blue", "resi 299 & chain A")

cmd.select ("Outward", "resi 299 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.color ("blue", "resi 301 & chain A")

cmd.select ("Outward", "resi 301 & chain A", merge=1)

cmd.color ("blue", "resi 302 & chain A")

cmd.select ("Outward", "resi 302 & chain A", merge=1)

cmd.color ("blue", "resi 303 & chain A")

cmd.select ("Outward", "resi 303 & chain A", merge=1)

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

cmd.color ("blue", "resi 305 & chain A")

cmd.select ("Outward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 306 & chain A")

cmd.select ("Outward", "resi 306 & chain A", merge=1)

cmd.color ("blue", "resi 307 & chain A")

cmd.select ("Outward", "resi 307 & chain A", merge=1)

cmd.color ("blue", "resi 308 & chain A")

cmd.select ("Outward", "resi 308 & chain A", merge=1)

cmd.color ("blue", "resi 309 & chain A")

cmd.select ("Outward", "resi 309 & chain A", merge=1)

cmd.color ("blue", "resi 332 & chain A")

cmd.select ("Outward", "resi 332 & chain A", merge=1)

cmd.color ("blue", "resi 333 & chain A")

cmd.select ("Outward", "resi 333 & chain A", merge=1)

cmd.color ("blue", "resi 334 & chain A")

cmd.select ("Outward", "resi 334 & chain A", merge=1)

cmd.color ("blue", "resi 377 & chain A")

cmd.select ("Outward", "resi 377 & chain A", merge=1)

cmd.color ("blue", "resi 376 & chain A")

cmd.select ("Outward", "resi 376 & chain A", merge=1)

cmd.color ("blue", "resi 335 & chain A")

cmd.select ("Outward", "resi 335 & chain A", merge=1)

cmd.color ("blue", "resi 375 & chain A")

cmd.select ("Outward", "resi 375 & chain A", merge=1)

cmd.color ("blue", "resi 336 & chain A")

cmd.select ("Outward", "resi 336 & chain A", merge=1)

cmd.color ("blue", "resi 374 & chain A")

cmd.select ("Outward", "resi 374 & chain A", merge=1)

cmd.color ("blue", "resi 380 & chain A")

cmd.select ("Outward", "resi 380 & chain A", merge=1)

cmd.color ("blue", "resi 381 & chain A")

cmd.select ("Outward", "resi 381 & chain A", merge=1)

cmd.color ("blue", "resi 337 & chain A")

cmd.select ("Outward", "resi 337 & chain A", merge=1)

cmd.color ("blue", "resi 436 & chain A")

cmd.select ("Outward", "resi 436 & chain A", merge=1)

cmd.color ("blue", "resi 438 & chain A")

cmd.select ("Outward", "resi 438 & chain A", merge=1)

cmd.color ("blue", "resi 437 & chain A")

cmd.select ("Outward", "resi 437 & chain A", merge=1)

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("blue", "resi 439 & chain A")

cmd.select ("Outward", "resi 439 & chain A", merge=1)

cmd.color ("blue", "resi 338 & chain A")

cmd.select ("Outward", "resi 338 & chain A", merge=1)

cmd.color ("blue", "resi 440 & chain A")

cmd.select ("Outward", "resi 440 & chain A", merge=1)

cmd.color ("blue", "resi 383 & chain A")

cmd.select ("Outward", "resi 383 & chain A", merge=1)

cmd.color ("blue", "resi 441 & chain A")

cmd.select ("Outward", "resi 441 & chain A", merge=1)

cmd.color ("blue", "resi 339 & chain A")

cmd.select ("Outward", "resi 339 & chain A", merge=1)

cmd.color ("blue", "resi 442 & chain A")

cmd.select ("Outward", "resi 442 & chain A", merge=1)

cmd.color ("blue", "resi 384 & chain A")

cmd.select ("Outward", "resi 384 & chain A", merge=1)

cmd.color ("blue", "resi 443 & chain A")

cmd.select ("Outward", "resi 443 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 385 & chain A")

cmd.select ("Outward", "resi 385 & chain A", merge=1)

cmd.color ("blue", "resi 444 & chain A")

cmd.select ("Outward", "resi 444 & chain A", merge=1)

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 386 & chain A")

cmd.select ("Outward", "resi 386 & chain A", merge=1)

cmd.color ("blue", "resi 483 & chain A")

cmd.select ("Outward", "resi 483 & chain A", merge=1)

cmd.color ("blue", "resi 484 & chain A")

cmd.select ("Outward", "resi 484 & chain A", merge=1)

cmd.color ("blue", "resi 445 & chain A")

cmd.select ("Outward", "resi 445 & chain A", merge=1)

cmd.color ("blue", "resi 535 & chain A")

cmd.select ("Outward", "resi 535 & chain A", merge=1)

cmd.color ("blue", "resi 485 & chain A")

cmd.select ("Outward", "resi 485 & chain A", merge=1)

cmd.color ("blue", "resi 446 & chain A")

cmd.select ("Outward", "resi 446 & chain A", merge=1)

cmd.color ("blue", "resi 486 & chain A")

cmd.select ("Outward", "resi 486 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("blue", "resi 387 & chain A")

cmd.select ("Outward", "resi 387 & chain A", merge=1)

cmd.color ("blue", "resi 536 & chain A")

cmd.select ("Outward", "resi 536 & chain A", merge=1)

cmd.color ("blue", "resi 537 & chain A")

cmd.select ("Outward", "resi 537 & chain A", merge=1)

cmd.color ("blue", "resi 487 & chain A")

cmd.select ("Outward", "resi 487 & chain A", merge=1)

cmd.color ("blue", "resi 388 & chain A")

cmd.select ("Outward", "resi 388 & chain A", merge=1)

cmd.color ("blue", "resi 447 & chain A")

cmd.select ("Outward", "resi 447 & chain A", merge=1)

cmd.color ("blue", "resi 343 & chain A")

cmd.select ("Outward", "resi 343 & chain A", merge=1)

cmd.color ("blue", "resi 488 & chain A")

cmd.select ("Outward", "resi 488 & chain A", merge=1)

cmd.color ("blue", "resi 448 & chain A")

cmd.select ("Outward", "resi 448 & chain A", merge=1)

cmd.color ("blue", "resi 490 & chain A")

cmd.select ("Outward", "resi 490 & chain A", merge=1)

cmd.color ("blue", "resi 489 & chain A")

cmd.select ("Outward", "resi 489 & chain A", merge=1)

cmd.color ("blue", "resi 539 & chain A")

cmd.select ("Outward", "resi 539 & chain A", merge=1)

cmd.color ("blue", "resi 538 & chain A")

cmd.select ("Outward", "resi 538 & chain A", merge=1)

cmd.color ("blue", "resi 389 & chain A")

cmd.select ("Outward", "resi 389 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("blue", "resi 492 & chain A")

cmd.select ("Outward", "resi 492 & chain A", merge=1)

cmd.color ("blue", "resi 449 & chain A")

cmd.select ("Outward", "resi 449 & chain A", merge=1)

cmd.color ("blue", "resi 491 & chain A")

cmd.select ("Outward", "resi 491 & chain A", merge=1)

cmd.color ("blue", "resi 450 & chain A")

cmd.select ("Outward", "resi 450 & chain A", merge=1)

cmd.color ("blue", "resi 540 & chain A")

cmd.select ("Outward", "resi 540 & chain A", merge=1)

cmd.color ("blue", "resi 541 & chain A")

cmd.select ("Outward", "resi 541 & chain A", merge=1)

cmd.color ("blue", "resi 390 & chain A")

cmd.select ("Outward", "resi 390 & chain A", merge=1)

cmd.color ("blue", "resi 345 & chain A")

cmd.select ("Outward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 494 & chain A")

cmd.select ("Outward", "resi 494 & chain A", merge=1)

cmd.color ("blue", "resi 493 & chain A")

cmd.select ("Outward", "resi 493 & chain A", merge=1)

cmd.color ("blue", "resi 543 & chain A")

cmd.select ("Outward", "resi 543 & chain A", merge=1)

cmd.color ("blue", "resi 542 & chain A")

cmd.select ("Outward", "resi 542 & chain A", merge=1)

cmd.color ("blue", "resi 545 & chain A")

cmd.select ("Outward", "resi 545 & chain A", merge=1)

cmd.color ("blue", "resi 451 & chain A")

cmd.select ("Outward", "resi 451 & chain A", merge=1)

cmd.color ("blue", "resi 391 & chain A")

cmd.select ("Outward", "resi 391 & chain A", merge=1)

cmd.color ("blue", "resi 496 & chain A")

cmd.select ("Outward", "resi 496 & chain A", merge=1)

cmd.color ("blue", "resi 544 & chain A")

cmd.select ("Outward", "resi 544 & chain A", merge=1)

cmd.color ("blue", "resi 452 & chain A")

cmd.select ("Outward", "resi 452 & chain A", merge=1)

cmd.color ("blue", "resi 495 & chain A")

cmd.select ("Outward", "resi 495 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("blue", "resi 546 & chain A")

cmd.select ("Outward", "resi 546 & chain A", merge=1)

cmd.color ("blue", "resi 392 & chain A")

cmd.select ("Outward", "resi 392 & chain A", merge=1)

cmd.color ("blue", "resi 547 & chain A")

cmd.select ("Outward", "resi 547 & chain A", merge=1)

cmd.color ("blue", "resi 497 & chain A")

cmd.select ("Outward", "resi 497 & chain A", merge=1)

cmd.color ("blue", "resi 498 & chain A")

cmd.select ("Outward", "resi 498 & chain A", merge=1)

cmd.color ("blue", "resi 454 & chain A")

cmd.select ("Outward", "resi 454 & chain A", merge=1)

cmd.color ("blue", "resi 453 & chain A")

cmd.select ("Outward", "resi 453 & chain A", merge=1)

cmd.color ("blue", "resi 393 & chain A")

cmd.select ("Outward", "resi 393 & chain A", merge=1)

cmd.color ("blue", "resi 499 & chain A")

cmd.select ("Outward", "resi 499 & chain A", merge=1)

cmd.color ("blue", "resi 455 & chain A")

cmd.select ("Outward", "resi 455 & chain A", merge=1)

cmd.color ("blue", "resi 500 & chain A")

cmd.select ("Outward", "resi 500 & chain A", merge=1)

cmd.color ("blue", "resi 394 & chain A")

cmd.select ("Outward", "resi 394 & chain A", merge=1)

cmd.color ("blue", "resi 456 & chain A")

cmd.select ("Outward", "resi 456 & chain A", merge=1)

cmd.color ("blue", "resi 501 & chain A")

cmd.select ("Outward", "resi 501 & chain A", merge=1)

cmd.color ("blue", "resi 502 & chain A")

cmd.select ("Outward", "resi 502 & chain A", merge=1)

cmd.color ("blue", "resi 395 & chain A")

cmd.select ("Outward", "resi 395 & chain A", merge=1)

cmd.color ("blue", "resi 457 & chain A")

cmd.select ("Outward", "resi 457 & chain A", merge=1)

cmd.color ("blue", "resi 396 & chain A")

cmd.select ("Outward", "resi 396 & chain A", merge=1)

cmd.color ("blue", "resi 397 & chain A")

cmd.select ("Outward", "resi 397 & chain A", merge=1)

cmd.color ("blue", "resi 551 & chain A")

cmd.select ("Outward", "resi 551 & chain A", merge=1)

cmd.color ("blue", "resi 552 & chain A")

cmd.select ("Outward", "resi 552 & chain A", merge=1)

cmd.color ("blue", "resi 553 & chain A")

cmd.select ("Outward", "resi 553 & chain A", merge=1)

cmd.color ("blue", "resi 554 & chain A")

cmd.select ("Outward", "resi 554 & chain A", merge=1)

cmd.color ("blue", "resi 505 & chain A")

cmd.select ("Outward", "resi 505 & chain A", merge=1)

cmd.color ("blue", "resi 555 & chain A")

cmd.select ("Outward", "resi 555 & chain A", merge=1)

cmd.color ("blue", "resi 506 & chain A")

cmd.select ("Outward", "resi 506 & chain A", merge=1)

cmd.color ("blue", "resi 507 & chain A")

cmd.select ("Outward", "resi 507 & chain A", merge=1)

cmd.color ("blue", "resi 556 & chain A")

cmd.select ("Outward", "resi 556 & chain A", merge=1)

cmd.color ("blue", "resi 508 & chain A")

cmd.select ("Outward", "resi 508 & chain A", merge=1)

cmd.color ("blue", "resi 557 & chain A")

cmd.select ("Outward", "resi 557 & chain A", merge=1)

cmd.color ("blue", "resi 509 & chain A")

cmd.select ("Outward", "resi 509 & chain A", merge=1)

cmd.color ("blue", "resi 558 & chain A")

cmd.select ("Outward", "resi 558 & chain A", merge=1)

cmd.color ("blue", "resi 460 & chain A")

cmd.select ("Outward", "resi 460 & chain A", merge=1)

cmd.color ("blue", "resi 461 & chain A")

cmd.select ("Outward", "resi 461 & chain A", merge=1)

cmd.color ("blue", "resi 510 & chain A")

cmd.select ("Outward", "resi 510 & chain A", merge=1)

cmd.color ("blue", "resi 462 & chain A")

cmd.select ("Outward", "resi 462 & chain A", merge=1)

cmd.color ("blue", "resi 559 & chain A")

cmd.select ("Outward", "resi 559 & chain A", merge=1)

cmd.color ("blue", "resi 463 & chain A")

cmd.select ("Outward", "resi 463 & chain A", merge=1)

cmd.color ("blue", "resi 511 & chain A")

cmd.select ("Outward", "resi 511 & chain A", merge=1)

cmd.color ("blue", "resi 560 & chain A")

cmd.select ("Outward", "resi 560 & chain A", merge=1)

cmd.color ("blue", "resi 512 & chain A")

cmd.select ("Outward", "resi 512 & chain A", merge=1)

cmd.color ("blue", "resi 401 & chain A")

cmd.select ("Outward", "resi 401 & chain A", merge=1)

cmd.color ("blue", "resi 403 & chain A")

cmd.select ("Outward", "resi 403 & chain A", merge=1)

cmd.color ("blue", "resi 464 & chain A")

cmd.select ("Outward", "resi 464 & chain A", merge=1)

cmd.color ("blue", "resi 400 & chain A")

cmd.select ("Outward", "resi 400 & chain A", merge=1)

cmd.color ("blue", "resi 402 & chain A")

cmd.select ("Outward", "resi 402 & chain A", merge=1)

cmd.color ("blue", "resi 465 & chain A")

cmd.select ("Outward", "resi 465 & chain A", merge=1)

cmd.color ("blue", "resi 514 & chain A")

cmd.select ("Outward", "resi 514 & chain A", merge=1)

cmd.color ("blue", "resi 513 & chain A")

cmd.select ("Outward", "resi 513 & chain A", merge=1)

cmd.color ("blue", "resi 561 & chain A")

cmd.select ("Outward", "resi 561 & chain A", merge=1)

cmd.color ("blue", "resi 405 & chain A")

cmd.select ("Outward", "resi 405 & chain A", merge=1)

cmd.color ("blue", "resi 404 & chain A")

cmd.select ("Outward", "resi 404 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("blue", "resi 562 & chain A")

cmd.select ("Outward", "resi 562 & chain A", merge=1)

cmd.color ("blue", "resi 466 & chain A")

cmd.select ("Outward", "resi 466 & chain A", merge=1)

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("blue", "resi 515 & chain A")

cmd.select ("Outward", "resi 515 & chain A", merge=1)

cmd.color ("blue", "resi 467 & chain A")

cmd.select ("Outward", "resi 467 & chain A", merge=1)

cmd.color ("blue", "resi 406 & chain A")

cmd.select ("Outward", "resi 406 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 407 & chain A")

cmd.select ("Outward", "resi 407 & chain A", merge=1)

cmd.color ("blue", "resi 354 & chain A")

cmd.select ("Outward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 516 & chain A")

cmd.select ("Outward", "resi 516 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("blue", "resi 563 & chain A")

cmd.select ("Outward", "resi 563 & chain A", merge=1)

cmd.color ("blue", "resi 356 & chain A")

cmd.select ("Outward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 408 & chain A")

cmd.select ("Outward", "resi 408 & chain A", merge=1)

cmd.color ("blue", "resi 468 & chain A")

cmd.select ("Outward", "resi 468 & chain A", merge=1)

cmd.color ("blue", "resi 409 & chain A")

cmd.select ("Outward", "resi 409 & chain A", merge=1)

cmd.color ("blue", "resi 565 & chain A")

cmd.select ("Outward", "resi 565 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("blue", "resi 358 & chain A")

cmd.select ("Outward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 469 & chain A")

cmd.select ("Outward", "resi 469 & chain A", merge=1)

cmd.color ("blue", "resi 564 & chain A")

cmd.select ("Outward", "resi 564 & chain A", merge=1)

cmd.color ("blue", "resi 361 & chain A")

cmd.select ("Outward", "resi 361 & chain A", merge=1)

cmd.color ("blue", "resi 411 & chain A")

cmd.select ("Outward", "resi 411 & chain A", merge=1)

cmd.color ("blue", "resi 360 & chain A")

cmd.select ("Outward", "resi 360 & chain A", merge=1)

cmd.color ("blue", "resi 410 & chain A")

cmd.select ("Outward", "resi 410 & chain A", merge=1)

cmd.color ("blue", "resi 363 & chain A")

cmd.select ("Outward", "resi 363 & chain A", merge=1)

cmd.color ("blue", "resi 470 & chain A")

cmd.select ("Outward", "resi 470 & chain A", merge=1)

cmd.color ("blue", "resi 362 & chain A")

cmd.select ("Outward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 365 & chain A")

cmd.select ("Outward", "resi 365 & chain A", merge=1)

cmd.color ("blue", "resi 471 & chain A")

cmd.select ("Outward", "resi 471 & chain A", merge=1)

cmd.color ("blue", "resi 413 & chain A")

cmd.select ("Outward", "resi 413 & chain A", merge=1)

cmd.color ("blue", "resi 412 & chain A")

cmd.select ("Outward", "resi 412 & chain A", merge=1)

cmd.color ("blue", "resi 364 & chain A")

cmd.select ("Outward", "resi 364 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("blue", "resi 367 & chain A")

cmd.select ("Outward", "resi 367 & chain A", merge=1)

cmd.color ("blue", "resi 472 & chain A")

cmd.select ("Outward", "resi 472 & chain A", merge=1)

cmd.color ("blue", "resi 414 & chain A")

cmd.select ("Outward", "resi 414 & chain A", merge=1)

cmd.color ("blue", "resi 473 & chain A")

cmd.select ("Outward", "resi 473 & chain A", merge=1)

cmd.color ("blue", "resi 415 & chain A")

cmd.select ("Outward", "resi 415 & chain A", merge=1)

cmd.color ("blue", "resi 369 & chain A")

cmd.select ("Outward", "resi 369 & chain A", merge=1)

cmd.color ("blue", "resi 368 & chain A")

cmd.select ("Outward", "resi 368 & chain A", merge=1)

cmd.color ("blue", "resi 417 & chain A")

cmd.select ("Outward", "resi 417 & chain A", merge=1)

cmd.color ("blue", "resi 416 & chain A")

cmd.select ("Outward", "resi 416 & chain A", merge=1)

cmd.color ("blue", "resi 474 & chain A")

cmd.select ("Outward", "resi 474 & chain A", merge=1)

cmd.color ("blue", "resi 370 & chain A")

cmd.select ("Outward", "resi 370 & chain A", merge=1)

cmd.color ("blue", "resi 475 & chain A")

cmd.select ("Outward", "resi 475 & chain A", merge=1)

cmd.color ("blue", "resi 371 & chain A")

cmd.select ("Outward", "resi 371 & chain A", merge=1)

cmd.color ("blue", "resi 418 & chain A")

cmd.select ("Outward", "resi 418 & chain A", merge=1)

cmd.color ("blue", "resi 419 & chain A")

cmd.select ("Outward", "resi 419 & chain A", merge=1)

cmd.color ("blue", "resi 476 & chain A")

cmd.select ("Outward", "resi 476 & chain A", merge=1)

cmd.color ("blue", "resi 420 & chain A")

cmd.select ("Outward", "resi 420 & chain A", merge=1)

cmd.color ("blue", "resi 477 & chain A")

cmd.select ("Outward", "resi 477 & chain A", merge=1)

cmd.color ("blue", "resi 421 & chain A")

cmd.select ("Outward", "resi 421 & chain A", merge=1)

cmd.color ("blue", "resi 422 & chain A")

cmd.select ("Outward", "resi 422 & chain A", merge=1)

cmd.color ("blue", "resi 423 & chain A")

cmd.select ("Outward", "resi 423 & chain A", merge=1)

cmd.color ("blue", "resi 579 & chain A")

cmd.select ("Outward", "resi 579 & chain A", merge=1)

cmd.color ("blue", "resi 580 & chain A")

cmd.select ("Outward", "resi 580 & chain A", merge=1)

cmd.color ("blue", "resi 581 & chain A")

cmd.select ("Outward", "resi 581 & chain A", merge=1)

cmd.color ("blue", "resi 582 & chain A")

cmd.select ("Outward", "resi 582 & chain A", merge=1)

cmd.color ("blue", "resi 583 & chain A")

cmd.select ("Outward", "resi 583 & chain A", merge=1)

cmd.color ("blue", "resi 584 & chain A")

cmd.select ("Outward", "resi 584 & chain A", merge=1)

cmd.color ("blue", "resi 585 & chain A")

cmd.select ("Outward", "resi 585 & chain A", merge=1)

cmd.color ("blue", "resi 586 & chain A")

cmd.select ("Outward", "resi 586 & chain A", merge=1)

cmd.color ("blue", "resi 587 & chain A")

cmd.select ("Outward", "resi 587 & chain A", merge=1)

cmd.color ("blue", "resi 588 & chain A")

cmd.select ("Outward", "resi 588 & chain A", merge=1)

cmd.color ("blue", "resi 589 & chain A")

cmd.select ("Outward", "resi 589 & chain A", merge=1)

cmd.color ("blue", "resi 590 & chain A")

cmd.select ("Outward", "resi 590 & chain A", merge=1)

cmd.color ("blue", "resi 591 & chain A")

cmd.select ("Outward", "resi 591 & chain A", merge=1)

cmd.color ("blue", "resi 592 & chain A")

cmd.select ("Outward", "resi 592 & chain A", merge=1)

cmd.color ("blue", "resi 593 & chain A")

cmd.select ("Outward", "resi 593 & chain A", merge=1)

cmd.color ("blue", "resi 604 & chain A")

cmd.select ("Outward", "resi 604 & chain A", merge=1)

cmd.color ("blue", "resi 605 & chain A")

cmd.select ("Outward", "resi 605 & chain A", merge=1)

cmd.color ("blue", "resi 606 & chain A")

cmd.select ("Outward", "resi 606 & chain A", merge=1)

cmd.color ("blue", "resi 607 & chain A")

cmd.select ("Outward", "resi 607 & chain A", merge=1)

cmd.color ("blue", "resi 608 & chain A")

cmd.select ("Outward", "resi 608 & chain A", merge=1)

cmd.color ("blue", "resi 609 & chain A")

cmd.select ("Outward", "resi 609 & chain A", merge=1)

cmd.color ("blue", "resi 610 & chain A")

cmd.select ("Outward", "resi 610 & chain A", merge=1)

cmd.color ("blue", "resi 611 & chain A")

cmd.select ("Outward", "resi 611 & chain A", merge=1)

cmd.color ("blue", "resi 612 & chain A")

cmd.select ("Outward", "resi 612 & chain A", merge=1)

cmd.color ("blue", "resi 613 & chain A")

cmd.select ("Outward", "resi 613 & chain A", merge=1)

cmd.color ("blue", "resi 614 & chain A")

cmd.select ("Outward", "resi 614 & chain A", merge=1)

cmd.color ("blue", "resi 615 & chain A")

cmd.select ("Outward", "resi 615 & chain A", merge=1)

cmd.color ("blue", "resi 616 & chain A")

cmd.select ("Outward", "resi 616 & chain A", merge=1)

cmd.color ("blue", "resi 617 & chain A")

cmd.select ("Outward", "resi 617 & chain A", merge=1)

cmd.color ("blue", "resi 634 & chain A")

cmd.select ("Outward", "resi 634 & chain A", merge=1)

cmd.color ("blue", "resi 635 & chain A")

cmd.select ("Outward", "resi 635 & chain A", merge=1)

cmd.color ("blue", "resi 636 & chain A")

cmd.select ("Outward", "resi 636 & chain A", merge=1)

cmd.color ("blue", "resi 637 & chain A")

cmd.select ("Outward", "resi 637 & chain A", merge=1)

cmd.color ("blue", "resi 638 & chain A")

cmd.select ("Outward", "resi 638 & chain A", merge=1)

cmd.color ("blue", "resi 639 & chain A")

cmd.select ("Outward", "resi 639 & chain A", merge=1)

cmd.color ("blue", "resi 640 & chain A")

cmd.select ("Outward", "resi 640 & chain A", merge=1)

cmd.color ("blue", "resi 641 & chain A")

cmd.select ("Outward", "resi 641 & chain A", merge=1)

cmd.color ("blue", "resi 642 & chain A")

cmd.select ("Outward", "resi 642 & chain A", merge=1)

cmd.color ("blue", "resi 647 & chain A")

cmd.select ("Outward", "resi 647 & chain A", merge=1)

cmd.color ("blue", "resi 648 & chain A")

cmd.select ("Outward", "resi 648 & chain A", merge=1)

cmd.color ("blue", "resi 649 & chain A")

cmd.select ("Outward", "resi 649 & chain A", merge=1)

cmd.color ("blue", "resi 650 & chain A")

cmd.select ("Outward", "resi 650 & chain A", merge=1)

cmd.color ("blue", "resi 651 & chain A")

cmd.select ("Outward", "resi 651 & chain A", merge=1)

cmd.color ("blue", "resi 652 & chain A")

cmd.select ("Outward", "resi 652 & chain A", merge=1)

cmd.color ("blue", "resi 653 & chain A")

cmd.select ("Outward", "resi 653 & chain A", merge=1)

cmd.color ("blue", "resi 654 & chain A")

cmd.select ("Outward", "resi 654 & chain A", merge=1)

cmd.color ("blue", "resi 655 & chain A")

cmd.select ("Outward", "resi 655 & chain A", merge=1)

cmd.color ("blue", "resi 656 & chain A")

cmd.select ("Outward", "resi 656 & chain A", merge=1)

cmd.color ("blue", "resi 681 & chain A")

cmd.select ("Outward", "resi 681 & chain A", merge=1)

cmd.color ("blue", "resi 682 & chain A")

cmd.select ("Outward", "resi 682 & chain A", merge=1)

cmd.color ("blue", "resi 683 & chain A")

cmd.select ("Outward", "resi 683 & chain A", merge=1)

cmd.color ("blue", "resi 684 & chain A")

cmd.select ("Outward", "resi 684 & chain A", merge=1)

cmd.color ("blue", "resi 685 & chain A")

cmd.select ("Outward", "resi 685 & chain A", merge=1)

cmd.color ("blue", "resi 686 & chain A")

cmd.select ("Outward", "resi 686 & chain A", merge=1)

cmd.color ("blue", "resi 687 & chain A")

cmd.select ("Outward", "resi 687 & chain A", merge=1)

cmd.color ("blue", "resi 688 & chain A")

cmd.select ("Outward", "resi 688 & chain A", merge=1)

cmd.color ("blue", "resi 689 & chain A")

cmd.select ("Outward", "resi 689 & chain A", merge=1)

cmd.color ("blue", "resi 690 & chain A")

cmd.select ("Outward", "resi 690 & chain A", merge=1)

cmd.color ("blue", "resi 691 & chain A")

cmd.select ("Outward", "resi 691 & chain A", merge=1)

cmd.color ("blue", "resi 700 & chain A")

cmd.select ("Outward", "resi 700 & chain A", merge=1)

cmd.color ("blue", "resi 701 & chain A")

cmd.select ("Outward", "resi 701 & chain A", merge=1)

cmd.color ("blue", "resi 702 & chain A")

cmd.select ("Outward", "resi 702 & chain A", merge=1)

cmd.color ("blue", "resi 703 & chain A")

cmd.select ("Outward", "resi 703 & chain A", merge=1)

cmd.color ("blue", "resi 704 & chain A")

cmd.select ("Outward", "resi 704 & chain A", merge=1)

cmd.color ("blue", "resi 705 & chain A")

cmd.select ("Outward", "resi 705 & chain A", merge=1)

cmd.color ("blue", "resi 706 & chain A")

cmd.select ("Outward", "resi 706 & chain A", merge=1)

cmd.color ("blue", "resi 732 & chain A")

cmd.select ("Outward", "resi 732 & chain A", merge=1)

cmd.color ("blue", "resi 733 & chain A")

cmd.select ("Outward", "resi 733 & chain A", merge=1)

cmd.color ("blue", "resi 734 & chain A")

cmd.select ("Outward", "resi 734 & chain A", merge=1)

cmd.color ("blue", "resi 735 & chain A")

cmd.select ("Outward", "resi 735 & chain A", merge=1)

cmd.color ("blue", "resi 736 & chain A")

cmd.select ("Outward", "resi 736 & chain A", merge=1)

cmd.color ("blue", "resi 737 & chain A")

cmd.select ("Outward", "resi 737 & chain A", merge=1)

cmd.color ("blue", "resi 738 & chain A")

cmd.select ("Outward", "resi 738 & chain A", merge=1)

cmd.color ("blue", "resi 739 & chain A")

cmd.select ("Outward", "resi 739 & chain A", merge=1)

cmd.color ("blue", "resi 740 & chain A")

cmd.select ("Outward", "resi 740 & chain A", merge=1)

cmd.load_cgo( [9.0, 18.298643,3.264143,39.996494, 13.834071, 9.537643, 11.283857, 1, 1,1,0,0,0,1], "axis" )
