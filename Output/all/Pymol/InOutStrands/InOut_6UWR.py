from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Hstrand261", "resi 300+301+302+303+304+305+306+307+308+309+310 & chain H ")


cmd.select("Hstrand262", "resi 322+323+324+325+326+327+328+329+330 & chain H ")


cmd.select("Hstrand264", "resi 362+363+364+365+366+367 & chain H ")


cmd.select("Hstrand265", "resi 387+388+389+390+391+392+393+394+395+396+397 & chain H ")


cmd.select("Hstrand270", "resi 460+461+462 & chain H ")


cmd.select("Hstrand271", "resi 477+478+479+480+481+482+483+484+485+486 & chain H ")


cmd.select("Hstrand266", "resi 404+405+406+407+408+409+410+411+412+413 & chain H ")


cmd.select("Hstrand267", "resi 418+419+420+421+422+423 & chain H ")


cmd.select("barrel", "Hstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 300 & chain H")

cmd.select ("Outward", "resi 300 & chain H", merge=1)

cmd.color ("blue", "resi 301 & chain H")

cmd.select ("Outward", "resi 301 & chain H", merge=1)

cmd.color ("blue", "resi 302 & chain H")

cmd.select ("Outward", "resi 302 & chain H", merge=1)

cmd.color ("blue", "resi 303 & chain H")

cmd.select ("Outward", "resi 303 & chain H", merge=1)

cmd.color ("blue", "resi 304 & chain H")

cmd.select ("Outward", "resi 304 & chain H", merge=1)

cmd.color ("blue", "resi 305 & chain H")

cmd.select ("Outward", "resi 305 & chain H", merge=1)

cmd.color ("blue", "resi 306 & chain H")

cmd.select ("Outward", "resi 306 & chain H", merge=1)

cmd.color ("blue", "resi 307 & chain H")

cmd.select ("Outward", "resi 307 & chain H", merge=1)

cmd.color ("blue", "resi 308 & chain H")

cmd.select ("Outward", "resi 308 & chain H", merge=1)

cmd.color ("blue", "resi 309 & chain H")

cmd.select ("Outward", "resi 309 & chain H", merge=1)

cmd.color ("blue", "resi 310 & chain H")

cmd.select ("Outward", "resi 310 & chain H", merge=1)

cmd.color ("blue", "resi 322 & chain H")

cmd.select ("Outward", "resi 322 & chain H", merge=1)

cmd.color ("blue", "resi 323 & chain H")

cmd.select ("Outward", "resi 323 & chain H", merge=1)

cmd.color ("blue", "resi 324 & chain H")

cmd.select ("Outward", "resi 324 & chain H", merge=1)

cmd.color ("blue", "resi 325 & chain H")

cmd.select ("Outward", "resi 325 & chain H", merge=1)

cmd.color ("blue", "resi 326 & chain H")

cmd.select ("Outward", "resi 326 & chain H", merge=1)

cmd.color ("blue", "resi 327 & chain H")

cmd.select ("Outward", "resi 327 & chain H", merge=1)

cmd.color ("blue", "resi 328 & chain H")

cmd.select ("Outward", "resi 328 & chain H", merge=1)

cmd.color ("blue", "resi 329 & chain H")

cmd.select ("Outward", "resi 329 & chain H", merge=1)

cmd.color ("blue", "resi 330 & chain H")

cmd.select ("Outward", "resi 330 & chain H", merge=1)

cmd.color ("blue", "resi 362 & chain H")

cmd.select ("Outward", "resi 362 & chain H", merge=1)

cmd.color ("blue", "resi 363 & chain H")

cmd.select ("Outward", "resi 363 & chain H", merge=1)

cmd.color ("blue", "resi 364 & chain H")

cmd.select ("Outward", "resi 364 & chain H", merge=1)

cmd.color ("blue", "resi 365 & chain H")

cmd.select ("Outward", "resi 365 & chain H", merge=1)

cmd.color ("blue", "resi 366 & chain H")

cmd.select ("Outward", "resi 366 & chain H", merge=1)

cmd.color ("blue", "resi 367 & chain H")

cmd.select ("Outward", "resi 367 & chain H", merge=1)

cmd.color ("blue", "resi 387 & chain H")

cmd.select ("Outward", "resi 387 & chain H", merge=1)

cmd.color ("blue", "resi 388 & chain H")

cmd.select ("Outward", "resi 388 & chain H", merge=1)

cmd.color ("blue", "resi 389 & chain H")

cmd.select ("Outward", "resi 389 & chain H", merge=1)

cmd.color ("blue", "resi 390 & chain H")

cmd.select ("Outward", "resi 390 & chain H", merge=1)

