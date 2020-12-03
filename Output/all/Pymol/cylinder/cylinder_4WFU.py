from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4WFU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 14+14+15+16+17+18+19+20+21+22+23+24+25+41+42+43+44+45+50+51+52+53+54+55+56+57+58+59+36+37+38+62+63+64+65+66+67+68+69+70+71+77+78+79+80+81+82+85+86+87+88+89+90+91+92+93+94+97+98+99+100+101+102+103+104+105+109+110+111+112+113+114+115+116+117+118+119 & chain A")
cmd.load_cgo( [9.0, -28.424767,13.620405,-31.150536, -35.862762, 39.6092, 2.6938753, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
