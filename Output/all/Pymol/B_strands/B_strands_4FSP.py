from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8+9+10+11+12+13+14+15+16+17+18+19+20+21+22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 362+363+364+365+366+367+368+369+370+371+372 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 31+32+33+34+35+36+37+89+38+90+39+91+129+92+40+93+41+130+181+94+131+42+95+182+183+43+132+133+96+184+185+97+134+135+187+186+98+188+136+189+99+190+191+100 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 194+195+196+197+142+198+143+199+144+145+200+146+103+201+104+147+105+202+110+106+148+149+203+107+109+56+52+51+108+54+53+150+152+55+58+57+151+59+60+61+62+63+64 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 246+247+248+249+250+251+252+253+254+255+256+257 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 224+225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 207+208+209+210+211+212+213+214+215+216+217+218+219 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 262+263+264+265+266+267+268+269+270+271+272 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 302+303+304+305+306+307+308+309+310+311 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 320+321+322+323+324+325+326+327+328+329+330 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 342+343+344+345+346+347+348+349+350+351+352 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 378+379+380+381+382+383+384+385+386+387+388+389+390 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
