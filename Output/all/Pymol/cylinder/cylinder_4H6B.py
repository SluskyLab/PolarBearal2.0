from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H6B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 12+12+13+14+15+16+17+18+19+56+57+58+59+65+66+67+68+69+70+71+72+73+74+75+76+77+78+79+50+51+52+53+84+85+86+87+88+89+90+91+92+93+94+100+101+102+103+104+105+106+107+108+113+114+115+116+117+118+119+120+128+129+130+131+132+133+134+135+136+137+141+142+143+144+145+146+147+148+149 & chain A")
cmd.load_cgo( [9.0, -3.8969822,-10.345402,-6.393749, -25.85812, 1.7501197, -44.66989, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
