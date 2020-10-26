﻿/*
**  File: BarrelStructures.cs
**  Started: 
**  Contributors: Meghan Franklin, Ryan Feehan, Rik Dhar
**  Overview: 
**
**  About: 
**
**  Last Edited: 
*/

using System;
using System.Numerics;
using System.Collections;
using System.Collections.Generic;
using System.IO;

namespace betaBarrelProgram
{

    namespace BarrelStructures
    {
        
        public interface Protein
        {
            List<Chain> Chains { get; set; }
            int ChainCount { get; set; }
            int totalResNum { get; set; }
            string PdbName { get; set; }
        }

        public interface Barrel : IEnumerable<Strand>
        {
        string PdbName { get; set; }
        List<BarrelStructures.Strand> Strands { get; set; }
        List<Vector3> NellipseCoords { get; set; }
        List<Vector3> CellipseCoords { get; set; }
        Vector3 Ncentroid { get; set; }
        Vector3 Ccentroid { get; set; }
        Vector3 Axis { get; set; }
        bool Direction { get; set; }
        double AvgTilt { get; set; }
        double AvgTilt_even { get; set; }
        double AvgTilt_odd { get; set; }
        double AvgRadius { get; set; }
        List<Res> LoopResies { get; set; }
        List<double> StrandLength { get; set; }
        Vector3 OriginalNcentroid { get; set; }
        Vector3 OriginalCcentroid { get; set; }
        Vector3 AxisVector { get; set; }
        Vector3 NewCaxisPt { get; set; }
        Vector3 OldCaxisPt { get; set; }
        int ShearNum { get; set; }
        List<double> PrevTwists { get; set; }
        public bool Success { get; set; }

        }

        public class Chain : IEnumerable<Res>
        {
            public List<Res> Residues = new List<Res>();
            public int ResidueCount { get; set; }
            public int ChainNum { get; set; }
            public string PdbName { get; set; }
            public string ChainName { get; set; }
            public bool MonovsPoly { get; set; }

