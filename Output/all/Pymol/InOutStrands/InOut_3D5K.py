from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3D5K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain A ")


cmd.select("Astrand1", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain A ")


cmd.select("Astrand2", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain A ")


cmd.select("Astrand3", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A ")


cmd.select("Bstrand7", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain B ")


cmd.select("Bstrand6", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain B ")


cmd.select("Bstrand5", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain B ")


cmd.select("Bstrand4", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain B ")


cmd.select("Cstrand8", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain C ")


cmd.select("Cstrand9", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain C ")


cmd.select("Cstrand10", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain C ")


cmd.select("Cstrand11", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain C ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 95 & chain A")

cmd.select ("Outward", "resi 95 & chain A", merge=1)

cmd.color ("blue", "resi 96 & chain A")

cmd.select ("Outward", "resi 96 & chain A", merge=1)

cmd.color ("blue", "resi 97 & chain A")

cmd.select ("Outward", "resi 97 & chain A", merge=1)

cmd.color ("blue", "resi 98 & chain A")

cmd.select ("Outward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 99 & chain A")

cmd.select ("Outward", "resi 99 & chain A", merge=1)

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

cmd.color ("blue", "resi 122 & chain A")

cmd.select ("Outward", "resi 122 & chain A", merge=1)

cmd.color ("blue", "resi 123 & chain A")

cmd.select ("Outward", "resi 123 & chain A", merge=1)

cmd.color ("blue", "resi 124 & chain A")

cmd.select ("Outward", "resi 124 & chain A", merge=1)

cmd.color ("blue", "resi 125 & chain A")

cmd.select ("Outward", "resi 125 & chain A", merge=1)

cmd.color ("blue", "resi 126 & chain A")

cmd.select ("Outward", "resi 126 & chain A", merge=1)

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

cmd.color ("blue", "resi 310 & chain A")

cmd.select ("Outward", "resi 310 & chain A", merge=1)

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

cmd.color ("blue", "resi 333 & chain A")

cmd.select ("Outward", "resi 333 & chain A", merge=1)

cmd.color ("blue", "resi 334 & chain A")

cmd.select ("Outward", "resi 334 & chain A", merge=1)

cmd.color ("blue", "resi 335 & chain A")

cmd.select ("Outward", "resi 335 & chain A", merge=1)

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

cmd.color ("blue", "resi 333 & chain B")

cmd.select ("Outward", "resi 333 & chain B", merge=1)

cmd.color ("blue", "resi 334 & chain B")

cmd.select ("Outward", "resi 334 & chain B", merge=1)

cmd.color ("blue", "resi 335 & chain B")

cmd.select ("Outward", "resi 335 & chain B", merge=1)

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

cmd.color ("blue", "resi 307 & chain B")

cmd.select ("Outward", "resi 307 & chain B", merge=1)

cmd.color ("blue", "resi 308 & chain B")

cmd.select ("Outward", "resi 308 & chain B", merge=1)

cmd.color ("blue", "resi 309 & chain B")

cmd.select ("Outward", "resi 309 & chain B", merge=1)

cmd.color ("blue", "resi 310 & chain B")

cmd.select ("Outward", "resi 310 & chain B", merge=1)

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

cmd.color ("blue", "resi 122 & chain B")

cmd.select ("Outward", "resi 122 & chain B", merge=1)

cmd.color ("blue", "resi 123 & chain B")

cmd.select ("Outward", "resi 123 & chain B", merge=1)

cmd.color ("blue", "resi 124 & chain B")

cmd.select ("Outward", "resi 124 & chain B", merge=1)

cmd.color ("blue", "resi 125 & chain B")

cmd.select ("Outward", "resi 125 & chain B", merge=1)

cmd.color ("blue", "resi 126 & chain B")

cmd.select ("Outward", "resi 126 & chain B", merge=1)

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

cmd.color ("blue", "resi 95 & chain B")

cmd.select ("Outward", "resi 95 & chain B", merge=1)

cmd.color ("blue", "resi 96 & chain B")

cmd.select ("Outward", "resi 96 & chain B", merge=1)

cmd.color ("blue", "resi 97 & chain B")

cmd.select ("Outward", "resi 97 & chain B", merge=1)

cmd.color ("blue", "resi 98 & chain B")

cmd.select ("Outward", "resi 98 & chain B", merge=1)

cmd.color ("blue", "resi 99 & chain B")

cmd.select ("Outward", "resi 99 & chain B", merge=1)

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

cmd.color ("blue", "resi 95 & chain C")

cmd.select ("Outward", "resi 95 & chain C", merge=1)

cmd.color ("blue", "resi 96 & chain C")

cmd.select ("Outward", "resi 96 & chain C", merge=1)

cmd.color ("blue", "resi 97 & chain C")

cmd.select ("Outward", "resi 97 & chain C", merge=1)

cmd.color ("blue", "resi 98 & chain C")

cmd.select ("Outward", "resi 98 & chain C", merge=1)

cmd.color ("blue", "resi 99 & chain C")

cmd.select ("Outward", "resi 99 & chain C", merge=1)

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

cmd.color ("blue", "resi 121 & chain C")

cmd.select ("Outward", "resi 121 & chain C", merge=1)

cmd.color ("blue", "resi 122 & chain C")

cmd.select ("Outward", "resi 122 & chain C", merge=1)

cmd.color ("blue", "resi 123 & chain C")

cmd.select ("Outward", "resi 123 & chain C", merge=1)

cmd.color ("blue", "resi 124 & chain C")

cmd.select ("Outward", "resi 124 & chain C", merge=1)

cmd.color ("blue", "resi 125 & chain C")

cmd.select ("Outward", "resi 125 & chain C", merge=1)

cmd.color ("blue", "resi 126 & chain C")

cmd.select ("Outward", "resi 126 & chain C", merge=1)

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

cmd.color ("blue", "resi 307 & chain C")

cmd.select ("Outward", "resi 307 & chain C", merge=1)

cmd.color ("blue", "resi 308 & chain C")

cmd.select ("Outward", "resi 308 & chain C", merge=1)

cmd.color ("blue", "resi 309 & chain C")

cmd.select ("Outward", "resi 309 & chain C", merge=1)

cmd.color ("blue", "resi 310 & chain C")

cmd.select ("Outward", "resi 310 & chain C", merge=1)

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

cmd.color ("blue", "resi 332 & chain C")

cmd.select ("Outward", "resi 332 & chain C", merge=1)

cmd.color ("blue", "resi 333 & chain C")

cmd.select ("Outward", "resi 333 & chain C", merge=1)

cmd.color ("blue", "resi 334 & chain C")

cmd.select ("Outward", "resi 334 & chain C", merge=1)

cmd.color ("blue", "resi 335 & chain C")

cmd.select ("Outward", "resi 335 & chain C", merge=1)

cmd.load_cgo( [9.0, -24.972666,-1.0095829,-6.5274167, -27.08375, -0.51166654, 15.985999, 1, 1,1,0,0,0,1], "axis" )
