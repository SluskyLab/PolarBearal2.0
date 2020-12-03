from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UCU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 83+84+85+86+87+88+89+90+91+92+93 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 350+351+352+353+354+355+356+357+358+359+360+361+362 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 337+338+339+340+341+342+343+344+345 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 323+324+325+326+327+328+329+330+331 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 312+313+314+315+316+317+318+319 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 299+300+301+302+303+304+305+306+307+308 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 267+268+269+270+271+272+273+274+275 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 243+244+245+246+247+248+249 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 227+228+229+230+231+232+233+234+235+236+237 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 209+210+211+212+213+214+215+216+217+218+219 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 193+194+195+196+197+198+199+200+201+202+203 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 176+177+178+179+180+181+182+183+184+185+186+187 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 164+165+166+167+168+169+170+171+172 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 150+151+152+153+154+155+156+157 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 137+138+139+140+141+142+143 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 125+126+127+128+129+130+131+132 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 97+98+99+100+101+102+103+104+105+106 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