            public Chain(ref AtomParser.AtomCategory _myAtomCat, int chainNum, string pdbName, bool mono_status, string dssp_dir)
            {
                this.ChainName = _myAtomCat.ChainAtomList[chainNum].AuthAsymChain;
                this.ChainNum = chainNum;
                this.ResidueCount = 0;
                this.PdbName = pdbName.ToUpper();
                int mySeqID = -1;
                this.MonovsPoly = mono_status;

                int startRes = -15; //Changed from 0 on 11-15-17: This causes horrible problems for PDBs that start at neg values of res nums 
                if (this.PdbName.Contains("7AHL") || this.PdbName.Contains("3W9T")) startRes = 100; //These lines also explain why these can fail to build loops in Rosetta. 
                if (this.PdbName.Contains("3O44")) startRes = 130;

                for (int atomCtr = 0; atomCtr < _myAtomCat.ChainAtomList[chainNum].cartnAtoms.Count; atomCtr++)//_myAtomCat.ChainAtomList[chainNum].cartnAtoms.Count includes ALL atoms in chain
                {
                    if (Convert.ToInt32(_myAtomCat.ChainAtomList[chainNum].CartnAtoms[atomCtr].authSeqId) < startRes) continue;
                    if (Convert.ToInt32(_myAtomCat.ChainAtomList[chainNum].CartnAtoms[atomCtr].authSeqId) > 350 && this.PdbName.Contains("3O44")) break;
                    if (mySeqID == Convert.ToInt32(_myAtomCat.ChainAtomList[chainNum].CartnAtoms[atomCtr].seqId)) continue;//if the residue has already been added, keep going
                    else
                    {
                        mySeqID = Convert.ToInt32(_myAtomCat.ChainAtomList[chainNum].CartnAtoms[atomCtr].seqId);//the first new atom in residue is "atomCtr"

                        Res myRes = new Res(ref _myAtomCat, chainNum, ResidueCount, atomCtr);
                        this.ResidueCount++;
                        this.Residues.Add(myRes);
                    }
                }

                //set residue Direction
                for (int residueCtr = 0; residueCtr < ResidueCount - 1; residueCtr++)
                {
                    Vector3 myDirection = new Vector3();
                    if (Residues[residueCtr].BackboneCoords.Count == 4 && Residues[residueCtr + 1].BackboneCoords.Count == 4)
                    {
                        myDirection = Residues[residueCtr].BackboneCoords["CA"] - Residues[residueCtr + 1].BackboneCoords["CA"];
                        Residues[residueCtr].Direction = myDirection;
                    }
                    else { }
                }
                //Set rel b-factors - added 6/2/17 for loops
                double largest_bfac = 0;
                foreach (Res Res1 in Residues) { if (Res1.BFacCA > largest_bfac) largest_bfac = Res1.BFacCA; }
                foreach (Res Res1 in Residues) { Res1.RelBFac = Res1.BFacCA / largest_bfac; }

                //set residue PhiPsiOmega
                for (int residueCtr = 0; residueCtr < ResidueCount; residueCtr++)
                {
                    if (residueCtr != 0)
                    {
                        if (Residues[residueCtr - 1].BackboneCoords.Count == 4 && Residues[residueCtr].BackboneCoords.Count == 4)
                        {
                            Residues[residueCtr].Omega = SharedFunctions.CalculateTorsion(Residues[residueCtr - 1].BackboneCoords["CA"], Residues[residueCtr - 1].BackboneCoords["C"], Residues[residueCtr].BackboneCoords["N"], Residues[residueCtr].BackboneCoords["CA"]);
                            Residues[residueCtr].Phi = SharedFunctions.CalculateTorsion(Residues[residueCtr - 1].BackboneCoords["C"], Residues[residueCtr].BackboneCoords["N"], Residues[residueCtr].BackboneCoords["CA"], Residues[residueCtr].BackboneCoords["C"]);

                        }
                        for (int atomCtr = 0; atomCtr < Residues[residueCtr].Atoms.Count; atomCtr++)
                        {
                            if (Residues[residueCtr].Atoms[atomCtr].AtomName == "N" && Residues[residueCtr].ThreeLetCode != "PRO")
                            {// get H coords for NH
                                // make sure backbone atoms exist (case in point: 4FSO_B ALA160)
                                if (Residues[residueCtr - 1].BackboneCoords.ContainsKey("C") && Residues[residueCtr - 1].BackboneCoords.ContainsKey("O"))
                                {
                                    Vector3 COvec = new Vector3();
                                    COvec = Residues[residueCtr - 1].BackboneCoords["C"] - Residues[residueCtr - 1].BackboneCoords["O"];
                                    COvec = Vector3.Normalize(COvec);
                                    COvec = COvec * (float)0.9;
                                    COvec += Residues[residueCtr].Atoms[atomCtr].Coords;
                                    Residues[residueCtr].Atoms[atomCtr].Hydrogen = COvec;
                                }
                            }
                            if (Residues[residueCtr - 1].BackboneCoords.ContainsKey("C") && Residues[residueCtr - 1].BackboneCoords.ContainsKey("O") && Residues[residueCtr].BackboneCoords.ContainsKey("N"))
                            {
                                //get e2 vector for carbonyl
                                Vector3 e2 = new Vector3();
                                e2 = Residues[residueCtr - 1].BackboneCoords["C"] - Residues[residueCtr].BackboneCoords["N"];
                                e2 = Vector3.Normalize(e2);
                                for (int atomCtr2 = 0; atomCtr2 < Residues[residueCtr - 1].Atoms.Count; atomCtr2++)
                                {
                                    if (Residues[residueCtr - 1].Atoms[atomCtr2].AtomName == "O") Residues[residueCtr - 1].Atoms[atomCtr2].e2 = e2;
                                }
                            }

                        }

                    }
                    if (residueCtr != ResidueCount - 1)
                    {

                        if (Residues[residueCtr + 1].BackboneCoords.Count == 4 && Residues[residueCtr].BackboneCoords.Count == 4)
                        {
                            Residues[residueCtr].Psi = SharedFunctions.CalculateTorsion(Residues[residueCtr].BackboneCoords["N"], Residues[residueCtr].BackboneCoords["CA"], Residues[residueCtr].BackboneCoords["C"], Residues[residueCtr + 1].BackboneCoords["N"]);
                        }
                    }
                    
                }
                //8-10-2020 - Rik - Added a new method to read SSType from PDB File
                var PDB_SS_dict = getSSfromPDB(this.PdbName, this.ChainName);

                // set SecondaryStructure
                for (int residueCtr = 1; residueCtr < ResidueCount - 1; residueCtr++)
                {
                    string bigPValue = "P";
                    string littlePValue = "p";
                    string geoSeq = "";

                    double phiValue = Residues[residueCtr].Phi;
                    double psiValue = Residues[residueCtr].Psi;
                    double omgValue = Residues[residueCtr].Omega;
                    bool transPeptide = new bool();
                    transPeptide = true;
                    if (Math.Abs(omgValue) < 90)
                    { transPeptide = false; }
                    if (phiValue < 0)
                    {
                        if (psiValue >= -100 && psiValue <= 50)
                        { // alphaR or D
                            if (phiValue < -100)
                            {// D
                                if (transPeptide) { geoSeq += "D"; }
                                else { geoSeq += "d"; }
                            }
                            else
                            {
                                if (transPeptide) { geoSeq += "A"; }
                                else { geoSeq += "a"; }
                            }
                        }
                        else // beta or polyproII
                        {
                            if (MonovsPoly == false && phiValue < -80) //Changed from -100 on 12/1/15; needs to be -90 for multi-chain barrels
                            {
                                if (transPeptide) { geoSeq += "B"; }
                                else { geoSeq += "b"; }
                            }
                            else if (MonovsPoly == true && phiValue < -100) //Changed from -100 on 12/1/15; needs to be -100 for single-chain barrels
                            {
                                if (transPeptide) { geoSeq += "B"; }
                                else { geoSeq += "b"; }
                            }
                            else // polyproII
                            {
                                if (transPeptide) { geoSeq += bigPValue; } // switch to B to merge
                                else { geoSeq += littlePValue; } // switch to b to merge
                            }
                        }
                    }
                    else // phi >= 0
                    {
                        if (psiValue >= -50 && psiValue <= 100)
                        { // alpha-L
                            if (transPeptide) { geoSeq += "L"; }
                            else { geoSeq += "l"; }
                        }
                        else
                        {
                            if (phiValue > 150)
                            {  //extension of beta
                                if (transPeptide) { geoSeq += "B"; }
                                else { geoSeq += "b"; }
                            }
                            else // gamma conformation
                            {
                                if (transPeptide) { geoSeq += "G"; }
                                else { geoSeq += "g"; }
                            }
                        }
                    }

                    Residues[residueCtr].SSType = geoSeq;
                    
                    if (PDB_SS_dict.ContainsKey(Residues[residueCtr].SeqID))
                    {
                        Residues[residueCtr].DSSP = "E";
                    }
                    else
                    {
                        Residues[residueCtr].DSSP = "*";
                    }

                }
            }

