from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F1V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+11+12+13+14+15+16+36+37+38+39+40+41+42+43+44+45+46+51+52+53+54+55+56+57+58+82+83+84+85+86+87+88+96+97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+71+72+73+74+75+76+77+78+79+61+62+63+64+65+66+67+131+132+133+134+135+136+137+138+139+140+141+142+143+148+149+150+151+152+153+154+155+156+157+181+182+183+184+185+186+187+188+189+190+191 & chain A")
cmd.load_cgo( [9.0, 15.273507,-14.93167,34.474808, -44.830566, -14.931785, 34.474907, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
