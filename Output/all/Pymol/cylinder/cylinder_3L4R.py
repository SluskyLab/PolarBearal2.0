from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3L4R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 17+17+18+19+20+21+22+23+24+25+26+41+42+43+44+45+46+47+48+51+52+53+54+55+56+57+58+59+64+65+66+67+68+69+70+71+72+73+79+80+81+82+83+87+88+89+90+91+92+93+94+95+96+100+101+102+103+104+105+106+107+108+109+112+113+114+115+116+117+118+119+120+121+148+149+150 & chain A")
cmd.load_cgo( [9.0, 20.883093,21.01321,25.084774, 11.821043, 21.013271, -17.038185, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
