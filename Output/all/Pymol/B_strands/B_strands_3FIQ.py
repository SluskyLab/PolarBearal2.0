from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14+15+16+17+18+19+20+21+22+23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 50+51+52+53+54+55+56+57+58+59 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 62+63+64+65+66+67+68+69+70+71+72 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 78+79+80+81 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 85+86+87+88+89+90+91+92+93 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 97+98+99+100+101+102+103+104+105 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 38+39+40+41+42+43+44 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 111+112+113+114+115+116+117+118+119 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
