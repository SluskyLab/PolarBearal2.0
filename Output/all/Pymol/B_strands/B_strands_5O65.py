from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O65.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 108+109+110+111+112+113+114+115+116+117+118+119 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 164+165+166+167+168+169+170+171+172+173+174+175+176+177+178+179+180+194+195+196+197+198+199+200+201+202+203 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 207+208+209+210+211+212+213+214+215 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 223+224+225+226+227+228+229+230+231 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 266+267+268+269+270+271+272+273+274+275+276+277 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 280+281+282+283+284+285+286+287+288+289+290+291 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 316+317+318+319+320+321+322+323+324+325+326 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 362+363+364+365+366+367+368+369+370+371+372+373+374 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 380+381+382+383+384+385+386+387+388 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 396+397+398+399+400+401+402+403+404+405 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
