from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12+13+14+15+16+17+18+19+20+21+22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 116+117+118+119+120+121+122+123+124+125+126 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 103+104+105+106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 172+173+174+175+176+177+178+179+180+181+182+183 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 156+157+158+159+160+161+162+163+164+165+166+167 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 139+140+141+142+145+146+147+148+149+150+151 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 195+196+197+198+199+200+201+202+203+204+205 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 213+214+215+216+217+218+219+220+221+222+223 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 41+42+43+44+45+46+47+48 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 25+26+27+28+29+30+31+32+33+34+35 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
