from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VYF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+11+12+13+14+39+40+41+42+43+44+45+48+49+50+51+52+53+54+60+61+62+63+64+123+124+125+126+127+128+129+130+131+113+114+115+116+117+118+119+120+102+103+104+105+106+107+108+109+110+91+92+93+94+95+96+97+79+80+81+82+83+84+85+86+87+88+70+71+72+73 & chain A")
cmd.load_cgo( [9.0, 24.846199,32.74636,28.768332, 17.399773, 32.746414, -9.04281, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
