from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RL9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 20+21+22+23+24+25+26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 164+165+166+167+168+169+170+171+172+173+174+179+180+181+182+122+121+120+183+119+184+185+187+186+189+188 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 129+128+136+127+137+126+138+125+139+140+141+142+143+144+145+146+149+147+151+148+153+152+150+154+155+156 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 95+96+97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 66+67+68+69+70+71+72+73+74+75+76+77+78+79+80+81 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 216+217+218+219+220+221+222+223+224+225+226 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 42+43+44+45+46+47+48+49+50+51+52+53+54+55+56 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 29+30+31+32+33+34+35+36+37+38+39 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")