from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1TLY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13+14+15+16+17+18+19+20+21+22+23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35+36+37+38+39+40+41+42+43+44+45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48+49+50+51+52+53+54+55+56+57 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 179+180+181+182+183+184+185+186+187+188+189+190+191 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 77+78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 159+160+161+162+163+164+165+166+167+168+169+170+171+172+173+174+175+176 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 120+121+122+123+124+125+126+127+128+129+130+131 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 138+139+140+141+142+143+144+145+146+147+148+149+150+151 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 213+214+215+216+217+218+219+220+221+222+223 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 227+228+229+230+231+232+233+234+235+236+237 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 261+262+263+264+265+266+267+268+269+270+271+272 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
