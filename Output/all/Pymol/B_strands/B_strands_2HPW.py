from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HPW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 15+16+17+18+19+20+21+22+23+24+25 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 28+29+30+31+32+33+34+35+36+37+38+39 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 44+45+46+47+48+49+50+51 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 219+220+221+222+223+224+225+226+227+228+229 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 161+162+163+164+165+166+167+168+169+170+171 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 149+150+151+152+153+154+155+156 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 177+178+179+180+181+182+183+184+185+186+187+188 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 93+94+95+96+97+98+99+100+101 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 106+107+108+109+110+111+112+113+114+115+116 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 119+120+121+122+123+124+125+126+127+128+129 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
