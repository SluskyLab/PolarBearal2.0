from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1R0U.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 38+39+40+41+42+5+7+43+6+9+8+11+44+10+45+12+13+46+14+47+15+16+17 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 129+130+131+132+133+134+135+136+137 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 111+112+113+114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107+108 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 81+82+83+84+85+86+87+88+89 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 71+72+73+74+75+76+77+78 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 62+63+64+65+66+67+68 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 20+21+22+23+24+25+26+27+52+28+54+56+53+55+29+58+57+30+59+31+32+33+34+35 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
