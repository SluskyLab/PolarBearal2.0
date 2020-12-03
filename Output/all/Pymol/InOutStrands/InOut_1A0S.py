from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A0S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Pstrand0", "resi 73+74+75+76+77+78+79+80+81+82+83+84+85+86 & chain P ")


cmd.select("Pstrand19", "resi 472+473+474+475+476+477+478+479+480+481+482 & chain P ")


cmd.select("Pstrand18", "resi 439+440+441+442+443+444+445+446+447+448+449 & chain P ")


cmd.select("Pstrand17", "resi 413+414+415+416+417+418+419+420+421+422+423+424+425+426+427 & chain P ")


cmd.select("Pstrand16", "resi 389+390+391+392+393+394+395+396+397+398+399+400+401+402+403 & chain P ")


cmd.select("Pstrand15", "resi 371+372+373+374+375+376+377+378+379+380+381+382+383+384 & chain P ")


cmd.select("Pstrand14", "resi 351+352+353+354+355+356+357+358+359+360+361+362+363 & chain P ")


cmd.select("Pstrand13", "resi 335+336+337+338+339+340+341+342+343+344 & chain P ")


cmd.select("Pstrand12", "resi 306+307+308+309+310+311+312+313+314+315+316 & chain P ")


cmd.select("Pstrand11", "resi 286+287+288+289+290+291+292+293+294+295+296 & chain P ")


cmd.select("Pstrand10", "resi 256+257+258+259+260+261+262+263+264 & chain P ")


cmd.select("Pstrand9", "resi 241+242+243+244+245+246+247+248+249+250+251+252+253 & chain P ")


