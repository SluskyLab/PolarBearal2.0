from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 13+13+14+15+16+17+18+19+20+21+37+38+39+40+41+42+43+44+47+48+49+50+51+52+53+54+55+56+59+60+61+62+63+64+65+66+67+68+69+75+76+77+78+79+84+85+86+87+88+89+90+91+92+97+98+99+100+101+102+103+104+111+112+113+114+115+116+117+118+145+146+147 & chain A")
cmd.load_cgo( [9.0, 11.891999,3.475823,21.161194, -18.211296, 18.790937, -1.034235, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
