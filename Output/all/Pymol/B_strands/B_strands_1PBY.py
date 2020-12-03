from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PBY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 175+176+177+178+179+180+181+182+183 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 187+188+189+190+191+192+193+194+195+196+197+198 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 260+261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 214+215+216+217+218+219+220+221+222+223+224 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 228+229+230+231+232+233+234+235 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 238+239+240+241+242+243+244+245+246+247 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 250+251+252+253+254+255+256+257 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
