from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 151+152+153+154+155+156+157+158+159 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 340+341+342+343+344+345+346+347+348+349+350+351 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 166+167+168+169+170+171+172+173 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 312+313+314+315+316+317+318+319+320+321+322+323 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 181+182+183+184+185+186+187+188+189+190+191+192 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 195+196+197+198+199+200+201+202+203+204+205+206+207+208 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 211+212+213+214+215+216+217+218+219+220+221 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 227+228+229+230+231+232+233+234+235+236+237+238 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 241+242+243+244+245+246+247+248+249+252+253+254+257+255+256 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 285+286+287+288+289+290+380+381+291+382+292+383+384+293+385+386+294+387+295+388+389 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 326+327+328+329+330+331+332+333+334+335 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
