from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XQB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 33+34+35+36+37+38 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 116+117+118+119+120+121+122+123 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 131+132+133+134+135+136+137 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 100+101+102+103+104+105+106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 56+57+58+59+60+61+62 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
