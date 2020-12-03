from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JIW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Istrand0", "resi 13+14+15+16+17+18+19 & chain I ")
cmd.color ("red", "Istrand0")


cmd.select("Istrand1", "resi 25+26+27+28+29+30+31+32+33+34+35 & chain I ")
cmd.color ("green", "Istrand1")


cmd.select("Istrand2", "resi 40+41+42+43+44+45 & chain I ")
cmd.color ("orange", "Istrand2")


cmd.select("Istrand3", "resi 60+61+62+63+64 & chain I ")
cmd.color ("teal", "Istrand3")


cmd.select("Istrand4", "resi 67+68+69+70+71 & chain I ")
cmd.color ("yellow", "Istrand4")


cmd.select("Istrand5", "resi 77+78+79+80+81+82+83+84+85 & chain I ")
cmd.color ("blue", "Istrand5")


cmd.select("Istrand6", "resi 88+89+90+91+92 & chain I ")
cmd.color ("red", "Istrand6")


cmd.select("Istrand7", "resi 98+99+100+101+102+103 & chain I ")
cmd.color ("green", "Istrand7")


cmd.select("barrel", "Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
