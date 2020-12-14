from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3JTY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 38+39+40+41+42+43+44+45+46+47+48+49+50+51+52 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 406+407+408+409+410+411+412+413+414+415+416+417+418 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 389+390+391+392+393+394+395+396+397+398+399 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 367+368+369+370+371+372+373+374+375+376+377+378+379 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 347+348+349+350+351+352+353+354+355+356+357+358+359 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 329+330+331+332+333+334+335+336+337+338 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 288+289+290+291+292+293+294+295+296+297+298+299 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 273+274+275+276+277+278+279+280+281+282+283+284+285 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 250+251+252+253+254+255+256+257+258+259+260+261+262+263 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 234+235+236+237+238+239+240+241+242+243+244+245+246+247 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 221+222+223+224+225+226+227+228+229+230 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 207+208+209+210+211+212+213+214+215+216 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 173+174+175+176+177+178+179+180+181+182+183+184 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 159+160+161+162+163+164+165+166+167 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 134+135+136+137+138+139+140+141 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 119+120+121+122+123+124+125+126+127+128+129+130+131 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73+74 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
