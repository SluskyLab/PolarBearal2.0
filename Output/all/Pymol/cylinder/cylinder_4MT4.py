from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MT4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 84+84+85+86+87+88+89+90+91+92+93+94+95+96+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+299+300+301+302+303+304+305+306+307+308+309+310+322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A or resi 84+84+85+86+87+88+89+90+91+92+93+94+95+96+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+299+300+301+302+303+304+305+306+307+308+309+310+322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain B or resi 84+84+85+86+87+88+89+90+91+92+93+94+95+96+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+299+300+301+302+303+304+305+306+307+308+309+310+322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain C")
cmd.load_cgo( [9.0, 20.659187,25.103424,4.8682055, -32.374397, 25.103329, 4.9860854, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
