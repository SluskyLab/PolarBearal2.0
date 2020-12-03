from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ALO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 34+35+36+37+38+39+40+41+42+43 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 128+129+130+131+132+133+134+135+136+137+138+139+140+141+142 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 115+116+117+118+119+120+121+122+123+124 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 100+101+102+103+104+105+106+107+108+109+110 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 92+93+94+95+96+97 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 62+63+64+65+66+67+68+69+70 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 75+76+77+78+79+80+81+82+83+84 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 165+166+167+168+169+53+54+55+56+57+58 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
