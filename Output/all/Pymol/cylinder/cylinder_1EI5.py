from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EI5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 348+348+349+350+351+358+359+360+361+362+363+368+369+370+371+372+378+379+380+381+382+383+384+387+388+389+394+395+396+397+398+401+402+403+404+405+406+411+412+413+414+415+416+417 & chain A")
cmd.load_cgo( [9.0, 21.220188,6.935242,3.2251034, 7.112184, -5.2691493, 27.811268, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
