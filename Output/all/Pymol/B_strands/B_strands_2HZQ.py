from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HZQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 24+25+26+27+28+29+30+31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 108+109+110+111+112+113+114+115+116 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 96+97+98+99+100+101+102+103 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 84+85+86+87+88 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 67+68+69+70+71+72+73+74+75+76 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 121+122+123+124+125+126+127+128+129+130 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 54+55+56+57+58+59+60+61 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 40+41+42+43+44+45+46+47+48 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
