from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2L5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 51+51+52+53+54+55+56+57+58+59+60+75+76+77+78+79+80+86+87+88+89+90+91+92+93+94+97+98+99+100+101+102+103+104+105+106+107+113+114+115+116+128+129+130+131+132+133+134+135+136+140+141+142+143+144+145+146+147+148+153+154+155+156+157+158+159+160+161 & chain A")
cmd.load_cgo( [9.0, -18.427057,2.5850642,-13.2791195, 18.17467, -8.179005, 12.8516865, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
