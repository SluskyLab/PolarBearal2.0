from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EW3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 98+99+100+101+102 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 59+60+61+62+63+64+65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 82+83+84+85+86+87+88+89+90+91+92 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 71+72+73+74+75+76+77+78+79 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 35+36+37+38+39+40+41+42+43+44 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 133+134+135+136+137+138+139+140 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 119+120+121+122+123+124+125+126 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
