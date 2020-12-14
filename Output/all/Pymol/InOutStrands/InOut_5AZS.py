from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 83+84+85+86+87+88+89+90+91+92+93+94 & chain A ")


cmd.select("Astrand1", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121 & chain A ")


cmd.select("Astrand2", "resi 295+296+297+298+299+300+301+302+303+304+305+306 & chain A ")


cmd.select("Astrand3", "resi 318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain A ")


cmd.select("Bstrand4", "resi 83+84+85+86+87+88+89+90+91+92+93+94 & chain B ")


cmd.select("Bstrand5", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121 & chain B ")


cmd.select("Bstrand6", "resi 295+296+297+298+299+300+301+302+303+304+305+306 & chain B ")


cmd.select("Bstrand7", "resi 318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain B ")


cmd.select("Cstrand8", "resi 83+84+85+86+87+88+89+90+91+92+93+94 & chain C ")


cmd.select("Cstrand9", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120 & chain C ")


cmd.select("Cstrand10", "resi 295+296+297+298+299+300+301+302+303+304+305+306 & chain C ")


cmd.select("Cstrand11", "resi 318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain C ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 83 & chain A")

cmd.select ("Outward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 84 & chain A")

cmd.select ("Outward", "resi 84 & chain A", merge=1)

cmd.color ("blue", "resi 85 & chain A")

cmd.select ("Outward", "resi 85 & chain A", merge=1)

cmd.color ("blue", "resi 86 & chain A")

cmd.select ("Outward", "resi 86 & chain A", merge=1)

cmd.color ("blue", "resi 87 & chain A")

cmd.select ("Outward", "resi 87 & chain A", merge=1)

cmd.color ("blue", "resi 88 & chain A")

cmd.select ("Outward", "resi 88 & chain A", merge=1)

cmd.color ("blue", "resi 89 & chain A")

cmd.select ("Outward", "resi 89 & chain A", merge=1)

cmd.color ("blue", "resi 90 & chain A")

cmd.select ("Outward", "resi 90 & chain A", merge=1)

cmd.color ("blue", "resi 91 & chain A")

cmd.select ("Outward", "resi 91 & chain A", merge=1)

cmd.color ("blue", "resi 92 & chain A")

cmd.select ("Outward", "resi 92 & chain A", merge=1)

cmd.color ("blue", "resi 93 & chain A")

cmd.select ("Outward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("blue", "resi 112 & chain A")

cmd.select ("Outward", "resi 112 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("blue", "resi 114 & chain A")

cmd.select ("Outward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 115 & chain A")

cmd.select ("Outward", "resi 115 & chain A", merge=1)

cmd.color ("blue", "resi 116 & chain A")

cmd.select ("Outward", "resi 116 & chain A", merge=1)

cmd.color ("blue", "resi 117 & chain A")

cmd.select ("Outward", "resi 117 & chain A", merge=1)

cmd.color ("blue", "resi 118 & chain A")

cmd.select ("Outward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("blue", "resi 120 & chain A")

cmd.select ("Outward", "resi 120 & chain A", merge=1)

cmd.color ("blue", "resi 121 & chain A")

cmd.select ("Outward", "resi 121 & chain A", merge=1)

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

cmd.color ("blue", "resi 83 & chain B")

cmd.select ("Outward", "resi 83 & chain B", merge=1)

cmd.color ("blue", "resi 84 & chain B")

cmd.select ("Outward", "resi 84 & chain B", merge=1)

cmd.color ("blue", "resi 85 & chain B")

cmd.select ("Outward", "resi 85 & chain B", merge=1)

cmd.color ("blue", "resi 86 & chain B")

cmd.select ("Outward", "resi 86 & chain B", merge=1)

cmd.color ("blue", "resi 87 & chain B")

cmd.select ("Outward", "resi 87 & chain B", merge=1)

cmd.color ("blue", "resi 88 & chain B")

cmd.select ("Outward", "resi 88 & chain B", merge=1)

cmd.color ("blue", "resi 89 & chain B")

cmd.select ("Outward", "resi 89 & chain B", merge=1)

cmd.color ("blue", "resi 90 & chain B")

cmd.select ("Outward", "resi 90 & chain B", merge=1)

cmd.color ("blue", "resi 91 & chain B")

cmd.select ("Outward", "resi 91 & chain B", merge=1)

cmd.color ("blue", "resi 92 & chain B")

cmd.select ("Outward", "resi 92 & chain B", merge=1)

cmd.color ("blue", "resi 93 & chain B")

cmd.select ("Outward", "resi 93 & chain B", merge=1)

cmd.color ("blue", "resi 94 & chain B")

cmd.select ("Outward", "resi 94 & chain B", merge=1)

cmd.color ("blue", "resi 105 & chain B")

cmd.select ("Outward", "resi 105 & chain B", merge=1)

cmd.color ("blue", "resi 106 & chain B")

cmd.select ("Outward", "resi 106 & chain B", merge=1)

cmd.color ("blue", "resi 107 & chain B")

cmd.select ("Outward", "resi 107 & chain B", merge=1)

cmd.color ("blue", "resi 108 & chain B")

cmd.select ("Outward", "resi 108 & chain B", merge=1)

cmd.color ("blue", "resi 109 & chain B")

cmd.select ("Outward", "resi 109 & chain B", merge=1)

cmd.color ("blue", "resi 110 & chain B")

cmd.select ("Outward", "resi 110 & chain B", merge=1)

cmd.color ("blue", "resi 111 & chain B")

cmd.select ("Outward", "resi 111 & chain B", merge=1)

cmd.color ("blue", "resi 112 & chain B")

cmd.select ("Outward", "resi 112 & chain B", merge=1)

cmd.color ("blue", "resi 113 & chain B")

cmd.select ("Outward", "resi 113 & chain B", merge=1)

cmd.color ("blue", "resi 114 & chain B")

cmd.select ("Outward", "resi 114 & chain B", merge=1)

cmd.color ("blue", "resi 115 & chain B")

cmd.select ("Outward", "resi 115 & chain B", merge=1)

cmd.color ("blue", "resi 116 & chain B")

cmd.select ("Outward", "resi 116 & chain B", merge=1)

cmd.color ("blue", "resi 117 & chain B")

cmd.select ("Outward", "resi 117 & chain B", merge=1)

cmd.color ("blue", "resi 118 & chain B")

cmd.select ("Outward", "resi 118 & chain B", merge=1)

cmd.color ("blue", "resi 119 & chain B")

cmd.select ("Outward", "resi 119 & chain B", merge=1)

cmd.color ("blue", "resi 120 & chain B")

cmd.select ("Outward", "resi 120 & chain B", merge=1)

cmd.color ("blue", "resi 121 & chain B")

cmd.select ("Outward", "resi 121 & chain B", merge=1)

cmd.color ("blue", "resi 295 & chain B")

cmd.select ("Outward", "resi 295 & chain B", merge=1)

cmd.color ("blue", "resi 296 & chain B")

cmd.select ("Outward", "resi 296 & chain B", merge=1)

cmd.color ("blue", "resi 297 & chain B")

cmd.select ("Outward", "resi 297 & chain B", merge=1)

cmd.color ("blue", "resi 298 & chain B")

cmd.select ("Outward", "resi 298 & chain B", merge=1)

cmd.color ("blue", "resi 299 & chain B")

cmd.select ("Outward", "resi 299 & chain B", merge=1)

cmd.color ("blue", "resi 300 & chain B")

cmd.select ("Outward", "resi 300 & chain B", merge=1)

cmd.color ("blue", "resi 301 & chain B")

cmd.select ("Outward", "resi 301 & chain B", merge=1)

cmd.color ("blue", "resi 302 & chain B")

cmd.select ("Outward", "resi 302 & chain B", merge=1)

cmd.color ("blue", "resi 303 & chain B")

cmd.select ("Outward", "resi 303 & chain B", merge=1)

cmd.color ("blue", "resi 304 & chain B")

cmd.select ("Outward", "resi 304 & chain B", merge=1)

cmd.color ("blue", "resi 305 & chain B")

cmd.select ("Outward", "resi 305 & chain B", merge=1)

cmd.color ("blue", "resi 306 & chain B")

cmd.select ("Outward", "resi 306 & chain B", merge=1)

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

cmd.color ("blue", "resi 83 & chain C")

cmd.select ("Outward", "resi 83 & chain C", merge=1)

cmd.color ("blue", "resi 84 & chain C")

cmd.select ("Outward", "resi 84 & chain C", merge=1)

cmd.color ("blue", "resi 85 & chain C")

cmd.select ("Outward", "resi 85 & chain C", merge=1)

cmd.color ("blue", "resi 86 & chain C")

cmd.select ("Outward", "resi 86 & chain C", merge=1)

cmd.color ("blue", "resi 87 & chain C")

cmd.select ("Outward", "resi 87 & chain C", merge=1)

cmd.color ("blue", "resi 88 & chain C")

cmd.select ("Outward", "resi 88 & chain C", merge=1)

cmd.color ("blue", "resi 89 & chain C")

cmd.select ("Outward", "resi 89 & chain C", merge=1)

cmd.color ("blue", "resi 90 & chain C")

cmd.select ("Outward", "resi 90 & chain C", merge=1)

cmd.color ("blue", "resi 91 & chain C")

cmd.select ("Outward", "resi 91 & chain C", merge=1)

cmd.color ("blue", "resi 92 & chain C")

cmd.select ("Outward", "resi 92 & chain C", merge=1)

cmd.color ("blue", "resi 93 & chain C")

cmd.select ("Outward", "resi 93 & chain C", merge=1)

cmd.color ("blue", "resi 94 & chain C")

cmd.select ("Outward", "resi 94 & chain C", merge=1)

cmd.color ("blue", "resi 105 & chain C")

cmd.select ("Outward", "resi 105 & chain C", merge=1)

cmd.color ("blue", "resi 106 & chain C")

cmd.select ("Outward", "resi 106 & chain C", merge=1)

cmd.color ("blue", "resi 107 & chain C")

cmd.select ("Outward", "resi 107 & chain C", merge=1)

cmd.color ("blue", "resi 108 & chain C")

cmd.select ("Outward", "resi 108 & chain C", merge=1)

cmd.color ("blue", "resi 109 & chain C")

cmd.select ("Outward", "resi 109 & chain C", merge=1)

cmd.color ("blue", "resi 110 & chain C")

cmd.select ("Outward", "resi 110 & chain C", merge=1)

cmd.color ("blue", "resi 111 & chain C")

cmd.select ("Outward", "resi 111 & chain C", merge=1)

cmd.color ("blue", "resi 112 & chain C")

cmd.select ("Outward", "resi 112 & chain C", merge=1)

cmd.color ("blue", "resi 113 & chain C")

cmd.select ("Outward", "resi 113 & chain C", merge=1)

cmd.color ("blue", "resi 114 & chain C")

cmd.select ("Outward", "resi 114 & chain C", merge=1)

cmd.color ("blue", "resi 115 & chain C")

cmd.select ("Outward", "resi 115 & chain C", merge=1)

cmd.color ("blue", "resi 116 & chain C")

cmd.select ("Outward", "resi 116 & chain C", merge=1)

cmd.color ("blue", "resi 117 & chain C")

cmd.select ("Outward", "resi 117 & chain C", merge=1)

cmd.color ("blue", "resi 118 & chain C")

cmd.select ("Outward", "resi 118 & chain C", merge=1)

cmd.color ("blue", "resi 119 & chain C")

cmd.select ("Outward", "resi 119 & chain C", merge=1)

cmd.color ("blue", "resi 120 & chain C")

cmd.select ("Outward", "resi 120 & chain C", merge=1)

cmd.color ("blue", "resi 295 & chain C")

cmd.select ("Outward", "resi 295 & chain C", merge=1)

cmd.color ("blue", "resi 296 & chain C")

cmd.select ("Outward", "resi 296 & chain C", merge=1)

cmd.color ("blue", "resi 297 & chain C")

cmd.select ("Outward", "resi 297 & chain C", merge=1)

cmd.color ("blue", "resi 298 & chain C")

cmd.select ("Outward", "resi 298 & chain C", merge=1)

cmd.color ("blue", "resi 299 & chain C")

cmd.select ("Outward", "resi 299 & chain C", merge=1)

cmd.color ("blue", "resi 300 & chain C")

cmd.select ("Outward", "resi 300 & chain C", merge=1)

cmd.color ("blue", "resi 301 & chain C")

cmd.select ("Outward", "resi 301 & chain C", merge=1)

cmd.color ("blue", "resi 302 & chain C")

cmd.select ("Outward", "resi 302 & chain C", merge=1)

cmd.color ("blue", "resi 303 & chain C")

cmd.select ("Outward", "resi 303 & chain C", merge=1)

cmd.color ("blue", "resi 304 & chain C")

cmd.select ("Outward", "resi 304 & chain C", merge=1)

cmd.color ("blue", "resi 305 & chain C")

cmd.select ("Outward", "resi 305 & chain C", merge=1)

cmd.color ("blue", "resi 306 & chain C")

cmd.select ("Outward", "resi 306 & chain C", merge=1)

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

cmd.color ("blue", "resi 326 & chain C")

cmd.select ("Outward", "resi 326 & chain C", merge=1)

cmd.color ("blue", "resi 327 & chain C")

cmd.select ("Outward", "resi 327 & chain C", merge=1)

cmd.color ("blue", "resi 328 & chain C")

cmd.select ("Outward", "resi 328 & chain C", merge=1)

cmd.color ("blue", "resi 329 & chain C")

cmd.select ("Outward", "resi 329 & chain C", merge=1)

cmd.color ("blue", "resi 330 & chain C")

cmd.select ("Outward", "resi 330 & chain C", merge=1)

cmd.color ("blue", "resi 331 & chain C")

cmd.select ("Outward", "resi 331 & chain C", merge=1)

cmd.load_cgo( [9.0, 0,0,0, 0, 0, 0, 1, 1,1,0,0,0,1], "axis" )
