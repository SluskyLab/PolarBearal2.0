from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 14+14+15+16+17+18+19+20+21+22+23+38+39+40+41+42+43+44+50+51+52+53+54+55+56+57+58+59+62+63+64+65+66+67+68+69+70+71+72+78+79+80+81+85+86+87+88+89+90+91+92+93+97+98+99+100+101+102+103+104+105+111+112+113+114+115+116+117+118+119 & chain A")
cmd.load_cgo( [9.0, -3.2982154,-0.30038404,-48.227882, 17.319635, -14.445587, -13.375917, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
