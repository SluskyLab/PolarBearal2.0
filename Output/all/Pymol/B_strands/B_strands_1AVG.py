from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AVG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Istrand0", "resi 24+25+26+27+28 & chain I ")
cmd.color ("red", "Istrand0")


cmd.select("Istrand1", "resi 51+52+53+54+55+56 & chain I ")
cmd.color ("green", "Istrand1")


cmd.select("Istrand2", "resi 37+38+39+40+41+42+43 & chain I ")
cmd.color ("orange", "Istrand2")


cmd.select("Istrand3", "resi 66+67+68+69+70+71 & chain I ")
cmd.color ("teal", "Istrand3")


cmd.select("Istrand4", "resi 80+81+82+83+84+85+86 & chain I ")
cmd.color ("yellow", "Istrand4")


cmd.select("Istrand5", "resi 92+93+94+95+96+97+98+99+100+101 & chain I ")
cmd.color ("blue", "Istrand5")


cmd.select("Istrand6", "resi 106+107+108+109+110+111+112+113+114+115 & chain I ")
cmd.color ("red", "Istrand6")


cmd.select("Istrand7", "resi 122+123+124+125+126+127+128 & chain I ")
cmd.color ("green", "Istrand7")


cmd.select("barrel", "Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
