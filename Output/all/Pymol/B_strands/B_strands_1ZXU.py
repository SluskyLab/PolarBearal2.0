from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1ZXU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 38+39+40+41+42+43 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 54+55+56+57+58 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 63+64+65+66+67+68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 77+78+79+80+81 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 87+88+89+90+91+92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 101+102+103+104+105+106 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 115+116+117+118+119+120 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 131+132+133+134+135 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 146+147+148+149 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 158+159+160+161 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 167+168+169+170+171+172+173 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 187+188+189+190+191 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
