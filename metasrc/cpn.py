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

print ("Section Companion"+str(n)+".")
print ("")

for i in range(n):
    print ("Variable T"+str(i)+" : "+ifpstr(i,"forall"),end="")
    for j in range(i):
        print (" (x"+str(j)+": @T"+str(j)+itrstr(" x",j)+")",end="")
    print (ifpstr(i,", ")+"Type.")
print ("")

print ("Local Notation rel := (rel"+str(n)+itrstr(" T", n)+").")
print ("")

print ("Section Companion"+str(n)+"_main.")
print ("")

print ("Variable gf: rel -> rel.")
print ("Hypothesis gf_mon: monotone"+str(n)+" gf.")
print ("")

print ("(** ")
print ("  Compatibility, Companion & Guarded Companion")
print ("*)")
print ("")
print ("Structure compatible"+str(n)+" (clo: rel -> rel) : Prop :=")
print ("  compat"+str(n)+"_intro {")
print ("      compat"+str(n)+"_mon: monotone"+str(n)+" clo;")
print ("      compat"+str(n)+"_compat : forall r,")
print ("          clo (gf r) <"+str(n)+"= gf (clo r);")
print ("    }.")
print ("")
print ("Inductive cpn"+str(n)+" (r: rel)"+itrstr(" e", n)+" : Prop :=")
print ("| cpn"+str(n)+"_intro")
print ("    clo")
print ("    (COM: compatible"+str(n)+" clo)")
print ("    (CLO: clo r"+itrstr(" e", n)+")")
print (".")
print ("")
print ("Definition gcpn"+str(n)+" := compose gf cpn"+str(n)+".")
print ("")
print ("Lemma cpn"+str(n)+"_mon: monotone"+str(n)+" cpn"+str(n)+".")
print ("Proof.")
print ("  red. intros.")
print ("  destruct IN. exists clo.")
print ("  - apply COM.")
print ("  - eapply compat"+str(n)+"_mon; [apply COM|apply CLO|apply LE].")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_compat: compatible"+str(n)+" cpn"+str(n)+".")
print ("Proof.")
print ("  econstructor; [apply cpn"+str(n)+"_mon|intros].")
print ("  destruct PR; eapply gf_mon with (r:=clo r).")
print ("  - eapply (compat"+str(n)+"_compat COM); apply CLO.")
print ("  - intros. econstructor; [apply COM|apply PR].")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_greatest: forall clo (COM: compatible"+str(n)+" clo), clo <"+str(n+1)+"= cpn"+str(n)+".")
print ("Proof. intros. econstructor;[apply COM|apply PR]. Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_comp: forall r,")
print ("    cpn"+str(n)+" (cpn"+str(n)+" r) <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. exists (compose cpn"+str(n)+" cpn"+str(n)+"); [|apply PR].")
print ("  econstructor.")
print ("  - repeat intro. eapply cpn"+str(n)+"_mon; [apply IN|].")
print ("    intros. eapply cpn"+str(n)+"_mon; [apply PR0|apply LE].")
print ("  - intros. eapply (compat"+str(n)+"_compat cpn"+str(n)+"_compat).")
print ("    eapply cpn"+str(n)+"_mon; [apply PR0|].")
print ("    intros. eapply (compat"+str(n)+"_compat cpn"+str(n)+"_compat), PR1. ")
print ("Qed.")
print ("")
print ("Lemma gcpn"+str(n)+"_mon: monotone"+str(n)+" gcpn"+str(n)+".")
print ("Proof.")
print ("  repeat intro. eapply gf_mon; [eapply IN|].")
print ("  intros. eapply cpn"+str(n)+"_mon; [apply PR|apply LE].")
print ("Qed.")
print ("")
print ("Lemma gcpn"+str(n)+"_sound:")
print ("  paco"+str(n)+" gcpn"+str(n)+" bot"+str(n)+" <"+str(n)+"= paco"+str(n)+" gf bot"+str(n)+".")
print ("Proof.")
print ("  intros.")
print ("  set (rclo := fix rclo clo n (r: rel) :=")
print ("         match n with")
print ("         | 0 => r")
print ("         | S n' => rclo clo n' r \\"+str(n)+"/ clo (rclo clo n' r)")
print ("         end).")
print ("  assert (RC: exists n, rclo cpn"+str(n)+" n (paco"+str(n)+" gcpn"+str(n)+" bot"+str(n)+")"+itrstr(" x", n)+") by (exists 0; apply PR); clear PR.")
print ("  ")
print ("  cut (forall n, rclo cpn"+str(n)+" n (paco"+str(n)+" gcpn"+str(n)+" bot"+str(n)+") <"+str(n)+"= gf (rclo cpn"+str(n)+" (S n) (paco"+str(n)+" gcpn"+str(n)+" bot"+str(n)+"))).")
print ("  { intro X. revert"+itrstr(" x", n)+" RC; pcofix CIH; intros.")
print ("    pfold. eapply gf_mon.")
print ("    - apply X. apply RC.")
print ("    - intros. right. eapply CIH. apply PR.")
print ("  }")
print ("")
print ("  induction n; intros.")
print ("  - eapply gf_mon.")
print ("    + _punfold PR; [apply PR|apply gcpn"+str(n)+"_mon].")
print ("    + intros. right. eapply cpn"+str(n)+"_mon; [apply PR0|].")
print ("      intros. pclearbot. apply PR1.")
print ("  - destruct PR.")
print ("    + eapply gf_mon; [eapply IHn, H|]. intros. left. apply PR.")
print ("    + eapply gf_mon.")
print ("      * eapply (compat"+str(n)+"_compat cpn"+str(n)+"_compat).")
print ("        eapply (compat"+str(n)+"_mon cpn"+str(n)+"_compat); [apply H|apply IHn].")
print ("      * intros. econstructor 2. apply PR.")
print ("Qed.")
print ("")
print ("(** ")
print ("  Recursive Closure & Weak Compatibility")
print ("*)")
print ("")
print ("Inductive rclo"+str(n)+" (clo: rel->rel) (r: rel): rel :=")
print ("| rclo"+str(n)+"_base")
print ("   "+itrstr(" e", n)+"")
print ("    (R: r"+itrstr(" e", n)+"):")
print ("    @rclo"+str(n)+" clo r"+itrstr(" e", n)+"")
print ("| rclo"+str(n)+"_clo'")
print ("    r'"+itrstr(" e", n)+"")
print ("    (R': r' <"+str(n)+"= rclo"+str(n)+" clo r)")
print ("    (CLOR': clo r'"+itrstr(" e", n)+"):")
print ("    @rclo"+str(n)+" clo r"+itrstr(" e", n)+"")
print ("| rclo"+str(n)+"_step'")
print ("    r'"+itrstr(" e", n)+"")
print ("    (R': r' <"+str(n)+"= rclo"+str(n)+" clo r)")
print ("    (CLOR': @gf r'"+itrstr(" e", n)+"):")
print ("    @rclo"+str(n)+" clo r"+itrstr(" e", n)+"")
print ("| rclo"+str(n)+"_cpn'")
print ("    r'"+itrstr(" e", n)+"")
print ("    (R': r' <"+str(n)+"= rclo"+str(n)+" clo r)")
print ("    (CLOR': @cpn"+str(n)+" r'"+itrstr(" e", n)+"):")
print ("    @rclo"+str(n)+" clo r"+itrstr(" e", n)+"")
print (".")
print ("")
print ("Structure wcompatible"+str(n)+" (clo: rel -> rel) : Prop :=")
print ("  wcompat"+str(n)+"_intro {")
print ("      wcompat"+str(n)+"_mon: monotone"+str(n)+" clo;")
print ("      wcompat"+str(n)+"_wcompat: forall r,")
print ("          clo (gf r) <"+str(n)+"= gf (rclo"+str(n)+" clo r);")
print ("    }.")
print ("")
print ("Lemma rclo"+str(n)+"_mon_gen clo clo' r r'"+itrstr(" e", n)+"")
print ("      (IN: @rclo"+str(n)+" clo r"+itrstr(" e", n)+")")
print ("      (LEclo: clo <"+str(n+1)+"= clo')")
print ("      (LEr: r <"+str(n)+"= r') :")
print ("  @rclo"+str(n)+" clo' r'"+itrstr(" e", n)+".")
print ("Proof.")
print ("  induction IN; intros.")
print ("  - econstructor 1. apply LEr, R.")
print ("  - econstructor 2; [intros; eapply H, PR|apply LEclo, CLOR'].")
print ("  - econstructor 3; [intros; eapply H, PR|apply CLOR'].")
print ("  - econstructor 4; [intros; eapply H, PR|].")
print ("    eapply cpn"+str(n)+"_mon; [apply CLOR'|].")
print ("    intros. apply PR.")
print ("Qed.")
print ("")
print ("Lemma rclo"+str(n)+"_mon clo:")
print ("  monotone"+str(n)+" (rclo"+str(n)+" clo).")
print ("Proof.")
print ("  repeat intro. eapply rclo"+str(n)+"_mon_gen; [apply IN|intros; apply PR|apply LE].")
print ("Qed.")
print ("")
print ("Lemma rclo"+str(n)+"_clo clo r:")
print ("  clo (rclo"+str(n)+" clo r) <"+str(n)+"= rclo"+str(n)+" clo r.")
print ("Proof.")
print ("  intros. econstructor 2; [|apply PR]. ")
print ("  intros. apply PR0.")
print ("Qed.")
print ("")
print ("Lemma rclo"+str(n)+"_step clo r:")
print ("  gf (rclo"+str(n)+" clo r) <"+str(n)+"= rclo"+str(n)+" clo r.")
print ("Proof.")
print ("  intros. econstructor 3; [|apply PR].")
print ("  intros. apply PR0.")
print ("Qed.")
print ("")
print ("Lemma rclo"+str(n)+"_cpn clo r:")
print ("  cpn"+str(n)+" (rclo"+str(n)+" clo r) <"+str(n)+"= rclo"+str(n)+" clo r.")
print ("Proof.")
print ("  intros. econstructor 4; [|apply PR]. ")
print ("  intros. apply PR0.")
print ("Qed.")
print ("")
print ("Lemma rclo"+str(n)+"_mult clo r:")
print ("  rclo"+str(n)+" clo (rclo"+str(n)+" clo r) <"+str(n)+"= rclo"+str(n)+" clo r.")
print ("Proof.")
print ("  intros. induction PR.")
print ("  - eapply R.")
print ("  - econstructor 2; [eapply H | eapply CLOR'].")
print ("  - econstructor 3; [eapply H | eapply CLOR'].")
print ("  - econstructor 4; [eapply H | eapply CLOR'].")
print ("Qed.")
print ("")
print ("Lemma rclo"+str(n)+"_compose clo r:")
print ("  rclo"+str(n)+" (rclo"+str(n)+" clo) r <"+str(n)+"= rclo"+str(n)+" clo r.")
print ("Proof.")
print ("  intros. induction PR.")
print ("  - apply rclo"+str(n)+"_base, R.")
print ("  - apply rclo"+str(n)+"_mult.")
print ("    eapply rclo"+str(n)+"_mon; [apply CLOR'|apply H].")
print ("  - apply rclo"+str(n)+"_step.")
print ("    eapply gf_mon; [apply CLOR'|apply H].")
print ("  - apply rclo"+str(n)+"_cpn.")
print ("    eapply cpn"+str(n)+"_mon; [apply CLOR'|apply H].")
print ("Qed.")
print ("")
print ("Lemma wcompat"+str(n)+"_compat")
print ("      clo (WCOM: wcompatible"+str(n)+" clo):")
print ("  compatible"+str(n)+" (rclo"+str(n)+" clo).")
print ("Proof.")
print ("  econstructor; [eapply rclo"+str(n)+"_mon|]. intros.")
print ("  induction PR; intros.")
print ("  - eapply gf_mon; [apply R|]. intros.")
print ("    apply rclo"+str(n)+"_base. apply PR.")
print ("  - eapply gf_mon.")
print ("    + eapply (wcompat"+str(n)+"_wcompat WCOM).")
print ("      eapply (wcompat"+str(n)+"_mon WCOM); [apply CLOR'|apply H].")
print ("    + intros. apply rclo"+str(n)+"_mult, PR.")
print ("  - eapply gf_mon; [apply CLOR'|].")
print ("    intros. apply H in PR. apply rclo"+str(n)+"_step, PR.")
print ("  - eapply gf_mon; [|intros; apply rclo"+str(n)+"_cpn, PR].")
print ("    apply (compat"+str(n)+"_compat cpn"+str(n)+"_compat).")
print ("    eapply cpn"+str(n)+"_mon; [apply CLOR'|apply H].")
print ("Qed.")
print ("")
print ("Lemma wcompat"+str(n)+"_sound clo (WCOM: wcompatible"+str(n)+" clo):")
print ("  clo <"+str(n+1)+"= cpn"+str(n)+".")
print ("Proof.")
print ("  intros. exists (rclo"+str(n)+" clo).")
print ("  - apply wcompat"+str(n)+"_compat, WCOM.")
print ("  - apply rclo"+str(n)+"_clo.")
print ("    eapply (wcompat"+str(n)+"_mon WCOM); [apply PR|].")
print ("    intros. apply rclo"+str(n)+"_base, PR0.")
print ("Qed.")
print ("")
print ("(** ")
print ("  Lemmas for tactics")
print ("*)")
print ("")
print ("Lemma cpn"+str(n)+"_base: forall r, r <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. exists id.")
print ("  - econstructor; repeat intro.")
print ("    + apply LE, IN.")
print ("    + apply PR0.")
print ("  - apply PR.")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_from_upaco r:")
print ("  upaco"+str(n)+" gcpn"+str(n)+" r <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. destruct PR; [| apply cpn"+str(n)+"_base, H].")
print ("  exists (rclo"+str(n)+" (paco"+str(n)+" gcpn"+str(n)+")).")
print ("  - apply wcompat"+str(n)+"_compat.")
print ("    econstructor; [apply paco"+str(n)+"_mon|].")
print ("    intros. _punfold PR; [|apply gcpn"+str(n)+"_mon].")
print ("    eapply gf_mon; [apply PR|].")
print ("    intros. apply rclo"+str(n)+"_cpn.")
print ("    eapply cpn"+str(n)+"_mon; [apply PR0|].")
print ("    intros. destruct PR1.")
print ("    + apply rclo"+str(n)+"_clo.")
print ("      eapply paco"+str(n)+"_mon; [apply H0|].")
print ("      intros. apply rclo"+str(n)+"_step.")
print ("      eapply gf_mon; [apply PR1|].")
print ("      intros. apply rclo"+str(n)+"_base, PR2.")
print ("    + apply rclo"+str(n)+"_step.")
print ("      eapply gf_mon; [apply H0|].")
print ("      intros. apply rclo"+str(n)+"_base, PR1.")
print ("  - apply rclo"+str(n)+"_clo.")
print ("    eapply paco"+str(n)+"_mon; [apply H|].")
print ("    intros. apply rclo"+str(n)+"_base, PR.")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_from_paco r:")
print ("  paco"+str(n)+" gcpn"+str(n)+" r <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof. intros. apply cpn"+str(n)+"_from_upaco. left. apply PR. Qed.")
print ("")
print ("Lemma gcpn"+str(n)+"_from_paco r:")
print ("  paco"+str(n)+" gcpn"+str(n)+" r <"+str(n)+"= gcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. _punfold PR; [|apply gcpn"+str(n)+"_mon].")
print ("  eapply gf_mon; [apply PR|].")
print ("  intros. apply cpn"+str(n)+"_comp.")
print ("  eapply cpn"+str(n)+"_mon; [apply PR0|].")
print ("  apply cpn"+str(n)+"_from_upaco.")
print ("Qed.")
print ("")
print ("Lemma gcpn"+str(n)+"_to_paco r:")
print ("  gcpn"+str(n)+" r <"+str(n)+"= paco"+str(n)+" gcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. pfold. eapply gcpn"+str(n)+"_mon; [apply PR|].")
print ("  intros. right. apply PR0.")
print ("Qed.  ")
print ("")
print ("Lemma cpn"+str(n)+"_complete:")
print ("  paco"+str(n)+" gf bot"+str(n)+" <"+str(n)+"= cpn"+str(n)+" bot"+str(n)+".")
print ("Proof.")
print ("  intros. apply cpn"+str(n)+"_from_paco.")
print ("  eapply paco"+str(n)+"_mon_gen.")
print ("  - apply PR.")
print ("  - intros. eapply gf_mon; [apply PR0|apply cpn"+str(n)+"_base].")
print ("  - intros. apply PR0.")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_init:")
print ("  cpn"+str(n)+" bot"+str(n)+" <"+str(n)+"= paco"+str(n)+" gf bot"+str(n)+".")
print ("Proof.")
print ("  intros. apply gcpn"+str(n)+"_sound, gcpn"+str(n)+"_to_paco, (compat"+str(n)+"_compat cpn"+str(n)+"_compat).")
print ("  eapply cpn"+str(n)+"_mon; [apply PR|contradiction].")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_clo")
print ("      r clo (LE: clo <"+str(n+1)+"= cpn"+str(n)+"):")
print ("  clo (cpn"+str(n)+" r) <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. apply cpn"+str(n)+"_comp, LE, PR.")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_unfold:")
print ("  cpn"+str(n)+" bot"+str(n)+" <"+str(n)+"= gcpn"+str(n)+" bot"+str(n)+".")
print ("Proof.")
print ("  intros. apply cpn"+str(n)+"_init in PR. punfold PR.")
print ("  eapply gf_mon; [apply PR|].")
print ("  intros. pclearbot. apply cpn"+str(n)+"_complete, PR0.")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_step r:")
print ("  gcpn"+str(n)+" r <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. eapply cpn"+str(n)+"_clo, PR.")
print ("  intros. eapply wcompat"+str(n)+"_sound, PR0.")
print ("  econstructor; [apply gf_mon|].")
print ("  intros. eapply gf_mon; [apply PR1|].")
print ("  intros. apply rclo"+str(n)+"_step.")
print ("  eapply gf_mon; [apply PR2|].")
print ("  intros. apply rclo"+str(n)+"_base, PR3.")
print ("Qed.")
print ("")
print ("Lemma gcpn"+str(n)+"_clo")
print ("      r clo (LE: clo <"+str(n+1)+"= cpn"+str(n)+"):")
print ("  clo (gcpn"+str(n)+" r) <"+str(n)+"= gcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. apply LE, (compat"+str(n)+"_compat cpn"+str(n)+"_compat) in PR.")
print ("  eapply gf_mon; [apply PR|].")
print ("  intros. apply cpn"+str(n)+"_comp, PR0.")
print ("Qed.")
print ("")
print ("Lemma cpn"+str(n)+"_final: forall r, upaco"+str(n)+" gf r <"+str(n)+"= cpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. eapply cpn"+str(n)+"_from_upaco.")
print ("  intros. eapply upaco"+str(n)+"_mon_gen; [apply PR| |intros; apply PR0].")
print ("  intros. eapply gf_mon; [apply PR0|].")
print ("  intros. apply cpn"+str(n)+"_base, PR1.")
print ("Qed.")
print ("")
print ("Lemma gcpn"+str(n)+"_final: forall r, paco"+str(n)+" gf r <"+str(n)+"= gcpn"+str(n)+" r.")
print ("Proof.")
print ("  intros. _punfold PR; [|apply gf_mon].")
print ("  eapply gf_mon; [apply PR | apply cpn"+str(n)+"_final].")
print ("Qed.")
print ("")
print ("End Companion"+str(n)+"_main.")
print ("")
print ("Lemma cpn"+str(n)+"_mon_bot (gf gf': rel -> rel)"+itrstr(" e", n)+" r")
print ("      (IN: @cpn"+str(n)+" gf bot"+str(n)+itrstr(" e", n)+")")
print ("      (MONgf: monotone"+str(n)+" gf)")
print ("      (MONgf': monotone"+str(n)+" gf')")
print ("      (LE: gf <"+str(n+1)+"= gf'):")
print ("  @cpn"+str(n)+" gf' r"+itrstr(" e", n)+".")
print ("Proof.")
print ("  apply cpn"+str(n)+"_init in IN; [|apply MONgf].")
print ("  apply cpn"+str(n)+"_final; [apply MONgf'|].")
print ("  left. eapply paco"+str(n)+"_mon_gen; [apply IN| apply LE| contradiction].")
print ("Qed.")
print ("")
print ("End Companion"+str(n)+".")
print ("")
print ("Hint Unfold gcpn"+str(n)+" : paco.")
print ("")
print ("Hint Resolve cpn"+str(n)+"_base : paco.")
print ("Hint Resolve cpn"+str(n)+"_step : paco.")
print ("Hint Resolve cpn"+str(n)+"_final gcpn"+str(n)+"_final : paco.")
print ("(* Hint Resolve cpn"+str(n)+"_mon : paco.")
print ("Hint Resolve gcpn"+str(n)+"_mon : paco.")
print ("Hint Resolve rclo"+str(n)+"_mon : paco. *)")
print ("")
print ("Hint Constructors cpn"+str(n)+" compatible"+str(n)+" wcompatible"+str(n)+".")
print ("")
print ("Hint Constructors rclo"+str(n)+" : rclo.")
print ("Hint Resolve rclo"+str(n)+"_clo rclo"+str(n)+"_step rclo"+str(n)+"_cpn : rclo.")
print ("")
