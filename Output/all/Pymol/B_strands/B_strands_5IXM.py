from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 15+16+17+18+19 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 30+31+32+33+34+35+36+37+38+39 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 43+44+45+46+47+48+49+50+51+52+53+54 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 57+58+59+60+61+62+63+64+65+66+67+68+69 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 99+100+101+102+103+104+105+106+107+108 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 128+129+130+131+132+133+134+135+136+137+138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 142+143+144+145+146+147+148+149+150+151+152+153 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 164+165+166+167+168+169+170+171+172+173+174+175+176+177+178 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 181+182+183+184+185+186+187+188+189+190+191+192+193 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 253+254+255+256+257+258+259+260+261+262+263+264+265+266+269+270+271+272 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 280+281+282+283+284+285+286+287+288+289+290+291+292 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 330+331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 348+349+350+351+352+353+354+355+356+357+358+359 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 378+379+380+381+382+383+384+385+386+387+388+389 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 394+395+396+397+398+399+400+401+402+403 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 409+410+411+412+413+414+415+416+417+418+419 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 425+426+427+428+429+430+431+432+433 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 454+455+456+457+458+459+460+461+462+463+464 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 469+470+471+472+473+474+475+476+477+478 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 483+484+485+486+487+488+489+490+491+492+493+494 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 499+500+501+502+503+504+505+506+507+508+509+510+511 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 518+519+520+521+522+523+524+525+526+527 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")