from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 300+300+301+302+303+304+305+306+307+308+309+310+322+323+324+325+326+327+328+329+330+362+363+364+365+366+367+387+388+389+390+391+392+393+394+395+396+397+460+461+462+477+478+479+480+481+482+483+484+485+486+404+405+406+407+408+409+410+411+412+413+418+419+420+421+422+423 & chain H")
cmd.load_cgo( [9.0, 235.76854,213.99803,128.00897, 246.73897, 225.42293, 173.17093, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
