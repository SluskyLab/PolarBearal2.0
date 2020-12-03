from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H3I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Fstrand0", "resi 72+73+74+75+76+77+78 & chain F ")
cmd.color ("red", "Fstrand0")


cmd.select("Fstrand1", "resi 389+390+391+392+393+394 & chain F ")
cmd.color ("green", "Fstrand1")


cmd.select("Fstrand2", "resi 88+89+90+91+92+93+94+95+96+97+98 & chain F ")
cmd.color ("orange", "Fstrand2")


cmd.select("Fstrand3", "resi 367+368+369+370+371+372 & chain F ")
cmd.color ("teal", "Fstrand3")


cmd.select("Fstrand4", "resi 357+358+359+360+361+362 & chain F ")
cmd.color ("yellow", "Fstrand4")


cmd.select("Fstrand5", "resi 336+337+338+339+340+341+342+343+344 & chain F ")
cmd.color ("blue", "Fstrand5")


cmd.select("Fstrand6", "resi 246+247+248+249+250+251+252+253+254 & chain F ")
cmd.color ("red", "Fstrand6")


cmd.select("Fstrand7", "resi 323+324+325+326+327+328 & chain F ")
cmd.color ("green", "Fstrand7")


cmd.select("Fstrand8", "resi 201+202+203+204+205+206+207+208 & chain F ")
cmd.color ("orange", "Fstrand8")


cmd.select("Fstrand9", "resi 231+232+233+234+235+236+237+238+239+240 & chain F ")
cmd.color ("teal", "Fstrand9")


cmd.select("Fstrand10", "resi 178+179+180+181+182+183+184+185+186+187+188+189 & chain F ")
cmd.color ("yellow", "Fstrand10")


cmd.select("Fstrand11", "resi 152+153+154+155+156+157+158+159+160+161+162 & chain F ")
cmd.color ("blue", "Fstrand11")


cmd.select("Fstrand12", "resi 139+140+141+142+143+144+145+146 & chain F ")
cmd.color ("red", "Fstrand12")


cmd.select("Fstrand13", "resi 104+105+106+107+108+109+110+111+112+113+114+115+116 & chain F ")
cmd.color ("green", "Fstrand13")


cmd.select("barrel", "Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
