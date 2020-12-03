from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y32.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+14+15+16+17+18+19+20+26+27+28+29+30+31+32+45+46+47+48+49+50+51+52+53+58+59+60+61+62+63+64+65+66+71+72+73+74+75+76+77+78+85+86+87+88+89+90+91+92+93+102+103+104+105+106+107+108+109+110+111+112+113 & chain A")
cmd.load_cgo( [9.0, 58.833523,2.2766747,56.443176, 20.633335, -10.322763, 56.443207, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
