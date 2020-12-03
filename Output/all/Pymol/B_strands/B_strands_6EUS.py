from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EUS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+85+86 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 105+106+107+108+109+114+115+116+117+118+119+120+121+122+123 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 126+127+128+129+130+131+132+133+134+135 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 148+149+150+151+152+153+154+155+156 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 159+160+161+162+163+164+165 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 189+190+191+192+193+194+195+196+197+198+199+200 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 203+204+205+206+207+208+209+210 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 229+230+231+232+233+234+235+236+237+238 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 243+244+245+246+247+248+249+250+251+252+253+254+255+256 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 261+262+263+264+265+266+267+268+269+270+271+272+273+274 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 284+285+286+287+288+289+290 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 330+331+332+333+334+335+336+337+338+339+340+341+303+304+305+306 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 355+356+357+358+359+360+361+362+363+364+365+366+367 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 375+376+377+378+379+380+381+382+383+384+385+386 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 391+392+393+394+395+396+397+398+399 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
