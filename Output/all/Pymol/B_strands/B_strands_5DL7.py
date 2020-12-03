from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19+20+21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 391+392+393+394+395+396+397+398+399+400+401+402+403 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 51+52+53+54+55+56+57+58+59+60+61+62+63+64 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 90+91+92+93+94+95+96+97+98+99+100+101+102 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 105+106+107+108+109+110+111+112 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 130+131+132+133+134+135+136+137+138 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 183+184+185+186+187+188+189+190+191 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 195+196+197+198+199+200+201+202+203+204 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 208+209+210+211+212+213+214+215+216+217+218+219+220 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 225+226+227+228+229+230+231+232+233+234+235+236+237+238 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 248+249+250+251+252+253+254+255+256+257+258+259+260 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 263+264+265+266+267+268+269+270+271+272+273 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 144+145+146+147+148+149+150+151+152+153+154+155 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 303+304+305+306+307+308+309+310+311+312 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 348+349+350+351+352+353+354+355+356+357+358+359+360 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 369+370+371+372+373+374+375+376+377+378+379+380 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 31+32+33+34+35+36+37+38+39+40+41+42+43 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
