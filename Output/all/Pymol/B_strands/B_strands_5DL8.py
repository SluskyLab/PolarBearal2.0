from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13+14+15+16+17+18+19+20+21+22+23+24 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 32+33+34+35+36+37+38+39+40+41+42+43+44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+72 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 96+97+98+99+100+101+102+103+104+105+106+48+107+49+108+50+51+52+53+54 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 111+112+113+114+115+116+117+118 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 136+137+138+139+140+141+142+143+144+145 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 150+151+152+153+154+155+156+157+158+159+160+161 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 185+186+187+188+189+190+191+192+193 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 211+212+213+214+215+216+217+218+219+220+221+222+223 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 228+229+230+231+232+233+234+235+236+237+238+239+240 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 248+249+250+251+252+253+254+255+256+257+258+259+260 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 263+264+265+266+267+268+269+270+271+272+273 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 304+305+306+307+308+309+310+311+312+313 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 321+322+323+324+325+326+327+328+329+330+331+332+333+334 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 340+341+342+343+344+345+346+347+348+349+350+351+352+353 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 362+363+364+365+366+367+368+369+370+371+372+373 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 379+380+381+382+383+384+385+386+387+388+389+390+391 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
