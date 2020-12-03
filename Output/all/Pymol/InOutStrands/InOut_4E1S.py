from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 212+213+214+215+216+217+218+219 & chain A ")


cmd.select("Astrand13", "resi 398+399+400+401+402+403+404+405+406+407+408+409+410 & chain A ")


cmd.select("Astrand12", "resi 385+386+387+388+389+390+391+392+393+394 & chain A ")


cmd.select("Astrand11", "resi 371+372+373+374+375+376+377+378+379+380+381+382 & chain A ")


cmd.select("Astrand5", "resi 286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")


cmd.select("Astrand6", "resi 300+301+302+303+304+305+306+307+308+309 & chain A ")


cmd.select("Astrand9", "resi 329+330+331+332+333+334+335+336+337+338 & chain A ")


cmd.select("Astrand4", "resi 271+272+273+274+275+276+277+278+279+280+281 & chain A ")


cmd.select("Astrand10", "resi 341+342+343+344+345+346+347+348+349+350+351+352+353 & chain A ")


cmd.select("Astrand3", "resi 254+255+256+257+258+259+260+261+262+263+264+265+266 & chain A ")


cmd.select("Astrand2", "resi 240+241+242+243+244+245+246+247+248+249+250+251 & chain A ")


cmd.select("Astrand1", "resi 225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 212 & chain A")

cmd.select ("Inward", "resi 212 & chain A", merge=1)

cmd.color ("blue", "resi 213 & chain A")

cmd.select ("Outward", "resi 213 & chain A", merge=1)

cmd.color ("red", "resi 214 & chain A")

cmd.select ("Inward", "resi 214 & chain A", merge=1)

cmd.color ("blue", "resi 215 & chain A")

cmd.select ("Outward", "resi 215 & chain A", merge=1)

cmd.color ("red", "resi 216 & chain A")

cmd.select ("Inward", "resi 216 & chain A", merge=1)

cmd.color ("blue", "resi 217 & chain A")

cmd.select ("Outward", "resi 217 & chain A", merge=1)

cmd.color ("red", "resi 218 & chain A")

cmd.select ("Inward", "resi 218 & chain A", merge=1)

cmd.color ("blue", "resi 219 & chain A")

cmd.select ("Outward", "resi 219 & chain A", merge=1)

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

cmd.color ("red", "resi 406 & chain A")

cmd.select ("Inward", "resi 406 & chain A", merge=1)

cmd.color ("blue", "resi 407 & chain A")

cmd.select ("Outward", "resi 407 & chain A", merge=1)

cmd.color ("red", "resi 408 & chain A")

cmd.select ("Inward", "resi 408 & chain A", merge=1)

cmd.color ("blue", "resi 409 & chain A")

cmd.select ("Outward", "resi 409 & chain A", merge=1)

cmd.color ("blue", "resi 410 & chain A")

cmd.select ("Outward", "resi 410 & chain A", merge=1)

cmd.color ("blue", "resi 385 & chain A")

cmd.select ("Outward", "resi 385 & chain A", merge=1)

cmd.color ("red", "resi 386 & chain A")

cmd.select ("Inward", "resi 386 & chain A", merge=1)

cmd.color ("blue", "resi 387 & chain A")

cmd.select ("Outward", "resi 387 & chain A", merge=1)

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

cmd.color ("blue", "resi 382 & chain A")

cmd.select ("Outward", "resi 382 & chain A", merge=1)

cmd.color ("red", "resi 286 & chain A")

cmd.select ("Inward", "resi 286 & chain A", merge=1)

cmd.color ("blue", "resi 287 & chain A")

cmd.select ("Outward", "resi 287 & chain A", merge=1)

cmd.color ("red", "resi 288 & chain A")

cmd.select ("Inward", "resi 288 & chain A", merge=1)

cmd.color ("blue", "resi 289 & chain A")

cmd.select ("Outward", "resi 289 & chain A", merge=1)

cmd.color ("red", "resi 290 & chain A")

cmd.select ("Inward", "resi 290 & chain A", merge=1)

cmd.color ("blue", "resi 291 & chain A")

cmd.select ("Outward", "resi 291 & chain A", merge=1)

cmd.color ("red", "resi 292 & chain A")

cmd.select ("Inward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 295 & chain A")

cmd.select ("Outward", "resi 295 & chain A", merge=1)

cmd.color ("red", "resi 296 & chain A")

cmd.select ("Inward", "resi 296 & chain A", merge=1)

cmd.color ("blue", "resi 297 & chain A")

cmd.select ("Outward", "resi 297 & chain A", merge=1)

