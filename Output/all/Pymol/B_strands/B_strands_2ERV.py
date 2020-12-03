from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ERV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 15+16+17+18+19+20+21+22+23+24+29+30+31+32 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 35+36+37+38+39+40+41+42+43+44+45+46+47+48 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 57+58+59+60+61+62+63+64+65+66+67+68+69+70 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 75+76+77+78+79+80+81+82+83+84+85+86+87+88 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 102+103+104+105+106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 119+120+121+122+123+124+125+126+127+128 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 139+140+141+142+143+144+145+146+147+148+149 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