cmd.color ("blue", "resi 391 & chain H")

cmd.select ("Outward", "resi 391 & chain H", merge=1)

cmd.color ("blue", "resi 392 & chain H")

cmd.select ("Outward", "resi 392 & chain H", merge=1)

cmd.color ("blue", "resi 393 & chain H")

cmd.select ("Outward", "resi 393 & chain H", merge=1)

cmd.color ("blue", "resi 394 & chain H")

cmd.select ("Outward", "resi 394 & chain H", merge=1)

cmd.color ("blue", "resi 395 & chain H")

cmd.select ("Outward", "resi 395 & chain H", merge=1)

cmd.color ("blue", "resi 396 & chain H")

cmd.select ("Outward", "resi 396 & chain H", merge=1)

cmd.color ("blue", "resi 397 & chain H")

cmd.select ("Outward", "resi 397 & chain H", merge=1)

cmd.color ("blue", "resi 460 & chain H")

cmd.select ("Outward", "resi 460 & chain H", merge=1)

cmd.color ("blue", "resi 461 & chain H")

cmd.select ("Outward", "resi 461 & chain H", merge=1)

cmd.color ("blue", "resi 462 & chain H")

cmd.select ("Outward", "resi 462 & chain H", merge=1)

cmd.color ("blue", "resi 477 & chain H")

cmd.select ("Outward", "resi 477 & chain H", merge=1)

cmd.color ("blue", "resi 478 & chain H")

cmd.select ("Outward", "resi 478 & chain H", merge=1)

cmd.color ("blue", "resi 479 & chain H")

cmd.select ("Outward", "resi 479 & chain H", merge=1)

cmd.color ("blue", "resi 480 & chain H")

cmd.select ("Outward", "resi 480 & chain H", merge=1)

cmd.color ("blue", "resi 481 & chain H")

cmd.select ("Outward", "resi 481 & chain H", merge=1)

cmd.color ("blue", "resi 482 & chain H")

cmd.select ("Outward", "resi 482 & chain H", merge=1)

cmd.color ("blue", "resi 483 & chain H")

cmd.select ("Outward", "resi 483 & chain H", merge=1)

cmd.color ("blue", "resi 484 & chain H")

cmd.select ("Outward", "resi 484 & chain H", merge=1)

cmd.color ("blue", "resi 485 & chain H")

cmd.select ("Outward", "resi 485 & chain H", merge=1)

cmd.color ("blue", "resi 486 & chain H")

cmd.select ("Outward", "resi 486 & chain H", merge=1)

cmd.color ("blue", "resi 404 & chain H")

cmd.select ("Outward", "resi 404 & chain H", merge=1)

cmd.color ("blue", "resi 405 & chain H")

cmd.select ("Outward", "resi 405 & chain H", merge=1)

cmd.color ("blue", "resi 406 & chain H")

cmd.select ("Outward", "resi 406 & chain H", merge=1)

cmd.color ("blue", "resi 407 & chain H")

cmd.select ("Outward", "resi 407 & chain H", merge=1)

cmd.color ("blue", "resi 408 & chain H")

cmd.select ("Outward", "resi 408 & chain H", merge=1)

cmd.color ("blue", "resi 409 & chain H")

cmd.select ("Outward", "resi 409 & chain H", merge=1)

cmd.color ("blue", "resi 410 & chain H")

cmd.select ("Outward", "resi 410 & chain H", merge=1)

cmd.color ("blue", "resi 411 & chain H")

cmd.select ("Outward", "resi 411 & chain H", merge=1)

cmd.color ("blue", "resi 412 & chain H")

cmd.select ("Outward", "resi 412 & chain H", merge=1)

cmd.color ("blue", "resi 413 & chain H")

cmd.select ("Outward", "resi 413 & chain H", merge=1)

cmd.color ("blue", "resi 418 & chain H")

cmd.select ("Outward", "resi 418 & chain H", merge=1)

cmd.color ("blue", "resi 419 & chain H")

cmd.select ("Outward", "resi 419 & chain H", merge=1)

cmd.color ("blue", "resi 420 & chain H")

cmd.select ("Outward", "resi 420 & chain H", merge=1)

cmd.color ("blue", "resi 421 & chain H")

cmd.select ("Outward", "resi 421 & chain H", merge=1)

cmd.color ("blue", "resi 422 & chain H")

cmd.select ("Outward", "resi 422 & chain H", merge=1)

cmd.color ("blue", "resi 423 & chain H")

cmd.select ("Outward", "resi 423 & chain H", merge=1)

cmd.load_cgo( [9.0, 241.25652,220.49483,138.306, 243.7325, 219.87434, 160.728, 1, 1,1,0,0,0,1], "axis" )
