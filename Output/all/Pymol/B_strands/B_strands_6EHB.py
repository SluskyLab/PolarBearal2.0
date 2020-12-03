from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 311+312+313+38+314+39+40+315+41+316+44+317+45+318+46+319+84+83+86+47+85+87+48+88+49+12+50+89+13+90+51+14+91+52+15+93+92+16+94+53+54+55+56 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 287+288+289+290+291+292+293+294+295+296 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 269+270+271+272+273+274+275+276+277+278+279+280+281+282+283+284 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 255+256+257+258+259+260+261+262+263+264+265+266 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 239+240+241+242+243+244+245+246+247+248+249+250+251+252 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 224+225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 210+211+212+213+214+215+216+217+218+219+220 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 184+185+186+187+188+189+190+191+192 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 148+149+150+151+152+153+154+155 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 138+139+140+141+142+143+144+145 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 97+98+99+59+100+60+61+62+101+63+64+102+103+20+21+65+22+23+66+25+24+26+67+27+68+28+69+29+30+31+32+33+34+35 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
