from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Bstrand1", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Astrand3", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Cstrand5", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Cstrand6", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Cstrand7", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117 & chain C ")
cmd.color ("green", "Cstrand7")


cmd.select("Bstrand8", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Cstrand9", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("Bstrand10", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Astrand11", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
