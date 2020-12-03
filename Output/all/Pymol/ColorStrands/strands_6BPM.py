from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6BPM.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6BPM_C_S0", "resi 182-190 & chain C & 6BPM ")
cmd.color ("red", "6BPM_C_S0")


cmd.select("6BPM_C_S1", "resi 194-205 & chain C & 6BPM ")
cmd.color ("yellow", "6BPM_C_S1")


cmd.select("6BPM_C_S2", "resi 209-222 & chain C & 6BPM ")
cmd.color ("green", "6BPM_C_S2")


cmd.select("6BPM_C_S3", "resi 228-241 & chain C & 6BPM ")
cmd.color ("cyan", "6BPM_C_S3")


cmd.select("6BPM_C_S4", "resi 248-261 & chain C & 6BPM ")
cmd.color ("blue", "6BPM_C_S4")


cmd.select("6BPM_C_S5", "resi 302-318 & chain C & 6BPM ")
cmd.color ("magenta", "6BPM_C_S5")


cmd.select("6BPM_C_S6", "resi 321-343 & chain C & 6BPM ")
cmd.color ("red", "6BPM_C_S6")


cmd.select("6BPM_C_S7", "resi 362-385 & chain C & 6BPM ")
cmd.color ("yellow", "6BPM_C_S7")


cmd.select("6BPM_C_S8", "resi 392-408 & chain C & 6BPM ")
cmd.color ("green", "6BPM_C_S8")


cmd.select("6BPM_C_S9", "resi 438-456 & chain C & 6BPM ")
cmd.color ("cyan", "6BPM_C_S9")


cmd.select("6BPM_C_S10", "resi 460-479 & chain C & 6BPM ")
cmd.color ("blue", "6BPM_C_S10")


cmd.select("6BPM_C_S11", "resi 501-523 & chain C & 6BPM ")
cmd.color ("magenta", "6BPM_C_S11")


cmd.select("6BPM_C_S12", "resi 527-538 & chain C & 6BPM ")
cmd.color ("red", "6BPM_C_S12")


cmd.select("6BPM_C_S13", "resi 564-577 & chain C & 6BPM ")
cmd.color ("yellow", "6BPM_C_S13")


cmd.select("6BPM_C_S14", "resi 581-598 & chain C & 6BPM ")
cmd.color ("green", "6BPM_C_S14")


cmd.select("6BPM_C_S15", "resi 606-623 & chain C & 6BPM ")
cmd.color ("cyan", "6BPM_C_S15")


cmd.select("6BPM_C_S16", "resi 628-643 & chain C & 6BPM ")
cmd.color ("blue", "6BPM_C_S16")


cmd.select("6BPM_C_S17", "resi 660-671 & chain C & 6BPM ")
cmd.color ("magenta", "6BPM_C_S17")


cmd.select("6BPM_C_S18", "resi 675-687 & chain C & 6BPM ")
cmd.color ("red", "6BPM_C_S18")


cmd.select("6BPM_C_S19", "resi 701-715 & chain C & 6BPM ")
cmd.color ("yellow", "6BPM_C_S19")


cmd.select("6BPM_C_S20", "resi 718-738 & chain C & 6BPM ")
cmd.color ("green", "6BPM_C_S20")


cmd.select("6BPM_C_S21", "resi 743-759 & chain C & 6BPM ")
cmd.color ("cyan", "6BPM_C_S21")


cmd.select("6BPM_barrel", "6BPM_C_S*")
cmd.show("cartoon", "6BPM_barrel")
cmd.zoom("6BPM_barrel")
