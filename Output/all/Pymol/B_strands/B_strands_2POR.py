from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2POR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9+10+11+12+13+14+15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 18+19+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 39+40+41+42+43+44+45+46 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59+60+61+62+63+64+65 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 68+69+70+71+72+73+74 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 118+119+120+121+122+123+124+125 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 128+129+130+131+132+133+134+135 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148+149+150+151+152+153+154+155+156+157+158 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 161+162+163+164+165+166+167+168+169+170+171 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 181+182+183+184+185+186+187+188+189+190+191+192 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 195+196+197+198+199+200+201+202+203+204+205+206 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 227+228+229+230+231+232+233+234+235+236+237+238+239+240 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 243+244+245+246+247+248+249+250+251+252+253+254 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 258+259+260+261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 275+276+277+278+279+280+281+282+283+284+285 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 292+293+294+295+296+297+298+299+300 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
