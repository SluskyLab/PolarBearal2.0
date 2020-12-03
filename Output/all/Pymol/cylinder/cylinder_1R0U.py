from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1R0U.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 5+5+6+7+8+9+10+11+12+13+14+15+16+17+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35+38+39+40+41+42+43+44+45+46+47+52+53+54+55+56+57+58+59+62+63+64+65+66+67+68+71+72+73+74+75+76+77+78+81+82+83+84+85+86+87+88+89+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107+108+111+112+113+114+115+116+117+118+119+120+121+129+130+131+132+133+134+135+136+137 & chain A")
cmd.load_cgo( [9.0, 28.4173,41.095863,-9.343731, 21.929869, 9.387583, 26.081009, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