cmd.select("Pstrand8", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233 & chain P ")


cmd.select("Pstrand7", "resi 206+207+208+209+210+211+212+213+214+215+216+217 & chain P ")


cmd.select("Pstrand4", "resi 181+182+183+184+185+186+187+188 & chain P ")


cmd.select("Pstrand3", "resi 159+160+161+162+163+164+165+166+167+168 & chain P ")


cmd.select("Pstrand2", "resi 134+135+136+137+138+139+140+141+142+143+144+145 & chain P ")


cmd.select("Pstrand1", "resi 117+118+119+120+121+122+123+124+125+126+127+128 & chain P ")


cmd.select("barrel", "Pstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 73 & chain P")

cmd.select ("Outward", "resi 73 & chain P", merge=1)

cmd.color ("red", "resi 74 & chain P")

cmd.select ("Inward", "resi 74 & chain P", merge=1)

cmd.color ("blue", "resi 75 & chain P")

cmd.select ("Outward", "resi 75 & chain P", merge=1)

cmd.color ("red", "resi 76 & chain P")

cmd.select ("Inward", "resi 76 & chain P", merge=1)

cmd.color ("blue", "resi 77 & chain P")

cmd.select ("Outward", "resi 77 & chain P", merge=1)

cmd.color ("red", "resi 78 & chain P")

cmd.select ("Inward", "resi 78 & chain P", merge=1)

cmd.color ("blue", "resi 79 & chain P")

cmd.select ("Outward", "resi 79 & chain P", merge=1)

cmd.color ("red", "resi 80 & chain P")

cmd.select ("Inward", "resi 80 & chain P", merge=1)

cmd.color ("blue", "resi 81 & chain P")

cmd.select ("Outward", "resi 81 & chain P", merge=1)

cmd.color ("red", "resi 82 & chain P")

cmd.select ("Inward", "resi 82 & chain P", merge=1)

cmd.color ("blue", "resi 83 & chain P")

cmd.select ("Outward", "resi 83 & chain P", merge=1)

cmd.color ("red", "resi 84 & chain P")

cmd.select ("Inward", "resi 84 & chain P", merge=1)

cmd.color ("blue", "resi 85 & chain P")

cmd.select ("Outward", "resi 85 & chain P", merge=1)

cmd.color ("blue", "resi 86 & chain P")

cmd.select ("Outward", "resi 86 & chain P", merge=1)

cmd.color ("red", "resi 472 & chain P")

cmd.select ("Inward", "resi 472 & chain P", merge=1)

cmd.color ("blue", "resi 473 & chain P")

cmd.select ("Outward", "resi 473 & chain P", merge=1)

cmd.color ("red", "resi 474 & chain P")

cmd.select ("Inward", "resi 474 & chain P", merge=1)

cmd.color ("blue", "resi 475 & chain P")

cmd.select ("Outward", "resi 475 & chain P", merge=1)

cmd.color ("red", "resi 476 & chain P")

cmd.select ("Inward", "resi 476 & chain P", merge=1)

cmd.color ("blue", "resi 477 & chain P")

cmd.select ("Outward", "resi 477 & chain P", merge=1)

cmd.color ("red", "resi 478 & chain P")

cmd.select ("Inward", "resi 478 & chain P", merge=1)

cmd.color ("blue", "resi 479 & chain P")

cmd.select ("Outward", "resi 479 & chain P", merge=1)

cmd.color ("red", "resi 480 & chain P")

cmd.select ("Inward", "resi 480 & chain P", merge=1)

cmd.color ("blue", "resi 481 & chain P")

cmd.select ("Outward", "resi 481 & chain P", merge=1)

cmd.color ("red", "resi 482 & chain P")

cmd.select ("Inward", "resi 482 & chain P", merge=1)

cmd.color ("red", "resi 439 & chain P")

cmd.select ("Inward", "resi 439 & chain P", merge=1)

cmd.color ("blue", "resi 440 & chain P")

cmd.select ("Outward", "resi 440 & chain P", merge=1)

cmd.color ("red", "resi 441 & chain P")

cmd.select ("Inward", "resi 441 & chain P", merge=1)

cmd.color ("blue", "resi 442 & chain P")

cmd.select ("Outward", "resi 442 & chain P", merge=1)

cmd.color ("red", "resi 443 & chain P")

cmd.select ("Inward", "resi 443 & chain P", merge=1)

cmd.color ("blue", "resi 444 & chain P")

cmd.select ("Outward", "resi 444 & chain P", merge=1)

cmd.color ("red", "resi 445 & chain P")

cmd.select ("Inward", "resi 445 & chain P", merge=1)

cmd.color ("blue", "resi 446 & chain P")

cmd.select ("Outward", "resi 446 & chain P", merge=1)

cmd.color ("red", "resi 447 & chain P")

cmd.select ("Inward", "resi 447 & chain P", merge=1)

cmd.color ("blue", "resi 448 & chain P")

cmd.select ("Outward", "resi 448 & chain P", merge=1)

cmd.color ("red", "resi 449 & chain P")

cmd.select ("Inward", "resi 449 & chain P", merge=1)

cmd.color ("red", "resi 413 & chain P")

cmd.select ("Inward", "resi 413 & chain P", merge=1)

cmd.color ("blue", "resi 414 & chain P")

cmd.select ("Outward", "resi 414 & chain P", merge=1)

cmd.color ("red", "resi 415 & chain P")

cmd.select ("Inward", "resi 415 & chain P", merge=1)

cmd.color ("blue", "resi 416 & chain P")

cmd.select ("Outward", "resi 416 & chain P", merge=1)

cmd.color ("red", "resi 417 & chain P")

cmd.select ("Inward", "resi 417 & chain P", merge=1)

cmd.color ("blue", "resi 418 & chain P")

cmd.select ("Outward", "resi 418 & chain P", merge=1)

cmd.color ("red", "resi 419 & chain P")

cmd.select ("Inward", "resi 419 & chain P", merge=1)

cmd.color ("blue", "resi 420 & chain P")

cmd.select ("Outward", "resi 420 & chain P", merge=1)

cmd.color ("red", "resi 421 & chain P")

cmd.select ("Inward", "resi 421 & chain P", merge=1)

cmd.color ("blue", "resi 422 & chain P")

cmd.select ("Outward", "resi 422 & chain P", merge=1)

cmd.color ("red", "resi 423 & chain P")

cmd.select ("Inward", "resi 423 & chain P", merge=1)

cmd.color ("blue", "resi 424 & chain P")

cmd.select ("Outward", "resi 424 & chain P", merge=1)

cmd.color ("red", "resi 425 & chain P")

cmd.select ("Inward", "resi 425 & chain P", merge=1)

cmd.color ("blue", "resi 426 & chain P")

cmd.select ("Outward", "resi 426 & chain P", merge=1)

cmd.color ("red", "resi 427 & chain P")

cmd.select ("Inward", "resi 427 & chain P", merge=1)

cmd.color ("blue", "resi 389 & chain P")

cmd.select ("Outward", "resi 389 & chain P", merge=1)

cmd.color ("red", "resi 390 & chain P")

cmd.select ("Inward", "resi 390 & chain P", merge=1)

cmd.color ("blue", "resi 391 & chain P")

cmd.select ("Outward", "resi 391 & chain P", merge=1)

cmd.color ("red", "resi 392 & chain P")

cmd.select ("Inward", "resi 392 & chain P", merge=1)

cmd.color ("blue", "resi 393 & chain P")

cmd.select ("Outward", "resi 393 & chain P", merge=1)

cmd.color ("red", "resi 394 & chain P")

cmd.select ("Inward", "resi 394 & chain P", merge=1)

cmd.color ("blue", "resi 395 & chain P")

cmd.select ("Outward", "resi 395 & chain P", merge=1)

cmd.color ("red", "resi 396 & chain P")

cmd.select ("Inward", "resi 396 & chain P", merge=1)

cmd.color ("blue", "resi 397 & chain P")

cmd.select ("Outward", "resi 397 & chain P", merge=1)

cmd.color ("red", "resi 398 & chain P")

cmd.select ("Inward", "resi 398 & chain P", merge=1)

cmd.color ("blue", "resi 399 & chain P")

cmd.select ("Outward", "resi 399 & chain P", merge=1)

cmd.color ("red", "resi 400 & chain P")

cmd.select ("Inward", "resi 400 & chain P", merge=1)

cmd.color ("blue", "resi 401 & chain P")

cmd.select ("Outward", "resi 401 & chain P", merge=1)

cmd.color ("red", "resi 402 & chain P")

cmd.select ("Inward", "resi 402 & chain P", merge=1)

cmd.color ("blue", "resi 403 & chain P")

cmd.select ("Outward", "resi 403 & chain P", merge=1)

cmd.color ("blue", "resi 371 & chain P")

cmd.select ("Outward", "resi 371 & chain P", merge=1)

cmd.color ("red", "resi 372 & chain P")

cmd.select ("Inward", "resi 372 & chain P", merge=1)

cmd.color ("blue", "resi 373 & chain P")

cmd.select ("Outward", "resi 373 & chain P", merge=1)

cmd.color ("red", "resi 374 & chain P")

cmd.select ("Inward", "resi 374 & chain P", merge=1)

cmd.color ("blue", "resi 375 & chain P")

cmd.select ("Outward", "resi 375 & chain P", merge=1)

cmd.color ("red", "resi 376 & chain P")

cmd.select ("Inward", "resi 376 & chain P", merge=1)

cmd.color ("blue", "resi 377 & chain P")

cmd.select ("Outward", "resi 377 & chain P", merge=1)

cmd.color ("red", "resi 378 & chain P")

cmd.select ("Inward", "resi 378 & chain P", merge=1)

cmd.color ("blue", "resi 379 & chain P")

cmd.select ("Outward", "resi 379 & chain P", merge=1)

cmd.color ("red", "resi 380 & chain P")

cmd.select ("Inward", "resi 380 & chain P", merge=1)

cmd.color ("blue", "resi 381 & chain P")

cmd.select ("Outward", "resi 381 & chain P", merge=1)

cmd.color ("red", "resi 382 & chain P")

cmd.select ("Inward", "resi 382 & chain P", merge=1)

cmd.color ("blue", "resi 383 & chain P")

cmd.select ("Outward", "resi 383 & chain P", merge=1)

cmd.color ("blue", "resi 384 & chain P")

cmd.select ("Outward", "resi 384 & chain P", merge=1)

cmd.color ("blue", "resi 351 & chain P")

cmd.select ("Outward", "resi 351 & chain P", merge=1)

cmd.color ("red", "resi 352 & chain P")

cmd.select ("Inward", "resi 352 & chain P", merge=1)

cmd.color ("blue", "resi 353 & chain P")

cmd.select ("Outward", "resi 353 & chain P", merge=1)

cmd.color ("red", "resi 354 & chain P")

cmd.select ("Inward", "resi 354 & chain P", merge=1)

cmd.color ("blue", "resi 355 & chain P")

cmd.select ("Outward", "resi 355 & chain P", merge=1)

cmd.color ("red", "resi 356 & chain P")

cmd.select ("Inward", "resi 356 & chain P", merge=1)

cmd.color ("blue", "resi 357 & chain P")

cmd.select ("Outward", "resi 357 & chain P", merge=1)

cmd.color ("red", "resi 358 & chain P")

cmd.select ("Inward", "resi 358 & chain P", merge=1)

cmd.color ("blue", "resi 359 & chain P")

cmd.select ("Outward", "resi 359 & chain P", merge=1)

cmd.color ("red", "resi 360 & chain P")

cmd.select ("Inward", "resi 360 & chain P", merge=1)

cmd.color ("blue", "resi 361 & chain P")

cmd.select ("Outward", "resi 361 & chain P", merge=1)

cmd.color ("red", "resi 362 & chain P")

cmd.select ("Inward", "resi 362 & chain P", merge=1)

cmd.color ("blue", "resi 363 & chain P")

cmd.select ("Outward", "resi 363 & chain P", merge=1)

cmd.color ("blue", "resi 335 & chain P")

cmd.select ("Outward", "resi 335 & chain P", merge=1)

cmd.color ("red", "resi 336 & chain P")

cmd.select ("Inward", "resi 336 & chain P", merge=1)

cmd.color ("blue", "resi 337 & chain P")

cmd.select ("Outward", "resi 337 & chain P", merge=1)

cmd.color ("red", "resi 338 & chain P")

cmd.select ("Inward", "resi 338 & chain P", merge=1)

cmd.color ("blue", "resi 339 & chain P")

cmd.select ("Outward", "resi 339 & chain P", merge=1)

cmd.color ("red", "resi 340 & chain P")

cmd.select ("Inward", "resi 340 & chain P", merge=1)

cmd.color ("blue", "resi 341 & chain P")

cmd.select ("Outward", "resi 341 & chain P", merge=1)

cmd.color ("red", "resi 342 & chain P")

cmd.select ("Inward", "resi 342 & chain P", merge=1)

cmd.color ("blue", "resi 343 & chain P")

cmd.select ("Outward", "resi 343 & chain P", merge=1)

cmd.color ("red", "resi 344 & chain P")

cmd.select ("Inward", "resi 344 & chain P", merge=1)

cmd.color ("red", "resi 306 & chain P")

cmd.select ("Inward", "resi 306 & chain P", merge=1)

cmd.color ("blue", "resi 307 & chain P")

cmd.select ("Outward", "resi 307 & chain P", merge=1)

cmd.color ("red", "resi 308 & chain P")

cmd.select ("Inward", "resi 308 & chain P", merge=1)

cmd.color ("blue", "resi 309 & chain P")

cmd.select ("Outward", "resi 309 & chain P", merge=1)

cmd.color ("red", "resi 310 & chain P")

cmd.select ("Inward", "resi 310 & chain P", merge=1)

cmd.color ("blue", "resi 311 & chain P")

cmd.select ("Outward", "resi 311 & chain P", merge=1)

cmd.color ("red", "resi 312 & chain P")

cmd.select ("Inward", "resi 312 & chain P", merge=1)

cmd.color ("blue", "resi 313 & chain P")

cmd.select ("Outward", "resi 313 & chain P", merge=1)

cmd.color ("red", "resi 314 & chain P")

cmd.select ("Inward", "resi 314 & chain P", merge=1)

cmd.color ("blue", "resi 315 & chain P")

cmd.select ("Outward", "resi 315 & chain P", merge=1)

cmd.color ("blue", "resi 316 & chain P")

cmd.select ("Outward", "resi 316 & chain P", merge=1)

cmd.color ("blue", "resi 286 & chain P")

cmd.select ("Outward", "resi 286 & chain P", merge=1)

cmd.color ("red", "resi 287 & chain P")

cmd.select ("Inward", "resi 287 & chain P", merge=1)

cmd.color ("blue", "resi 288 & chain P")

cmd.select ("Outward", "resi 288 & chain P", merge=1)

cmd.color ("red", "resi 289 & chain P")

cmd.select ("Inward", "resi 289 & chain P", merge=1)

cmd.color ("blue", "resi 290 & chain P")

cmd.select ("Outward", "resi 290 & chain P", merge=1)

cmd.color ("red", "resi 291 & chain P")

cmd.select ("Inward", "resi 291 & chain P", merge=1)

cmd.color ("blue", "resi 292 & chain P")

cmd.select ("Outward", "resi 292 & chain P", merge=1)

cmd.color ("red", "resi 293 & chain P")

cmd.select ("Inward", "resi 293 & chain P", merge=1)

cmd.color ("blue", "resi 294 & chain P")

cmd.select ("Outward", "resi 294 & chain P", merge=1)

cmd.color ("red", "resi 295 & chain P")

cmd.select ("Inward", "resi 295 & chain P", merge=1)

cmd.color ("blue", "resi 296 & chain P")

cmd.select ("Outward", "resi 296 & chain P", merge=1)

cmd.color ("blue", "resi 256 & chain P")

cmd.select ("Outward", "resi 256 & chain P", merge=1)

cmd.color ("red", "resi 257 & chain P")

cmd.select ("Inward", "resi 257 & chain P", merge=1)

cmd.color ("blue", "resi 258 & chain P")

cmd.select ("Outward", "resi 258 & chain P", merge=1)

cmd.color ("red", "resi 259 & chain P")

cmd.select ("Inward", "resi 259 & chain P", merge=1)

cmd.color ("blue", "resi 260 & chain P")

cmd.select ("Outward", "resi 260 & chain P", merge=1)

cmd.color ("red", "resi 261 & chain P")

cmd.select ("Inward", "resi 261 & chain P", merge=1)

cmd.color ("blue", "resi 262 & chain P")

cmd.select ("Outward", "resi 262 & chain P", merge=1)

cmd.color ("red", "resi 263 & chain P")

cmd.select ("Inward", "resi 263 & chain P", merge=1)

cmd.color ("blue", "resi 264 & chain P")

cmd.select ("Outward", "resi 264 & chain P", merge=1)

cmd.color ("blue", "resi 241 & chain P")

cmd.select ("Outward", "resi 241 & chain P", merge=1)

cmd.color ("red", "resi 242 & chain P")

cmd.select ("Inward", "resi 242 & chain P", merge=1)

cmd.color ("blue", "resi 243 & chain P")

cmd.select ("Outward", "resi 243 & chain P", merge=1)

cmd.color ("red", "resi 244 & chain P")

cmd.select ("Inward", "resi 244 & chain P", merge=1)

cmd.color ("blue", "resi 245 & chain P")

cmd.select ("Outward", "resi 245 & chain P", merge=1)

cmd.color ("red", "resi 246 & chain P")

cmd.select ("Inward", "resi 246 & chain P", merge=1)

cmd.color ("blue", "resi 247 & chain P")

cmd.select ("Outward", "resi 247 & chain P", merge=1)

cmd.color ("red", "resi 248 & chain P")

cmd.select ("Inward", "resi 248 & chain P", merge=1)

cmd.color ("blue", "resi 249 & chain P")

cmd.select ("Outward", "resi 249 & chain P", merge=1)

cmd.color ("red", "resi 250 & chain P")

cmd.select ("Inward", "resi 250 & chain P", merge=1)

cmd.color ("blue", "resi 251 & chain P")

cmd.select ("Outward", "resi 251 & chain P", merge=1)

cmd.color ("red", "resi 252 & chain P")

cmd.select ("Inward", "resi 252 & chain P", merge=1)

cmd.color ("blue", "resi 253 & chain P")

cmd.select ("Outward", "resi 253 & chain P", merge=1)

cmd.color ("blue", "resi 221 & chain P")

cmd.select ("Outward", "resi 221 & chain P", merge=1)

cmd.color ("red", "resi 222 & chain P")

cmd.select ("Inward", "resi 222 & chain P", merge=1)

cmd.color ("blue", "resi 223 & chain P")

cmd.select ("Outward", "resi 223 & chain P", merge=1)

cmd.color ("red", "resi 224 & chain P")

cmd.select ("Inward", "resi 224 & chain P", merge=1)

cmd.color ("blue", "resi 225 & chain P")

cmd.select ("Outward", "resi 225 & chain P", merge=1)

cmd.color ("red", "resi 226 & chain P")

cmd.select ("Inward", "resi 226 & chain P", merge=1)

cmd.color ("blue", "resi 227 & chain P")

cmd.select ("Outward", "resi 227 & chain P", merge=1)

cmd.color ("red", "resi 228 & chain P")

cmd.select ("Inward", "resi 228 & chain P", merge=1)

cmd.color ("blue", "resi 229 & chain P")

cmd.select ("Outward", "resi 229 & chain P", merge=1)

cmd.color ("red", "resi 230 & chain P")

cmd.select ("Inward", "resi 230 & chain P", merge=1)

cmd.color ("blue", "resi 231 & chain P")

cmd.select ("Outward", "resi 231 & chain P", merge=1)

cmd.color ("blue", "resi 232 & chain P")

cmd.select ("Outward", "resi 232 & chain P", merge=1)

cmd.color ("blue", "resi 233 & chain P")

cmd.select ("Outward", "resi 233 & chain P", merge=1)

cmd.color ("blue", "resi 206 & chain P")

cmd.select ("Outward", "resi 206 & chain P", merge=1)

cmd.color ("red", "resi 207 & chain P")

cmd.select ("Inward", "resi 207 & chain P", merge=1)

cmd.color ("blue", "resi 208 & chain P")

cmd.select ("Outward", "resi 208 & chain P", merge=1)

cmd.color ("red", "resi 209 & chain P")

cmd.select ("Inward", "resi 209 & chain P", merge=1)

cmd.color ("blue", "resi 210 & chain P")

cmd.select ("Outward", "resi 210 & chain P", merge=1)

cmd.color ("red", "resi 211 & chain P")

cmd.select ("Inward", "resi 211 & chain P", merge=1)

cmd.color ("blue", "resi 212 & chain P")

cmd.select ("Outward", "resi 212 & chain P", merge=1)

cmd.color ("red", "resi 213 & chain P")

cmd.select ("Inward", "resi 213 & chain P", merge=1)

cmd.color ("blue", "resi 214 & chain P")

cmd.select ("Outward", "resi 214 & chain P", merge=1)

cmd.color ("red", "resi 215 & chain P")

cmd.select ("Inward", "resi 215 & chain P", merge=1)

cmd.color ("blue", "resi 216 & chain P")

cmd.select ("Outward", "resi 216 & chain P", merge=1)

cmd.color ("red", "resi 217 & chain P")

cmd.select ("Inward", "resi 217 & chain P", merge=1)

cmd.color ("red", "resi 181 & chain P")

cmd.select ("Inward", "resi 181 & chain P", merge=1)

cmd.color ("blue", "resi 182 & chain P")

cmd.select ("Outward", "resi 182 & chain P", merge=1)

cmd.color ("red", "resi 183 & chain P")

cmd.select ("Inward", "resi 183 & chain P", merge=1)

cmd.color ("blue", "resi 184 & chain P")

cmd.select ("Outward", "resi 184 & chain P", merge=1)

cmd.color ("red", "resi 185 & chain P")

cmd.select ("Inward", "resi 185 & chain P", merge=1)

cmd.color ("blue", "resi 186 & chain P")

cmd.select ("Outward", "resi 186 & chain P", merge=1)

cmd.color ("red", "resi 187 & chain P")

cmd.select ("Inward", "resi 187 & chain P", merge=1)

cmd.color ("blue", "resi 188 & chain P")

cmd.select ("Outward", "resi 188 & chain P", merge=1)

cmd.color ("red", "resi 159 & chain P")

cmd.select ("Inward", "resi 159 & chain P", merge=1)

cmd.color ("blue", "resi 160 & chain P")

cmd.select ("Outward", "resi 160 & chain P", merge=1)

cmd.color ("red", "resi 161 & chain P")

cmd.select ("Inward", "resi 161 & chain P", merge=1)

cmd.color ("blue", "resi 162 & chain P")

cmd.select ("Outward", "resi 162 & chain P", merge=1)

cmd.color ("blue", "resi 163 & chain P")

cmd.select ("Outward", "resi 163 & chain P", merge=1)

cmd.color ("red", "resi 164 & chain P")

cmd.select ("Inward", "resi 164 & chain P", merge=1)

cmd.color ("blue", "resi 165 & chain P")

cmd.select ("Outward", "resi 165 & chain P", merge=1)

cmd.color ("red", "resi 166 & chain P")

cmd.select ("Inward", "resi 166 & chain P", merge=1)

cmd.color ("blue", "resi 167 & chain P")

cmd.select ("Outward", "resi 167 & chain P", merge=1)

cmd.color ("red", "resi 168 & chain P")

cmd.select ("Inward", "resi 168 & chain P", merge=1)

cmd.color ("red", "resi 134 & chain P")

cmd.select ("Inward", "resi 134 & chain P", merge=1)

cmd.color ("blue", "resi 135 & chain P")

cmd.select ("Outward", "resi 135 & chain P", merge=1)

cmd.color ("red", "resi 136 & chain P")

cmd.select ("Inward", "resi 136 & chain P", merge=1)

cmd.color ("blue", "resi 137 & chain P")

cmd.select ("Outward", "resi 137 & chain P", merge=1)

cmd.color ("red", "resi 138 & chain P")

cmd.select ("Inward", "resi 138 & chain P", merge=1)

cmd.color ("blue", "resi 139 & chain P")

cmd.select ("Outward", "resi 139 & chain P", merge=1)

cmd.color ("red", "resi 140 & chain P")

cmd.select ("Inward", "resi 140 & chain P", merge=1)

cmd.color ("blue", "resi 141 & chain P")

cmd.select ("Outward", "resi 141 & chain P", merge=1)

cmd.color ("red", "resi 142 & chain P")

cmd.select ("Inward", "resi 142 & chain P", merge=1)

cmd.color ("blue", "resi 143 & chain P")

cmd.select ("Outward", "resi 143 & chain P", merge=1)

cmd.color ("red", "resi 144 & chain P")

cmd.select ("Inward", "resi 144 & chain P", merge=1)

cmd.color ("blue", "resi 145 & chain P")

cmd.select ("Outward", "resi 145 & chain P", merge=1)

cmd.color ("blue", "resi 117 & chain P")

cmd.select ("Outward", "resi 117 & chain P", merge=1)

cmd.color ("red", "resi 118 & chain P")

cmd.select ("Inward", "resi 118 & chain P", merge=1)

cmd.color ("blue", "resi 119 & chain P")

cmd.select ("Outward", "resi 119 & chain P", merge=1)

cmd.color ("red", "resi 120 & chain P")

cmd.select ("Inward", "resi 120 & chain P", merge=1)

cmd.color ("blue", "resi 121 & chain P")

cmd.select ("Outward", "resi 121 & chain P", merge=1)

cmd.color ("red", "resi 122 & chain P")

cmd.select ("Inward", "resi 122 & chain P", merge=1)

cmd.color ("blue", "resi 123 & chain P")

cmd.select ("Outward", "resi 123 & chain P", merge=1)

cmd.color ("red", "resi 124 & chain P")

cmd.select ("Inward", "resi 124 & chain P", merge=1)

cmd.color ("blue", "resi 125 & chain P")

cmd.select ("Outward", "resi 125 & chain P", merge=1)

cmd.color ("red", "resi 126 & chain P")

cmd.select ("Inward", "resi 126 & chain P", merge=1)

cmd.color ("blue", "resi 127 & chain P")

cmd.select ("Outward", "resi 127 & chain P", merge=1)

cmd.color ("blue", "resi 128 & chain P")

cmd.select ("Outward", "resi 128 & chain P", merge=1)

cmd.load_cgo( [9.0, -52.502384,-17.450613,-25.578499, -52.502384, -17.450613, -25.578499, 1, 1,1,0,0,0,1], "axis" )
