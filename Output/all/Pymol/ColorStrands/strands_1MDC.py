from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MDC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1MDC_A_S0", "resi 10-13 & chain A & 1MDC ")
cmd.color ("red", "1MDC_A_S0")


cmd.select("1MDC_A_S1", "resi 38-41 & chain A & 1MDC ")
cmd.color ("yellow", "1MDC_A_S1")


cmd.select("1MDC_A_S2", "resi 50-53 & chain A & 1MDC ")
cmd.color ("green", "1MDC_A_S2")


cmd.select("1MDC_A_S3", "resi 59-69 & chain A & 1MDC ")
cmd.color ("cyan", "1MDC_A_S3")


cmd.select("1MDC_A_S4", "resi 80-84 & chain A & 1MDC ")
cmd.color ("blue", "1MDC_A_S4")


cmd.select("1MDC_A_S5", "resi 88-95 & chain A & 1MDC ")
cmd.color ("magenta", "1MDC_A_S5")


cmd.select("1MDC_A_S6", "resi 100-107 & chain A & 1MDC ")
cmd.color ("red", "1MDC_A_S6")


cmd.select("1MDC_A_S7", "resi 112-119 & chain A & 1MDC ")
cmd.color ("yellow", "1MDC_A_S7")


cmd.select("1MDC_A_S8", "resi 125-130 & chain A & 1MDC ")
cmd.color ("green", "1MDC_A_S8")


cmd.select("1MDC_barrel", "1MDC_A_S*")
cmd.show("cartoon", "1MDC_barrel")
cmd.zoom("1MDC_barrel")