cmd.color ("blue", "resi 300 & chain A")

cmd.select ("Outward", "resi 300 & chain A", merge=1)

cmd.color ("red", "resi 301 & chain A")

cmd.select ("Inward", "resi 301 & chain A", merge=1)

cmd.color ("blue", "resi 302 & chain A")

cmd.select ("Outward", "resi 302 & chain A", merge=1)

cmd.color ("red", "resi 303 & chain A")

cmd.select ("Inward", "resi 303 & chain A", merge=1)

cmd.color ("blue", "resi 304 & chain A")

cmd.select ("Outward", "resi 304 & chain A", merge=1)

cmd.color ("red", "resi 305 & chain A")

cmd.select ("Inward", "resi 305 & chain A", merge=1)

cmd.color ("blue", "resi 306 & chain A")

cmd.select ("Outward", "resi 306 & chain A", merge=1)

cmd.color ("red", "resi 307 & chain A")

cmd.select ("Inward", "resi 307 & chain A", merge=1)

cmd.color ("blue", "resi 308 & chain A")

cmd.select ("Outward", "resi 308 & chain A", merge=1)

cmd.color ("blue", "resi 309 & chain A")

cmd.select ("Outward", "resi 309 & chain A", merge=1)

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

cmd.color ("red", "resi 338 & chain A")

cmd.select ("Inward", "resi 338 & chain A", merge=1)

cmd.color ("red", "resi 271 & chain A")

cmd.select ("Inward", "resi 271 & chain A", merge=1)

cmd.color ("blue", "resi 272 & chain A")

cmd.select ("Outward", "resi 272 & chain A", merge=1)

cmd.color ("red", "resi 273 & chain A")

cmd.select ("Inward", "resi 273 & chain A", merge=1)

cmd.color ("blue", "resi 274 & chain A")

cmd.select ("Outward", "resi 274 & chain A", merge=1)

cmd.color ("red", "resi 275 & chain A")

cmd.select ("Inward", "resi 275 & chain A", merge=1)

cmd.color ("blue", "resi 276 & chain A")

cmd.select ("Outward", "resi 276 & chain A", merge=1)

cmd.color ("red", "resi 277 & chain A")

cmd.select ("Inward", "resi 277 & chain A", merge=1)

cmd.color ("blue", "resi 278 & chain A")

cmd.select ("Outward", "resi 278 & chain A", merge=1)

cmd.color ("red", "resi 279 & chain A")

cmd.select ("Inward", "resi 279 & chain A", merge=1)

cmd.color ("blue", "resi 280 & chain A")

cmd.select ("Outward", "resi 280 & chain A", merge=1)

cmd.color ("red", "resi 281 & chain A")

cmd.select ("Inward", "resi 281 & chain A", merge=1)

cmd.color ("red", "resi 341 & chain A")

cmd.select ("Inward", "resi 341 & chain A", merge=1)

cmd.color ("blue", "resi 342 & chain A")

cmd.select ("Outward", "resi 342 & chain A", merge=1)

cmd.color ("blue", "resi 343 & chain A")

cmd.select ("Outward", "resi 343 & chain A", merge=1)

cmd.color ("blue", "resi 344 & chain A")

cmd.select ("Outward", "resi 344 & chain A", merge=1)

cmd.color ("red", "resi 345 & chain A")

cmd.select ("Inward", "resi 345 & chain A", merge=1)

cmd.color ("blue", "resi 346 & chain A")

cmd.select ("Outward", "resi 346 & chain A", merge=1)

cmd.color ("red", "resi 347 & chain A")

cmd.select ("Inward", "resi 347 & chain A", merge=1)

cmd.color ("blue", "resi 348 & chain A")

cmd.select ("Outward", "resi 348 & chain A", merge=1)

cmd.color ("red", "resi 349 & chain A")

cmd.select ("Inward", "resi 349 & chain A", merge=1)

cmd.color ("blue", "resi 350 & chain A")

cmd.select ("Outward", "resi 350 & chain A", merge=1)

cmd.color ("red", "resi 351 & chain A")

cmd.select ("Inward", "resi 351 & chain A", merge=1)

cmd.color ("blue", "resi 352 & chain A")

cmd.select ("Outward", "resi 352 & chain A", merge=1)

cmd.color ("red", "resi 353 & chain A")

cmd.select ("Inward", "resi 353 & chain A", merge=1)

cmd.color ("red", "resi 254 & chain A")

cmd.select ("Inward", "resi 254 & chain A", merge=1)

cmd.color ("blue", "resi 255 & chain A")

