from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LHF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4+5+6+7+8+9+10+11 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 41+42+43+44+45+46+47+48+49+50 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 73+74+75+76+77+78+79+80+81 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 93+94+95+96+97+98+99+100+101+102+103+104 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 119+120+121+122+123+124+125+126+127+128+129+130 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 136+137+138+139+140+141+142+143+144+145 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 170+171+172+173+174+175+176+177+178 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