            //8-10-2020 - Rik - Get_DSSP from PDB
            public static Dictionary<int, string> getSSfromPDB(string pdbName, string ChainName)
            {

                Dictionary<int, string> PDB_SS_values = new Dictionary<int, string>();
                string PDB_file = Global.DB_DIR + pdbName + ".pdb";

                if (File.Exists(PDB_file))
                {
                    using (StreamReader sr = new StreamReader(PDB_file))
                    {
                        String line;
                        while ((line = sr.ReadLine()) != null)
                        {
                            if (line.Substring(21, 1) == ChainName && line.Substring(0, 5) == "SHEET")
                            {
                                //Console.WriteLine(line.Substring(21, 1));
                                int ResStart = Convert.ToInt32(line.Substring(22, 4));
                                int ResEnd = Convert.ToInt32(line.Substring(33, 4));

                                for (int i = ResStart; i <= ResEnd; i++)
                                {
                                    if (!PDB_SS_values.ContainsKey(i))
                                    {
                                        PDB_SS_values.Add(i, "E");
                                    }

                                }

                            }

                        }
                    }
                }
                if (PDB_SS_values.Count == 0) { Console.WriteLine("NO SS VALUES ADDED FROM PDB"); }
                return PDB_SS_values;
            }

            public static Dictionary<int, string> getDSSP(string pdbName, string DBpath, string ChainName)
            {
                Directory.SetCurrentDirectory(DBpath);

                if (pdbName.ToUpper() == "1A0S") { ChainName = "A"; }

                Dictionary<int, string> DSSP_values = new Dictionary<int, string>();
                string DSSP_file = "DSSP\\" + pdbName + ".dssp";
                bool start = false;

                if (File.Exists(DSSP_file))
                {
                    using (StreamReader sr = new StreamReader(DSSP_file))
                    {
                        String line;
                        while ((line = sr.ReadLine()) != null)
                        {
                            if (line.Substring(0,5) == "  #  ") start = true;

                            else if (start == false) continue;

                            else if (start == true)
                            {
                                //Console.WriteLine(line.Substring(11, 1));
                                if (line.Substring(11, 1) == ChainName && DSSP_values.ContainsKey(Convert.ToInt32(line.Substring(5, 5).Trim())) == false)
                                {
                                    DSSP_values.Add(Convert.ToInt32(line.Substring(6, 5).Trim()), line.Substring(16, 1));
                                }
                            }
                        }
                    }
                }
                //foreach (KeyValuePair<int, string> entry in DSSP_values) { Console.WriteLine(entry.Key + " " + entry.Value); }
                if (DSSP_values.Count == 0) { Console.WriteLine("NO VALUES ADDED TO DSSP"); }
                return DSSP_values;
            }
			
