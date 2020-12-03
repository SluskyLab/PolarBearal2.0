from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 8+8+9+10+11+38+39+40+41+42+43+44+45+50+51+52+53+54+55+56+57+58+86+87+88+89+90+91+92+93+94+95+96+99+100+101+102+103+104+105+106+107+108+109+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+134+135+136+137+138+139+140+141+142+143+144+145+162+163+164+165+166+167+168+169+170+171+172+173+17+18+19+20+21+22+23+24+29+30+31+32+33+34+35 & chain A")
cmd.load_cgo( [9.0, 100.5903,25.624802,8.764377, 46.93065, 25.62473, 8.764461, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
