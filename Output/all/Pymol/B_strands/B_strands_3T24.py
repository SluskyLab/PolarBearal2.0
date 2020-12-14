from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T24.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 379+380+381+382+383+384+385+386+387+388+389+390+391+392 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 58+59+60+61+62+63+64+65+66 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 104+105+106+107+108+111+109+110+150+151+152+153+154+161+155+156+160+159+158+157 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 89+90+91+92+93+94+129+130+95+131+96+132+97+133+98+134+135+99+136+100+137+101 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 185+186+187+188+189+190+191+192+193+194+195 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 211+212+213+214+215+273+272+216+271+217+270+218+269+219+268+220+267+266+221+265+222+264+223+263+224+225 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 228+229+260+259+230+258+231+257+256+232+311+310+312+309+233+255+308+307+234+254+306+235+253+305+252+236+304+251+303+237+250+238+249+239+248+240+247+241+246+242+245+243+244 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 321+322+323+324+325+326+327+328+329+330+331+332+333+334 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 341+342+343+344+345+346+347+348+349+350+351+352+353+354 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 364+365+366+367+368+369+370+371+372+373+374 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42+43 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
