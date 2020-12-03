from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3W9T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand18", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain A ")


cmd.select("Astrand19", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain A ")


cmd.select("Bstrand45", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain B ")


cmd.select("Bstrand44", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain B ")


cmd.select("Cstrand72", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain C ")


cmd.select("Cstrand70", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325 & chain C ")


cmd.select("Cstrand71", "resi 328+329+330+331+332 & chain C ")


cmd.select("Dstrand98", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain D ")


cmd.select("Dstrand97", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain D ")


cmd.select("Estrand124", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain E ")


cmd.select("Estrand123", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain E ")


cmd.select("Fstrand150", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain F ")


cmd.select("Fstrand149", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain F ")


cmd.select("Gstrand175", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain G ")


cmd.select("Gstrand176", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain G ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

cmd.color ("blue", "resi 311 & chain A")

cmd.select ("Outward", "resi 311 & chain A", merge=1)

cmd.color ("blue", "resi 312 & chain A")

cmd.select ("Outward", "resi 312 & chain A", merge=1)

cmd.color ("blue", "resi 313 & chain A")

cmd.select ("Outward", "resi 313 & chain A", merge=1)

cmd.color ("blue", "resi 314 & chain A")

cmd.select ("Outward", "resi 314 & chain A", merge=1)

cmd.color ("blue", "resi 315 & chain A")

cmd.select ("Outward", "resi 315 & chain A", merge=1)

cmd.color ("blue", "resi 316 & chain A")

cmd.select ("Outward", "resi 316 & chain A", merge=1)

cmd.color ("blue", "resi 317 & chain A")

cmd.select ("Outward", "resi 317 & chain A", merge=1)

cmd.color ("blue", "resi 318 & chain A")

cmd.select ("Outward", "resi 318 & chain A", merge=1)

cmd.color ("blue", "resi 319 & chain A")

cmd.select ("Outward", "resi 319 & chain A", merge=1)

cmd.color ("blue", "resi 320 & chain A")

cmd.select ("Outward", "resi 320 & chain A", merge=1)

cmd.color ("blue", "resi 321 & chain A")

cmd.select ("Outward", "resi 321 & chain A", merge=1)

cmd.color ("blue", "resi 322 & chain A")

cmd.select ("Outward", "resi 322 & chain A", merge=1)

cmd.color ("blue", "resi 323 & chain A")

cmd.select ("Outward", "resi 323 & chain A", merge=1)

cmd.color ("blue", "resi 324 & chain A")

cmd.select ("Outward", "resi 324 & chain A", merge=1)

cmd.color ("blue", "resi 325 & chain A")

cmd.select ("Outward", "resi 325 & chain A", merge=1)

cmd.color ("blue", "resi 326 & chain A")

cmd.select ("Outward", "resi 326 & chain A", merge=1)

cmd.color ("blue", "resi 327 & chain A")

cmd.select ("Outward", "resi 327 & chain A", merge=1)

cmd.color ("blue", "resi 328 & chain A")

cmd.select ("Outward", "resi 328 & chain A", merge=1)

cmd.color ("blue", "resi 329 & chain A")

cmd.select ("Outward", "resi 329 & chain A", merge=1)

cmd.color ("blue", "resi 330 & chain A")

cmd.select ("Outward", "resi 330 & chain A", merge=1)

cmd.color ("blue", "resi 331 & chain A")

cmd.select ("Outward", "resi 331 & chain A", merge=1)

cmd.color ("blue", "resi 332 & chain A")

cmd.select ("Outward", "resi 332 & chain A", merge=1)

cmd.color ("blue", "resi 337 & chain A")

cmd.select ("Outward", "resi 337 & chain A", merge=1)

cmd.color ("blue", "resi 338 & chain A")

cmd.select ("Outward", "resi 338 & chain A", merge=1)

cmd.color ("blue", "resi 339 & chain A")

cmd.select ("Outward", "resi 339 & chain A", merge=1)

cmd.color ("blue", "resi 340 & chain A")

cmd.select ("Outward", "resi 340 & chain A", merge=1)

cmd.color ("blue", "resi 341 & chain A")

cmd.select ("Outward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("blue", "resi 343 & chain A")

cmd.select ("Outward", "resi 343 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("blue", "resi 345 & chain A")

cmd.select ("Outward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("blue", "resi 347 & chain A")

cmd.select ("Outward", "resi 347 & chain A", merge=1)

cmd.color ("blue", "resi 348 & chain A")

cmd.select ("Outward", "resi 348 & chain A", merge=1)

cmd.color ("blue", "resi 349 & chain A")

cmd.select ("Outward", "resi 349 & chain A", merge=1)

cmd.color ("blue", "resi 350 & chain A")

cmd.select ("Outward", "resi 350 & chain A", merge=1)

cmd.color ("blue", "resi 351 & chain A")

cmd.select ("Outward", "resi 351 & chain A", merge=1)

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("blue", "resi 353 & chain A")

cmd.select ("Outward", "resi 353 & chain A", merge=1)

cmd.color ("blue", "resi 354 & chain A")

cmd.select ("Outward", "resi 354 & chain A", merge=1)

cmd.color ("blue", "resi 355 & chain A")

cmd.select ("Outward", "resi 355 & chain A", merge=1)

cmd.color ("blue", "resi 356 & chain A")

cmd.select ("Outward", "resi 356 & chain A", merge=1)

cmd.color ("blue", "resi 357 & chain A")

cmd.select ("Outward", "resi 357 & chain A", merge=1)

cmd.color ("blue", "resi 358 & chain A")

cmd.select ("Outward", "resi 358 & chain A", merge=1)

cmd.color ("blue", "resi 359 & chain A")

cmd.select ("Outward", "resi 359 & chain A", merge=1)

cmd.color ("blue", "resi 360 & chain A")

cmd.select ("Outward", "resi 360 & chain A", merge=1)

cmd.color ("blue", "resi 361 & chain A")

cmd.select ("Outward", "resi 361 & chain A", merge=1)

cmd.color ("blue", "resi 362 & chain A")

cmd.select ("Outward", "resi 362 & chain A", merge=1)

cmd.color ("blue", "resi 363 & chain A")

cmd.select ("Outward", "resi 363 & chain A", merge=1)

cmd.color ("blue", "resi 364 & chain A")

cmd.select ("Outward", "resi 364 & chain A", merge=1)

cmd.color ("blue", "resi 365 & chain A")

cmd.select ("Outward", "resi 365 & chain A", merge=1)

cmd.color ("blue", "resi 366 & chain A")

cmd.select ("Outward", "resi 366 & chain A", merge=1)

cmd.color ("blue", "resi 337 & chain B")

cmd.select ("Outward", "resi 337 & chain B", merge=1)

cmd.color ("blue", "resi 338 & chain B")

cmd.select ("Outward", "resi 338 & chain B", merge=1)

cmd.color ("blue", "resi 339 & chain B")

cmd.select ("Outward", "resi 339 & chain B", merge=1)

cmd.color ("blue", "resi 340 & chain B")

cmd.select ("Outward", "resi 340 & chain B", merge=1)

cmd.color ("blue", "resi 341 & chain B")

cmd.select ("Outward", "resi 341 & chain B", merge=1)

cmd.color ("blue", "resi 342 & chain B")

cmd.select ("Outward", "resi 342 & chain B", merge=1)

cmd.color ("blue", "resi 343 & chain B")

cmd.select ("Outward", "resi 343 & chain B", merge=1)

cmd.color ("blue", "resi 344 & chain B")

cmd.select ("Outward", "resi 344 & chain B", merge=1)

cmd.color ("blue", "resi 345 & chain B")

cmd.select ("Outward", "resi 345 & chain B", merge=1)

cmd.color ("blue", "resi 346 & chain B")

cmd.select ("Outward", "resi 346 & chain B", merge=1)

cmd.color ("blue", "resi 347 & chain B")

cmd.select ("Outward", "resi 347 & chain B", merge=1)

cmd.color ("blue", "resi 348 & chain B")

cmd.select ("Outward", "resi 348 & chain B", merge=1)

cmd.color ("blue", "resi 349 & chain B")

cmd.select ("Outward", "resi 349 & chain B", merge=1)

cmd.color ("blue", "resi 350 & chain B")

cmd.select ("Outward", "resi 350 & chain B", merge=1)

cmd.color ("blue", "resi 351 & chain B")

cmd.select ("Outward", "resi 351 & chain B", merge=1)

cmd.color ("blue", "resi 352 & chain B")

cmd.select ("Outward", "resi 352 & chain B", merge=1)

cmd.color ("blue", "resi 353 & chain B")

cmd.select ("Outward", "resi 353 & chain B", merge=1)

cmd.color ("blue", "resi 354 & chain B")

cmd.select ("Outward", "resi 354 & chain B", merge=1)

cmd.color ("blue", "resi 355 & chain B")

cmd.select ("Outward", "resi 355 & chain B", merge=1)

cmd.color ("blue", "resi 356 & chain B")

cmd.select ("Outward", "resi 356 & chain B", merge=1)

cmd.color ("blue", "resi 357 & chain B")

cmd.select ("Outward", "resi 357 & chain B", merge=1)

cmd.color ("blue", "resi 358 & chain B")

cmd.select ("Outward", "resi 358 & chain B", merge=1)

cmd.color ("blue", "resi 359 & chain B")

cmd.select ("Outward", "resi 359 & chain B", merge=1)

cmd.color ("blue", "resi 360 & chain B")

cmd.select ("Outward", "resi 360 & chain B", merge=1)

cmd.color ("blue", "resi 361 & chain B")

cmd.select ("Outward", "resi 361 & chain B", merge=1)

cmd.color ("blue", "resi 362 & chain B")

cmd.select ("Outward", "resi 362 & chain B", merge=1)

cmd.color ("blue", "resi 363 & chain B")

cmd.select ("Outward", "resi 363 & chain B", merge=1)

cmd.color ("blue", "resi 364 & chain B")

cmd.select ("Outward", "resi 364 & chain B", merge=1)

cmd.color ("blue", "resi 365 & chain B")

cmd.select ("Outward", "resi 365 & chain B", merge=1)

cmd.color ("blue", "resi 366 & chain B")

cmd.select ("Outward", "resi 366 & chain B", merge=1)

cmd.color ("blue", "resi 304 & chain B")

cmd.select ("Outward", "resi 304 & chain B", merge=1)

cmd.color ("blue", "resi 305 & chain B")

cmd.select ("Outward", "resi 305 & chain B", merge=1)

cmd.color ("blue", "resi 306 & chain B")

cmd.select ("Outward", "resi 306 & chain B", merge=1)

cmd.color ("blue", "resi 307 & chain B")

cmd.select ("Outward", "resi 307 & chain B", merge=1)

cmd.color ("blue", "resi 308 & chain B")

cmd.select ("Outward", "resi 308 & chain B", merge=1)

cmd.color ("blue", "resi 309 & chain B")

cmd.select ("Outward", "resi 309 & chain B", merge=1)

cmd.color ("blue", "resi 310 & chain B")

cmd.select ("Outward", "resi 310 & chain B", merge=1)

cmd.color ("blue", "resi 311 & chain B")

cmd.select ("Outward", "resi 311 & chain B", merge=1)

cmd.color ("blue", "resi 312 & chain B")

cmd.select ("Outward", "resi 312 & chain B", merge=1)

cmd.color ("blue", "resi 313 & chain B")

cmd.select ("Outward", "resi 313 & chain B", merge=1)

cmd.color ("blue", "resi 314 & chain B")

cmd.select ("Outward", "resi 314 & chain B", merge=1)

cmd.color ("blue", "resi 315 & chain B")

cmd.select ("Outward", "resi 315 & chain B", merge=1)

cmd.color ("blue", "resi 316 & chain B")

cmd.select ("Outward", "resi 316 & chain B", merge=1)

cmd.color ("blue", "resi 317 & chain B")

cmd.select ("Outward", "resi 317 & chain B", merge=1)

cmd.color ("blue", "resi 318 & chain B")

cmd.select ("Outward", "resi 318 & chain B", merge=1)

cmd.color ("blue", "resi 319 & chain B")

cmd.select ("Outward", "resi 319 & chain B", merge=1)

cmd.color ("blue", "resi 320 & chain B")

cmd.select ("Outward", "resi 320 & chain B", merge=1)

cmd.color ("blue", "resi 321 & chain B")

cmd.select ("Outward", "resi 321 & chain B", merge=1)

cmd.color ("blue", "resi 322 & chain B")

cmd.select ("Outward", "resi 322 & chain B", merge=1)

cmd.color ("blue", "resi 323 & chain B")

cmd.select ("Outward", "resi 323 & chain B", merge=1)

cmd.color ("blue", "resi 324 & chain B")

cmd.select ("Outward", "resi 324 & chain B", merge=1)

cmd.color ("blue", "resi 325 & chain B")

cmd.select ("Outward", "resi 325 & chain B", merge=1)

cmd.color ("blue", "resi 326 & chain B")

cmd.select ("Outward", "resi 326 & chain B", merge=1)

cmd.color ("blue", "resi 327 & chain B")

cmd.select ("Outward", "resi 327 & chain B", merge=1)

cmd.color ("blue", "resi 328 & chain B")

cmd.select ("Outward", "resi 328 & chain B", merge=1)

cmd.color ("blue", "resi 329 & chain B")

cmd.select ("Outward", "resi 329 & chain B", merge=1)

cmd.color ("blue", "resi 330 & chain B")

cmd.select ("Outward", "resi 330 & chain B", merge=1)

cmd.color ("blue", "resi 331 & chain B")

cmd.select ("Outward", "resi 331 & chain B", merge=1)

cmd.color ("blue", "resi 332 & chain B")

cmd.select ("Outward", "resi 332 & chain B", merge=1)

cmd.color ("blue", "resi 337 & chain C")

cmd.select ("Outward", "resi 337 & chain C", merge=1)

cmd.color ("blue", "resi 338 & chain C")

cmd.select ("Outward", "resi 338 & chain C", merge=1)

cmd.color ("blue", "resi 339 & chain C")

cmd.select ("Outward", "resi 339 & chain C", merge=1)

cmd.color ("blue", "resi 340 & chain C")

cmd.select ("Outward", "resi 340 & chain C", merge=1)

cmd.color ("blue", "resi 341 & chain C")

cmd.select ("Outward", "resi 341 & chain C", merge=1)

cmd.color ("blue", "resi 342 & chain C")

cmd.select ("Outward", "resi 342 & chain C", merge=1)

cmd.color ("blue", "resi 343 & chain C")

cmd.select ("Outward", "resi 343 & chain C", merge=1)

cmd.color ("blue", "resi 344 & chain C")

cmd.select ("Outward", "resi 344 & chain C", merge=1)

cmd.color ("blue", "resi 345 & chain C")

cmd.select ("Outward", "resi 345 & chain C", merge=1)

cmd.color ("blue", "resi 346 & chain C")

cmd.select ("Outward", "resi 346 & chain C", merge=1)

cmd.color ("blue", "resi 347 & chain C")

cmd.select ("Outward", "resi 347 & chain C", merge=1)

cmd.color ("blue", "resi 348 & chain C")

cmd.select ("Outward", "resi 348 & chain C", merge=1)

cmd.color ("blue", "resi 349 & chain C")

cmd.select ("Outward", "resi 349 & chain C", merge=1)

cmd.color ("blue", "resi 350 & chain C")

cmd.select ("Outward", "resi 350 & chain C", merge=1)

cmd.color ("blue", "resi 351 & chain C")

cmd.select ("Outward", "resi 351 & chain C", merge=1)

cmd.color ("blue", "resi 352 & chain C")

cmd.select ("Outward", "resi 352 & chain C", merge=1)

cmd.color ("blue", "resi 353 & chain C")

cmd.select ("Outward", "resi 353 & chain C", merge=1)

cmd.color ("blue", "resi 354 & chain C")

cmd.select ("Outward", "resi 354 & chain C", merge=1)

cmd.color ("blue", "resi 355 & chain C")

cmd.select ("Outward", "resi 355 & chain C", merge=1)

cmd.color ("blue", "resi 356 & chain C")

cmd.select ("Outward", "resi 356 & chain C", merge=1)

cmd.color ("blue", "resi 357 & chain C")

cmd.select ("Outward", "resi 357 & chain C", merge=1)

cmd.color ("blue", "resi 358 & chain C")

cmd.select ("Outward", "resi 358 & chain C", merge=1)

cmd.color ("blue", "resi 359 & chain C")

cmd.select ("Outward", "resi 359 & chain C", merge=1)

cmd.color ("blue", "resi 360 & chain C")

cmd.select ("Outward", "resi 360 & chain C", merge=1)

cmd.color ("blue", "resi 361 & chain C")

cmd.select ("Outward", "resi 361 & chain C", merge=1)

cmd.color ("blue", "resi 362 & chain C")

cmd.select ("Outward", "resi 362 & chain C", merge=1)

cmd.color ("blue", "resi 363 & chain C")

cmd.select ("Outward", "resi 363 & chain C", merge=1)

cmd.color ("blue", "resi 364 & chain C")

cmd.select ("Outward", "resi 364 & chain C", merge=1)

cmd.color ("blue", "resi 365 & chain C")

cmd.select ("Outward", "resi 365 & chain C", merge=1)

cmd.color ("blue", "resi 366 & chain C")

cmd.select ("Outward", "resi 366 & chain C", merge=1)

cmd.color ("blue", "resi 304 & chain C")

cmd.select ("Outward", "resi 304 & chain C", merge=1)

cmd.color ("blue", "resi 305 & chain C")

cmd.select ("Outward", "resi 305 & chain C", merge=1)

cmd.color ("blue", "resi 306 & chain C")

cmd.select ("Outward", "resi 306 & chain C", merge=1)

cmd.color ("blue", "resi 307 & chain C")

cmd.select ("Outward", "resi 307 & chain C", merge=1)

cmd.color ("blue", "resi 308 & chain C")

cmd.select ("Outward", "resi 308 & chain C", merge=1)

cmd.color ("blue", "resi 309 & chain C")

cmd.select ("Outward", "resi 309 & chain C", merge=1)

cmd.color ("blue", "resi 310 & chain C")

cmd.select ("Outward", "resi 310 & chain C", merge=1)

cmd.color ("blue", "resi 311 & chain C")

cmd.select ("Outward", "resi 311 & chain C", merge=1)

cmd.color ("blue", "resi 312 & chain C")

cmd.select ("Outward", "resi 312 & chain C", merge=1)

cmd.color ("blue", "resi 313 & chain C")

cmd.select ("Outward", "resi 313 & chain C", merge=1)

cmd.color ("blue", "resi 314 & chain C")

cmd.select ("Outward", "resi 314 & chain C", merge=1)

cmd.color ("blue", "resi 315 & chain C")

cmd.select ("Outward", "resi 315 & chain C", merge=1)

cmd.color ("blue", "resi 316 & chain C")

cmd.select ("Outward", "resi 316 & chain C", merge=1)

cmd.color ("blue", "resi 317 & chain C")

cmd.select ("Outward", "resi 317 & chain C", merge=1)

cmd.color ("blue", "resi 318 & chain C")

cmd.select ("Outward", "resi 318 & chain C", merge=1)

cmd.color ("blue", "resi 319 & chain C")

cmd.select ("Outward", "resi 319 & chain C", merge=1)

cmd.color ("blue", "resi 320 & chain C")

cmd.select ("Outward", "resi 320 & chain C", merge=1)

cmd.color ("blue", "resi 321 & chain C")

cmd.select ("Outward", "resi 321 & chain C", merge=1)

cmd.color ("blue", "resi 322 & chain C")

cmd.select ("Outward", "resi 322 & chain C", merge=1)

cmd.color ("blue", "resi 323 & chain C")

cmd.select ("Outward", "resi 323 & chain C", merge=1)

cmd.color ("blue", "resi 324 & chain C")

cmd.select ("Outward", "resi 324 & chain C", merge=1)

cmd.color ("blue", "resi 325 & chain C")

cmd.select ("Outward", "resi 325 & chain C", merge=1)

cmd.color ("blue", "resi 328 & chain C")

cmd.select ("Outward", "resi 328 & chain C", merge=1)

cmd.color ("blue", "resi 329 & chain C")

cmd.select ("Outward", "resi 329 & chain C", merge=1)

cmd.color ("blue", "resi 330 & chain C")

cmd.select ("Outward", "resi 330 & chain C", merge=1)

cmd.color ("blue", "resi 331 & chain C")

cmd.select ("Outward", "resi 331 & chain C", merge=1)

cmd.color ("blue", "resi 332 & chain C")

cmd.select ("Outward", "resi 332 & chain C", merge=1)

cmd.color ("blue", "resi 337 & chain D")

cmd.select ("Outward", "resi 337 & chain D", merge=1)

cmd.color ("blue", "resi 338 & chain D")

cmd.select ("Outward", "resi 338 & chain D", merge=1)

cmd.color ("blue", "resi 339 & chain D")

cmd.select ("Outward", "resi 339 & chain D", merge=1)

cmd.color ("blue", "resi 340 & chain D")

cmd.select ("Outward", "resi 340 & chain D", merge=1)

cmd.color ("blue", "resi 341 & chain D")

cmd.select ("Outward", "resi 341 & chain D", merge=1)

cmd.color ("blue", "resi 342 & chain D")

cmd.select ("Outward", "resi 342 & chain D", merge=1)

cmd.color ("blue", "resi 343 & chain D")

cmd.select ("Outward", "resi 343 & chain D", merge=1)

cmd.color ("blue", "resi 344 & chain D")

cmd.select ("Outward", "resi 344 & chain D", merge=1)

cmd.color ("blue", "resi 345 & chain D")

cmd.select ("Outward", "resi 345 & chain D", merge=1)

cmd.color ("blue", "resi 346 & chain D")

cmd.select ("Outward", "resi 346 & chain D", merge=1)

cmd.color ("blue", "resi 347 & chain D")

cmd.select ("Outward", "resi 347 & chain D", merge=1)

cmd.color ("blue", "resi 348 & chain D")

cmd.select ("Outward", "resi 348 & chain D", merge=1)

cmd.color ("blue", "resi 349 & chain D")

cmd.select ("Outward", "resi 349 & chain D", merge=1)

cmd.color ("blue", "resi 350 & chain D")

cmd.select ("Outward", "resi 350 & chain D", merge=1)

cmd.color ("blue", "resi 351 & chain D")

cmd.select ("Outward", "resi 351 & chain D", merge=1)

cmd.color ("blue", "resi 352 & chain D")

cmd.select ("Outward", "resi 352 & chain D", merge=1)

cmd.color ("blue", "resi 353 & chain D")

cmd.select ("Outward", "resi 353 & chain D", merge=1)

cmd.color ("blue", "resi 354 & chain D")

cmd.select ("Outward", "resi 354 & chain D", merge=1)

cmd.color ("blue", "resi 355 & chain D")

cmd.select ("Outward", "resi 355 & chain D", merge=1)

cmd.color ("blue", "resi 356 & chain D")

cmd.select ("Outward", "resi 356 & chain D", merge=1)

cmd.color ("blue", "resi 357 & chain D")

cmd.select ("Outward", "resi 357 & chain D", merge=1)

cmd.color ("blue", "resi 358 & chain D")

cmd.select ("Outward", "resi 358 & chain D", merge=1)

cmd.color ("blue", "resi 359 & chain D")

cmd.select ("Outward", "resi 359 & chain D", merge=1)

cmd.color ("blue", "resi 360 & chain D")

cmd.select ("Outward", "resi 360 & chain D", merge=1)

cmd.color ("blue", "resi 361 & chain D")

cmd.select ("Outward", "resi 361 & chain D", merge=1)

cmd.color ("blue", "resi 362 & chain D")

cmd.select ("Outward", "resi 362 & chain D", merge=1)

cmd.color ("blue", "resi 363 & chain D")

cmd.select ("Outward", "resi 363 & chain D", merge=1)

cmd.color ("blue", "resi 364 & chain D")

cmd.select ("Outward", "resi 364 & chain D", merge=1)

cmd.color ("blue", "resi 365 & chain D")

cmd.select ("Outward", "resi 365 & chain D", merge=1)

cmd.color ("blue", "resi 366 & chain D")

cmd.select ("Outward", "resi 366 & chain D", merge=1)

cmd.color ("blue", "resi 304 & chain D")

cmd.select ("Outward", "resi 304 & chain D", merge=1)

cmd.color ("blue", "resi 305 & chain D")

cmd.select ("Outward", "resi 305 & chain D", merge=1)

cmd.color ("blue", "resi 306 & chain D")

cmd.select ("Outward", "resi 306 & chain D", merge=1)

cmd.color ("blue", "resi 307 & chain D")

cmd.select ("Outward", "resi 307 & chain D", merge=1)

cmd.color ("blue", "resi 308 & chain D")

cmd.select ("Outward", "resi 308 & chain D", merge=1)

cmd.color ("blue", "resi 309 & chain D")

cmd.select ("Outward", "resi 309 & chain D", merge=1)

cmd.color ("blue", "resi 310 & chain D")

cmd.select ("Outward", "resi 310 & chain D", merge=1)

cmd.color ("blue", "resi 311 & chain D")

cmd.select ("Outward", "resi 311 & chain D", merge=1)

cmd.color ("blue", "resi 312 & chain D")

cmd.select ("Outward", "resi 312 & chain D", merge=1)

cmd.color ("blue", "resi 313 & chain D")

cmd.select ("Outward", "resi 313 & chain D", merge=1)

cmd.color ("blue", "resi 314 & chain D")

cmd.select ("Outward", "resi 314 & chain D", merge=1)

cmd.color ("blue", "resi 315 & chain D")

cmd.select ("Outward", "resi 315 & chain D", merge=1)

cmd.color ("blue", "resi 316 & chain D")

cmd.select ("Outward", "resi 316 & chain D", merge=1)

cmd.color ("blue", "resi 317 & chain D")

cmd.select ("Outward", "resi 317 & chain D", merge=1)

cmd.color ("blue", "resi 318 & chain D")

cmd.select ("Outward", "resi 318 & chain D", merge=1)

cmd.color ("blue", "resi 319 & chain D")

cmd.select ("Outward", "resi 319 & chain D", merge=1)

cmd.color ("blue", "resi 320 & chain D")

cmd.select ("Outward", "resi 320 & chain D", merge=1)

cmd.color ("blue", "resi 321 & chain D")

cmd.select ("Outward", "resi 321 & chain D", merge=1)

cmd.color ("blue", "resi 322 & chain D")

cmd.select ("Outward", "resi 322 & chain D", merge=1)

cmd.color ("blue", "resi 323 & chain D")

cmd.select ("Outward", "resi 323 & chain D", merge=1)

cmd.color ("blue", "resi 324 & chain D")

cmd.select ("Outward", "resi 324 & chain D", merge=1)

cmd.color ("blue", "resi 325 & chain D")

cmd.select ("Outward", "resi 325 & chain D", merge=1)

cmd.color ("blue", "resi 326 & chain D")

cmd.select ("Outward", "resi 326 & chain D", merge=1)

cmd.color ("blue", "resi 327 & chain D")

cmd.select ("Outward", "resi 327 & chain D", merge=1)

cmd.color ("blue", "resi 328 & chain D")

cmd.select ("Outward", "resi 328 & chain D", merge=1)

cmd.color ("blue", "resi 329 & chain D")

cmd.select ("Outward", "resi 329 & chain D", merge=1)

cmd.color ("blue", "resi 330 & chain D")

cmd.select ("Outward", "resi 330 & chain D", merge=1)

cmd.color ("blue", "resi 331 & chain D")

cmd.select ("Outward", "resi 331 & chain D", merge=1)

cmd.color ("blue", "resi 332 & chain D")

cmd.select ("Outward", "resi 332 & chain D", merge=1)

cmd.color ("blue", "resi 337 & chain E")

cmd.select ("Outward", "resi 337 & chain E", merge=1)

cmd.color ("blue", "resi 338 & chain E")

cmd.select ("Outward", "resi 338 & chain E", merge=1)

cmd.color ("blue", "resi 339 & chain E")

cmd.select ("Outward", "resi 339 & chain E", merge=1)

cmd.color ("blue", "resi 340 & chain E")

cmd.select ("Outward", "resi 340 & chain E", merge=1)

cmd.color ("blue", "resi 341 & chain E")

cmd.select ("Outward", "resi 341 & chain E", merge=1)

cmd.color ("blue", "resi 342 & chain E")

cmd.select ("Outward", "resi 342 & chain E", merge=1)

cmd.color ("blue", "resi 343 & chain E")

cmd.select ("Outward", "resi 343 & chain E", merge=1)

cmd.color ("blue", "resi 344 & chain E")

cmd.select ("Outward", "resi 344 & chain E", merge=1)

cmd.color ("blue", "resi 345 & chain E")

cmd.select ("Outward", "resi 345 & chain E", merge=1)

cmd.color ("blue", "resi 346 & chain E")

cmd.select ("Outward", "resi 346 & chain E", merge=1)

cmd.color ("blue", "resi 347 & chain E")

cmd.select ("Outward", "resi 347 & chain E", merge=1)

cmd.color ("blue", "resi 348 & chain E")

cmd.select ("Outward", "resi 348 & chain E", merge=1)

cmd.color ("blue", "resi 349 & chain E")

cmd.select ("Outward", "resi 349 & chain E", merge=1)

cmd.color ("blue", "resi 350 & chain E")

cmd.select ("Outward", "resi 350 & chain E", merge=1)

cmd.color ("blue", "resi 351 & chain E")

cmd.select ("Outward", "resi 351 & chain E", merge=1)

cmd.color ("blue", "resi 352 & chain E")

cmd.select ("Outward", "resi 352 & chain E", merge=1)

cmd.color ("blue", "resi 353 & chain E")

cmd.select ("Outward", "resi 353 & chain E", merge=1)

cmd.color ("blue", "resi 354 & chain E")

cmd.select ("Outward", "resi 354 & chain E", merge=1)

cmd.color ("blue", "resi 355 & chain E")

cmd.select ("Outward", "resi 355 & chain E", merge=1)

cmd.color ("blue", "resi 356 & chain E")

cmd.select ("Outward", "resi 356 & chain E", merge=1)

cmd.color ("blue", "resi 357 & chain E")

cmd.select ("Outward", "resi 357 & chain E", merge=1)

cmd.color ("blue", "resi 358 & chain E")

cmd.select ("Outward", "resi 358 & chain E", merge=1)

cmd.color ("blue", "resi 359 & chain E")

cmd.select ("Outward", "resi 359 & chain E", merge=1)

cmd.color ("blue", "resi 360 & chain E")

cmd.select ("Outward", "resi 360 & chain E", merge=1)

cmd.color ("blue", "resi 361 & chain E")

cmd.select ("Outward", "resi 361 & chain E", merge=1)

cmd.color ("blue", "resi 362 & chain E")

cmd.select ("Outward", "resi 362 & chain E", merge=1)

cmd.color ("blue", "resi 363 & chain E")

cmd.select ("Outward", "resi 363 & chain E", merge=1)

cmd.color ("blue", "resi 364 & chain E")

cmd.select ("Outward", "resi 364 & chain E", merge=1)

cmd.color ("blue", "resi 365 & chain E")

cmd.select ("Outward", "resi 365 & chain E", merge=1)

cmd.color ("blue", "resi 366 & chain E")

cmd.select ("Outward", "resi 366 & chain E", merge=1)

cmd.color ("blue", "resi 304 & chain E")

cmd.select ("Outward", "resi 304 & chain E", merge=1)

cmd.color ("blue", "resi 305 & chain E")

cmd.select ("Outward", "resi 305 & chain E", merge=1)

cmd.color ("blue", "resi 306 & chain E")

cmd.select ("Outward", "resi 306 & chain E", merge=1)

cmd.color ("blue", "resi 307 & chain E")

cmd.select ("Outward", "resi 307 & chain E", merge=1)

cmd.color ("blue", "resi 308 & chain E")

cmd.select ("Outward", "resi 308 & chain E", merge=1)

cmd.color ("blue", "resi 309 & chain E")

cmd.select ("Outward", "resi 309 & chain E", merge=1)

cmd.color ("blue", "resi 310 & chain E")

cmd.select ("Outward", "resi 310 & chain E", merge=1)

cmd.color ("blue", "resi 311 & chain E")

cmd.select ("Outward", "resi 311 & chain E", merge=1)

cmd.color ("blue", "resi 312 & chain E")

cmd.select ("Outward", "resi 312 & chain E", merge=1)

cmd.color ("blue", "resi 313 & chain E")

cmd.select ("Outward", "resi 313 & chain E", merge=1)

cmd.color ("blue", "resi 314 & chain E")

cmd.select ("Outward", "resi 314 & chain E", merge=1)

cmd.color ("blue", "resi 315 & chain E")

cmd.select ("Outward", "resi 315 & chain E", merge=1)

cmd.color ("blue", "resi 316 & chain E")

cmd.select ("Outward", "resi 316 & chain E", merge=1)

cmd.color ("blue", "resi 317 & chain E")

cmd.select ("Outward", "resi 317 & chain E", merge=1)

cmd.color ("blue", "resi 318 & chain E")

cmd.select ("Outward", "resi 318 & chain E", merge=1)

cmd.color ("blue", "resi 319 & chain E")

cmd.select ("Outward", "resi 319 & chain E", merge=1)

cmd.color ("blue", "resi 320 & chain E")

cmd.select ("Outward", "resi 320 & chain E", merge=1)

cmd.color ("blue", "resi 321 & chain E")

cmd.select ("Outward", "resi 321 & chain E", merge=1)

cmd.color ("blue", "resi 322 & chain E")

cmd.select ("Outward", "resi 322 & chain E", merge=1)

cmd.color ("blue", "resi 323 & chain E")

cmd.select ("Outward", "resi 323 & chain E", merge=1)

cmd.color ("blue", "resi 324 & chain E")

cmd.select ("Outward", "resi 324 & chain E", merge=1)

cmd.color ("blue", "resi 325 & chain E")

cmd.select ("Outward", "resi 325 & chain E", merge=1)

cmd.color ("blue", "resi 326 & chain E")

cmd.select ("Outward", "resi 326 & chain E", merge=1)

cmd.color ("blue", "resi 327 & chain E")

cmd.select ("Outward", "resi 327 & chain E", merge=1)

cmd.color ("blue", "resi 328 & chain E")

cmd.select ("Outward", "resi 328 & chain E", merge=1)

cmd.color ("blue", "resi 329 & chain E")

cmd.select ("Outward", "resi 329 & chain E", merge=1)

cmd.color ("blue", "resi 330 & chain E")

cmd.select ("Outward", "resi 330 & chain E", merge=1)

cmd.color ("blue", "resi 331 & chain E")

cmd.select ("Outward", "resi 331 & chain E", merge=1)

cmd.color ("blue", "resi 332 & chain E")

cmd.select ("Outward", "resi 332 & chain E", merge=1)

cmd.color ("blue", "resi 337 & chain F")

cmd.select ("Outward", "resi 337 & chain F", merge=1)

cmd.color ("blue", "resi 338 & chain F")

cmd.select ("Outward", "resi 338 & chain F", merge=1)

cmd.color ("blue", "resi 339 & chain F")

cmd.select ("Outward", "resi 339 & chain F", merge=1)

cmd.color ("blue", "resi 340 & chain F")

cmd.select ("Outward", "resi 340 & chain F", merge=1)

cmd.color ("blue", "resi 341 & chain F")

cmd.select ("Outward", "resi 341 & chain F", merge=1)

cmd.color ("blue", "resi 342 & chain F")

cmd.select ("Outward", "resi 342 & chain F", merge=1)

cmd.color ("blue", "resi 343 & chain F")

cmd.select ("Outward", "resi 343 & chain F", merge=1)

cmd.color ("blue", "resi 344 & chain F")

cmd.select ("Outward", "resi 344 & chain F", merge=1)

cmd.color ("blue", "resi 345 & chain F")

cmd.select ("Outward", "resi 345 & chain F", merge=1)

cmd.color ("blue", "resi 346 & chain F")

cmd.select ("Outward", "resi 346 & chain F", merge=1)

cmd.color ("blue", "resi 347 & chain F")

cmd.select ("Outward", "resi 347 & chain F", merge=1)

cmd.color ("blue", "resi 348 & chain F")

cmd.select ("Outward", "resi 348 & chain F", merge=1)

cmd.color ("blue", "resi 349 & chain F")

cmd.select ("Outward", "resi 349 & chain F", merge=1)

cmd.color ("blue", "resi 350 & chain F")

cmd.select ("Outward", "resi 350 & chain F", merge=1)

cmd.color ("blue", "resi 351 & chain F")

cmd.select ("Outward", "resi 351 & chain F", merge=1)

cmd.color ("blue", "resi 352 & chain F")

cmd.select ("Outward", "resi 352 & chain F", merge=1)

cmd.color ("blue", "resi 353 & chain F")

cmd.select ("Outward", "resi 353 & chain F", merge=1)

cmd.color ("blue", "resi 354 & chain F")

cmd.select ("Outward", "resi 354 & chain F", merge=1)

cmd.color ("blue", "resi 355 & chain F")

cmd.select ("Outward", "resi 355 & chain F", merge=1)

cmd.color ("blue", "resi 356 & chain F")

cmd.select ("Outward", "resi 356 & chain F", merge=1)

cmd.color ("blue", "resi 357 & chain F")

cmd.select ("Outward", "resi 357 & chain F", merge=1)

cmd.color ("blue", "resi 358 & chain F")

cmd.select ("Outward", "resi 358 & chain F", merge=1)

cmd.color ("blue", "resi 359 & chain F")

cmd.select ("Outward", "resi 359 & chain F", merge=1)

cmd.color ("blue", "resi 360 & chain F")

cmd.select ("Outward", "resi 360 & chain F", merge=1)

cmd.color ("blue", "resi 361 & chain F")

cmd.select ("Outward", "resi 361 & chain F", merge=1)

cmd.color ("blue", "resi 362 & chain F")

cmd.select ("Outward", "resi 362 & chain F", merge=1)

cmd.color ("blue", "resi 363 & chain F")

cmd.select ("Outward", "resi 363 & chain F", merge=1)

cmd.color ("blue", "resi 364 & chain F")

cmd.select ("Outward", "resi 364 & chain F", merge=1)

cmd.color ("blue", "resi 365 & chain F")

cmd.select ("Outward", "resi 365 & chain F", merge=1)

cmd.color ("blue", "resi 366 & chain F")

cmd.select ("Outward", "resi 366 & chain F", merge=1)

cmd.color ("blue", "resi 304 & chain F")

cmd.select ("Outward", "resi 304 & chain F", merge=1)

cmd.color ("blue", "resi 305 & chain F")

cmd.select ("Outward", "resi 305 & chain F", merge=1)

cmd.color ("blue", "resi 306 & chain F")

cmd.select ("Outward", "resi 306 & chain F", merge=1)

cmd.color ("blue", "resi 307 & chain F")

cmd.select ("Outward", "resi 307 & chain F", merge=1)

cmd.color ("blue", "resi 308 & chain F")

cmd.select ("Outward", "resi 308 & chain F", merge=1)

cmd.color ("blue", "resi 309 & chain F")

cmd.select ("Outward", "resi 309 & chain F", merge=1)

cmd.color ("blue", "resi 310 & chain F")

cmd.select ("Outward", "resi 310 & chain F", merge=1)

cmd.color ("blue", "resi 311 & chain F")

cmd.select ("Outward", "resi 311 & chain F", merge=1)

cmd.color ("blue", "resi 312 & chain F")

cmd.select ("Outward", "resi 312 & chain F", merge=1)

cmd.color ("blue", "resi 313 & chain F")

cmd.select ("Outward", "resi 313 & chain F", merge=1)

cmd.color ("blue", "resi 314 & chain F")

cmd.select ("Outward", "resi 314 & chain F", merge=1)

cmd.color ("blue", "resi 315 & chain F")

cmd.select ("Outward", "resi 315 & chain F", merge=1)

cmd.color ("blue", "resi 316 & chain F")

cmd.select ("Outward", "resi 316 & chain F", merge=1)

cmd.color ("blue", "resi 317 & chain F")

cmd.select ("Outward", "resi 317 & chain F", merge=1)

cmd.color ("blue", "resi 318 & chain F")

cmd.select ("Outward", "resi 318 & chain F", merge=1)

cmd.color ("blue", "resi 319 & chain F")

cmd.select ("Outward", "resi 319 & chain F", merge=1)

cmd.color ("blue", "resi 320 & chain F")

cmd.select ("Outward", "resi 320 & chain F", merge=1)

cmd.color ("blue", "resi 321 & chain F")

cmd.select ("Outward", "resi 321 & chain F", merge=1)

cmd.color ("blue", "resi 322 & chain F")

cmd.select ("Outward", "resi 322 & chain F", merge=1)

cmd.color ("blue", "resi 323 & chain F")

cmd.select ("Outward", "resi 323 & chain F", merge=1)

cmd.color ("blue", "resi 324 & chain F")

cmd.select ("Outward", "resi 324 & chain F", merge=1)

cmd.color ("blue", "resi 325 & chain F")

cmd.select ("Outward", "resi 325 & chain F", merge=1)

cmd.color ("blue", "resi 326 & chain F")

cmd.select ("Outward", "resi 326 & chain F", merge=1)

cmd.color ("blue", "resi 327 & chain F")

cmd.select ("Outward", "resi 327 & chain F", merge=1)

cmd.color ("blue", "resi 328 & chain F")

cmd.select ("Outward", "resi 328 & chain F", merge=1)

cmd.color ("blue", "resi 329 & chain F")

cmd.select ("Outward", "resi 329 & chain F", merge=1)

cmd.color ("blue", "resi 330 & chain F")

cmd.select ("Outward", "resi 330 & chain F", merge=1)

cmd.color ("blue", "resi 331 & chain F")

cmd.select ("Outward", "resi 331 & chain F", merge=1)

cmd.color ("blue", "resi 332 & chain F")

cmd.select ("Outward", "resi 332 & chain F", merge=1)

cmd.color ("blue", "resi 304 & chain G")

cmd.select ("Outward", "resi 304 & chain G", merge=1)

cmd.color ("blue", "resi 305 & chain G")

cmd.select ("Outward", "resi 305 & chain G", merge=1)

cmd.color ("blue", "resi 306 & chain G")

cmd.select ("Outward", "resi 306 & chain G", merge=1)

cmd.color ("blue", "resi 307 & chain G")

cmd.select ("Outward", "resi 307 & chain G", merge=1)

cmd.color ("blue", "resi 308 & chain G")

cmd.select ("Outward", "resi 308 & chain G", merge=1)

cmd.color ("blue", "resi 309 & chain G")

cmd.select ("Outward", "resi 309 & chain G", merge=1)

cmd.color ("blue", "resi 310 & chain G")

cmd.select ("Outward", "resi 310 & chain G", merge=1)

cmd.color ("blue", "resi 311 & chain G")

cmd.select ("Outward", "resi 311 & chain G", merge=1)

cmd.color ("blue", "resi 312 & chain G")

cmd.select ("Outward", "resi 312 & chain G", merge=1)

cmd.color ("blue", "resi 313 & chain G")

cmd.select ("Outward", "resi 313 & chain G", merge=1)

cmd.color ("blue", "resi 314 & chain G")

cmd.select ("Outward", "resi 314 & chain G", merge=1)

cmd.color ("blue", "resi 315 & chain G")

cmd.select ("Outward", "resi 315 & chain G", merge=1)

cmd.color ("blue", "resi 316 & chain G")

cmd.select ("Outward", "resi 316 & chain G", merge=1)

cmd.color ("blue", "resi 317 & chain G")

cmd.select ("Outward", "resi 317 & chain G", merge=1)

cmd.color ("blue", "resi 318 & chain G")

cmd.select ("Outward", "resi 318 & chain G", merge=1)

cmd.color ("blue", "resi 319 & chain G")

cmd.select ("Outward", "resi 319 & chain G", merge=1)

cmd.color ("blue", "resi 320 & chain G")

cmd.select ("Outward", "resi 320 & chain G", merge=1)

cmd.color ("blue", "resi 321 & chain G")

cmd.select ("Outward", "resi 321 & chain G", merge=1)

cmd.color ("blue", "resi 322 & chain G")

cmd.select ("Outward", "resi 322 & chain G", merge=1)

cmd.color ("blue", "resi 323 & chain G")

cmd.select ("Outward", "resi 323 & chain G", merge=1)

cmd.color ("blue", "resi 324 & chain G")

cmd.select ("Outward", "resi 324 & chain G", merge=1)

cmd.color ("blue", "resi 325 & chain G")

cmd.select ("Outward", "resi 325 & chain G", merge=1)

cmd.color ("blue", "resi 326 & chain G")

cmd.select ("Outward", "resi 326 & chain G", merge=1)

cmd.color ("blue", "resi 327 & chain G")

cmd.select ("Outward", "resi 327 & chain G", merge=1)

cmd.color ("blue", "resi 328 & chain G")

cmd.select ("Outward", "resi 328 & chain G", merge=1)

cmd.color ("blue", "resi 329 & chain G")

cmd.select ("Outward", "resi 329 & chain G", merge=1)

cmd.color ("blue", "resi 330 & chain G")

cmd.select ("Outward", "resi 330 & chain G", merge=1)

cmd.color ("blue", "resi 331 & chain G")

cmd.select ("Outward", "resi 331 & chain G", merge=1)

cmd.color ("blue", "resi 332 & chain G")

cmd.select ("Outward", "resi 332 & chain G", merge=1)

cmd.color ("blue", "resi 337 & chain G")

cmd.select ("Outward", "resi 337 & chain G", merge=1)

cmd.color ("blue", "resi 338 & chain G")

cmd.select ("Outward", "resi 338 & chain G", merge=1)

cmd.color ("blue", "resi 339 & chain G")

cmd.select ("Outward", "resi 339 & chain G", merge=1)

cmd.color ("blue", "resi 340 & chain G")

cmd.select ("Outward", "resi 340 & chain G", merge=1)

cmd.color ("blue", "resi 341 & chain G")

cmd.select ("Outward", "resi 341 & chain G", merge=1)

cmd.color ("blue", "resi 342 & chain G")

cmd.select ("Outward", "resi 342 & chain G", merge=1)

cmd.color ("blue", "resi 343 & chain G")

cmd.select ("Outward", "resi 343 & chain G", merge=1)

cmd.color ("blue", "resi 344 & chain G")

cmd.select ("Outward", "resi 344 & chain G", merge=1)

cmd.color ("blue", "resi 345 & chain G")

cmd.select ("Outward", "resi 345 & chain G", merge=1)

cmd.color ("blue", "resi 346 & chain G")

cmd.select ("Outward", "resi 346 & chain G", merge=1)

cmd.color ("blue", "resi 347 & chain G")

cmd.select ("Outward", "resi 347 & chain G", merge=1)

cmd.color ("blue", "resi 348 & chain G")

cmd.select ("Outward", "resi 348 & chain G", merge=1)

cmd.color ("blue", "resi 349 & chain G")

cmd.select ("Outward", "resi 349 & chain G", merge=1)

cmd.color ("blue", "resi 350 & chain G")

cmd.select ("Outward", "resi 350 & chain G", merge=1)

cmd.color ("blue", "resi 351 & chain G")

cmd.select ("Outward", "resi 351 & chain G", merge=1)

cmd.color ("blue", "resi 352 & chain G")

cmd.select ("Outward", "resi 352 & chain G", merge=1)

cmd.color ("blue", "resi 353 & chain G")

cmd.select ("Outward", "resi 353 & chain G", merge=1)

cmd.color ("blue", "resi 354 & chain G")

cmd.select ("Outward", "resi 354 & chain G", merge=1)

cmd.color ("blue", "resi 355 & chain G")

cmd.select ("Outward", "resi 355 & chain G", merge=1)

cmd.color ("blue", "resi 356 & chain G")

cmd.select ("Outward", "resi 356 & chain G", merge=1)

cmd.color ("blue", "resi 357 & chain G")

cmd.select ("Outward", "resi 357 & chain G", merge=1)

cmd.color ("blue", "resi 358 & chain G")

cmd.select ("Outward", "resi 358 & chain G", merge=1)

cmd.color ("blue", "resi 359 & chain G")

cmd.select ("Outward", "resi 359 & chain G", merge=1)

cmd.color ("blue", "resi 360 & chain G")

cmd.select ("Outward", "resi 360 & chain G", merge=1)

cmd.color ("blue", "resi 361 & chain G")

cmd.select ("Outward", "resi 361 & chain G", merge=1)

cmd.color ("blue", "resi 362 & chain G")

cmd.select ("Outward", "resi 362 & chain G", merge=1)

cmd.color ("blue", "resi 363 & chain G")

cmd.select ("Outward", "resi 363 & chain G", merge=1)

cmd.color ("blue", "resi 364 & chain G")

cmd.select ("Outward", "resi 364 & chain G", merge=1)

cmd.color ("blue", "resi 365 & chain G")

cmd.select ("Outward", "resi 365 & chain G", merge=1)

cmd.color ("blue", "resi 366 & chain G")

cmd.select ("Outward", "resi 366 & chain G", merge=1)

cmd.load_cgo( [9.0, 96.838005,61.7884,-29.432734, 66.10706, 62.128662, -95.34507, 1, 1,1,0,0,0,1], "axis" )
