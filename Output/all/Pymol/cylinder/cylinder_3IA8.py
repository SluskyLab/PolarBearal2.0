from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3IA8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 18+18+19+20+21+22+33+34+35+36+37+38+39+40+41+42+43+44+45+26+27+28+29+30+51+52+53+54+55+56+57+58+59+66+67+68+69+70+71+72+73+74+75+76+82+83+84+85+86+87+88+89+93+94+95+96+97+98+99+100+101+102+105+106+107+108+109+110+111+112+113+114+115+124+125+126+127+128+129+130+131+132+133+139+140+141+142+143+144+145+146+147+150+151+152+153+154+155+156+157+158+159+160+161+162+163 & chain A")
cmd.load_cgo( [9.0, 8.795113,48.143326,51.28161, 48.162357, 27.970978, 51.281647, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
