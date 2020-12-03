from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MK5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 19+19+20+21+22+23+28+29+30+31+32+33+38+39+40+41+42+43+44+54+55+56+57+58+59+60+71+72+73+74+75+76+77+78+79+80+85+86+87+88+89+90+91+92+93+94+95+96+97+103+104+105+106+107+108+109+110+111+112+123+124+125+126+127+128+129+130+131+132+133 & chain A")
cmd.load_cgo( [9.0, 22.795507,32.81657,8.68801, 17.354696, -4.682744, 18.453148, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
