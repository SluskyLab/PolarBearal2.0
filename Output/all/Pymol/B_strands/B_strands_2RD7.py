from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2RD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Cstrand0", "resi 29+30+31+32+33+34+35+36+37+38 & chain C ")
cmd.color ("red", "Cstrand0")


cmd.select("Cstrand1", "resi 54+55+56+57+58 & chain C ")
cmd.color ("green", "Cstrand1")


cmd.select("Cstrand2", "resi 65+66+67+68+69+70+71+72 & chain C ")
cmd.color ("orange", "Cstrand2")


cmd.select("Cstrand3", "resi 75+76+77+78+79+80+81+82 & chain C ")
cmd.color ("teal", "Cstrand3")


cmd.select("Cstrand4", "resi 91+92+93+94 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Cstrand5", "resi 103+104+105+106+107+108+109+110 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Cstrand6", "resi 115+116+117+118+119+120+121 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Cstrand7", "resi 127+128+129+130+131+132 & chain C ")
cmd.color ("green", "Cstrand7")


cmd.select("barrel", "Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
