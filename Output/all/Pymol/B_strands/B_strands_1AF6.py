from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AF6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9+10+11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40+41+42+43+44+45+46+47+48+49+50+51+52+53 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56+57+58+59+60+61+62+63+64+65+66+67+68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 80+81+82+83+84+85+86+87+88+89 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 99+100+101+102+103+104+105 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 124+125+126+127+128+129+130+131+132 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 138+139+140+141+142+143+144+145+146+147+148 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 167+168+169+170+171+172+173+174+175+176+177+178+179 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 186+187+188+189+190+191+192+193+194+195+196 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 211+212+213+214+215+216+217+218+219+220+221+222+223 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 267+268+269+270+271+272+273+274+275+276+277+278+279+280 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 284+285+286+287+288+289+290+291+292+293+294+295+296 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 303+304+305+306+307+308+309+310+311+312+313+314+315+316 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 320+321+322+323+324+325+326+327+328+329+330+331+332+333 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 362+363+364+365+366+367+368+369+370+371+372+373 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 408+409+410+411+412+413+414+415+416+417+418+419+420 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
