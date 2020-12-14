from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NXR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 9+10+11+12+13+14+15+16+17+18+19+20+21+22+23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 343+344+345+346+347+348+349+350+351 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 54+55+56+57+58+59+60+61+62+63+64+65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 316+317+318+319+320+321+322+323+324+325 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 75+76+77+78+79+80+81+82+83+84+85+86 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 298+299+300+301+302+303+304+305+306+307+308+309+310+311 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 277+278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 129+130+131+132+133+134+135+136+137+138 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 222+223+224+225+226+227+228+229+230+231+232+233+234 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 188+189+190+191+192+193+194+195+196+197+198 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 175+176+177+178+179+180+181+182+183+184+185 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 237+238+239+240+241+242+243+244+245+246+247 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 148+149+150+151+152+153+154+155 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 39+40+41+42+43+44+45+46+47+48+49 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
