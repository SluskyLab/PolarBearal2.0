from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand1", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain A ")


cmd.select("Bstrand11", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain B ")


cmd.select("Bstrand10", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain B ")


cmd.select("Astrand4", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain A ")


cmd.select("Astrand5", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain A ")


cmd.select("Cstrand17", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain C ")


cmd.select("Cstrand16", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain C ")


cmd.select("Cstrand14", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117 & chain C ")


cmd.select("Bstrand7", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain B ")


cmd.select("Cstrand13", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain C ")


cmd.select("Bstrand8", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118 & chain B ")


cmd.select("Astrand2", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117 & chain A ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 81 & chain A")

cmd.select ("Outward", "resi 81 & chain A", merge=1)

cmd.color ("blue", "resi 82 & chain A")

cmd.select ("Outward", "resi 82 & chain A", merge=1)

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

cmd.color ("blue", "resi 95 & chain A")

cmd.select ("Outward", "resi 95 & chain A", merge=1)

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

cmd.color ("blue", "resi 292 & chain B")

cmd.select ("Outward", "resi 292 & chain B", merge=1)

cmd.color ("blue", "resi 293 & chain B")

cmd.select ("Outward", "resi 293 & chain B", merge=1)

cmd.color ("blue", "resi 294 & chain B")

cmd.select ("Outward", "resi 294 & chain B", merge=1)

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

cmd.color ("blue", "resi 292 & chain A")

cmd.select ("Outward", "resi 292 & chain A", merge=1)

cmd.color ("blue", "resi 293 & chain A")

cmd.select ("Outward", "resi 293 & chain A", merge=1)

cmd.color ("blue", "resi 294 & chain A")

cmd.select ("Outward", "resi 294 & chain A", merge=1)

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

cmd.color ("blue", "resi 292 & chain C")

cmd.select ("Outward", "resi 292 & chain C", merge=1)

cmd.color ("blue", "resi 293 & chain C")

cmd.select ("Outward", "resi 293 & chain C", merge=1)

cmd.color ("blue", "resi 294 & chain C")

cmd.select ("Outward", "resi 294 & chain C", merge=1)

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

cmd.color ("blue", "resi 99 & chain C")

cmd.select ("Outward", "resi 99 & chain C", merge=1)

cmd.color ("blue", "resi 100 & chain C")

cmd.select ("Outward", "resi 100 & chain C", merge=1)

cmd.color ("blue", "resi 101 & chain C")

cmd.select ("Outward", "resi 101 & chain C", merge=1)

cmd.color ("blue", "resi 102 & chain C")

cmd.select ("Outward", "resi 102 & chain C", merge=1)

cmd.color ("blue", "resi 103 & chain C")

cmd.select ("Outward", "resi 103 & chain C", merge=1)

cmd.color ("blue", "resi 104 & chain C")

cmd.select ("Outward", "resi 104 & chain C", merge=1)

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

cmd.color ("blue", "resi 81 & chain B")

cmd.select ("Outward", "resi 81 & chain B", merge=1)

cmd.color ("blue", "resi 82 & chain B")

cmd.select ("Outward", "resi 82 & chain B", merge=1)

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

cmd.color ("blue", "resi 95 & chain B")

cmd.select ("Outward", "resi 95 & chain B", merge=1)

cmd.color ("blue", "resi 81 & chain C")

cmd.select ("Outward", "resi 81 & chain C", merge=1)

cmd.color ("blue", "resi 82 & chain C")

cmd.select ("Outward", "resi 82 & chain C", merge=1)

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

cmd.color ("blue", "resi 95 & chain C")

cmd.select ("Outward", "resi 95 & chain C", merge=1)

cmd.color ("blue", "resi 99 & chain B")

cmd.select ("Outward", "resi 99 & chain B", merge=1)

cmd.color ("blue", "resi 100 & chain B")

cmd.select ("Outward", "resi 100 & chain B", merge=1)

cmd.color ("blue", "resi 101 & chain B")

cmd.select ("Outward", "resi 101 & chain B", merge=1)

cmd.color ("blue", "resi 102 & chain B")

cmd.select ("Outward", "resi 102 & chain B", merge=1)

cmd.color ("blue", "resi 103 & chain B")

cmd.select ("Outward", "resi 103 & chain B", merge=1)

cmd.color ("blue", "resi 104 & chain B")

cmd.select ("Outward", "resi 104 & chain B", merge=1)

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

cmd.color ("blue", "resi 99 & chain A")

cmd.select ("Outward", "resi 99 & chain A", merge=1)

cmd.color ("blue", "resi 100 & chain A")

cmd.select ("Outward", "resi 100 & chain A", merge=1)

cmd.color ("blue", "resi 101 & chain A")

cmd.select ("Outward", "resi 101 & chain A", merge=1)

cmd.color ("blue", "resi 102 & chain A")

cmd.select ("Outward", "resi 102 & chain A", merge=1)

cmd.color ("blue", "resi 103 & chain A")

cmd.select ("Outward", "resi 103 & chain A", merge=1)

cmd.color ("blue", "resi 104 & chain A")

cmd.select ("Outward", "resi 104 & chain A", merge=1)

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

cmd.load_cgo( [9.0, 0,0,0, 0, 0, 0, 1, 1,1,0,0,0,1], "axis" )
