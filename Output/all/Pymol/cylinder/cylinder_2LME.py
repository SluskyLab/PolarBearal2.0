from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LME.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 52+52+53+54+55+56+57+58+59+60+61+62+63+66+67+68+69+70+71+72+73+74+75+76+77+84+85+86+87+88+89+90+94+95+96+97+98+99+100+101+102+103+104 & chain A or resi 94+94+95+96+97+98+99+100+101+102+103+104+84+85+86+87+88+89+90+66+67+68+69+70+71+72+73+74+75+76+77+52+53+54+55+56+57+58+59+60+61+62+63 & chain B or resi 52+52+53+54+55+56+57+58+59+60+61+62+63+66+67+68+69+70+71+72+73+74+75+76+77+84+85+86+87+88+89+90+94+95+96+97+98+99+100+101+102+103+104 & chain C")
cmd.load_cgo( [9.0, 9.42402,-5.3833885,19.911205, -8.870606, -18.66496, -20.810299, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
