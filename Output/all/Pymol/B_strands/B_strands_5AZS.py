from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 83+84+85+86+87+88+89+90+91+92+93+94 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 295+296+297+298+299+300+301+302+303+304+305+306 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Bstrand4", "resi 83+84+85+86+87+88+89+90+91+92+93+94 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 295+296+297+298+299+300+301+302+303+304+305+306 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Cstrand8", "resi 83+84+85+86+87+88+89+90+91+92+93+94 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Cstrand9", "resi 105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("Cstrand10", "resi 295+296+297+298+299+300+301+302+303+304+305+306 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
