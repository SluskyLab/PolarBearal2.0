from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2MAF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 65+66+67+68+69+70+71 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 115+116+117+118+119+120+121+122+123+124 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 131+132+133+134+135+136+137+138+139+140+141+142 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 191+192+193+194+195+196+197+198+199+200+201 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 206+207+208+209+210+211+212 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 230+231+232+233+234+235+236+237 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
