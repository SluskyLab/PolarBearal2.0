from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O8O.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 67+68+69+70+71+72+73+74+75+76 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 79+80+81+82+83+84+85 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 95+96+97+98+99+100+101+102 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 105+106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 117+118+119+120+121+122+123+124 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131+132+133+134+135+136+137 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 143+144+145+146+147+148+149+150+151 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 155+156+157+158+159+160+161+162 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 170+171+172+173+174+175+176+177+178+179+180+181+182 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 187+188+189+190+191+192+193+194+195+196+197 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 204+205+206+207+208+209+210+211+212+213+214+215 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 220+221+222+223+224+225 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 231+232+233+234+235+236+237+238 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 243+244+245+246+247+248+249+250+251+252 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 266+267+268+269+270+271+272+273+274+275 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 280+281+282+283+284+285+286+287+288 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 291+292+293+294+295+296+297+298+299 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 305+306+307+308+309+310+311+312+313+314 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 319+320+321+322+323+324+325+326+327+328+329 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
