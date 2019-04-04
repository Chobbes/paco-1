from __future__ import print_function
import sys
from pacolib import *

if len(sys.argv) < 2:
    sys.stderr.write("\nUsage: "+sys.argv[0]+" relsize\n\n")
    sys.exit(1)

relsize = int(sys.argv[1])
n = relsize

print ("Require Export Program.Basics. Open Scope program_scope.")
print ("Require Import paco"+str(n)+" pacotac.")
print ("Set Implicit Arguments.")
print ("")

print ("Section PacoCompanion"+str(n)+".")
print ("")
for i in range(n):
    print ("Variable T"+str(i)+" : "+ifpstr(i,"forall"),end="")
    for j in range(i):
        print (" (x"+str(j)+": @T"+str(j)+itrstr(" x",j)+")",end="")
    print (ifpstr(i,", ")+"Type.")
print ("")
print ("Local Notation rel := (rel"+str(n)+""+itrstr(" T",n)+").")
print ("")
print ("Section PacoCompanion"+str(n)+"_main.")
print ("")
print ("Variable gf: rel -> rel.")
print ("Hypothesis gf_mon: monotone"+str(n)+" gf.")
print ("")
print ("(** ")
print ("  Distributive Compatibility, Distributive Companion, (U)Paco Companion ")
print ("*)")
print ("")
print ("Structure dcompatible"+str(n)+" (clo: rel -> rel) : Prop :=")
print ("  dcompat"+str(n)+"_intro {")
print ("      dcompat"+str(n)+"_mon: monotone"+str(n)+" clo;")
print ("      dcompat"+str(n)+"_compat : forall r,")
print ("          clo (gf r) <"+str(n)+"= gf (clo r);")
print ("      dcompat"+str(n)+"_distr : forall r1 r2,")
print ("          clo (r1 \\"+str(n)+"/ r2) <"+str(n)+"= (clo r1 \\"+str(n)+"/ clo r2);")
print ("    }.")
print ("")
print ("Inductive dcpn"+str(n)+" (r: rel)"+itrstr(" x",n)+" : Prop :=")
print ("| dcpn"+str(n)+"_intro")
print ("    clo")
print ("    (COM: dcompatible"+str(n)+" clo)")
print ("    (CLO: clo r"+itrstr(" x",n)+")")
print (".")
print ("")
print ("Definition pcpn"+str(n)+" r := paco"+str(n)+" gf (dcpn"+str(n)+" r).")
print ("Definition ucpn"+str(n)+" r := upaco"+str(n)+" gf (dcpn"+str(n)+" r).")
print ("")
print ("Lemma dcpn"+str(n)+"_mon: monotone"+str(n)+" dcpn"+str(n)+".")
print ("Proof.")
print ("  red; intros.")
print ("  destruct IN. exists clo.")
print ("  - apply COM.")
print ("  - eapply dcompat"+str(n)+"_mon.")
print ("    + apply COM.")
print ("    + apply CLO.")
print ("    + apply LE.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_mon: monotone"+str(n)+" pcpn"+str(n)+".")
print ("Proof.")
print ("  red; intros. eapply paco"+str(n)+"_mon. apply IN.")
print ("  intros. eapply dcpn"+str(n)+"_mon. apply PR. apply LE.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_mon: monotone"+str(n)+" ucpn"+str(n)+".")
print ("Proof.")
print ("  red; intros. eapply upaco"+str(n)+"_mon. apply IN.")
print ("  intros. eapply dcpn"+str(n)+"_mon. apply PR. apply LE.")
print ("Qed.")
print ("")
print ("Lemma dcpn"+str(n)+"_greatest: forall clo (COM: dcompatible"+str(n)+" clo), clo <"+str(n+1)+"= dcpn"+str(n)+".")
print ("Proof. intros. econstructor;[apply COM|apply PR]. Qed.")
print ("")
print ("Lemma dcpn"+str(n)+"_compat: dcompatible"+str(n)+" dcpn"+str(n)+".")
print ("Proof.")
print ("  econstructor; [apply dcpn"+str(n)+"_mon| |]; intros.")
print ("  - destruct PR; eapply gf_mon with (r:=clo r).")
print ("    + eapply (dcompat"+str(n)+"_compat COM); apply CLO.")
print ("    + intros. econstructor; [apply COM|apply PR].")
print ("  - destruct PR.")
print ("    eapply (dcompat"+str(n)+"_distr COM) in CLO.")
print ("    destruct CLO.")
print ("    + left. eapply dcpn"+str(n)+"_greatest. apply COM. apply H.")
print ("    + right. eapply dcpn"+str(n)+"_greatest. apply COM. apply H.")
print ("Qed.")
print ("")
print ("Lemma dcpn"+str(n)+"_base: forall r, r <"+str(n)+"= dcpn"+str(n)+" r.")
print ("Proof.")
print ("  exists id; [|apply PR].")
print ("  econstructor; repeat intro.")
print ("  + apply LE, IN.")
print ("  + apply PR0.")
print ("  + destruct PR0.")
print ("    * left. apply H.")
print ("    * right. apply H.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_base: forall r, r <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof.")
print ("  right. apply dcpn"+str(n)+"_base. apply PR.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_from_dcpn"+str(n)+"_upaco r:")
print ("  dcpn"+str(n)+" (upaco"+str(n)+" gf r) <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof.")
print ("  intros.")
print ("  eapply (dcompat"+str(n)+"_distr dcpn"+str(n)+"_compat) in PR.")
print ("  destruct PR as [IN|IN]; cycle 1.")
print ("  - right. apply IN.")
print ("  - left. revert"+itrstr(" x",n)+" IN.")
print ("    pcofix CIH. intros.")
print ("    pstep. eapply gf_mon.")
print ("    + apply (dcompat"+str(n)+"_compat dcpn"+str(n)+"_compat).")
print ("      eapply dcpn"+str(n)+"_mon. apply IN.")
print ("      intros. _punfold PR. apply PR. apply gf_mon.")
print ("    + intros. apply (dcompat"+str(n)+"_distr dcpn"+str(n)+"_compat) in PR.")
print ("      right. destruct PR.")
print ("      * apply CIH. apply H.")
print ("      * apply CIH0. apply H.")
print ("Qed.")
print ("")
print ("Lemma dcpn"+str(n)+"_dcpn: forall r,")
print ("    dcpn"+str(n)+" (dcpn"+str(n)+" r) <"+str(n)+"= dcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. exists (compose dcpn"+str(n)+" dcpn"+str(n)+"); [|apply PR].")
print ("  econstructor.")
print ("  - repeat intro. eapply dcpn"+str(n)+"_mon; [apply IN|].")
print ("    intros. eapply dcpn"+str(n)+"_mon; [apply PR0|apply LE].")
print ("  - intros. eapply (dcompat"+str(n)+"_compat dcpn"+str(n)+"_compat).")
print ("    eapply dcpn"+str(n)+"_mon; [apply PR0|].")
print ("    intros. eapply (dcompat"+str(n)+"_compat dcpn"+str(n)+"_compat), PR1.")
print ("  - intros. eapply (dcompat"+str(n)+"_distr dcpn"+str(n)+"_compat).")
print ("    eapply dcpn"+str(n)+"_mon, (dcompat"+str(n)+"_distr dcpn"+str(n)+"_compat).")
print ("    apply PR0.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_ucpn: forall r,")
print ("    ucpn"+str(n)+" (ucpn"+str(n)+" r) <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. destruct PR.")
print ("  - left. eapply paco"+str(n)+"_mult_strong.")
print ("    eapply paco"+str(n)+"_mon. apply H.")
print ("    intros. apply ucpn"+str(n)+"_from_dcpn"+str(n)+"_upaco in PR.")
print ("    eapply upaco"+str(n)+"_mon. apply PR.")
print ("    intros. apply dcpn"+str(n)+"_dcpn. apply PR0.")
print ("  - red. apply ucpn"+str(n)+"_from_dcpn"+str(n)+"_upaco in H.")
print ("    eapply upaco"+str(n)+"_mon. apply H.")
print ("    intros. apply dcpn"+str(n)+"_dcpn. apply PR.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_compat r: ucpn"+str(n)+" (gf r) <"+str(n)+"= gf (ucpn"+str(n)+" r).")
print ("Proof.")
print ("  intros. destruct PR; cycle 1.")
print ("  - apply dcpn"+str(n)+"_compat in H.")
print ("    eapply gf_mon. apply H.")
print ("    intros. right. apply PR.")
print ("  - _punfold H; [|apply gf_mon]. eapply gf_mon. apply H.")
print ("    intros. apply ucpn"+str(n)+"_ucpn.")
print ("    eapply upaco"+str(n)+"_mon. apply PR.")
print ("    intros. eapply dcpn"+str(n)+"_mon. apply PR0.")
print ("    intros. left. pstep. eapply gf_mon. apply PR1.")
print ("    intros. apply ucpn"+str(n)+"_base. apply PR2.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_init:")
print ("  ucpn"+str(n)+" bot"+str(n)+" <"+str(n)+"= paco"+str(n)+" gf bot"+str(n)+".")
print ("Proof.")
print ("  pcofix CIH. intros.")
print ("  destruct PR; cycle 1.")
print ("  - eapply paco"+str(n)+"_mon_bot; [| intros; apply PR].")
print ("    eapply paco"+str(n)+"_algebra, H. apply gf_mon. intros.")
print ("    eapply (dcompat"+str(n)+"_compat dcpn"+str(n)+"_compat).")
print ("    eapply dcpn"+str(n)+"_mon. apply PR. contradiction.")
print ("  - _punfold H; [|apply gf_mon]. pstep.")
print ("    eapply gf_mon. apply H. intros.")
print ("    right. apply CIH. apply PR.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_final r:")
print ("  paco"+str(n)+" gf r <"+str(n)+"= pcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. eapply paco"+str(n)+"_mon. apply PR.")
print ("  intros. apply dcpn"+str(n)+"_base. apply PR0.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_final r:")
print ("  upaco"+str(n)+" gf r <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. eapply upaco"+str(n)+"_mon. apply PR.")
print ("  intros. apply dcpn"+str(n)+"_base. apply PR0.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_clo")
print ("      r clo (LE: clo <"+str(n+1)+"= ucpn"+str(n)+"):")
print ("  clo (ucpn"+str(n)+" r) <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. apply ucpn"+str(n)+"_ucpn, LE, PR.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_clo")
print ("      r clo (LE: clo <"+str(n+1)+"= ucpn"+str(n)+"):")
print ("  clo (pcpn"+str(n)+" r) <"+str(n)+"= pcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. pstep. eapply gf_mon, ucpn"+str(n)+"_ucpn.")
print ("  apply ucpn"+str(n)+"_compat. apply LE in PR.")
print ("  eapply ucpn"+str(n)+"_mon. apply PR.")
print ("  intros. _punfold PR0. apply PR0. apply gf_mon.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_unfold r:")
print ("  pcpn"+str(n)+" r <"+str(n)+"= gf (ucpn"+str(n)+" r).")
print ("Proof.")
print ("  intros. _punfold PR. apply PR. apply gf_mon.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_step r:")
print ("  gf (ucpn"+str(n)+" r) <"+str(n)+"= pcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. pstep. apply PR.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_step r:")
print ("  gf (ucpn"+str(n)+" r) <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof.")
print ("  left. apply pcpn"+str(n)+"_step. apply PR.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_id r : ucpn"+str(n)+" r <"+str(n)+"= ucpn"+str(n)+" r.")
print ("Proof. intros. apply PR. Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_id r : pcpn"+str(n)+" r <"+str(n)+"= pcpn"+str(n)+" r.")
print ("Proof. intros. apply PR. Qed.")
print ("")
print ("Lemma gf_dcpn"+str(n)+"_mon: monotone"+str(n)+" (compose gf dcpn"+str(n)+").")
print ("Proof.")
print ("  repeat intro. eapply gf_mon. apply IN.")
print ("  intros. eapply dcpn"+str(n)+"_mon. apply PR. apply LE.  ")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_from_paco r: paco"+str(n)+" (compose gf dcpn"+str(n)+") r <"+str(n)+"= pcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. apply dcpn"+str(n)+"_base in PR. revert"+itrstr(" x",n)+" PR.")
print ("  pcofix CIH. intros.")
print ("  pstep.")
print ("  eapply gf_mon; cycle 1.")
print ("  { instantiate (1:= _ \\"+str(n)+"/ _). right.")
print ("    destruct PR0; [apply CIH, H | apply CIH0, H]. }")
print ("  eapply gf_mon, (dcompat"+str(n)+"_distr dcpn"+str(n)+"_compat).")
print ("  eapply gf_mon, dcpn"+str(n)+"_dcpn.")
print ("  eapply (dcompat"+str(n)+"_compat dcpn"+str(n)+"_compat).")
print ("  eapply dcpn"+str(n)+"_mon. apply PR.")
print ("  intros. _punfold PR0. apply PR0. apply gf_dcpn"+str(n)+"_mon.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_to_paco r: pcpn"+str(n)+" r <"+str(n)+"= paco"+str(n)+" (compose gf dcpn"+str(n)+") r.")
print ("Proof.")
print ("  pcofix CIH. intros.")
print ("  pstep. _punfold PR; [|apply gf_mon].")
print ("  eapply gf_mon. apply PR. intros.")
print ("  destruct PR0; cycle 1.")
print ("  - eapply dcpn"+str(n)+"_mon. apply H. intros.")
print ("    right. apply CIH0, PR0. ")
print ("  - apply dcpn"+str(n)+"_base. right. apply CIH, H.")
print ("Qed.")
print ("")
print ("Lemma pcpn"+str(n)+"_cofix")
print ("    r l (OBG: forall rr (INC: r <"+str(n)+"= rr) (CIH: l <"+str(n)+"= rr), l <"+str(n)+"= pcpn"+str(n)+" rr):")
print ("  l <"+str(n)+"= pcpn"+str(n)+" r.")
print ("Proof.")
print ("  under_forall ltac:(apply pcpn"+str(n)+"_from_paco).")
print ("  pcofix CIH. intros. apply pcpn"+str(n)+"_to_paco.")
print ("  apply OBG. apply CIH0. apply CIH. apply PR.")
print ("Qed.")
print ("")
print ("End PacoCompanion"+str(n)+"_main.")
print ("")
print ("Lemma pcpn"+str(n)+"_mon_bot (gf gf': rel -> rel)"+itrstr(" x",n)+" r")
print ("      (IN: @pcpn"+str(n)+" gf bot"+str(n)+""+itrstr(" x",n)+")")
print ("      (MON: monotone"+str(n)+" gf)")
print ("      (LE: gf <"+str(n+1)+"= gf'):")
print ("  @pcpn"+str(n)+" gf' r"+itrstr(" x",n)+".")
print ("Proof.")
print ("  eapply paco"+str(n)+"_mon_bot, LE.")
print ("  apply ucpn"+str(n)+"_init. apply MON. left. apply IN.")
print ("Qed.")
print ("")
print ("Lemma ucpn"+str(n)+"_mon_bot (gf gf': rel -> rel)"+itrstr(" x",n)+" r")
print ("      (IN: @ucpn"+str(n)+" gf bot"+str(n)+""+itrstr(" x",n)+")")
print ("      (MON: monotone"+str(n)+" gf)")
print ("      (LE: gf <"+str(n+1)+"= gf'):")
print ("  @ucpn"+str(n)+" gf' r"+itrstr(" x",n)+".")
print ("Proof.")
print ("  eapply upaco"+str(n)+"_mon_bot, LE.")
print ("  left. apply ucpn"+str(n)+"_init. apply MON. apply IN.")
print ("Qed.")
print ("")
print ("End PacoCompanion"+str(n)+".")
print ("")
print ("Hint Resolve ucpn"+str(n)+"_base : paco.")
print ("Hint Resolve pcpn"+str(n)+"_step : paco.")
print ("Hint Resolve ucpn"+str(n)+"_step : paco.")
print ("")
