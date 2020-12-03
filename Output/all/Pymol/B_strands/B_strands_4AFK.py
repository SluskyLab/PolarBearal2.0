from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AFK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 42+43+44+45+46+47+48+49+50+51+52+53+54 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 479+480+481+482+483+484+485+486+487+488+489 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 457+458+459+460+461+462+463+464+465+466+467 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 425+426+427+428+429+430+431+432+433+434+435+436+437 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 392+393+394+395+396+397+398+399+400+401+402+403 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 377+378+379+380+381+382+383+384+385+386+387+388 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 324+325+326+327+328+329+330+331+332+333 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 297+298+299+300+301+302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 272+273+274+275+276+277+278+279+280+281+282+283+284+285+286+287+288+289+290+291+292 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 248+249+250+251+252+253+254+255+256+257+258+259+260+261 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 219+220+221+222+223+224+225+226+227+228+229+230 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 204+205+206+207+208+209+210+211+212+213+214+215+216 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 177+178+179+180+181+182+183+184+185 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 162+163+164+165+166+167+168+169+170+171+172+173 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 144+145+146+147+148+149+150+151+152+153+154 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 124+125+126+127+128+129+130+131+132+133+134+135 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 84+85+86+87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 66+67+68+69+70+71+72+73+74+75+76+77+78+79+80+81 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