cmd.select ("Outward", "resi 255 & chain A", merge=1)

cmd.color ("red", "resi 256 & chain A")

cmd.select ("Inward", "resi 256 & chain A", merge=1)

cmd.color ("blue", "resi 257 & chain A")

cmd.select ("Outward", "resi 257 & chain A", merge=1)

cmd.color ("red", "resi 258 & chain A")

cmd.select ("Inward", "resi 258 & chain A", merge=1)

cmd.color ("blue", "resi 259 & chain A")

cmd.select ("Outward", "resi 259 & chain A", merge=1)

cmd.color ("red", "resi 260 & chain A")

cmd.select ("Inward", "resi 260 & chain A", merge=1)

cmd.color ("blue", "resi 261 & chain A")

cmd.select ("Outward", "resi 261 & chain A", merge=1)

cmd.color ("red", "resi 262 & chain A")

cmd.select ("Inward", "resi 262 & chain A", merge=1)

cmd.color ("blue", "resi 263 & chain A")

cmd.select ("Outward", "resi 263 & chain A", merge=1)

cmd.color ("red", "resi 264 & chain A")

cmd.select ("Inward", "resi 264 & chain A", merge=1)

cmd.color ("blue", "resi 265 & chain A")

cmd.select ("Outward", "resi 265 & chain A", merge=1)

cmd.color ("red", "resi 266 & chain A")

cmd.select ("Inward", "resi 266 & chain A", merge=1)

cmd.color ("blue", "resi 240 & chain A")

cmd.select ("Outward", "resi 240 & chain A", merge=1)

cmd.color ("red", "resi 241 & chain A")

cmd.select ("Inward", "resi 241 & chain A", merge=1)

cmd.color ("blue", "resi 242 & chain A")

cmd.select ("Outward", "resi 242 & chain A", merge=1)

cmd.color ("red", "resi 243 & chain A")

cmd.select ("Inward", "resi 243 & chain A", merge=1)

cmd.color ("blue", "resi 244 & chain A")

cmd.select ("Outward", "resi 244 & chain A", merge=1)

cmd.color ("red", "resi 245 & chain A")

cmd.select ("Inward", "resi 245 & chain A", merge=1)

cmd.color ("blue", "resi 246 & chain A")

cmd.select ("Outward", "resi 246 & chain A", merge=1)

cmd.color ("red", "resi 247 & chain A")

cmd.select ("Inward", "resi 247 & chain A", merge=1)

cmd.color ("blue", "resi 248 & chain A")

cmd.select ("Outward", "resi 248 & chain A", merge=1)

cmd.color ("red", "resi 249 & chain A")

cmd.select ("Inward", "resi 249 & chain A", merge=1)

cmd.color ("blue", "resi 250 & chain A")

cmd.select ("Outward", "resi 250 & chain A", merge=1)

cmd.color ("red", "resi 251 & chain A")

cmd.select ("Inward", "resi 251 & chain A", merge=1)

cmd.color ("red", "resi 225 & chain A")

cmd.select ("Inward", "resi 225 & chain A", merge=1)

cmd.color ("blue", "resi 226 & chain A")

cmd.select ("Outward", "resi 226 & chain A", merge=1)

cmd.color ("red", "resi 227 & chain A")

cmd.select ("Inward", "resi 227 & chain A", merge=1)

cmd.color ("blue", "resi 228 & chain A")

cmd.select ("Outward", "resi 228 & chain A", merge=1)

cmd.color ("red", "resi 229 & chain A")

cmd.select ("Inward", "resi 229 & chain A", merge=1)

cmd.color ("blue", "resi 230 & chain A")

cmd.select ("Outward", "resi 230 & chain A", merge=1)

cmd.color ("red", "resi 231 & chain A")

cmd.select ("Inward", "resi 231 & chain A", merge=1)

cmd.color ("blue", "resi 232 & chain A")

cmd.select ("Outward", "resi 232 & chain A", merge=1)

cmd.color ("blue", "resi 233 & chain A")

cmd.select ("Outward", "resi 233 & chain A", merge=1)

cmd.color ("red", "resi 234 & chain A")

cmd.select ("Inward", "resi 234 & chain A", merge=1)

cmd.color ("blue", "resi 235 & chain A")

cmd.select ("Outward", "resi 235 & chain A", merge=1)

cmd.color ("red", "resi 236 & chain A")

cmd.select ("Inward", "resi 236 & chain A", merge=1)

cmd.load_cgo( [9.0, -42.788166,-14.979081,6.625667, -42.788166, -14.979081, 6.625667, 1, 1,1,0,0,0,1], "axis" )
