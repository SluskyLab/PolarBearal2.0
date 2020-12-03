from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PBY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 175+175+176+177+178+179+180+181+182+183+187+188+189+190+191+192+193+194+195+196+197+198+201+202+203+204+205+206+207+208+209+214+215+216+217+218+219+220+221+222+223+224+228+229+230+231+232+233+234+235+238+239+240+241+242+243+244+245+246+247+250+251+252+253+254+255+256+257+260+261+262+263+264+265+266+267+268+269+270+271 & chain A")
cmd.load_cgo( [9.0, 55.941013,43.12857,11.045204, 59.659313, 6.749811, 21.437355, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
