from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MT4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 84+85+86+87+88+89+90+91+92+93+94+95+96 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Bstrand4", "resi 84+85+86+87+88+89+90+91+92+93+94+95+96 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Cstrand8", "resi 84+85+86+87+88+89+90+91+92+93+94+95+96 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Cstrand9", "resi 109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("Cstrand10", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
