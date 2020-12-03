from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2O62.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 144+144+145+146+147+148+149+150+151+152+153+154+161+162+163+164+165+166+167+168+169+170+171+177+178+179+180+181+182+183+186+187+188+189+190+191+192+193+194+195+198+199+200+201+209+210+211+212+213+218+219+220+221+222+223+232+233+234+235+236+237+238+239+240+241+244+245+246+247+248+249+250+251+252+258+259+260+261+262+263+264+265+266+267+268 & chain A")
cmd.load_cgo( [9.0, -7.233246,24.250448,26.472609, 6.7956266, -15.190996, 25.075579, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
