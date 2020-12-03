from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2O62.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 144+145+146+147+148+149+150+151+152+153+154 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 161+162+163+164+165+166+167+168+169+170+171 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 177+178+179+180+181+182+183 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 186+187+188+189+190+191+192+193+194+195 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 198+199+200+201 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 209+210+211+212+213 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 218+219+220+221+222+223 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 232+233+234+235+236+237+238+239+240+241 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 244+245+246+247+248+249+250+251+252 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 258+259+260+261+262+263+264+265+266+267+268 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
