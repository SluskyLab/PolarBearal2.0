from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AW8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 37+37+38+39+40+41+82+83+84+85+86+87+88+91+92+93+94+95+96+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+120+121+122+123+124+125+126+127+128+138+139+140+141+142+154+155+156+157+158+159+175+176+177+178 & chain A")
cmd.load_cgo( [9.0, -5.826597,22.609987,9.882687, 34.08277, 8.359495, -5.034997, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
