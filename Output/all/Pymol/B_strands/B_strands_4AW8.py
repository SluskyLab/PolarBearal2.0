from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AW8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 37+38+39+40+41 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 175+176+177+178 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 120+121+122+123+124+125+126+127+128 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 138+139+140+141+142 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 154+155+156+157+158+159 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 91+92+93+94+95+96 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 82+83+84+85+86+87+88 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
