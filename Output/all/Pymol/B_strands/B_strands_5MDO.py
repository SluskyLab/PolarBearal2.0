from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5MDO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 47+48+49+50+51+52+55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 292+293+294+295+296+297+298+299+300+301+302+303+304 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 268+269+270+271+272+273+274+275+276+277 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 70+71+72+73+74+75+76 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 96+97+98+99+100+101+102 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148+149+150+151+152+153+154+155+156 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 164+165+166+167+168+169+170+171+172 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 184+185+186+187+188+189+190+191+192+193+194 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 214+215+216+217+218+219+220+221+222+223+224+225+226+227+228 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 197+198+199+200+201+202+203+204+205+206+207+208+209+210+211 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 233+234+235+236+237+238+239+240+241+242+243+244+245+246 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 251+252+253+254+255+256+257+258+259+260+261+262+263+264+265 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 307+308+309+310+311+312+313+314+315+316+317 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 338+339+340+341+342+343+344+345+346+347+348+349 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
