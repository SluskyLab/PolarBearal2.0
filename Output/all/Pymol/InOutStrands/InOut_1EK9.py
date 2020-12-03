from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EK9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53 & chain A ")


cmd.select("Astrand1", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain A ")


cmd.select("Astrand3", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain A ")


cmd.select("Astrand5", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292+293+294 & chain A ")


cmd.select("Bstrand12", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292+293+294 & chain B ")


cmd.select("Bstrand10", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain B ")


cmd.select("Bstrand8", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain B ")


cmd.select("Bstrand7", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53 & chain B ")


cmd.select("Cstrand14", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53 & chain C ")


cmd.select("Cstrand15", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain C ")


cmd.select("Cstrand17", "resi 247+248+249+250+251+252+253+254+255+256+257 & chain C ")


cmd.select("Cstrand19", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292+293+294 & chain C ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 41 & chain A")

cmd.select ("Outward", "resi 41 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("blue", "resi 43 & chain A")

cmd.select ("Outward", "resi 43 & chain A", merge=1)

cmd.color ("blue", "resi 44 & chain A")

cmd.select ("Outward", "resi 44 & chain A", merge=1)

cmd.color ("blue", "resi 45 & chain A")

cmd.select ("Outward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 46 & chain A")

cmd.select ("Outward", "resi 46 & chain A", merge=1)

cmd.color ("blue", "resi 47 & chain A")

cmd.select ("Outward", "resi 47 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("blue", "resi 49 & chain A")

cmd.select ("Outward", "resi 49 & chain A", merge=1)

cmd.color ("blue", "resi 50 & chain A")

cmd.select ("Outward", "resi 50 & chain A", merge=1)

cmd.color ("blue", "resi 51 & chain A")

cmd.select ("Outward", "resi 51 & chain A", merge=1)

cmd.color ("blue", "resi 52 & chain A")

cmd.select ("Outward", "resi 52 & chain A", merge=1)

cmd.color ("blue", "resi 53 & chain A")

cmd.select ("Outward", "resi 53 & chain A", merge=1)

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("blue", "resi 62 & chain A")

cmd.select ("Outward", "resi 62 & chain A", merge=1)

cmd.color ("blue", "resi 63 & chain A")

cmd.select ("Outward", "resi 63 & chain A", merge=1)

cmd.color ("blue", "resi 64 & chain A")

cmd.select ("Outward", "resi 64 & chain A", merge=1)

cmd.color ("blue", "resi 65 & chain A")

cmd.select ("Outward", "resi 65 & chain A", merge=1)

cmd.color ("blue", "resi 66 & chain A")

cmd.select ("Outward", "resi 66 & chain A", merge=1)

cmd.color ("blue", "resi 67 & chain A")

cmd.select ("Outward", "resi 67 & chain A", merge=1)

cmd.color ("blue", "resi 68 & chain A")

cmd.select ("Outward", "resi 68 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

cmd.color ("blue", "resi 70 & chain A")

cmd.select ("Outward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.color ("blue", "resi 72 & chain A")

cmd.select ("Outward", "resi 72 & chain A", merge=1)

cmd.color ("blue", "resi 73 & chain A")

cmd.select ("Outward", "resi 73 & chain A", merge=1)

cmd.color ("blue", "resi 74 & chain A")

cmd.select ("Outward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("blue", "resi 76 & chain A")

cmd.select ("Outward", "resi 76 & chain A", merge=1)

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

cmd.color ("blue", "resi 254 & chain A")

cmd.select ("Outward", "resi 254 & chain A", merge=1)

cmd.color ("blue", "resi 255 & chain A")

cmd.select ("Outward", "resi 255 & chain A", merge=1)

cmd.color ("blue", "resi 256 & chain A")

cmd.select ("Outward", "resi 256 & chain A", merge=1)

cmd.color ("blue", "resi 257 & chain A")

cmd.select ("Outward", "resi 257 & chain A", merge=1)

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

cmd.color ("blue", "resi 290 & chain A")

cmd.select ("Outward", "resi 290 & chain A", merge=1)

cmd.color ("blue", "resi 291 & chain A")

cmd.select ("Outward", "resi 291 & chain A", merge=1)

cmd.color ("blue", "resi 292 & chain A")

cmd.select ("Outward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

cmd.color ("blue", "resi 280 & chain B")

cmd.select ("Outward", "resi 280 & chain B", merge=1)

cmd.color ("blue", "resi 281 & chain B")

cmd.select ("Outward", "resi 281 & chain B", merge=1)

cmd.color ("blue", "resi 282 & chain B")

cmd.select ("Outward", "resi 282 & chain B", merge=1)

cmd.color ("blue", "resi 283 & chain B")

cmd.select ("Outward", "resi 283 & chain B", merge=1)

cmd.color ("blue", "resi 284 & chain B")

cmd.select ("Outward", "resi 284 & chain B", merge=1)

cmd.color ("blue", "resi 285 & chain B")

cmd.select ("Outward", "resi 285 & chain B", merge=1)

cmd.color ("blue", "resi 286 & chain B")

cmd.select ("Outward", "resi 286 & chain B", merge=1)

cmd.color ("blue", "resi 287 & chain B")

cmd.select ("Outward", "resi 287 & chain B", merge=1)

cmd.color ("blue", "resi 288 & chain B")

cmd.select ("Outward", "resi 288 & chain B", merge=1)

cmd.color ("blue", "resi 289 & chain B")

cmd.select ("Outward", "resi 289 & chain B", merge=1)

cmd.color ("blue", "resi 290 & chain B")

cmd.select ("Outward", "resi 290 & chain B", merge=1)

cmd.color ("blue", "resi 291 & chain B")

cmd.select ("Outward", "resi 291 & chain B", merge=1)

cmd.color ("blue", "resi 292 & chain B")

cmd.select ("Outward", "resi 292 & chain B", merge=1)

cmd.color ("blue", "resi 293 & chain B")

cmd.select ("Outward", "resi 293 & chain B", merge=1)

cmd.color ("blue", "resi 294 & chain B")

cmd.select ("Outward", "resi 294 & chain B", merge=1)

cmd.color ("blue", "resi 247 & chain B")

cmd.select ("Outward", "resi 247 & chain B", merge=1)

cmd.color ("blue", "resi 248 & chain B")

cmd.select ("Outward", "resi 248 & chain B", merge=1)

cmd.color ("blue", "resi 249 & chain B")

cmd.select ("Outward", "resi 249 & chain B", merge=1)

cmd.color ("blue", "resi 250 & chain B")

cmd.select ("Outward", "resi 250 & chain B", merge=1)

cmd.color ("blue", "resi 251 & chain B")

cmd.select ("Outward", "resi 251 & chain B", merge=1)

cmd.color ("blue", "resi 252 & chain B")

cmd.select ("Outward", "resi 252 & chain B", merge=1)

cmd.color ("blue", "resi 253 & chain B")

cmd.select ("Outward", "resi 253 & chain B", merge=1)

cmd.color ("blue", "resi 254 & chain B")

cmd.select ("Outward", "resi 254 & chain B", merge=1)

cmd.color ("blue", "resi 255 & chain B")

cmd.select ("Outward", "resi 255 & chain B", merge=1)

cmd.color ("blue", "resi 256 & chain B")

cmd.select ("Outward", "resi 256 & chain B", merge=1)

cmd.color ("blue", "resi 257 & chain B")

cmd.select ("Outward", "resi 257 & chain B", merge=1)

cmd.color ("blue", "resi 61 & chain B")

cmd.select ("Outward", "resi 61 & chain B", merge=1)

cmd.color ("blue", "resi 62 & chain B")

cmd.select ("Outward", "resi 62 & chain B", merge=1)

cmd.color ("blue", "resi 63 & chain B")

cmd.select ("Outward", "resi 63 & chain B", merge=1)

cmd.color ("blue", "resi 64 & chain B")

cmd.select ("Outward", "resi 64 & chain B", merge=1)

cmd.color ("blue", "resi 65 & chain B")

cmd.select ("Outward", "resi 65 & chain B", merge=1)

cmd.color ("blue", "resi 66 & chain B")

cmd.select ("Outward", "resi 66 & chain B", merge=1)

cmd.color ("blue", "resi 67 & chain B")

cmd.select ("Outward", "resi 67 & chain B", merge=1)

cmd.color ("blue", "resi 68 & chain B")

cmd.select ("Outward", "resi 68 & chain B", merge=1)

cmd.color ("blue", "resi 69 & chain B")

cmd.select ("Outward", "resi 69 & chain B", merge=1)

cmd.color ("blue", "resi 70 & chain B")

cmd.select ("Outward", "resi 70 & chain B", merge=1)

cmd.color ("blue", "resi 71 & chain B")

cmd.select ("Outward", "resi 71 & chain B", merge=1)

cmd.color ("blue", "resi 72 & chain B")

cmd.select ("Outward", "resi 72 & chain B", merge=1)

cmd.color ("blue", "resi 73 & chain B")

cmd.select ("Outward", "resi 73 & chain B", merge=1)

cmd.color ("blue", "resi 74 & chain B")

cmd.select ("Outward", "resi 74 & chain B", merge=1)

cmd.color ("blue", "resi 75 & chain B")

cmd.select ("Outward", "resi 75 & chain B", merge=1)

cmd.color ("blue", "resi 76 & chain B")

cmd.select ("Outward", "resi 76 & chain B", merge=1)

cmd.color ("blue", "resi 41 & chain B")

cmd.select ("Outward", "resi 41 & chain B", merge=1)

cmd.color ("blue", "resi 42 & chain B")

cmd.select ("Outward", "resi 42 & chain B", merge=1)

cmd.color ("blue", "resi 43 & chain B")

cmd.select ("Outward", "resi 43 & chain B", merge=1)

cmd.color ("blue", "resi 44 & chain B")

cmd.select ("Outward", "resi 44 & chain B", merge=1)

cmd.color ("blue", "resi 45 & chain B")

cmd.select ("Outward", "resi 45 & chain B", merge=1)

cmd.color ("blue", "resi 46 & chain B")

cmd.select ("Outward", "resi 46 & chain B", merge=1)

cmd.color ("blue", "resi 47 & chain B")

cmd.select ("Outward", "resi 47 & chain B", merge=1)

cmd.color ("blue", "resi 48 & chain B")

cmd.select ("Outward", "resi 48 & chain B", merge=1)

cmd.color ("blue", "resi 49 & chain B")

cmd.select ("Outward", "resi 49 & chain B", merge=1)

cmd.color ("blue", "resi 50 & chain B")

cmd.select ("Outward", "resi 50 & chain B", merge=1)

cmd.color ("blue", "resi 51 & chain B")

cmd.select ("Outward", "resi 51 & chain B", merge=1)

cmd.color ("blue", "resi 52 & chain B")

cmd.select ("Outward", "resi 52 & chain B", merge=1)

cmd.color ("blue", "resi 53 & chain B")

cmd.select ("Outward", "resi 53 & chain B", merge=1)

cmd.color ("blue", "resi 41 & chain C")

cmd.select ("Outward", "resi 41 & chain C", merge=1)

cmd.color ("blue", "resi 42 & chain C")

cmd.select ("Outward", "resi 42 & chain C", merge=1)

cmd.color ("blue", "resi 43 & chain C")

cmd.select ("Outward", "resi 43 & chain C", merge=1)

cmd.color ("blue", "resi 44 & chain C")

cmd.select ("Outward", "resi 44 & chain C", merge=1)

cmd.color ("blue", "resi 45 & chain C")

cmd.select ("Outward", "resi 45 & chain C", merge=1)

cmd.color ("blue", "resi 46 & chain C")

cmd.select ("Outward", "resi 46 & chain C", merge=1)

cmd.color ("blue", "resi 47 & chain C")

cmd.select ("Outward", "resi 47 & chain C", merge=1)

cmd.color ("blue", "resi 48 & chain C")

cmd.select ("Outward", "resi 48 & chain C", merge=1)

cmd.color ("blue", "resi 49 & chain C")

cmd.select ("Outward", "resi 49 & chain C", merge=1)

cmd.color ("blue", "resi 50 & chain C")

cmd.select ("Outward", "resi 50 & chain C", merge=1)

cmd.color ("blue", "resi 51 & chain C")

cmd.select ("Outward", "resi 51 & chain C", merge=1)

cmd.color ("blue", "resi 52 & chain C")

cmd.select ("Outward", "resi 52 & chain C", merge=1)

cmd.color ("blue", "resi 53 & chain C")

cmd.select ("Outward", "resi 53 & chain C", merge=1)

cmd.color ("blue", "resi 61 & chain C")

cmd.select ("Outward", "resi 61 & chain C", merge=1)

cmd.color ("blue", "resi 62 & chain C")

cmd.select ("Outward", "resi 62 & chain C", merge=1)

cmd.color ("blue", "resi 63 & chain C")

cmd.select ("Outward", "resi 63 & chain C", merge=1)

cmd.color ("blue", "resi 64 & chain C")

cmd.select ("Outward", "resi 64 & chain C", merge=1)

cmd.color ("blue", "resi 65 & chain C")

cmd.select ("Outward", "resi 65 & chain C", merge=1)

cmd.color ("blue", "resi 66 & chain C")

cmd.select ("Outward", "resi 66 & chain C", merge=1)

cmd.color ("blue", "resi 67 & chain C")

cmd.select ("Outward", "resi 67 & chain C", merge=1)

cmd.color ("blue", "resi 68 & chain C")

cmd.select ("Outward", "resi 68 & chain C", merge=1)

cmd.color ("blue", "resi 69 & chain C")

cmd.select ("Outward", "resi 69 & chain C", merge=1)

cmd.color ("blue", "resi 70 & chain C")

cmd.select ("Outward", "resi 70 & chain C", merge=1)

cmd.color ("blue", "resi 71 & chain C")

cmd.select ("Outward", "resi 71 & chain C", merge=1)

cmd.color ("blue", "resi 72 & chain C")

cmd.select ("Outward", "resi 72 & chain C", merge=1)

cmd.color ("blue", "resi 73 & chain C")

cmd.select ("Outward", "resi 73 & chain C", merge=1)

cmd.color ("blue", "resi 74 & chain C")

cmd.select ("Outward", "resi 74 & chain C", merge=1)

cmd.color ("blue", "resi 75 & chain C")

cmd.select ("Outward", "resi 75 & chain C", merge=1)

cmd.color ("blue", "resi 76 & chain C")

cmd.select ("Outward", "resi 76 & chain C", merge=1)

cmd.color ("blue", "resi 247 & chain C")

cmd.select ("Outward", "resi 247 & chain C", merge=1)

cmd.color ("blue", "resi 248 & chain C")

cmd.select ("Outward", "resi 248 & chain C", merge=1)

cmd.color ("blue", "resi 249 & chain C")

cmd.select ("Outward", "resi 249 & chain C", merge=1)

cmd.color ("blue", "resi 250 & chain C")

cmd.select ("Outward", "resi 250 & chain C", merge=1)

cmd.color ("blue", "resi 251 & chain C")

cmd.select ("Outward", "resi 251 & chain C", merge=1)

cmd.color ("blue", "resi 252 & chain C")

cmd.select ("Outward", "resi 252 & chain C", merge=1)

cmd.color ("blue", "resi 253 & chain C")

cmd.select ("Outward", "resi 253 & chain C", merge=1)

cmd.color ("blue", "resi 254 & chain C")

cmd.select ("Outward", "resi 254 & chain C", merge=1)

cmd.color ("blue", "resi 255 & chain C")

cmd.select ("Outward", "resi 255 & chain C", merge=1)

cmd.color ("blue", "resi 256 & chain C")

cmd.select ("Outward", "resi 256 & chain C", merge=1)

cmd.color ("blue", "resi 257 & chain C")

cmd.select ("Outward", "resi 257 & chain C", merge=1)

cmd.color ("blue", "resi 280 & chain C")

cmd.select ("Outward", "resi 280 & chain C", merge=1)

cmd.color ("blue", "resi 281 & chain C")

cmd.select ("Outward", "resi 281 & chain C", merge=1)

cmd.color ("blue", "resi 282 & chain C")

cmd.select ("Outward", "resi 282 & chain C", merge=1)

cmd.color ("blue", "resi 283 & chain C")

cmd.select ("Outward", "resi 283 & chain C", merge=1)

cmd.color ("blue", "resi 284 & chain C")

cmd.select ("Outward", "resi 284 & chain C", merge=1)

cmd.color ("blue", "resi 285 & chain C")

cmd.select ("Outward", "resi 285 & chain C", merge=1)

cmd.color ("blue", "resi 286 & chain C")

cmd.select ("Outward", "resi 286 & chain C", merge=1)

cmd.color ("blue", "resi 287 & chain C")

cmd.select ("Outward", "resi 287 & chain C", merge=1)

cmd.color ("blue", "resi 288 & chain C")

cmd.select ("Outward", "resi 288 & chain C", merge=1)

cmd.color ("blue", "resi 289 & chain C")

cmd.select ("Outward", "resi 289 & chain C", merge=1)

cmd.color ("blue", "resi 290 & chain C")

cmd.select ("Outward", "resi 290 & chain C", merge=1)

cmd.color ("blue", "resi 291 & chain C")

cmd.select ("Outward", "resi 291 & chain C", merge=1)

cmd.color ("blue", "resi 292 & chain C")

cmd.select ("Outward", "resi 292 & chain C", merge=1)

cmd.color ("blue", "resi 293 & chain C")

cmd.select ("Outward", "resi 293 & chain C", merge=1)

cmd.color ("blue", "resi 294 & chain C")

cmd.select ("Outward", "resi 294 & chain C", merge=1)

cmd.load_cgo( [9.0, -32.987667,35.267834,33.310833, -50.38075, 22.212667, 25.388754, 1, 1,1,0,0,0,1], "axis" )
