from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AUI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233+234 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 86+87+88+89+90+91+92+93+94 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213+214 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 124+125+126+127+128+129+130+131+132+133+134+135 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 185+186+187+188+189+190+191+192+193+194+195+196+197+198 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 138+139+140+141+142+143+144+145 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 157+158+159+160+161+162+163+164+165 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 169+170+171+172+173+174+175+176+177+178 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 78+79+80+81+82+83 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 54+55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 40+41+42+43+44+45+46+47 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 242+243+244+245+246+247+248 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 262+263+264+265+266+267+268+269+270+271+272 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 277+278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 293+294+295+296+297+298+299+300+301+302+303+304+305+306+307 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
