from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3D5K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Cstrand4", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Cstrand5", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Cstrand6", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Cstrand7", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain C ")
cmd.color ("green", "Cstrand7")


cmd.select("Bstrand8", "resi 88+89+90+91+92+93+94+95+96+97+98+99 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 299+300+301+302+303+304+305+306+307+308+309+310 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("barrel", "Astrand* or Cstrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
