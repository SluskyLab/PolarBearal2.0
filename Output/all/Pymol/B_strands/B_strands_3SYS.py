from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13+14+15+16+17+18+19+20+21+22+23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 361+362+363+364+365+366+367+368+369+370+371 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 319+320+321+322+323+324+325+326+327+328+329+330+331 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 145+146+147+148+149+150+151+152+153+154+155+156 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 260+261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 206+207+208+209+210+211+212+213+214+215+216+217+218+219 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 222+223+224+225+226+227+228+229+230+231+232+233+234+235 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 193+194+195+196+197+198+199+200+201+202 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 245+246+247+248+249+250+251+252+253+254+255+256+257 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 179+180+181+182+183+184+185+186+187+188 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 301+302+303+304+305+306+307+308+309+310 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 131+132+133+134+135+136+137+138+139 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 91+92+93+94+95+96+97+98+99+100+101+102+103 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 55+56+57+58+59+60+61+62+63+64+65+66+67+68 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 377+378+379+380+381+382+383+384+385+386+387+388+389 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")