            public IEnumerator<Res> GetEnumerator()
            {
                return Residues.GetEnumerator();
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                return this.GetEnumerator();
            }

            public Vector3 getAvgPosition()
            {
                Vector3 averagePosition = new Vector3();
                for (int residueCtr = 0; residueCtr < this.ResidueCount; residueCtr++)
                {
                    for (int atomCtr = 0; atomCtr < this.Residues[residueCtr].Atoms.Count; atomCtr++)
                    {
                        if (this.Residues[residueCtr].Atoms[atomCtr].AtomName == "N" || this.Residues[residueCtr].Atoms[atomCtr].AtomName == "CA" || this.Residues[residueCtr].Atoms[atomCtr].AtomName == "C")
                        {
                            averagePosition = averagePosition + this.Residues[residueCtr].Atoms[atomCtr].Coords;

                        }
                    }
                }
                averagePosition.X = averagePosition.X / (this.ResidueCount * 3);
                averagePosition.Y = averagePosition.Y / (this.ResidueCount * 3);
                averagePosition.Z = averagePosition.Z / (this.ResidueCount * 3);

                return averagePosition;
            }

            public void translate(Vector3 translationCoords)
            {

                for (int residueCtr = 0; residueCtr < this.ResidueCount; residueCtr++)
                {
                    this.Residues[residueCtr].translate(translationCoords);

                }
                for (int residueCtr = 0; residueCtr < ResidueCount - 1; residueCtr++)
                {
                    Vector3 myDirection = new Vector3();
                    myDirection = Residues[residueCtr + 1].BackboneCoords["CA"] - Residues[residueCtr].BackboneCoords["CA"];
                    Residues[residueCtr].Direction = myDirection;
                }
            }

        }

        //creates a strand 
        public class Strand : IEnumerable<Res>
        {
            public List<Res> Residues { get; set; }//list of res
            public int ResNumStart { get; set; }//first res in strand
            public int ResNumEnd { get; set; }//last res in strand
            public int StrandNum { get; set; }//strand num relative to start of barrel
            public int betaStrandNum { get; set; }//strand num relative to all beta strands in PDB
            public int NumOfRes { get; set; }//number of res in strand
            public double AvgTilt { get; set; }
            public double MinTilt { get; set; }
            public double MaxTilt { get; set; }
            public double AvgTilt_even { get; set; }
            public double AvgTilt_odd { get; set; }
            public string ChainName { get; set; }
            public int ChainNum { get; set; }

            public Vector3 CEllipseCoords { get; set; }
            public double angle { get; set; }

