from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RL8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35+36+37+38+253+254+255+256+257+258+259+260+261+262+263+264+265+266+267 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 67+68+69+70+71+72+73+74+75+76+77+78+79 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87+88+89+90+93+94+95+96+99+100+101+102 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 109+110+111+112+113+114+115+116+117+118 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 152+153+154+155+156+157+158+159+160+161+162+163 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 137+138+139+140+141+142+143+144+145+146+147+148 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 181+182+183+184+185+186+187+188+189+190+191+192+193 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 196+197+198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 238+239+240+241+242+243+244+245+246+247+248+249+250 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
