from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SAO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13+14+15+16+17+18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34+35+36+37+38+39+40+41 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 45+46+47+48+49+50+51+52 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 82+83+84+85+86+87+88+89 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 74+75+76+77 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 94+95+96+97+98+99+100+101+102+103 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 59+60+61+62+63+64+65+66 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 106+107+108+109+110+111+112+113+114+115 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