            public Strand(Chain chain, int resNumStart, int resNumEnd, int strandNum)
            {
                this.Residues = new List<Res>();
                this.ResNumStart = resNumStart;
                this.ResNumEnd = resNumEnd;
                this.StrandNum = strandNum;
                this.betaStrandNum = -1; //not kept track of in poly or mono
                this.NumOfRes = resNumEnd - resNumStart;
                this.ChainName = chain.ChainName;
                this.ChainNum = chain.ChainNum;

                this.CEllipseCoords = new Vector3();
                this.angle = 0;
                for (int resCtr = this.ResNumStart; resCtr < this.ResNumEnd + 1; resCtr++)
                {
                    chain.Residues[resCtr].StrandNum = strandNum;
                    chain.Residues[resCtr].ResStrandNum = resCtr - this.ResNumStart;

                    this.Residues.Add(chain.Residues[resCtr]);
                }

            }
            // overload constructor so that all method can have two different strand counters (barrel and all beta)
            public Strand(Chain chain, int resNumStart, int resNumEnd, int strandNum, int betaStrandNum)
            {
                this.Residues = new List<Res>();
                this.ResNumStart = resNumStart;
                this.ResNumEnd = resNumEnd;
                this.StrandNum = strandNum;
                this.betaStrandNum = betaStrandNum;
                this.NumOfRes = resNumEnd - resNumStart;
                this.ChainName = chain.ChainName;
                this.ChainNum = chain.ChainNum;

                this.CEllipseCoords = new Vector3();
                this.angle = 0;
                for (int resCtr = this.ResNumStart; resCtr < this.ResNumEnd + 1; resCtr++)
                {
                    chain.Residues[resCtr].StrandNum = strandNum;
                    chain.Residues[resCtr].ResStrandNum = resCtr - this.ResNumStart;

                    this.Residues.Add(chain.Residues[resCtr]);
                }

            }

