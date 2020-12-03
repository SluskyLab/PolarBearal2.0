from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1ZXU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 38+38+39+40+41+42+43+54+55+56+57+58+63+64+65+66+67+68+77+78+79+80+81+87+88+89+90+91+92+101+102+103+104+105+106+115+116+117+118+119+120+131+132+133+134+135+146+147+148+149+158+159+160+161+167+168+169+170+171+172+173+187+188+189+190+191 & chain A")
cmd.load_cgo( [9.0, 19.427315,15.962619,8.952563, 0.29856205, -14.91105, -3.6072094, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
