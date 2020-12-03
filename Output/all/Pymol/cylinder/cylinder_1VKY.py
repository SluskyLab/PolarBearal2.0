from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 67+67+68+69+70+78+79+80+81+82+83+84+85+86+87+90+91+92+93+94+95+96+126+127+128+129+130+131+113+114+115+116+117+118+119+120+106+107+108+109+110 & chain A")
cmd.load_cgo( [9.0, 35.476738,37.592384,7.627936, 40.77491, 31.224367, -21.302385, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