            public void getTilts(Vector3 axis, int strandNum)
            {
                this.AvgTilt = 0;
                double other;
                for (int resCtr = 0; resCtr < this.Residues.Count; resCtr++)
                {
                    if (resCtr > 0 && resCtr < this.Residues.Count - 1)
                    {// calculate tilt

                        if (SharedFunctions.AngleBetween((this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"]), axis) < SharedFunctions.AngleBetween(this.Residues[resCtr + 1].BackboneCoords["CA"] - this.Residues[resCtr - 1].BackboneCoords["CA"], axis))
                        {
                            this.Residues[resCtr].Tilt = SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"], axis);
                            other = SharedFunctions.AngleBetween(this.Residues[resCtr + 1].BackboneCoords["CA"] - this.Residues[resCtr - 1].BackboneCoords["CA"], axis);
                            if (this.MinTilt == 0) this.MinTilt = this.Residues[resCtr].Tilt;
                            if (this.MaxTilt == 0) this.MaxTilt = this.Residues[resCtr].Tilt;
                            if (Residues[resCtr].Tilt < this.MinTilt) this.MinTilt = this.Residues[resCtr].Tilt;
                            if (Residues[resCtr].Tilt > this.MaxTilt) this.MaxTilt = this.Residues[resCtr].Tilt;
                            this.AvgTilt += Residues[resCtr].Tilt / (this.Residues.Count - 1);
                        }
                        else
                        {
                            this.Residues[resCtr].Tilt = SharedFunctions.AngleBetween(this.Residues[resCtr + 1].BackboneCoords["CA"] - this.Residues[resCtr - 1].BackboneCoords["CA"], axis);
                            other = SharedFunctions.AngleBetween(this.Residues[resCtr + 1].BackboneCoords["CA"] - this.Residues[resCtr - 1].BackboneCoords["CA"], axis);
                            if (this.MinTilt == 0) this.MinTilt = this.Residues[resCtr].Tilt;
                            if (this.MaxTilt == 0) this.MaxTilt = this.Residues[resCtr].Tilt;
                            if (Residues[resCtr].Tilt < this.MinTilt) this.MinTilt = this.Residues[resCtr].Tilt;
                            if (Residues[resCtr].Tilt > this.MaxTilt) this.MaxTilt = this.Residues[resCtr].Tilt;
                            this.AvgTilt += Residues[resCtr].Tilt / (this.Residues.Count - 1);
                        }
                        //Console.WriteLine("residue {0} of Strand {1} has tilt {2} the other angle is {3}", this.Residues[resCtr].SeqID, strandNum, this.Residues[resCtr].Tilt, other);

                    }
                }
                //Console.WriteLine(" AvgTilt is {0} Min tilit is {1} max tilt is {2}", this.AvgTilt, this.MinTilt, this.MaxTilt);
            }

            public void getTiltsbyAA_divided(Vector3 axis, int strandNum, ref Dictionary<string, AminoAcid> _aaDict)
            {


                if (this.StrandNum % 2 == 0)
                {// calculate tilt

                    for (int resCtr = 0; resCtr < this.Residues.Count; resCtr++)
                    {
                        if (resCtr > 0 && resCtr < this.Residues.Count - 1 && _aaDict.ContainsKey(this.Residues[resCtr].ThreeLetCode))
                        {
                            _aaDict[this.Residues[resCtr].ThreeLetCode].Tilt_even.Add(SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"], axis));
                            this.AvgTilt_even += (SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"], axis) / (this.Residues.Count - 2));
                        }
                    }
                }

                else // if odd
                {
                    for (int resCtr = 0; resCtr < this.Residues.Count; resCtr++)
                    {
                        if (resCtr > 0 && resCtr < this.Residues.Count - 1 && _aaDict.ContainsKey(this.Residues[resCtr].ThreeLetCode))
                        {
                            _aaDict[this.Residues[resCtr].ThreeLetCode].Tilt_odd.Add(SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"], axis));
                            this.AvgTilt_odd += (SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"], axis) / (this.Residues.Count - 2));
                        }
                    }
                }
            }

            public void getTiltsByAA(Vector3 axis, int strandNum, ref Dictionary<string, AminoAcid> _aaDict)
            {

                for (int resCtr = 0; resCtr < this.Residues.Count; resCtr++)
                {
                    double tilt = 999;
                    if (resCtr > 0 && resCtr < this.Residues.Count - 1 && _aaDict.ContainsKey(this.Residues[resCtr].ThreeLetCode))
                    {// calculate tilt

                        if (SharedFunctions.AngleBetween((this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"]), axis) < SharedFunctions.AngleBetween(this.Residues[resCtr + 1].BackboneCoords["CA"] - this.Residues[resCtr - 1].BackboneCoords["CA"], axis))
                        {
                            tilt = SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"], axis);
                            _aaDict[this.Residues[resCtr].ThreeLetCode].Tilt.Add(tilt);
                            this.AvgTilt += tilt / (this.Residues.Count - 2);
                            this.Residues[resCtr].Tilt = tilt;
                        }
                        else
                        {
                            tilt = SharedFunctions.AngleBetween(this.Residues[resCtr + 1].BackboneCoords["CA"] - this.Residues[resCtr - 1].BackboneCoords["CA"], axis);
                            _aaDict[this.Residues[resCtr].ThreeLetCode].Tilt.Add(tilt);
                            this.AvgTilt += tilt / (this.Residues.Count - 2);
                            this.Residues[resCtr].Tilt = tilt;
                        }

                        _aaDict[this.Residues[resCtr].ThreeLetCode].seqIDList.Add(this.Residues[resCtr].SeqID);
                        List<double> phiPsi = new List<double>();
                        phiPsi.Add(this.Residues[resCtr].Phi);
                        phiPsi.Add(this.Residues[resCtr].Psi);
                        _aaDict[this.Residues[resCtr].ThreeLetCode].phiPsiList.Add(phiPsi);
                        double coil = 180 - (SharedFunctions.AngleBetween(this.Residues[resCtr - 1].BackboneCoords["CA"] - this.Residues[resCtr].BackboneCoords["CA"], this.Residues[resCtr].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"]));
                        _aaDict[this.Residues[resCtr].ThreeLetCode].caThetaList.Add(coil);
                        this.Residues[resCtr].Coil2 = coil;
                        this.Residues[resCtr - 1].Coil1 = coil;
                        this.Residues[resCtr + 1].Coil3 = coil;

                        //if not the last residue aDist isthe distance from one Ca to the next Ca
                        this.Residues[resCtr].aDist = (this.Residues[resCtr].BackboneCoords["CA"] - this.Residues[resCtr + 1].BackboneCoords["CA"]).Length();

                    }
                }

            }

            public IEnumerator<Res> GetEnumerator()
            {
                return Residues.GetEnumerator();
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                return this.GetEnumerator();
            }
        }
   }
}
